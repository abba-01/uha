"""
shell_map_pipeline.py — 3D ξ-normalized shell map of the observable universe
Eric D. Martin, 2026-03-29

Paper 4 prototype: converts galaxy catalog (RA, Dec, z) into UHA shell
coordinates (ξ, θ, φ) and renders a 3D structural map without H₀ assumption.

Pipeline (Claim 60):
  1. Load catalog: RA, Dec, z per galaxy
  2. Compute ξ = d_c / R_H(a) for each object
  3. Convert to 3D Cartesian shell-space: (x, y, z) = ξ·(cos Dec cos RA, cos Dec sin RA, sin Dec)
  4. Render: point cloud, density shells, or voxel map

Data sources supported:
  - Synthetic (default, runs immediately)
  - DESI DR2 BGS/LRG/ELG catalog (FITS, when available)
  - 2MRS catalog (CSV/FITS)

Usage:
  python shell_map_pipeline.py                    # synthetic data
  python shell_map_pipeline.py --catalog FILE     # real FITS catalog
  python shell_map_pipeline.py --mode shells      # shell-slice view
  python shell_map_pipeline.py --mode voxel       # density field
  python shell_map_pipeline.py --mode points      # point cloud (default)
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

    # Convert to 3D shell-space Cartesian
    x, y, z_cart = radec_to_cartesian_shell(ra, dec, xi)

    # Summary
    print_summary(ra, dec, z, xi)

    # Render
    mode = args.mode
    out  = args.output

    if mode in ('points', 'all'):
        out_p = out.replace('.png', '_points.png') if out and mode == 'all' else out
        render_points(x, y, z_cart, xi, output_path=out_p)

    if mode in ('shells', 'all'):
        out_s = out.replace('.png', '_shells.png') if out and mode == 'all' else out
        render_shells(xi, output_path=out_s)

    if mode in ('voxel', 'all'):
        out_v = out.replace('.png', '_voxel.png') if out and mode == 'all' else out
        render_voxel(x, y, z_cart, output_path=out_v)


if __name__ == '__main__':
    main()
