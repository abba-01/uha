"""
pipeline_b_completeness.py — Pipeline B: Selection-corrected shell density
Eric D. Martin, 2026-03-29

Three-tiered completeness model for Paper 4:
  Tier 1: 2MRS   — debug/stabilize (K_s < 11.75, |b| > 5°, xi < 0.17)
  Tier 2: SDSS   — bridge, intermediate depth (r < 17.77, z < 0.8)
  Tier 3: DESI   — main science (BGS z < 0.4, LRG z < 1.1)

Produces:
  1. Raw shell density profile  rho_raw(xi)
  2. Selection function         phi(xi)
  3. Corrected density profile  rho_corr(xi) = rho_raw(xi) / phi(xi)
  4. Masked vs unmasked comparison (attractor cone removal)
  5. Output PNG + CSV

Method: V_max (Schmidt 1968) — each galaxy weighted by
  w_i = 1 / V_max,i
where V_max,i = volume within which galaxy i would pass the flux/magnitude limit.

xi definition (Paper 4):
  xi = d_c / d_H,  d_H = c/H0 ~ 4449 Mpc
  xi > 1 is physically correct for z > ~2
"""

import numpy as np
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from shell_map_pipeline import (
    comoving_distance, xi_normalize, horizon_radius,
    load_fits_catalog, load_synthetic,
    flag_attractor_los, angular_separation,
    compute_shell_density, H0, OM, OL, C
)

# ── Dataset profiles ──────────────────────────────────────────────────────────

DATASETS = {
    '2mrs': {
        'label':      '2MRS (K_s < 11.75)',
        'mag_limit':  11.75,
        'mag_band':   'K_s',
        'sky_mask':   {'b_min': 5.0},      # galactic latitude cut
        'z_max':      0.05,                # xi ~ 0.05
        'xi_max':     0.17,
        'tier':       1,
        'catalog':    '/scratch/repos/galaxy-survey-data/galaxy_catalogs/2mrs/2mrs_1175.fits',
        'ra_col':     'RA',
        'dec_col':    'DEC',
        'z_col':      'ZCAT',
        'mag_col':    'K',
    },
    'sdss': {
        'label':      'SDSS DR16 (r < 17.77)',
        'mag_limit':  17.77,
        'mag_band':   'r',
        'sky_mask':   None,
        'z_max':      0.80,
        'xi_max':     0.55,
        'tier':       2,
        'catalog':    '/scratch/repos/galaxy-survey-data/galaxy_catalogs/sdss_dr16/sdss_dr16_galaxies.csv',
        'ra_col':     'RA',
        'dec_col':    'DEC',
        'z_col':      'Z',
        'mag_col':    'MODELMAG_R',
        'ext_col':    'EXTINCTION_R',      # galactic extinction correction
    },
    'desi_bgs': {
        'label':      'DESI DR1 BGS Bright',
        'mag_limit':  19.5,
        'mag_band':   'r',
        'sky_mask':   None,
        'z_max':      0.40,
        'xi_max':     0.32,
        'tier':       3,
        'catalog':    '/scratch/repos/galaxy-survey-data/galaxy_catalogs/desi_dr1/BGS_BRIGHT_full.fits',
        'ra_col':     'RA',
        'dec_col':    'DEC',
        'z_col':      'Z',
        'mag_col':    None,  # use completeness weight from catalog if present
    },
    'desi_lrg': {
        'label':      'DESI DR1 LRG',
        'mag_limit':  None,
        'mag_band':   None,
        'sky_mask':   None,
        'z_max':      1.10,
        'xi_max':     0.73,
        'tier':       3,
        'catalog':    '/scratch/repos/galaxy-survey-data/galaxy_catalogs/desi_dr1/LRG_full.fits',
        'ra_col':     'RA',
        'dec_col':    'DEC',
        'z_col':      'Z',
        'mag_col':    None,
    },
}


# ── Cosmological utilities ────────────────────────────────────────────────────

def z_from_xi(xi, h0=H0, om=OM, n=1000):
    """Invert xi(z) to z(xi) via interpolation table."""
    z_grid  = np.linspace(0.0001, 10.0, n)
    xi_grid = np.array([comoving_distance(z, om, 1.0 - om) / horizon_radius(h0)
                        for z in z_grid])
    return float(np.interp(xi, xi_grid, z_grid))


def luminosity_distance(z, om=OM, h0=H0):
    """d_L = (1+z) * d_c  [Mpc]."""
    dc = comoving_distance(z, om, 1.0 - om)
    return (1.0 + z) * dc


def distance_modulus(z, om=OM, h0=H0):
    """mu = 5 log10(d_L/10 pc)."""
    dl = luminosity_distance(z, om, h0) * 1e6   # Mpc → pc
    return 5.0 * np.log10(dl / 10.0)


def abs_magnitude(apparent_mag, z, om=OM, h0=H0, k_corr=0.0):
    """M = m - DM - K  (K-correction default 0)."""
    mu = distance_modulus(z, om, h0)
    return apparent_mag - mu - k_corr


def z_max_for_galaxy(abs_mag, mag_limit, om=OM, h0=H0, z_survey_max=10.0):
    """
    Find z_max where the galaxy would just reach the survey flux limit.
    Binary search on distance modulus.
    """
    def dm_at_z(z_):
        return distance_modulus(z_, om, h0)

    dm_limit = mag_limit - abs_mag
    # Check if galaxy is too faint to ever be included
    if dm_at_z(0.0001) > dm_limit:
        return 0.0
    # Check if galaxy is always bright enough
    if dm_at_z(z_survey_max) <= dm_limit:
        return z_survey_max

    # Binary search
    z_lo, z_hi = 0.0001, z_survey_max
    for _ in range(50):
        z_mid = 0.5 * (z_lo + z_hi)
        if dm_at_z(z_mid) < dm_limit:
            z_lo = z_mid
        else:
            z_hi = z_mid
    return 0.5 * (z_lo + z_hi)


def vmax_weight(z_obs, abs_mag, mag_limit, z_survey_max, om=OM, h0=H0):
    """
    1/V_max weight for Schmidt (1968) estimator.
    V_max = comoving volume out to min(z_max_galaxy, z_survey_max).
    """
    z_max = min(z_max_for_galaxy(abs_mag, mag_limit, om, h0, z_survey_max), z_survey_max)
    if z_max <= z_obs:
        return 1.0  # galaxy at edge — minimum weight
    dc_max = comoving_distance(z_max, om, 1.0 - om)
    v_max  = (4.0 / 3.0) * np.pi * dc_max**3
    return 1.0 / max(v_max, 1e-10)


# ── Sky mask ──────────────────────────────────────────────────────────────────

def galactic_latitude(ra_deg, dec_deg):
    """Approximate Galactic latitude from equatorial (J2000)."""
    # NGP: ra=192.86°, dec=+27.13°, l=122.93°
    ra_r  = np.radians(ra_deg)
    dec_r = np.radians(dec_deg)
    ngp_ra  = np.radians(192.8595)
    ngp_dec = np.radians(27.1284)
    sin_b = (np.sin(dec_r) * np.sin(ngp_dec) +
             np.cos(dec_r) * np.cos(ngp_dec) * np.cos(ra_r - ngp_ra))
    return np.degrees(np.arcsin(np.clip(sin_b, -1, 1)))


def apply_sky_mask(ra, dec, mask_config):
    """Return boolean mask of objects passing sky cuts."""
    if mask_config is None:
        return np.ones(len(ra), dtype=bool)
    keep = np.ones(len(ra), dtype=bool)
    if 'b_min' in mask_config:
        b = galactic_latitude(ra, dec)
        keep &= np.abs(b) >= mask_config['b_min']
    return keep


# ── Shell density with completeness correction ───────────────────────────────

def corrected_shell_density(xi, weights=None, n_shells=20, xi_max=1.0):
    """
    Shell density profile with optional 1/V_max weighting.

    Returns:
      centers   — shell xi centers
      rho_raw   — unweighted counts per shell
      rho_corr  — 1/V_max weighted density
      phi       — selection function (rho_raw / rho_corr, normalized)
    """
    xi_min  = xi.min()
    edges   = np.linspace(xi_min, min(xi.max(), xi_max), n_shells + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    dxi     = edges[1:] - edges[:-1]

    rho_raw  = np.zeros(n_shells)
    rho_corr = np.zeros(n_shells)

    if weights is None:
        weights = np.ones(len(xi))

    for i in range(n_shells):
        in_shell     = (xi >= edges[i]) & (xi < edges[i + 1])
        n_raw        = in_shell.sum()
        rho_raw[i]   = n_raw / max(dxi[i], 1e-10)
        rho_corr[i]  = weights[in_shell].sum() / max(dxi[i], 1e-10)

    # Normalize selection function so mean = 1
    phi = np.ones(n_shells)
    mask = rho_corr > 0
    if mask.any():
        ratio = rho_raw[mask] / rho_corr[mask]
        phi[mask] = ratio / ratio.mean()

    return centers, rho_raw, rho_corr, phi


# ── Load catalog with magnitude column ───────────────────────────────────────

def load_catalog_with_mag(ds_config, max_rows=None):
    """
    Load RA, DEC, Z, and optional magnitude from a catalog file.
    Supports CSV and FITS.
    """
    path = ds_config['catalog']
    if not os.path.exists(path):
        raise FileNotFoundError(f"Catalog not found: {path}")

    ra_col  = ds_config['ra_col']
    dec_col = ds_config['dec_col']
    z_col   = ds_config['z_col']
    mag_col = ds_config.get('mag_col')
    ext_col = ds_config.get('ext_col')

    ext = os.path.splitext(path)[1].lower()

    if ext == '.csv':
        import csv
        rows = []
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
                if max_rows and len(rows) >= max_rows:
                    break
        ra  = np.array([float(r[ra_col])  for r in rows])
        dec = np.array([float(r[dec_col]) for r in rows])
        z   = np.array([float(r[z_col])   for r in rows])
        mag = None
        if mag_col and mag_col in rows[0]:
            mag = np.array([float(r[mag_col]) for r in rows])
            if ext_col and ext_col in rows[0]:
                ext_corr = np.array([float(r[ext_col]) for r in rows])
                mag = mag - ext_corr  # de-redden
    elif ext in ('.fits', '.fit'):
        from astropy.io import fits
        with fits.open(path) as hdul:
            data = hdul[1].data
            if max_rows:
                data = data[:max_rows]
            ra  = np.array(data[ra_col],  dtype=float)
            dec = np.array(data[dec_col], dtype=float)
            z   = np.array(data[z_col],   dtype=float)
            mag = None
            if mag_col and mag_col in data.dtype.names:
                mag = np.array(data[mag_col], dtype=float)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    # Basic quality cuts
    valid = (np.isfinite(ra) & np.isfinite(dec) & np.isfinite(z) &
             (z > 0.0001) & (z < ds_config['z_max'] * 1.05))
    ra, dec, z = ra[valid], dec[valid], z[valid]
    if mag is not None:
        mag = mag[valid]

    return ra, dec, z, mag


# ── Full pipeline for one dataset ─────────────────────────────────────────────

def run_pipeline_b(dataset_name, n_shells=20, attractor_cone=15.0,
                   output_prefix=None, max_rows=None, verbose=True):
    """
    Full Pipeline B for a single dataset.
    Returns dict of results for downstream use.
    """
    if dataset_name not in DATASETS:
        raise ValueError(f"Unknown dataset: {dataset_name}. "
                         f"Choose from {list(DATASETS.keys())}")

    ds = DATASETS[dataset_name]
    if verbose:
        print(f"\n{'='*65}")
        print(f"  Pipeline B — {ds['label']}")
        print(f"  Tier {ds['tier']} | z_max={ds['z_max']} | xi_max={ds['xi_max']}")
        print(f"{'='*65}")

    # ── Load ──────────────────────────────────────────────────────────────────
    if not os.path.exists(ds['catalog']):
        print(f"  [SKIP] Catalog not found: {ds['catalog']}")
        return None

    if verbose:
        print(f"  Loading {ds['catalog']} ...")
    ra, dec, z, mag = load_catalog_with_mag(ds, max_rows=max_rows)
    if verbose:
        print(f"  Loaded {len(z):,} galaxies after quality cuts")

    # ── Sky mask ──────────────────────────────────────────────────────────────
    sky_ok = apply_sky_mask(ra, dec, ds['sky_mask'])
    ra, dec, z = ra[sky_ok], dec[sky_ok], z[sky_ok]
    if mag is not None:
        mag = mag[sky_ok]
    if verbose and ds['sky_mask']:
        print(f"  After sky mask: {len(z):,} galaxies")

    # ── xi coordinate ─────────────────────────────────────────────────────────
    xi = xi_normalize(z)

    # ── 1/V_max weights ───────────────────────────────────────────────────────
    weights = None
    if mag is not None and ds['mag_limit'] is not None:
        if verbose:
            print(f"  Computing 1/V_max weights (mag_limit={ds['mag_limit']})...")
        abs_mags = abs_magnitude(mag, z)
        weights  = np.array([
            vmax_weight(z[i], abs_mags[i], ds['mag_limit'], ds['z_max'])
            for i in range(len(z))
        ])
        if verbose:
            w_median = np.median(weights)
            w_max    = weights.max()
            print(f"  Weight range: median={w_median:.3e}, max={w_max:.3e}")
    else:
        weights = np.ones(len(z))
        if verbose:
            print(f"  No magnitude data — uniform weights (counts only)")

    # ── Full-sky shell density ────────────────────────────────────────────────
    centers, rho_raw, rho_corr, phi = corrected_shell_density(
        xi, weights=weights, n_shells=n_shells, xi_max=ds['xi_max']
    )

    # ── Attractor masking ─────────────────────────────────────────────────────
    flagged   = flag_attractor_los(ra, dec, cone_deg=attractor_cone, verbose=False)
    keep_mask = ~flagged
    xi_masked = xi[keep_mask]
    w_masked  = weights[keep_mask] if weights is not None else None
    centers_m, rho_raw_m, rho_corr_m, phi_m = corrected_shell_density(
        xi_masked, weights=w_masked, n_shells=n_shells, xi_max=ds['xi_max']
    )

    if verbose:
        print(f"\n  Attractor masking: {flagged.sum():,} objects removed "
              f"({flagged.mean()*100:.1f}%)")
        print(f"\n  {'xi center':>10}  {'raw':>8}  {'corrected':>10}  {'phi':>8}")
        print(f"  {'-'*42}")
        for i in range(n_shells):
            if rho_raw[i] > 0:
                print(f"  {centers[i]:>10.4f}  {rho_raw[i]:>8.1f}  "
                      f"{rho_corr[i]:>10.3e}  {phi[i]:>8.4f}")

    # ── Plot ──────────────────────────────────────────────────────────────────
    out_png = None
    if output_prefix:
        out_png = f"{output_prefix}_{dataset_name}.png"
        _plot_pipeline_b(
            dataset_name, ds, centers, rho_raw, rho_corr, phi,
            centers_m, rho_raw_m, rho_corr_m, out_png
        )

    # ── CSV output ────────────────────────────────────────────────────────────
    out_csv = None
    if output_prefix:
        out_csv = f"{output_prefix}_{dataset_name}.csv"
        _save_csv(out_csv, centers, rho_raw, rho_corr, phi,
                  centers_m, rho_raw_m, rho_corr_m)

    result = {
        'dataset':      dataset_name,
        'label':        ds['label'],
        'n_galaxies':   len(z),
        'n_masked':     keep_mask.sum(),
        'centers':      centers,
        'rho_raw':      rho_raw,
        'rho_corr':     rho_corr,
        'phi':          phi,
        'centers_m':    centers_m,
        'rho_raw_m':    rho_raw_m,
        'rho_corr_m':   rho_corr_m,
        'phi_m':        phi_m,
        'output_png':   out_png,
        'output_csv':   out_csv,
    }

    if verbose:
        print(f"\n  Done — {dataset_name}")
        if out_png:
            print(f"  [saved] {out_png}")
        if out_csv:
            print(f"  [saved] {out_csv}")

    return result


# ── Plotting ──────────────────────────────────────────────────────────────────

def _plot_pipeline_b(name, ds, centers, rho_raw, rho_corr, phi,
                     centers_m, rho_raw_m, rho_corr_m, out_png):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  [skip plot] matplotlib not available")
        return

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle(
        f'Pipeline B — Selection-Corrected Shell Density\n{ds["label"]}',
        fontsize=11
    )

    w = centers[1] - centers[0] if len(centers) > 1 else 0.01

    # Panel 1: Raw counts
    ax = axes[0, 0]
    ax.bar(centers, rho_raw, width=w*0.85, color='steelblue', alpha=0.8, label='Full sky')
    ax.bar(centers_m, rho_raw_m, width=w*0.85, color='orange', alpha=0.5, label='Attractor-masked')
    ax.set_title('Raw galaxy counts per xi shell')
    ax.set_xlabel('xi = d_c / d_H')
    ax.set_ylabel('Count / dxi')
    ax.legend(fontsize=8)

    # Panel 2: Selection function
    ax = axes[0, 1]
    ax.plot(centers, phi, 'k-o', ms=3, label='Full sky')
    ax.axhline(1.0, color='r', lw=1, ls='--')
    ax.set_title('Selection function phi(xi)')
    ax.set_xlabel('xi = d_c / d_H')
    ax.set_ylabel('phi (normalized)')
    ax.legend(fontsize=8)

    # Panel 3: Corrected density
    ax = axes[1, 0]
    norm_corr  = rho_corr  / max(rho_corr.max(),  1e-30)
    norm_corr_m = rho_corr_m / max(rho_corr_m.max(), 1e-30)
    ax.plot(centers,   norm_corr,   'b-o', ms=3, label='Full sky')
    ax.plot(centers_m, norm_corr_m, 'r-s', ms=3, label='Attractor-masked')
    ax.axhline(1.0, color='gray', lw=0.8, ls='--', label='Uniform')
    ax.set_title('Corrected shell density (normalized)')
    ax.set_xlabel('xi = d_c / d_H')
    ax.set_ylabel('rho_corr / max(rho_corr)')
    ax.legend(fontsize=8)

    # Panel 4: Residual full - masked
    ax = axes[1, 1]
    n = min(len(rho_corr), len(rho_corr_m))
    if n > 0:
        residual = norm_corr[:n] - norm_corr_m[:n]
        ax.bar(centers[:n], residual, width=w*0.85, color='purple', alpha=0.7)
        ax.axhline(0, color='k', lw=1)
        ax.set_title('Attractor contribution: (full − masked)')
        ax.set_xlabel('xi = d_c / d_H')
        ax.set_ylabel('Delta rho_corr (normalized)')

    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    plt.close(fig)


def _save_csv(path, centers, rho_raw, rho_corr, phi,
              centers_m, rho_raw_m, rho_corr_m):
    import csv
    n = max(len(centers), len(centers_m))
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['xi_center', 'rho_raw', 'rho_corr', 'phi',
                    'xi_center_masked', 'rho_raw_masked', 'rho_corr_masked'])
        for i in range(n):
            row = [
                f"{centers[i]:.5f}"   if i < len(centers)   else '',
                f"{rho_raw[i]:.4f}"   if i < len(rho_raw)   else '',
                f"{rho_corr[i]:.6e}"  if i < len(rho_corr)  else '',
                f"{phi[i]:.6f}"       if i < len(phi)        else '',
                f"{centers_m[i]:.5f}" if i < len(centers_m) else '',
                f"{rho_raw_m[i]:.4f}" if i < len(rho_raw_m) else '',
                f"{rho_corr_m[i]:.6e}"if i < len(rho_corr_m)else '',
            ]
            w.writerow(row)


# ── Multi-tier run ────────────────────────────────────────────────────────────

def run_all_tiers(output_prefix=None, attractor_cone=15.0,
                  n_shells=20, max_rows=None):
    """Run all available tiers in order (2MRS → SDSS → DESI BGS → DESI LRG)."""
    results = {}
    for name in ['2mrs', 'sdss', 'desi_bgs', 'desi_lrg']:
        try:
            r = run_pipeline_b(
                name,
                n_shells=n_shells,
                attractor_cone=attractor_cone,
                output_prefix=output_prefix,
                max_rows=max_rows,
                verbose=True,
            )
            if r:
                results[name] = r
        except FileNotFoundError as e:
            print(f"\n  [SKIP] {name}: {e}")
        except Exception as e:
            print(f"\n  [ERROR] {name}: {e}")
            import traceback; traceback.print_exc()
    return results


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Pipeline B — Selection-corrected shell density (Paper 4)'
    )
    parser.add_argument('--dataset', default='sdss',
                        choices=list(DATASETS.keys()) + ['all'],
                        help='Dataset to process (default: sdss)')
    parser.add_argument('--output-prefix', default=None,
                        help='Output file prefix (generates PNG + CSV)')
    parser.add_argument('--n-shells',       default=20, type=int)
    parser.add_argument('--attractor-cone', default=15.0, type=float)
    parser.add_argument('--max-rows',       default=None, type=int,
                        help='Limit rows for testing')
    parser.add_argument('--list-datasets',  action='store_true')
    args = parser.parse_args()

    if args.list_datasets:
        print("\nAvailable datasets:")
        for name, ds in DATASETS.items():
            exists = '✓' if os.path.exists(ds['catalog']) else '✗ (not on disk)'
            print(f"  [{ds['tier']}] {name:12s} — {ds['label']}  {exists}")
        return

    if args.dataset == 'all':
        run_all_tiers(
            output_prefix=args.output_prefix,
            attractor_cone=args.attractor_cone,
            n_shells=args.n_shells,
            max_rows=args.max_rows,
        )
    else:
        run_pipeline_b(
            args.dataset,
            n_shells=args.n_shells,
            attractor_cone=args.attractor_cone,
            output_prefix=args.output_prefix,
            max_rows=args.max_rows,
            verbose=True,
        )


if __name__ == '__main__':
    main()
