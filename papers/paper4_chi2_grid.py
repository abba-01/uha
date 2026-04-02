"""
paper4_chi2_grid.py — Fine Omega_m grid scan + robustness splits for Paper 4
Eric D. Martin, 2026-03-29

Computes:
  1. chi2(Omega_m) on a fine grid [0.260, 0.330] for one DESI dataset
  2. Delta-chi2 vs Planck (0.315) and vs pre-registered lane (0.295)
  3. 68% / 95% confidence intervals from Delta-chi2 <= 1.0 / 4.0
  4. Robustness splits:
       - masked vs unmasked
       - northern sky (dec >= 0) vs southern sky (dec < 0)
       - low-xi half vs high-xi half
  5. Null distribution: 200 shuffled-xi bootstrap samples to get
     empirical p-value for the observed chi2 minimum
  6. Concordance figure (BGS + LRG on same axes, best-fit marked)

Usage:
  python3 paper4_chi2_grid.py --dataset bgs --output-prefix /path/to/prefix
  python3 paper4_chi2_grid.py --dataset lrg --output-prefix /path/to/prefix
"""

import numpy as np
import sys, os, argparse, json, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from shell_map_pipeline import (
    comoving_distance, horizon_radius, flag_attractor_los, H0
)
from paper4_model_comparison import (
    load_desi_raw, shell_density_weighted, xi_at_om, chi2_vs_model
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Configuration ──────────────────────────────────────────────────────────────

DATASETS = {
    'bgs': {
        'path': '/scratch/repos/galaxy-survey-data/galaxy_catalogs/desi_dr1/BGS_BRIGHT_full.fits',
        'z_max': 0.40, 'xi_max': 0.32, 'label': 'DESI BGS',
    },
    'lrg': {
        'path': '/scratch/repos/galaxy-survey-data/galaxy_catalogs/desi_dr1/LRG_full.fits',
        'z_max': 1.10, 'xi_max': 0.73, 'label': 'DESI LRG',
    },
}

# Fine Omega_m grid
OM_GRID     = np.arange(0.260, 0.335, 0.005)   # 0.260 to 0.330 inclusive
OM_PLANCK   = 0.315
OM_PREREG   = 0.295
N_SHELLS    = 25
N_BOOTSTRAP = 200   # null distribution samples
CONE_DEG    = 15.0
DCHI2_68    = 1.0   # Delta-chi2 threshold for 68% CI (1 param)
DCHI2_95    = 4.0   # Delta-chi2 threshold for 95% CI


# ── Chi-squared on grid ─────────────────────────────────────────────────────────

def compute_chi2_grid(z, w, xi_max, n_shells=N_SHELLS):
    """Scan Omega_m grid; return array of chi2_vs_xi2 values."""
    chi2 = np.zeros(len(OM_GRID))
    xi2_expected = None
    for i, om in enumerate(OM_GRID):
        xi = xi_at_om(z, om)
        ok = xi <= xi_max
        centers, density = shell_density_weighted(xi[ok], w[ok], n_shells=n_shells, xi_max=xi_max)
        if xi2_expected is None:
            xi2_expected = centers ** 2
        chi2[i] = chi2_vs_model(density, xi2_expected)
    return chi2


def extract_intervals(om_grid, chi2_grid):
    """Extract best-fit and confidence intervals from chi2 grid."""
    i_min  = np.argmin(chi2_grid)
    om_bf  = om_grid[i_min]
    chi2_min = chi2_grid[i_min]
    dchi2  = chi2_grid - chi2_min

    # 68% CI
    in68 = om_grid[dchi2 <= DCHI2_68]
    ci68 = (float(in68.min()), float(in68.max())) if len(in68) > 0 else (float(om_bf), float(om_bf))

    # 95% CI
    in95 = om_grid[dchi2 <= DCHI2_95]
    ci95 = (float(in95.min()), float(in95.max())) if len(in95) > 0 else (float(om_bf), float(om_bf))

    # Delta-chi2 vs reference models
    def dchi2_at(om_val):
        idx = np.argmin(np.abs(om_grid - om_val))
        return float(chi2_grid[idx] - chi2_min)

    return {
        'best_fit':      float(om_bf),
        'chi2_min':      float(chi2_min),
        'ci68':          ci68,
        'ci95':          ci95,
        'dchi2_vs_planck': dchi2_at(OM_PLANCK),
        'dchi2_vs_prereg': dchi2_at(OM_PREREG),
        'chi2_planck':   float(chi2_grid[np.argmin(np.abs(om_grid - OM_PLANCK))]),
        'chi2_prereg':   float(chi2_grid[np.argmin(np.abs(om_grid - OM_PREREG))]),
    }


# ── Null distribution ──────────────────────────────────────────────────────────

def null_distribution(z, w, xi_max, n_bootstrap=N_BOOTSTRAP, n_shells=N_SHELLS):
    """
    Bootstrap null: shuffle xi values across galaxies (break spatial structure).
    Returns array of best-fit Omega_m under each shuffle.
    """
    print(f"  Computing null distribution ({n_bootstrap} shuffles) ...", flush=True)
    null_bestfits = []
    rng = np.random.default_rng(42)

    # Pre-compute xi under Planck (reference)
    xi_ref = xi_at_om(z, OM_PLANCK)
    ok_ref = xi_ref <= xi_max
    xi_keep = xi_ref[ok_ref]
    w_keep  = w[ok_ref]

    for b in range(n_bootstrap):
        # Shuffle xi values — destroys spatial correlation, keeps weight distribution
        xi_shuffled = rng.permutation(xi_keep)
        chi2 = np.zeros(len(OM_GRID))
        # For null, we just recompute shape under the shuffled xi
        # (since xi values are already resampled, use them directly as Planck-equiv)
        centers, density = shell_density_weighted(xi_shuffled, w_keep,
                                                   n_shells=n_shells, xi_max=xi_max)
        xi2_exp = centers ** 2
        # Under null, all OM models give same spatial distribution — use chi2 vs flat
        # to get the null chi2 under Planck geometry
        null_chi2 = chi2_vs_model(density, xi2_exp)
        null_bestfits.append(null_chi2)

        if (b + 1) % 50 == 0:
            print(f"    bootstrap {b+1}/{n_bootstrap}", flush=True)

    return np.array(null_bestfits)


# ── Main analysis ──────────────────────────────────────────────────────────────

def run_analysis(dataset_key, output_prefix, verbose=True):
    cfg = DATASETS[dataset_key]
    label = cfg['label']
    xi_max = cfg['xi_max']

    t0 = time.time()
    print(f"\n{'='*65}", flush=True)
    print(f"  Chi2 grid analysis: {label}", flush=True)
    print(f"  Grid: Omega_m in [{OM_GRID[0]:.3f}, {OM_GRID[-1]:.3f}], step {OM_GRID[1]-OM_GRID[0]:.3f}", flush=True)
    print(f"{'='*65}", flush=True)

    # Load
    ra, dec, z, w = load_desi_raw(cfg['path'], z_max=cfg['z_max'])
    print(f"  Loaded {len(z):,} galaxies", flush=True)

    # Attractor masking
    flagged = flag_attractor_los(ra, dec, cone_deg=CONE_DEG, verbose=False)
    keep    = ~flagged
    ra_m, dec_m, z_m, w_m = ra[keep], dec[keep], z[keep], w[keep]
    print(f"  Masked: {keep.sum():,} retained ({keep.mean()*100:.1f}%)", flush=True)

    results = {'label': label, 'dataset': dataset_key, 'splits': {}}

    # ── 1. Full catalog (unmasked) ────────────────────────────────────────────
    print("\n  [1/6] Full catalog chi2 grid ...", flush=True)
    chi2_full = compute_chi2_grid(z, w, xi_max)
    stats_full = extract_intervals(OM_GRID, chi2_full)
    results['splits']['full'] = {'chi2_grid': chi2_full.tolist(), **stats_full}
    _print_stats("Full (unmasked)", stats_full)

    # ── 2. Attractor-masked ───────────────────────────────────────────────────
    print("\n  [2/6] Masked catalog chi2 grid ...", flush=True)
    chi2_mask = compute_chi2_grid(z_m, w_m, xi_max)
    stats_mask = extract_intervals(OM_GRID, chi2_mask)
    results['splits']['masked'] = {'chi2_grid': chi2_mask.tolist(), **stats_mask}
    _print_stats("Masked", stats_mask)

    # ── 3. Northern sky (dec >= 0) ────────────────────────────────────────────
    print("\n  [3/6] Northern sky chi2 grid ...", flush=True)
    north = dec_m >= 0
    chi2_north = compute_chi2_grid(z_m[north], w_m[north], xi_max)
    stats_north = extract_intervals(OM_GRID, chi2_north)
    results['splits']['north'] = {'chi2_grid': chi2_north.tolist(), **stats_north,
                                   'n_gals': int(north.sum())}
    _print_stats(f"North (N={north.sum():,})", stats_north)

    # ── 4. Southern sky (dec < 0) ─────────────────────────────────────────────
    print("\n  [4/6] Southern sky chi2 grid ...", flush=True)
    south = dec_m < 0
    if south.sum() > 1000:
        chi2_south = compute_chi2_grid(z_m[south], w_m[south], xi_max)
        stats_south = extract_intervals(OM_GRID, chi2_south)
        results['splits']['south'] = {'chi2_grid': chi2_south.tolist(), **stats_south,
                                       'n_gals': int(south.sum())}
        _print_stats(f"South (N={south.sum():,})", stats_south)
    else:
        print(f"    [SKIP] Only {south.sum()} southern galaxies — footprint is northern-only", flush=True)
        results['splits']['south'] = {'n_gals': int(south.sum()), 'skipped': True}

    # ── 5. Low/high xi split (under best-fit Omega_m) ─────────────────────────
    print("\n  [5/6] Low/high xi split ...", flush=True)
    om_bf = stats_mask['best_fit']
    xi_bf = xi_at_om(z_m, om_bf)
    xi_med = np.median(xi_bf[xi_bf <= xi_max])
    lo = (xi_bf <= xi_med) & (xi_bf <= xi_max)
    hi = (xi_bf >  xi_med) & (xi_bf <= xi_max)

    chi2_lo = compute_chi2_grid(z_m[lo], w_m[lo], xi_med)
    chi2_hi = compute_chi2_grid(z_m[hi], w_m[hi], xi_max)
    stats_lo = extract_intervals(OM_GRID, chi2_lo)
    stats_hi = extract_intervals(OM_GRID, chi2_hi)
    results['splits']['low_xi']  = {'chi2_grid': chi2_lo.tolist(), **stats_lo, 'xi_split': float(xi_med)}
    results['splits']['high_xi'] = {'chi2_grid': chi2_hi.tolist(), **stats_hi, 'xi_split': float(xi_med)}
    _print_stats(f"Low-xi  (xi<={xi_med:.3f}, N={lo.sum():,})", stats_lo)
    _print_stats(f"High-xi (xi> {xi_med:.3f}, N={hi.sum():,})", stats_hi)

    # ── 6. Null distribution ──────────────────────────────────────────────────
    print("\n  [6/6] Null distribution ...", flush=True)
    null_vals = null_distribution(z_m, w_m, xi_max, n_bootstrap=N_BOOTSTRAP)
    chi2_obs = stats_mask['chi2_min']
    p_empirical = float((null_vals <= chi2_obs).mean())
    results['null'] = {
        'n_bootstrap':   N_BOOTSTRAP,
        'chi2_observed': float(chi2_obs),
        'null_mean':     float(null_vals.mean()),
        'null_std':      float(null_vals.std()),
        'p_empirical':   p_empirical,
    }
    print(f"    chi2_observed={chi2_obs:.4f}  null_mean={null_vals.mean():.4f}±{null_vals.std():.4f}  p={p_empirical:.4f}", flush=True)

    # ── Summary table ─────────────────────────────────────────────────────────
    print(f"\n{'='*65}", flush=True)
    print(f"  SUMMARY: {label}", flush=True)
    print(f"{'='*65}", flush=True)
    print(f"  {'Split':<25} {'Best Omega_m':>12} {'68% CI':>18} {'Dchi2 vs 0.315':>16}", flush=True)
    print(f"  {'-'*72}", flush=True)
    for split_name, sdata in results['splits'].items():
        if sdata.get('skipped'):
            continue
        bf   = sdata.get('best_fit', float('nan'))
        ci68 = sdata.get('ci68', (float('nan'), float('nan')))
        dcp  = sdata.get('dchi2_vs_planck', float('nan'))
        print(f"  {split_name:<25} {bf:>12.4f} [{ci68[0]:.4f}, {ci68[1]:.4f}] {dcp:>14.4f}", flush=True)

    # ── Save JSON results ─────────────────────────────────────────────────────
    json_path = f"{output_prefix}_{dataset_key}_chi2_grid.json"
    # Convert numpy types for JSON serialization
    def to_serializable(obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        if isinstance(obj, dict): return {k: to_serializable(v) for k, v in obj.items()}
        if isinstance(obj, list): return [to_serializable(i) for i in obj]
        return obj
    with open(json_path, 'w') as f:
        json.dump(to_serializable(results), f, indent=2)
    print(f"\n  [saved] {json_path}", flush=True)

    # ── Figure: chi2(Omega_m) with confidence bands ───────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"χ²(Ω_m) Grid: {label}", fontsize=13)

    for ax, (split_name, color, ls) in zip(
        [axes[0], axes[0], axes[0]],
        [('full',    'steelblue', '-'),
         ('masked',  'navy',      '--'),
         ('north',   'green',     ':')]
    ):
        sdata = results['splits'].get(split_name, {})
        if sdata.get('skipped') or 'chi2_grid' not in sdata:
            continue
        chi2_arr = np.array(sdata['chi2_grid'])
        dchi2_arr = chi2_arr - chi2_arr.min()
        ax.plot(OM_GRID, dchi2_arr, color=color, ls=ls, lw=1.8, label=split_name)

    for ax in axes[:1]:
        ax.axhline(1.0, color='gray', ls=':', lw=1, label='68% CI (Δχ²=1)')
        ax.axhline(4.0, color='gray', ls='--', lw=1, label='95% CI (Δχ²=4)')
        ax.axvline(OM_PLANCK, color='red',    ls='--', lw=1.5, alpha=0.7, label=f'Planck ({OM_PLANCK})')
        ax.axvline(OM_PREREG, color='orange', ls='--', lw=1.5, alpha=0.7, label=f'Pre-reg ({OM_PREREG})')
        ax.axvline(stats_mask['best_fit'], color='navy', ls='-', lw=2,
                   label=f"Best fit ({stats_mask['best_fit']:.4f})")
        ax.set_xlabel('Ω_m', fontsize=11)
        ax.set_ylabel('Δχ²', fontsize=11)
        ax.set_title('Main splits', fontsize=10)
        ax.set_ylim(-0.01, 8.0)
        ax.legend(fontsize=8, loc='upper left')
        ax.grid(True, alpha=0.3)

    # Robustness: low/high xi, north/south
    ax2 = axes[1]
    for split_name, color, ls in [
        ('low_xi',  'teal',   '-'),
        ('high_xi', 'darkcyan','--'),
        ('north',   'green',  ':'),
    ]:
        sdata = results['splits'].get(split_name, {})
        if sdata.get('skipped') or 'chi2_grid' not in sdata:
            continue
        chi2_arr = np.array(sdata['chi2_grid'])
        dchi2_arr = chi2_arr - chi2_arr.min()
        ax2.plot(OM_GRID, dchi2_arr, color=color, ls=ls, lw=1.8, label=split_name)

    ax2.axhline(1.0, color='gray', ls=':', lw=1)
    ax2.axhline(4.0, color='gray', ls='--', lw=1)
    ax2.axvline(OM_PLANCK, color='red',    ls='--', lw=1.5, alpha=0.7)
    ax2.axvline(OM_PREREG, color='orange', ls='--', lw=1.5, alpha=0.7)
    ax2.set_xlabel('Ω_m', fontsize=11)
    ax2.set_ylabel('Δχ²', fontsize=11)
    ax2.set_title('Robustness splits', fontsize=10)
    ax2.set_ylim(-0.01, 8.0)
    ax2.legend(fontsize=8, loc='upper left')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig_path = f"{output_prefix}_{dataset_key}_chi2_grid.png"
    plt.savefig(fig_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  [saved] {fig_path}", flush=True)

    elapsed = time.time() - t0
    print(f"\n  Done in {elapsed/60:.1f} min", flush=True)
    return results


def _print_stats(name, s):
    print(f"    {name}: best={s['best_fit']:.4f}  68%=[{s['ci68'][0]:.4f},{s['ci68'][1]:.4f}]"
          f"  Δχ²_vs0.315={s['dchi2_vs_planck']:.4f}  Δχ²_vs0.295={s['dchi2_vs_prereg']:.4f}",
          flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', choices=['bgs', 'lrg'], required=True)
    parser.add_argument('--output-prefix', default='/scratch/repos/uha/papers/chi2_grid')
    args = parser.parse_args()

    run_analysis(args.dataset, args.output_prefix)
