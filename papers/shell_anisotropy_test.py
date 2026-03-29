"""
shell_anisotropy_test.py — 3% residual directional coherence test
Eric D. Martin, 2026-03-29

Tests whether the residual Hubble tension (after xi-normalization removes ~90%
coordinate artifact and ~6% Omega_m deficit) is directionally coherent — i.e.,
aligned with the bulk flow toward known attractors rather than isotropic noise.

If the 3% is recirculation-driven (the "Avrocar hypothesis"), it should be:
  1. Directionally coherent — aligned with bulk flow toward Great Attractor
  2. Scale-dependent — present at xi~0.05-0.15 (local recirculation scale)
  3. Reduced by attractor masking — attractor-cone objects drive it

Method:
  - Divide sky into hemispheres aligned with known bulk flow direction
  - Compute shell density profile separately for each hemisphere
  - Compare: isotropic residual is zero; recirculation residual is non-zero
    and has opposite sign in the two hemispheres
  - Run on full catalog, flagged-removed catalog, and compare

Bulk flow direction (toward Great Attractor / Laniakea convergence zone):
  RA ~ 243 deg, Dec ~ -65 deg (Norma region, confirmed by Cosmicflows surveys)
"""

import numpy as np
import argparse
import sys

# ── Import pipeline functions ─────────────────────────────────────────────────

sys.path.insert(0, '.')
from shell_map_pipeline import (
    load_fits_catalog, load_synthetic,
    xi_normalize, flag_attractor_los, angular_separation,
    compute_shell_density, H0, OM, OL
)

# ── Bulk flow direction (Laniakea convergence zone) ───────────────────────────

BULK_FLOW = {
    'ra':  243.0,
    'dec': -65.0,
    'label': 'Great Attractor / Laniakea (Cosmicflows-3)',
    'v_kms': 630,  # Local Group bulk flow magnitude
}

CMB_DIPOLE = {
    'ra':  168.0,
    'dec': -7.0,
    'label': 'CMB dipole apex (direction of motion)',
}


def hemisphere_split(ra, dec, apex_ra, apex_dec):
    """
    Split catalog into two hemispheres relative to a direction.
    'toward' = within 90 degrees of apex (infall side)
    'away'   = more than 90 degrees from apex (outflow side)
    Returns: toward_mask, away_mask
    """
    sep = angular_separation(ra, dec, apex_ra, apex_dec)
    toward = sep < 90.0
    away   = ~toward
    return toward, away


def shell_residual_vector(xi, n_shells=20):
    """
    Compute shell density residual profile.
    Returns centers, residual (observed - expected) / sqrt(expected)
    """
    centers, counts, expected = compute_shell_density(xi, n_shells=n_shells)
    residual = (counts - expected) / np.sqrt(expected + 1)
    return centers, residual


def anisotropy_score(res_toward, res_away):
    """
    Anisotropy score: mean absolute difference between hemisphere residuals.
    Zero for isotropic; non-zero for directional signal.
    Also returns the dipole pattern (toward - away).
    """
    dipole = res_toward - res_away
    score  = np.mean(np.abs(dipole))
    return score, dipole


def run_test(ra, dec, xi, label='full catalog', flagged=None, n_shells=20):
    """Run the full anisotropy test for a given catalog."""
    print(f"\n{'='*60}")
    print(f"  Anisotropy test: {label}")
    print(f"  N = {len(xi):,}")
    print(f"{'='*60}")

    results = {}

    for direction_name, direction in [
        ('Great Attractor', BULK_FLOW),
        ('CMB dipole',      CMB_DIPOLE),
    ]:
        toward, away = hemisphere_split(ra, dec, direction['ra'], direction['dec'])

        xi_toward = xi[toward]
        xi_away   = xi[away]

        print(f"\n  Direction: {direction_name} ({direction['label']})")
        print(f"  Toward hemisphere: {toward.sum():,} objects")
        print(f"  Away hemisphere:   {away.sum():,} objects")

        centers, res_t = shell_residual_vector(xi_toward, n_shells=n_shells)
        _,       res_a = shell_residual_vector(xi_away,   n_shells=n_shells)

        score, dipole = anisotropy_score(res_t, res_a)
        print(f"  Anisotropy score: {score:.4f} sigma (0 = isotropic)")

        # Shell-by-shell breakdown
        print(f"\n  {'xi center':>10}  {'toward':>8}  {'away':>8}  {'dipole':>8}")
        for i, (c, rt, ra_, d) in enumerate(zip(centers, res_t, res_a, dipole)):
            flag = ' <<' if abs(d) > 2.0 else ''
            print(f"  {c:>10.3f}  {rt:>8.2f}  {ra_:>8.2f}  {d:>8.2f}{flag}")

        results[direction_name] = {
            'score': score,
            'dipole': dipole,
            'centers': centers,
        }

    return results


def render_anisotropy(results_full, results_masked, output_path=None):
    """Plot dipole pattern: full vs masked, both directions."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("ERROR: matplotlib not installed.")
        return

    fig, axes = plt.subplots(2, 2, figsize=(14, 8), sharex=True)
    fig.suptitle(
        'Shell Density Anisotropy Test — 3% Residual Directional Coherence\n'
        'Non-zero dipole = directionally coherent signal (recirculation hypothesis)',
        fontsize=10
    )

    directions = list(results_full.keys())
    for col, direction in enumerate(directions):
        centers = results_full[direction]['centers']
        dipole_f = results_full[direction]['dipole']
        dipole_m = results_masked[direction]['dipole']
        score_f  = results_full[direction]['score']
        score_m  = results_masked[direction]['score']

        w = centers[1] - centers[0]

        ax = axes[0, col]
        ax.bar(centers, dipole_f, width=w*0.9, color='steelblue', alpha=0.7)
        ax.axhline(0, color='k', lw=1)
        ax.axhline(2,  color='r', lw=1, ls='--')
        ax.axhline(-2, color='r', lw=1, ls='--')
        ax.set_title(f'{direction} — Full catalog\n(anisotropy score = {score_f:.3f})')
        ax.set_ylabel('Toward - Away (sigma)')

        ax = axes[1, col]
        ax.bar(centers, dipole_m, width=w*0.9, color='darkorange', alpha=0.7)
        ax.axhline(0, color='k', lw=1)
        ax.axhline(2,  color='r', lw=1, ls='--')
        ax.axhline(-2, color='r', lw=1, ls='--')
        ax.set_title(f'{direction} — Attractor-masked\n(anisotropy score = {score_m:.3f})')
        ax.set_xlabel('xi = d_c / d_H')
        ax.set_ylabel('Toward - Away (sigma)')

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"[render] saved -> {output_path}")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(
        description='Shell anisotropy test — 3% residual directional coherence'
    )
    parser.add_argument('--catalog', default=None)
    parser.add_argument('--ra-col',  default='RA')
    parser.add_argument('--dec-col', default='DEC')
    parser.add_argument('--z-col',   default='Z')
    parser.add_argument('--n',       default=5000, type=int)
    parser.add_argument('--z-max',   default=1.5,  type=float)
    parser.add_argument('--attractor-cone', default=15.0, type=float)
    parser.add_argument('--n-shells', default=15, type=int)
    parser.add_argument('--output',  default=None)
    args = parser.parse_args()

    if args.catalog:
        ra, dec, z = load_fits_catalog(args.catalog, args.ra_col, args.dec_col, args.z_col)
    else:
        print("[mode] synthetic catalog")
        ra, dec, z = load_synthetic(n=args.n, z_max=args.z_max)

    xi = xi_normalize(z)

    # Full catalog test
    results_full = run_test(ra, dec, xi, label='full catalog', n_shells=args.n_shells)

    # Attractor-masked test
    flagged = flag_attractor_los(ra, dec, cone_deg=args.attractor_cone, verbose=False)
    keep    = ~flagged
    results_masked = run_test(
        ra[keep], dec[keep], xi[keep],
        label=f'attractor-masked (cone={args.attractor_cone}deg)',
        n_shells=args.n_shells
    )

    # Interpretation
    print(f"\n{'='*60}")
    print("  INTERPRETATION")
    print(f"{'='*60}")
    for direction in results_full:
        sf = results_full[direction]['score']
        sm = results_masked[direction]['score']
        delta = sf - sm
        print(f"\n  {direction}:")
        print(f"    Full catalog score:    {sf:.4f}")
        print(f"    Attractor-masked score:{sm:.4f}")
        print(f"    Delta (attractor contribution): {delta:.4f}")
        if sf > 1.0:
            print(f"    >> DIRECTIONAL SIGNAL PRESENT — anisotropy exceeds 1 sigma")
            if delta > 0.2 * sf:
                print(f"    >> Attractor masking reduces signal — consistent with recirculation")
            else:
                print(f"    >> Attractor masking does not reduce signal — signal is real structure")
        else:
            print(f"    >> Consistent with isotropy at this catalog depth")
    print(f"{'='*60}\n")

    render_anisotropy(results_full, results_masked, output_path=args.output)


if __name__ == '__main__':
    main()
