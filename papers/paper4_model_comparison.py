"""
paper4_model_comparison.py — Omega_m model comparison for Paper 4
Eric D. Martin, 2026-03-29

Tests whether DESI BGS/LRG corrected shell-density profiles are better
described by Planck LCDM (Omega_m=0.315) or the Paper 1/2 prediction
(Omega_m=0.290/0.295).

Method:
  Same galaxies, same FKP weights, different xi-mapping.
  xi = d_c(z, Omega_m) / d_H
  d_H = c/H0 (fixed at H0=67.4 — frame-agnostic by design)

  For each Omega_m hypothesis:
    1. Recompute xi(z) under that Omega_m
    2. Bin the FKP-weighted counts into xi shells
    3. Compare shell-density profile shape

The shape difference between models comes entirely from the d_c(z) mapping.
A lower Omega_m universe maps galaxies to slightly larger xi (more comoving
distance at same z), producing a different profile shape.

Panel outputs per dataset:
  1. Corrected shell density vs xi under Omega_m=0.315, 0.295, 0.290
  2. Residual: data - Planck LCDM (normalized)
  3. chi2 comparison: which model fits the observed FKP-weighted profile
  4. Masked vs unmasked under best-fit Omega_m

Pre-registered predictions (Papers 1 & 2):
  - Omega_m deficit: 0.290-0.295 (vs Planck 0.315)
  - w0wa: secondary signal, only in DH/rs at z=0.51-0.71
  - Shell residual should be monotonic (Omega_m-type), not wavy (w0wa-type)
"""

import numpy as np
import sys, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from shell_map_pipeline import comoving_distance, horizon_radius, H0, OM

# ── Cosmological model grid ───────────────────────────────────────────────────

OM_MODELS = {
    'Planck 2018 (0.315)':   0.315,
    'Paper 1/2 low (0.290)': 0.290,
    'Paper 1/2 mid (0.295)': 0.295,
    'DESI DR2 (0.289)':      0.289,
}

COLORS = {
    'Planck 2018 (0.315)':   '#e41a1c',   # red
    'Paper 1/2 low (0.290)': '#377eb8',   # blue
    'Paper 1/2 mid (0.295)': '#4daf4a',   # green
    'DESI DR2 (0.289)':      '#984ea3',   # purple
}

# ── Compute xi under a given Omega_m ─────────────────────────────────────────

def xi_at_om(z_array, om, h0=H0):
    """Compute xi = d_c/d_H for array of redshifts under given Omega_m."""
    dh = horizon_radius(h0)
    return np.array([comoving_distance(z, om, 1.0 - om) / dh for z in z_array])


def shell_density_weighted(xi, weights, n_shells=25, xi_max=None):
    """Bin FKP-weighted counts into xi shells."""
    if xi_max is None:
        xi_max = xi.max()
    edges   = np.linspace(xi.min(), xi_max, n_shells + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    dxi     = edges[1:] - edges[:-1]
    density = np.zeros(n_shells)
    for i in range(n_shells):
        mask = (xi >= edges[i]) & (xi < edges[i + 1])
        density[i] = weights[mask].sum() / max(dxi[i], 1e-10)
    return centers, density


# ── Load DESI catalog (raw z + FKP weights, ZWARN==0) ────────────────────────

def load_desi_raw(fits_path, z_col='Z_not4clus', weight_col='WEIGHT_FKP_NTILE',
                  zwarn_col='ZWARN', ra_col='RA', dec_col='DEC',
                  z_max=1.2, max_rows=None):
    """Load z, FKP weights, RA, DEC from DESI FITS catalog."""
    from astropy.io import fits
    with fits.open(fits_path) as hdul:
        data = hdul[1].data
        if max_rows:
            data = data[:max_rows]
        ra    = np.array(data[ra_col],    dtype=float)
        dec   = np.array(data[dec_col],   dtype=float)
        z     = np.array(data[z_col],     dtype=float)
        w     = np.array(data[weight_col],dtype=float)
        zwarn = np.array(data[zwarn_col], dtype=int)

    # Quality cuts
    ok = (zwarn == 0) & np.isfinite(z) & (z > 0.001) & (z < z_max) & \
         np.isfinite(w) & (w > 0)
    return ra[ok], dec[ok], z[ok], w[ok]


# ── Chi-squared model comparison ─────────────────────────────────────────────

def chi2_vs_model(data_density, model_density):
    """
    Chi-squared of data vs model (shape comparison).
    Both normalized to mean=1 so only shape is compared.
    """
    d = data_density / data_density.mean()
    m = model_density / model_density.mean()
    # Use Poisson-like errors: sigma ~ sqrt(N)/N -> relative error ~ 1/sqrt(counts)
    # Approximate: use |d| as variance proxy
    sigma = np.sqrt(np.abs(d)) + 1e-6
    return np.sum(((d - m) / sigma) ** 2) / len(d)


# ── Single dataset analysis ───────────────────────────────────────────────────

def run_model_comparison(fits_path, label, z_max, xi_max, n_shells=25,
                         output_prefix=None, attractor_cone=15.0,
                         max_rows=None, verbose=True):
    """
    Full model comparison for one DESI dataset.
    Returns dict of results.
    """
    from shell_map_pipeline import flag_attractor_los

    if verbose:
        print(f"\n{'='*65}")
        print(f"  Model comparison: {label}")
        print(f"  z_max={z_max}  xi_max={xi_max}")
        print(f"{'='*65}")

    if not os.path.exists(fits_path):
        print(f"  [SKIP] Not found: {fits_path}")
        return None

    # Load
    ra, dec, z, w = load_desi_raw(fits_path, z_max=z_max, max_rows=max_rows)
    if verbose:
        print(f"  Loaded {len(z):,} galaxies (ZWARN==0)")

    # Attractor masking
    flagged = flag_attractor_los(ra, dec, cone_deg=attractor_cone, verbose=False)
    keep    = ~flagged
    ra_m, dec_m, z_m, w_m = ra[keep], dec[keep], z[keep], w[keep]
    if verbose:
        print(f"  Attractor-masked: {keep.sum():,} ({keep.mean()*100:.1f}% retained)")

    results = {'label': label, 'models': {}, 'chi2': {}}

    # Compute shell profiles under each Omega_m model
    for model_name, om_val in OM_MODELS.items():
        xi      = xi_at_om(z,   om_val)
        xi_mask = xi_at_om(z_m, om_val)

        # Full catalog
        centers, density = shell_density_weighted(
            xi[xi <= xi_max], w[xi <= xi_max], n_shells=n_shells, xi_max=xi_max
        )
        # Masked catalog
        mask_ok = xi_mask <= xi_max
        centers_m, density_m = shell_density_weighted(
            xi_mask[mask_ok], w_m[mask_ok], n_shells=n_shells, xi_max=xi_max
        )

        results['models'][model_name] = {
            'om':       om_val,
            'centers':  centers,
            'density':  density,
            'centers_m':centers_m,
            'density_m':density_m,
        }

    # Reference: Planck model
    planck_density = results['models']['Planck 2018 (0.315)']['density']
    planck_centers = results['models']['Planck 2018 (0.315)']['centers']

    if verbose:
        print(f"\n  {'Model':<28} {'slope':>8} {'chi2_vs_planck':>14} {'chi2_vs_self':>12}")
        print(f"  {'-'*66}")

    for model_name, mdata in results['models'].items():
        d     = mdata['density']
        c     = mdata['centers']
        norm  = d / d.mean()
        slope = float(np.polyfit(c, norm, 1)[0])

        # Chi2 vs Planck shape (how different from Planck)
        chi2_p = chi2_vs_model(d, planck_density)

        # Chi2 vs uniform (ξ² expected — how well does it fit a simple rising model)
        xi2_expected = c**2
        chi2_s = chi2_vs_model(d, xi2_expected)

        results['chi2'][model_name] = {'vs_planck': chi2_p, 'vs_uniform': chi2_s, 'slope': slope}

        if verbose:
            marker = ' ◄ REFERENCE' if 'Planck' in model_name else ''
            print(f"  {model_name:<28} {slope:>8.4f} {chi2_p:>14.4f} {chi2_s:>12.4f}{marker}")

    # Find best-fit Omega_m (lowest chi2 vs xi^2 model)
    best_model = min(results['chi2'], key=lambda k: results['chi2'][k]['vs_uniform'])
    best_om    = OM_MODELS[best_model]
    if verbose:
        print(f"\n  Best-fit Omega_m: {best_om:.3f} ({best_model})")

    results['best_model'] = best_model
    results['best_om']    = best_om

    # ── Plot ──────────────────────────────────────────────────────────────────
    if output_prefix:
        out_png = f"{output_prefix}_{label.lower().replace(' ', '_')}.png"
        _plot_comparison(results, label, out_png, verbose)
        results['output_png'] = out_png

    return results


# ── Plot ──────────────────────────────────────────────────────────────────────

def _plot_comparison(results, label, out_png, verbose=True):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  [skip] matplotlib not available")
        return

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle(
        f'Paper 4 — Omega_m Model Comparison: {label}\n'
        f'Same galaxies, same FKP weights, different xi-mapping',
        fontsize=10
    )

    models = results['models']
    planck_d = models['Planck 2018 (0.315)']['density']

    # Panel 1: Corrected shell density, all models
    ax = axes[0, 0]
    for mname, mdata in models.items():
        c = mdata['centers']
        d = mdata['density'] / mdata['density'].mean()
        ax.plot(c, d, '-o', ms=3, color=COLORS[mname], label=mname, lw=1.5)
    # xi^2 reference
    c0 = list(models.values())[0]['centers']
    xi2 = c0**2; xi2 /= xi2.mean()
    ax.plot(c0, xi2, 'k--', lw=1, alpha=0.5, label='ξ² (uniform)')
    ax.set_title('Corrected shell density (normalized)')
    ax.set_xlabel('ξ = d_c / d_H')
    ax.set_ylabel('ρ_corr / mean')
    ax.legend(fontsize=7)

    # Panel 2: Residual vs Planck
    ax = axes[0, 1]
    for mname, mdata in models.items():
        if 'Planck' in mname:
            continue
        d_norm = mdata['density'] / mdata['density'].mean()
        p_norm = planck_d / planck_d.mean()
        c = mdata['centers']
        n = min(len(d_norm), len(p_norm))
        ax.plot(c[:n], d_norm[:n] - p_norm[:n], '-o', ms=3,
                color=COLORS[mname], label=f'{mname} − Planck', lw=1.5)
    ax.axhline(0, color='k', lw=1)
    ax.set_title('Residual vs Planck ΛCDM (Ω_m=0.315)')
    ax.set_xlabel('ξ = d_c / d_H')
    ax.set_ylabel('Δρ_corr (normalized)')
    ax.legend(fontsize=7)

    # Panel 3: Full vs masked under best-fit model
    ax = axes[1, 0]
    bm   = results['best_model']
    bdata = models[bm]
    c_f  = bdata['centers'];  d_f = bdata['density'] / bdata['density'].mean()
    c_m  = bdata['centers_m']; d_m = bdata['density_m'] / bdata['density_m'].mean()
    ax.plot(c_f, d_f, '-o', ms=3, color=COLORS[bm], label=f'Full ({bm})')
    ax.plot(c_m, d_m, '--s', ms=3, color=COLORS[bm], alpha=0.6, label='Attractor-masked')
    xi2_b = c_f**2; xi2_b /= xi2_b.mean()
    ax.plot(c_f, xi2_b, 'k--', lw=1, alpha=0.4, label='ξ² uniform')
    ax.set_title(f'Full vs masked — best fit: {bm}')
    ax.set_xlabel('ξ = d_c / d_H')
    ax.set_ylabel('ρ_corr / mean')
    ax.legend(fontsize=7)

    # Panel 4: Chi2 bar chart
    ax = axes[1, 1]
    mnames = list(results['chi2'].keys())
    chi2_vals = [results['chi2'][m]['vs_uniform'] for m in mnames]
    colors_bar = [COLORS[m] for m in mnames]
    bars = ax.bar(range(len(mnames)), chi2_vals, color=colors_bar, alpha=0.8)
    ax.set_xticks(range(len(mnames)))
    ax.set_xticklabels([m.split('(')[1].rstrip(')') for m in mnames], fontsize=8)
    ax.set_title('χ²/dof vs ξ² expected (lower = better fit to rising profile)')
    ax.set_ylabel('χ²/dof')
    for bar, val in zip(bars, chi2_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                f'{val:.3f}', ha='center', va='bottom', fontsize=7)

    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    plt.close(fig)
    if verbose:
        print(f"  [saved] {out_png}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Paper 4 Omega_m model comparison — DESI BGS/LRG vs LCDM'
    )
    parser.add_argument('--output-prefix',
                        default='/scratch/repos/uha/papers/model_comparison',
                        help='Output PNG prefix')
    parser.add_argument('--n-shells',       default=25, type=int)
    parser.add_argument('--attractor-cone', default=15.0, type=float)
    parser.add_argument('--max-rows',       default=None, type=int)
    args = parser.parse_args()

    base = '/scratch/repos/galaxy-survey-data/galaxy_catalogs/desi_dr1'

    datasets = [
        {
            'fits_path': f'{base}/BGS_BRIGHT_full.fits',
            'label':     'DESI BGS',
            'z_max':     0.40,
            'xi_max':    0.32,
        },
        {
            'fits_path': f'{base}/LRG_full.fits',
            'label':     'DESI LRG',
            'z_max':     1.10,
            'xi_max':    0.73,
        },
    ]

    all_results = {}
    for ds in datasets:
        r = run_model_comparison(
            fits_path=ds['fits_path'],
            label=ds['label'],
            z_max=ds['z_max'],
            xi_max=ds['xi_max'],
            n_shells=args.n_shells,
            output_prefix=args.output_prefix,
            attractor_cone=args.attractor_cone,
            max_rows=args.max_rows,
            verbose=True,
        )
        if r:
            all_results[ds['label']] = r

    # Summary table
    print(f"\n{'='*65}")
    print("  SUMMARY — Omega_m Model Comparison")
    print(f"{'='*65}")
    print(f"  {'Dataset':<12} {'Best Omega_m':>14} {'BGS/LRG slope':>14}")
    for dname, r in all_results.items():
        slope = r['chi2'][r['best_model']]['slope']
        print(f"  {dname:<12} {r['best_om']:>14.3f} {slope:>14.4f}")

    print(f"\n  Pre-registered prediction: Omega_m in [0.289, 0.295]")
    print(f"  Planck LCDM:              Omega_m = 0.315")
    print(f"{'='*65}\n")


if __name__ == '__main__':
    main()
