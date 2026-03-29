"""
shell_map_pipeline.py — 3D xi-normalized shell map of the observable universe
Eric D. Martin, 2026-03-29

Paper 4 prototype: converts galaxy catalog (RA, Dec, z) into UHA shell
coordinates (xi, theta, phi) and renders a 3D structural map without H0 assumption.

Pipeline (Claim 60):
  1. Load catalog: RA, Dec, z per galaxy
  2. Compute xi = d_c / d_H  where d_H = c/H0 (Hubble distance)
  3. Convert to 3D Cartesian shell-space: (x, y, z) = xi*(cos Dec cos RA, cos Dec sin RA, sin Dec)
  4. Optionally flag/mask lines of sight toward known gravity wells (peculiar velocity bias)
  5. Render: point cloud, density shells, or voxel map

Notation:
  xi = d_c / d_H  where d_H = c/H0 throughout Paper 4.
  This is the same normalization as Papers 1/2 — consistent frame-agnostic coordinate.
  d_H(=c/H0) is used for the shell comparison; R_H(a) is reserved for the full UHA
  cosmological-horizon formalism when scale factor dependence matters.

Gravity well treatment — three modes (run all three for Paper 4):
  --unmasked (default)    : full catalog, no exclusions — primary result
  --flag-attractors       : mark attractor-cone objects in render, keep all data
  --mask-attractors       : remove attractor-cone objects — sensitivity test only

  Lines of sight toward Virgo, Great Attractor, Shapley, Perseus-Pisces have
  peculiar velocity biases: Delta_xi = v_pec/c. At v_pec=1000 km/s -> Delta_xi~0.003.
  This smears shell boundaries and can create fake radial structure.

  Masking is a sensitivity test, not the primary analysis. The paper must show
  all three modes and demonstrate the shell profile does/does not materially change.
  If it changes -> real attractor contamination found. If it does not -> result is robust.

  Anchor directions were pre-registered to maximize separation from Virgo and
  Great Attractor/Norma region to reduce local peculiar-velocity anisotropy.

Usage:
  python shell_map_pipeline.py                         # unmasked, synthetic
  python shell_map_pipeline.py --catalog FILE          # real FITS/CSV catalog
  python shell_map_pipeline.py --mode shells           # shell density profile
  python shell_map_pipeline.py --mode voxel            # density field
  python shell_map_pipeline.py --mode points           # point cloud (default)
  python shell_map_pipeline.py --flag-attractors       # highlight but keep attractor LOS
  python shell_map_pipeline.py --mask-attractors       # remove attractor LOS (sensitivity)
  python shell_map_pipeline.py --compare-masked        # side-by-side unmasked vs masked
  python shell_map_pipeline.py --attractor-cone 15     # exclusion cone radius (degrees)
  python shell_map_pipeline.py --show-anchors          # print optimal pre-reg anchor dirs
"""

import numpy as np
import argparse
import sys
import os

# ── Cosmological parameters ───────────────────────────────────────────────────

H0 = 67.4          # km/s/Mpc (Planck 2018)
OM = 0.290         # Ωm (DESI DR2 best-fit, our Paper 2 result)
OL = 1.0 - OM      # ΩΛ (flat universe)
C  = 299792.458    # km/s

# ── Known gravity wells — peculiar velocity bias catalog ─────────────────────
#
# Lines of sight toward these structures have large peculiar velocities that
# shift apparent ξ values. Masking an exclusion cone removes the bias at the
# cost of sky coverage. Cone radius of 15° is conservative; 10° is aggressive.
#
# v_pec estimates from NED / literature; xi_center = d_c / R_H at listed distance.

KNOWN_ATTRACTORS = {
    'Virgo Cluster': {
        'ra': 187.7, 'dec': 12.4,
        'd_mpc': 16.5,
        'v_pec_kms': 1000,
        'notes': 'Nearest rich cluster; large infall region',
    },
    'Great Attractor (Norma)': {
        'ra': 243.5, 'dec': -65.0,
        'd_mpc': 65.0,
        'v_pec_kms': 600,
        'notes': 'Laniakea convergence zone; partially behind ZoA',
    },
    'Shapley Supercluster': {
        'ra': 201.9, 'dec': -31.5,
        'd_mpc': 200.0,
        'v_pec_kms': 700,
        'notes': 'Largest nearby mass concentration; drives bulk flow',
    },
    'Perseus-Pisces': {
        'ra': 25.0, 'dec': 35.0,
        'd_mpc': 70.0,
        'v_pec_kms': 500,
        'notes': ('Major filament; counterpole to Great Attractor. '
                  'Literature is more mixed on coherent peculiar-velocity role than '
                  'Virgo/Great Attractor — flag in sensitivity test, but justify any '
                  'full masking explicitly in Paper 4 methods text.'),
    },
    'Coma Cluster': {
        'ra': 194.9, 'dec': 27.9,
        'd_mpc': 100.0,
        'v_pec_kms': 800,
        'notes': 'Richest nearby cluster; strong finger-of-god',
    },
}


def angular_separation(ra1, dec1, ra2, dec2):
    """
    Angular separation in degrees between (ra1, dec1) and (ra2, dec2).
    Uses haversine formula. All inputs in degrees. Vectorized.
    """
    ra1, dec1, ra2, dec2 = map(np.radians, [ra1, dec1, ra2, dec2])
    dlat = dec2 - dec1
    dlon = ra2  - ra1
    a = np.sin(dlat/2)**2 + np.cos(dec1) * np.cos(dec2) * np.sin(dlon/2)**2
    return np.degrees(2 * np.arcsin(np.sqrt(np.clip(a, 0, 1))))


def flag_attractor_los(ra, dec, cone_deg=15.0, verbose=True):
    """
    Return boolean array: True = within an attractor exclusion cone (flagged).

    Does NOT remove objects — just marks them. Use for rendering flagged points
    in a different color while keeping the full dataset intact.

    For Paper 4: run unmasked (all objects), flagged (all objects, different color),
    and masked (attractor objects removed) and compare shell profiles. If the shell
    profile does not change materially -> result is robust to local flow contamination.

    Parameters
    ----------
    ra, dec  : arrays of object positions (degrees)
    cone_deg : cone half-angle (degrees)
    verbose  : print fraction flagged per attractor

    Returns
    -------
    flagged : boolean array, True = in attractor cone (potentially biased)
    """
    flagged = np.zeros(len(ra), dtype=bool)
    total_flagged = 0

    for name, att in KNOWN_ATTRACTORS.items():
        sep = angular_separation(ra, dec, att['ra'], att['dec'])
        in_cone = sep < cone_deg
        n_flag = int(in_cone.sum())
        if verbose and n_flag > 0:
            delta_xi = att['v_pec_kms'] / C   # Delta_xi = v_pec/c for d_H=c/H0
            print(f"  [attractor flag] {name}: {n_flag} objects "
                  f"(cone={cone_deg}deg, delta_xi_bias={delta_xi:.4f})")
        flagged |= in_cone
        total_flagged += n_flag

    if verbose:
        print(f"  [attractor flag] total flagged: {total_flagged} / {len(ra)} "
              f"({100*total_flagged/len(ra):.1f}%) — kept in dataset")
    return flagged


def mask_attractor_los(ra, dec, cone_deg=15.0, verbose=True):
    """
    Return boolean mask: True = keep, False = within exclusion cone of a gravity well.

    SENSITIVITY TEST ONLY — not the primary analysis. Always run unmasked first.
    Compare shell density profiles unmasked vs masked; report both in Paper 4.

    Parameters
    ----------
    ra, dec  : arrays of object positions (degrees)
    cone_deg : exclusion cone half-angle (degrees). Default 15.
               10 aggressive, 15 conservative, 20 very safe.
    verbose  : print excluded count per attractor

    Returns
    -------
    mask : boolean array, True = not in any exclusion cone
    """
    flagged = flag_attractor_los(ra, dec, cone_deg=cone_deg, verbose=False)
    n_excl = int(flagged.sum())
    if verbose:
        print(f"  [attractor mask] removing {n_excl} / {len(ra)} objects "
              f"({100*n_excl/len(ra):.1f}%) — sensitivity test")
    return ~flagged


def select_anchor_directions(n_anchors=4, cone_deg=15.0):
    """
    Select UHA anchor directions that are maximally separated from known
    gravity wells. Used for Paper 4 pre-registration anchor catalog.

    Returns list of (ra, dec, label) for anchor directions that satisfy:
    - Angular separation > cone_deg from all KNOWN_ATTRACTORS
    - Roughly uniform sky coverage (n_anchors quadrants)
    - Galactic latitude |b| > 20° to avoid Zone of Avoidance

    Strategy: seed candidates on a HEALPix-like grid, score by minimum
    angular distance to any attractor, pick top n_anchors well-separated.
    """
    from astropy.coordinates import SkyCoord
    import astropy.units as u

    # Generate candidate directions on a coarse grid
    ra_grid  = np.arange(0, 360, 15)
    dec_grid = np.arange(-75, 90, 15)
    candidates = []
    for r in ra_grid:
        for d in dec_grid:
            # Convert to Galactic to check Zone of Avoidance
            c = SkyCoord(ra=r*u.deg, dec=d*u.deg, frame='icrs')
            gal = c.galactic
            if abs(gal.b.deg) < 20:
                continue  # too close to Galactic plane
            # Minimum separation from any attractor
            min_sep = min(
                angular_separation(r, d, att['ra'], att['dec'])
                for att in KNOWN_ATTRACTORS.values()
            )
            candidates.append((r, d, min_sep))

    # Sort by separation (largest first) and greedily pick well-separated anchors
    candidates.sort(key=lambda x: -x[2])
    selected = []
    for ra_c, dec_c, min_sep in candidates:
        if min_sep < cone_deg:
            continue
        # Must be > 45° from already-selected anchors
        too_close = any(
            angular_separation(ra_c, dec_c, ra_s, dec_s) < 45
            for ra_s, dec_s, _ in selected
        )
        if too_close:
            continue
        selected.append((ra_c, dec_c, min_sep))
        if len(selected) >= n_anchors:
            break

    return selected


def print_anchor_report(anchors, cone_deg):
    """Print anchor direction summary for pre-registration."""
    print(f"\n{'='*60}")
    print(f"  UHA Anchor Directions — gravity-well-avoiding")
    print(f"  Exclusion cone: {cone_deg}° from known attractors")
    print(f"{'='*60}")
    for i, (ra, dec, min_sep) in enumerate(anchors):
        print(f"  Anchor {i+1}: RA={ra:.1f}°, Dec={dec:+.1f}°  "
              f"(min attractor sep: {min_sep:.1f}°)")
    print(f"{'='*60}\n")


def hubble_E(z, om=OM, ol=OL):
    """Dimensionless Hubble parameter E(z) = H(z)/H0."""
    return np.sqrt(om * (1 + z)**3 + ol)

def comoving_distance(z, om=OM, ol=OL, n=1000):
    """
    Comoving distance d_c(z) in Mpc via trapezoidal integration.
    d_c = (c/H0) * ∫₀ᶻ dz'/E(z')
    """
    if np.isscalar(z):
        zz = np.linspace(0, z, n)
        integrand = 1.0 / hubble_E(zz, om, ol)
        return (C / H0) * np.trapezoid(integrand, zz)
    else:
        result = np.zeros(len(z))
        for i, zi in enumerate(z):
            zz = np.linspace(0, zi, n)
            integrand = 1.0 / hubble_E(zz, om, ol)
            result[i] = (C / H0) * np.trapezoid(integrand, zz)
        return result

def horizon_radius(h0=H0):
    """Hubble horizon radius R_H = c/H0 in Mpc."""
    return C / h0

def xi_normalize(z, om=OM, ol=OL, h0=H0):
    """
    ξ = d_c(z) / R_H  — dimensionless, H₀-independent (Claim 55/57/60).
    ξ ∈ [0, 1] where 0 = observer, 1 = Hubble horizon.
    """
    dc = comoving_distance(z, om, ol)
    rh = horizon_radius(h0)
    return dc / rh

# ── Shell-space coordinate conversion ────────────────────────────────────────

def radec_to_cartesian_shell(ra_deg, dec_deg, xi):
    """
    Convert (RA, Dec, ξ) to 3D Cartesian shell-space coordinates.

    x = ξ · cos(Dec) · cos(RA)
    y = ξ · cos(Dec) · sin(RA)
    z = ξ · sin(Dec)

    Result is a unit-sphere point cloud scaled by ξ ∈ [0,1].
    """
    ra  = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    x = xi * np.cos(dec) * np.cos(ra)
    y = xi * np.cos(dec) * np.sin(ra)
    z = xi * np.sin(dec)
    return x, y, z

# ── Catalog loaders ───────────────────────────────────────────────────────────

def load_synthetic(n=5000, z_max=1.5, seed=42):
    """
    Generate a synthetic galaxy catalog for pipeline testing.
    Uniform in comoving volume, isotropic on sky.
    Returns: ra, dec, z arrays.
    """
    rng = np.random.default_rng(seed)
    # Uniform on sphere
    ra  = rng.uniform(0, 360, n)
    dec = np.degrees(np.arcsin(rng.uniform(-1, 1, n)))
    # Redshift: uniform in comoving volume approximation
    # Weight by dV/dz ~ d_c² / E(z)
    z_test = np.linspace(0.001, z_max, 500)
    dc_test = comoving_distance(z_test)
    weight  = dc_test**2 / hubble_E(z_test)
    weight /= weight.sum()
    z = rng.choice(z_test, size=n, p=weight)
    print(f"[synthetic] {n} galaxies, z ∈ [{z.min():.3f}, {z.max():.3f}]")
    return ra, dec, z

def load_fits_catalog(path, ra_col='RA', dec_col='DEC', z_col='Z'):
    """
    Load galaxy catalog from FITS file (DESI DR2, 2MRS, SDSS, etc.)
    Returns: ra, dec, z arrays.
    """
    try:
        from astropy.io import fits
        from astropy.table import Table
    except ImportError:
        print("ERROR: astropy not installed. Run: pip install astropy")
        sys.exit(1)

    print(f"[fits] loading {path}")
    t = Table.read(path)
    ra  = np.array(t[ra_col], dtype=float)
    dec = np.array(t[dec_col], dtype=float)
    z   = np.array(t[z_col], dtype=float)
    # Filter valid redshifts
    mask = (z > 0.001) & (z < 5.0) & np.isfinite(ra) & np.isfinite(dec)
    ra, dec, z = ra[mask], dec[mask], z[mask]
    print(f"[fits] {len(z)} valid objects, z ∈ [{z.min():.3f}, {z.max():.3f}]")
    return ra, dec, z

# ── Shell density profile ─────────────────────────────────────────────────────

def compute_shell_density(xi, n_shells=20):
    """
    Bin ξ values into radial shells and compute density profile.
    Returns: shell centers, counts, expected isotropic counts.
    """
    edges  = np.linspace(0, 1, n_shells + 1)
    counts, _ = np.histogram(xi, bins=edges)
    centers = 0.5 * (edges[:-1] + edges[1:])
    # Expected isotropic: dN/dξ ∝ ξ² (volume element in normalized coords)
    expected = centers**2
    expected = expected / expected.sum() * counts.sum()
    return centers, counts, expected

# ── Voxel density field ───────────────────────────────────────────────────────

def voxelize(x, y, z_cart, n_vox=50):
    """
    Bin 3D Cartesian shell-space into a voxel grid.
    Returns: 3D density array, grid edges.
    """
    edges = np.linspace(-1, 1, n_vox + 1)
    H, _ = np.histogramdd(
        np.column_stack([x, y, z_cart]),
        bins=[edges, edges, edges]
    )
    return H, edges

# ── Renderers ─────────────────────────────────────────────────────────────────

def render_points(x, y, z_cart, xi, output_path=None):
    """3D point cloud colored by ξ (redshift depth)."""
    try:
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
    except ImportError:
        print("ERROR: matplotlib not installed.")
        return

    fig = plt.figure(figsize=(10, 8))
    ax  = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(x, y, z_cart, c=xi, cmap='plasma', s=0.5, alpha=0.4)
    plt.colorbar(sc, ax=ax, label='ξ = d_c / R_H (normalized depth)', shrink=0.5)

    ax.set_xlabel('x (ξ-space)')
    ax.set_ylabel('y (ξ-space)')
    ax.set_zlabel('z (ξ-space)')
    ax.set_title('Observable Universe — ξ-Normalized Shell Map\n'
                 f'H₀={H0} km/s/Mpc, Ωm={OM} (DESI DR2), N={len(x):,} objects')

    # Draw Hubble horizon sphere outline
    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(xs, ys, zs, alpha=0.03, color='cyan')

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"[render] saved → {output_path}")
    else:
        plt.show()

def render_shells(xi, output_path=None):
    """Radial shell density profile vs ξ — shows structure vs isotropic."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("ERROR: matplotlib not installed.")
        return

    centers, counts, expected = compute_shell_density(xi)
    residual = (counts - expected) / np.sqrt(expected + 1)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    ax1.bar(centers, counts, width=centers[1]-centers[0]*0.9,
            color='steelblue', alpha=0.7, label='Observed')
    ax1.plot(centers, expected, 'r--', lw=2, label='Isotropic expected')
    ax1.set_ylabel('Galaxy count per shell')
    ax1.set_title('Shell Density Profile in ξ-Normalized Coordinates\n'
                  '(residuals reveal real structure, not H₀ artifact)')
    ax1.legend()

    ax2.bar(centers, residual, width=centers[1]-centers[0]*0.9,
            color='darkorange', alpha=0.7)
    ax2.axhline(0, color='k', lw=1)
    ax2.axhline(2, color='r', lw=1, ls='--', label='±2σ')
    ax2.axhline(-2, color='r', lw=1, ls='--')
    ax2.set_xlabel('ξ = d_c / R_H')
    ax2.set_ylabel('Residual (σ)')
    ax2.legend()

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"[render] saved → {output_path}")
    else:
        plt.show()

def render_voxel(x, y, z_cart, output_path=None):
    """2D projection of 3D voxel density field."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("ERROR: matplotlib not installed.")
        return

    H, edges = voxelize(x, y, z_cart, n_vox=80)
    # Project along z-axis (line of sight)
    proj = np.log1p(H.sum(axis=2))

    fig, ax = plt.subplots(figsize=(9, 9))
    c = ax.imshow(proj.T, origin='lower', cmap='inferno',
                  extent=[-1, 1, -1, 1], aspect='equal')
    plt.colorbar(c, ax=ax, label='log(1 + N) per voxel')
    ax.set_xlabel('x (ξ-space)')
    ax.set_ylabel('y (ξ-space)')
    ax.set_title('Large-Scale Structure — ξ-Normalized Density Field\n'
                 '(projected along line of sight)')
    # Draw horizon circle
    theta = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(theta), np.sin(theta), 'c--', lw=1, alpha=0.5, label='Hubble horizon ξ=1')
    ax.legend()

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"[render] saved → {output_path}")
    else:
        plt.show()

# ── Attractor comparison render ───────────────────────────────────────────────

def render_compare_masked(xi_full, xi_masked, cone_deg, n_flagged, output_path=None):
    """
    Side-by-side shell density profile: unmasked vs attractor-masked.

    This is the Paper 4 sensitivity figure. The argument is:
      - If profiles agree -> shell structure is not driven by attractor LOS bias
      - If profiles differ -> attractor contamination is real; masked version is cleaner
    Either outcome is publishable. Showing both is the only defensible approach.
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("ERROR: matplotlib not installed.")
        return

    centers_f, counts_f, expected_f = compute_shell_density(xi_full)
    centers_m, counts_m, expected_m = compute_shell_density(xi_masked)

    res_f = (counts_f - expected_f) / np.sqrt(expected_f + 1)
    res_m = (counts_m - expected_m) / np.sqrt(expected_m + 1)

    fig, axes = plt.subplots(2, 2, figsize=(14, 8), sharex=True)
    fig.suptitle(
        f'Shell Density Profile: Unmasked vs Attractor-Masked (cone={cone_deg}deg)\n'
        f'N_full={len(xi_full):,}   N_flagged={n_flagged:,}   N_masked={len(xi_masked):,}   '
        f'({100*n_flagged/len(xi_full):.1f}% removed)\n'
        'Primary result: unmasked. Masked shown as sensitivity test only.',
        fontsize=10
    )

    w = centers_f[1] - centers_f[0]

    ax = axes[0, 0]
    ax.bar(centers_f, counts_f, width=w*0.9, color='steelblue', alpha=0.7, label='Observed')
    ax.plot(centers_f, expected_f, 'r--', lw=2, label='Isotropic')
    ax.set_ylabel('Count / shell')
    ax.set_title('Unmasked (full catalog)')
    ax.legend(fontsize=8)

    ax = axes[0, 1]
    ax.bar(centers_m, counts_m, width=w*0.9, color='darkorange', alpha=0.7, label='Observed')
    ax.plot(centers_m, expected_m, 'r--', lw=2, label='Isotropic')
    ax.set_ylabel('Count / shell')
    ax.set_title(f'Attractor-masked (cone={cone_deg}deg)')
    ax.legend(fontsize=8)

    ax = axes[1, 0]
    ax.bar(centers_f, res_f, width=w*0.9, color='steelblue', alpha=0.7)
    ax.axhline(0, color='k', lw=1)
    ax.axhline(2, color='r', lw=1, ls='--')
    ax.axhline(-2, color='r', lw=1, ls='--')
    ax.set_xlabel('xi = d_c / d_H')
    ax.set_ylabel('Residual (sigma)')

    ax = axes[1, 1]
    ax.bar(centers_m, res_m, width=w*0.9, color='darkorange', alpha=0.7)
    ax.axhline(0, color='k', lw=1)
    ax.axhline(2, color='r', lw=1, ls='--', label='+-2sigma')
    ax.axhline(-2, color='r', lw=1, ls='--')
    ax.set_xlabel('xi = d_c / d_H')
    ax.set_ylabel('Residual (sigma)')
    ax.legend(fontsize=8)

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"[render] saved → {output_path}")
    else:
        plt.show()


def render_flagged_points(x, y, z_cart, xi, flagged, output_path=None):
    """
    3D point cloud with attractor-cone objects highlighted (not removed).
    Clean objects: steelblue. Flagged (potentially biased): red.
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("ERROR: matplotlib not installed.")
        return

    fig = plt.figure(figsize=(10, 8))
    ax  = fig.add_subplot(111, projection='3d')

    clean = ~flagged
    ax.scatter(x[clean], y[clean], z_cart[clean],
               c=xi[clean], cmap='plasma', s=0.5, alpha=0.4, label='Clean LOS')
    if flagged.sum() > 0:
        ax.scatter(x[flagged], y[flagged], z_cart[flagged],
                   c='red', s=1.5, alpha=0.6, label=f'Attractor LOS ({flagged.sum():,})')

    ax.set_xlabel('x (xi-space)')
    ax.set_ylabel('y (xi-space)')
    ax.set_zlabel('z (xi-space)')
    ax.set_title('Shell Map — Attractor Lines of Sight Flagged\n'
                 '(red = within attractor exclusion cone, kept in dataset)')
    ax.legend(fontsize=8)

    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(xs, ys, zs, alpha=0.03, color='cyan')

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"[render] saved → {output_path}")
    else:
        plt.show()


# ── Summary statistics ────────────────────────────────────────────────────────

def print_summary(ra, dec, z, xi):
    rh = horizon_radius()
    dc = comoving_distance(z)
    print(f"\n{'='*60}")
    print(f"  UHA Shell Map — Summary")
    print(f"{'='*60}")
    print(f"  Objects:          {len(z):>10,}")
    print(f"  z range:          {z.min():.4f} – {z.max():.4f}")
    print(f"  ξ range:          {xi.min():.4f} – {xi.max():.4f}")
    print(f"  d_c range (Mpc):  {dc.min():.1f} – {dc.max():.1f}")
    print(f"  R_H (Mpc):        {rh:.1f}")
    print(f"  H₀:               {H0} km/s/Mpc")
    print(f"  Ωm:               {OM} (DESI DR2)")
    print(f"  Frame-agnostic:   YES (ξ removes H₀ dependence)")
    print(f"{'='*60}\n")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    global H0, OM, OL
    parser = argparse.ArgumentParser(
        description='UHA 3D shell map pipeline — Paper 4'
    )
    parser.add_argument('--catalog', default=None,
                        help='FITS galaxy catalog (default: synthetic)')
    parser.add_argument('--ra-col',  default='RA')
    parser.add_argument('--dec-col', default='DEC')
    parser.add_argument('--z-col',   default='Z')
    parser.add_argument('--mode', default='points',
                        choices=['points', 'shells', 'voxel', 'all'],
                        help='Visualization mode (default: points)')
    parser.add_argument('--n',    default=5000, type=int,
                        help='Synthetic catalog size (default: 5000)')
    parser.add_argument('--z-max', default=1.5, type=float,
                        help='Max redshift for synthetic catalog')
    parser.add_argument('--output', default=None,
                        help='Output PNG path (default: interactive display)')
    parser.add_argument('--h0', default=H0, type=float,
                        help=f'H0 value (default: {H0})')
    parser.add_argument('--om', default=OM, type=float,
                        help=f'Om value (default: {OM})')
    parser.add_argument('--flag-attractors', action='store_true',
                        help='Highlight attractor LOS objects in render (keep in dataset)')
    parser.add_argument('--mask-attractors', action='store_true',
                        help='Remove attractor LOS objects — sensitivity test only')
    parser.add_argument('--compare-masked', action='store_true',
                        help='Side-by-side shell profile: unmasked vs masked (Paper 4 fig)')
    parser.add_argument('--attractor-cone', default=15.0, type=float,
                        help='Exclusion cone radius in degrees (default: 15)')
    parser.add_argument('--show-anchors', action='store_true',
                        help='Compute and print optimal UHA anchor directions')
    args = parser.parse_args()

    # Allow overriding cosmology from command line
    H0 = args.h0
    OM = args.om
    OL = 1.0 - OM

    # Load catalog
    if args.catalog:
        ra, dec, z = load_fits_catalog(args.catalog, args.ra_col, args.dec_col, args.z_col)
    else:
        print("[mode] synthetic catalog (use --catalog FILE for real data)")
        ra, dec, z = load_synthetic(n=args.n, z_max=args.z_max)

    # Compute ξ for each object
    print(f"[pipeline] computing ξ for {len(z):,} objects...")
    xi = xi_normalize(z, om=OM, ol=OL, h0=H0)

    # Flag attractor lines of sight (marks objects, does not remove)
    flagged = np.zeros(len(ra), dtype=bool)
    if args.flag_attractors or args.compare_masked or args.mask_attractors:
        print(f"\n[attractor] identifying gravity-well sight lines (cone={args.attractor_cone}deg):")
        flagged = flag_attractor_los(ra, dec, cone_deg=args.attractor_cone, verbose=True)

    # --compare-masked: generate side-by-side figure before any masking
    if args.compare_masked:
        xi_full   = xi.copy()
        keep      = ~flagged
        xi_masked = xi[keep]
        out_cmp   = args.output.replace('.png', '_compare_masked.png') if args.output else None
        render_compare_masked(xi_full, xi_masked, args.attractor_cone,
                              int(flagged.sum()), output_path=out_cmp)

    # --mask-attractors: remove flagged objects (sensitivity test only)
    if args.mask_attractors:
        keep = ~flagged
        ra, dec, z, xi = ra[keep], dec[keep], z[keep], xi[keep]
        flagged = flagged[keep]  # all False after masking
        print(f"[attractor mask] {len(z):,} objects retained for sensitivity analysis\n")

    # Optional: compute and print optimal anchor directions
    if args.show_anchors:
        try:
            anchors = select_anchor_directions(n_anchors=4, cone_deg=args.attractor_cone)
            print_anchor_report(anchors, args.attractor_cone)
        except ImportError:
            print("[anchors] requires astropy — run: pip install astropy")

    # Convert to 3D shell-space Cartesian
    x, y, z_cart = radec_to_cartesian_shell(ra, dec, xi)

    # Summary
    print_summary(ra, dec, z, xi)

    # Render
    mode = args.mode
    out  = args.output

    if mode in ('points', 'all'):
        out_p = out.replace('.png', '_points.png') if out and mode == 'all' else out
        if args.flag_attractors and flagged.any():
            render_flagged_points(x, y, z_cart, xi, flagged, output_path=out_p)
        else:
            render_points(x, y, z_cart, xi, output_path=out_p)

    if mode in ('shells', 'all'):
        out_s = out.replace('.png', '_shells.png') if out and mode == 'all' else out
        render_shells(xi, output_path=out_s)

    if mode in ('voxel', 'all'):
        out_v = out.replace('.png', '_voxel.png') if out and mode == 'all' else out
        render_voxel(x, y, z_cart, output_path=out_v)


if __name__ == '__main__':
    main()
