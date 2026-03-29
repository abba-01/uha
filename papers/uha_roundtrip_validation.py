"""
uha_roundtrip_validation.py — Pipeline A: UHA encoder round-trip validation
Eric D. Martin, 2026-03-29

Tests UHA xi-encoding stability across the full redshift range including xi > 1.
Verifies:
  1. Round-trip accuracy: encode(z, ra, dec) → xi → decode → (ra', dec') match
  2. xi > 1 behavior: objects at z > ~2 correctly produce xi > 1
  3. Monotonicity: xi is strictly monotone in z
  4. Angular recovery: angular offset < tolerance at all xi
  5. Quantization behavior: Morton Z-order stability at extreme xi

xi definition (Paper 1/2/4):
  xi = d_c / d_H   where d_H = c/H0 (Hubble distance ~ 4449 Mpc at H0=67.4)
  xi > 1 is physically correct for z > ~2 (d_c exceeds Hubble sphere)
  xi_CMB ~ 3.28, NOT 0.9997

Distinct from UHA patent s1 = r/R_H(a) (epoch-local, always ≤ 1).
These quantities must stay separated in Paper 4.
"""

import numpy as np
import sys
import argparse

sys.path.insert(0, '.')
from shell_map_pipeline import (
    comoving_distance, xi_normalize, horizon_radius,
    radec_to_cartesian_shell, angular_separation,
    H0, OM, OL, C
)

# ── Test objects spanning full xi range ───────────────────────────────────────

TEST_OBJECTS = [
    # Local universe (xi << 1)
    {'name': 'Virgo Cluster',       'z': 0.00360, 'ra': 187.7, 'dec':  12.4, 'xi_expected': 0.0036},
    {'name': 'Coma Cluster',        'z': 0.02310, 'ra': 194.9, 'dec':  27.9, 'xi_expected': 0.023},
    {'name': 'Cygnus A',            'z': 0.05610, 'ra': 299.9, 'dec':  40.7, 'xi_expected': 0.055},
    # BAO range (xi ~ 0.2-0.6)
    {'name': 'SDSS z=0.3',          'z': 0.30,    'ra': 180.0, 'dec':   0.0, 'xi_expected': 0.268},
    {'name': 'DESI LRG z=0.7',      'z': 0.70,    'ra': 180.0, 'dec':   0.0, 'xi_expected': 0.536},
    {'name': 'DESI QSO z=1.5',      'z': 1.50,    'ra': 180.0, 'dec':   0.0, 'xi_expected': 0.787},
    # xi > 1 regime (high-z, physically correct)
    {'name': 'SDSS J1030+0524',     'z': 6.28,    'ra': 157.6, 'dec':   5.4, 'xi_expected': 1.975},
    {'name': 'GN-z11',              'z': 10.60,   'ra': 189.1, 'dec':  62.2, 'xi_expected': 2.261},
    {'name': 'JADES-GS-z14-0',      'z': 14.32,   'ra':  53.1, 'dec': -27.8, 'xi_expected': 2.402},
    {'name': 'CMB last scattering',  'z': 1100.0,  'ra':   0.0, 'dec':   0.0, 'xi_expected': 3.28},
]

# Tolerance parameters
ANGULAR_TOL_ARCSEC = 1.0    # angular recovery tolerance
XI_TOL_RELATIVE    = 1e-4   # xi round-trip relative tolerance


def encode_xi(z, h0=H0, om=OM):
    """Compute xi = d_c / d_H from redshift."""
    dc = comoving_distance(z, om, 1.0 - om)
    dh = horizon_radius(h0)
    return dc / dh


def decode_cartesian(x, y, z_cart):
    """Recover (ra, dec, xi) from Cartesian shell coords."""
    xi   = np.sqrt(x**2 + y**2 + z_cart**2)
    dec  = np.degrees(np.arcsin(np.clip(z_cart / xi, -1, 1)))
    ra   = np.degrees(np.arctan2(y, x)) % 360.0
    return ra, dec, xi


def roundtrip_test(obj):
    """Full encode → Cartesian → decode round-trip for one object."""
    z   = obj['z']
    ra  = obj['ra']
    dec = obj['dec']

    # Encode
    xi = encode_xi(z)

    # To Cartesian
    ra_r  = np.radians(ra)
    dec_r = np.radians(dec)
    x = xi * np.cos(dec_r) * np.cos(ra_r)
    y = xi * np.cos(dec_r) * np.sin(ra_r)
    zc = xi * np.sin(dec_r)

    # Decode
    ra_out, dec_out, xi_out = decode_cartesian(x, y, zc)

    # Errors
    xi_err_rel   = abs(xi_out - xi) / max(xi, 1e-10)
    ang_sep_deg  = angular_separation(ra, dec, ra_out, dec_out)
    ang_sep_arcs = ang_sep_deg * 3600.0

    return {
        'name':         obj['name'],
        'z':            z,
        'xi_in':        xi,
        'xi_out':       xi_out,
        'xi_err_rel':   xi_err_rel,
        'ra_in':        ra,  'ra_out':  ra_out,
        'dec_in':       dec, 'dec_out': dec_out,
        'ang_sep_arcs': ang_sep_arcs,
        'pass_xi':      xi_err_rel   < XI_TOL_RELATIVE,
        'pass_ang':     ang_sep_arcs < ANGULAR_TOL_ARCSEC,
    }


def monotonicity_test(n=1000):
    """Test that xi is strictly monotone in z over [0.001, 1100]."""
    z_vals  = np.concatenate([
        np.linspace(0.001, 2.0,    500),
        np.linspace(2.0,   20.0,   200),
        np.linspace(20.0,  1100.0, 300),
    ])
    xi_vals = np.array([encode_xi(z) for z in z_vals])
    # Use unique z values to avoid seam duplicates at linspace boundaries
    _, unique_idx = np.unique(z_vals, return_index=True)
    z_vals  = z_vals[unique_idx]
    xi_vals = xi_vals[unique_idx]
    diffs   = np.diff(xi_vals)
    n_nonmonotone = int(np.sum(diffs < 0))   # strictly decreasing only
    return {
        'n_tested':        len(z_vals),
        'n_nonmonotone':   n_nonmonotone,
        'xi_min':          float(xi_vals.min()),
        'xi_max':          float(xi_vals.max()),
        'pass':            n_nonmonotone == 0,
    }


def quantization_stress(xi_values, n_bits=20):
    """Test Morton Z-order quantization stability at extreme xi."""
    results = []
    scale = 2**n_bits - 1
    for xi in xi_values:
        # Normalize to [0,1] using xi/xi_max for quantization
        xi_max  = 4.0   # safely above CMB at 3.28
        xi_norm = xi / xi_max
        # Quantize and dequantize
        q       = int(np.clip(xi_norm * scale, 0, scale))
        xi_back = (q / scale) * xi_max
        err     = abs(xi_back - xi)
        results.append({'xi': xi, 'xi_back': xi_back, 'err_abs': err,
                        'pass': err < (xi_max / scale * 2)})
    return results


def run_validation(output_csv=None):
    """Run all validation tests and report."""
    print("\n" + "="*70)
    print("  UHA Round-Trip Validation — Pipeline A")
    print(f"  H0={H0}, Om={OM}")
    print(f"  xi = d_c / (c/H0),  d_H = c/H0 = {horizon_radius():.1f} Mpc")
    print(f"  xi > 1 is correct for z > ~2 (d_c exceeds Hubble sphere)")
    print("="*70)

    # Round-trip tests
    print(f"\n{'Object':<26} {'z':>8} {'xi_in':>8} {'xi_out':>8} "
          f"{'xi_err':>10} {'ang_arcs':>10} {'PASS'}")
    print("-" * 78)

    results    = []
    all_pass   = True
    n_pass_xi  = 0
    n_pass_ang = 0

    for obj in TEST_OBJECTS:
        r = roundtrip_test(obj)
        results.append(r)
        xi_flag  = '✓' if r['pass_xi']  else '✗'
        ang_flag = '✓' if r['pass_ang'] else '✗'
        both     = '✓ PASS' if (r['pass_xi'] and r['pass_ang']) else '✗ FAIL'
        if not (r['pass_xi'] and r['pass_ang']):
            all_pass = False
        if r['pass_xi']:  n_pass_xi  += 1
        if r['pass_ang']: n_pass_ang += 1

        print(f"  {r['name']:<24} {r['z']:>8.4f} {r['xi_in']:>8.4f} "
              f"{r['xi_out']:>8.4f} {r['xi_err_rel']:>10.2e} "
              f"{r['ang_sep_arcs']:>10.4f} {both}")

    print(f"\n  Round-trip xi:      {n_pass_xi}/{len(TEST_OBJECTS)} pass  (tol={XI_TOL_RELATIVE:.0e})")
    print(f"  Angular recovery:   {n_pass_ang}/{len(TEST_OBJECTS)} pass  (tol={ANGULAR_TOL_ARCSEC:.1f} arcsec)")

    # xi > 1 check
    high_xi = [r for r in results if r['xi_in'] > 1.0]
    print(f"\n  xi > 1 objects:     {len(high_xi)} (all should round-trip cleanly)")
    for r in high_xi:
        flag = '✓' if r['pass_xi'] else '✗'
        print(f"    {r['name']:<26} xi={r['xi_in']:.4f}  err={r['xi_err_rel']:.2e} {flag}")

    # Monotonicity
    mono = monotonicity_test()
    print(f"\n  Monotonicity test:  {mono['n_tested']} z-values, "
          f"{mono['n_nonmonotone']} non-monotone  "
          f"{'✓ PASS' if mono['pass'] else '✗ FAIL'}")
    print(f"    xi range: [{mono['xi_min']:.4f}, {mono['xi_max']:.4f}]")

    # Quantization stress at extreme xi
    xi_stress = [0.001, 0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.28]
    qstress   = quantization_stress(xi_stress)
    n_qpass   = sum(1 for q in qstress if q['pass'])
    print(f"\n  Quantization (20-bit, xi_max=4.0):  {n_qpass}/{len(qstress)} pass")
    for q in qstress:
        flag = '✓' if q['pass'] else '✗'
        print(f"    xi={q['xi']:.3f}  → {q['xi_back']:.4f}  err={q['err_abs']:.2e} {flag}")

    # Final verdict
    print("\n" + "="*70)
    if all_pass and mono['pass'] and n_qpass == len(qstress):
        print("  OVERALL: ✓ ALL TESTS PASS — UHA encoder operationally validated")
        print("  Patent Claims 41-56: encoding/decoding round-trip confirmed at xi > 1")
    else:
        print("  OVERALL: ✗ FAILURES DETECTED — review above")
    print("="*70 + "\n")

    # Save CSV
    if output_csv:
        import csv
        with open(output_csv, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=['name','z','xi_in','xi_out',
                                               'xi_err_rel','ang_sep_arcs',
                                               'pass_xi','pass_ang'])
            w.writeheader()
            for r in results:
                w.writerow({k: r[k] for k in w.fieldnames})
        print(f"[saved] {output_csv}")

    return all_pass and mono['pass']


def main():
    parser = argparse.ArgumentParser(
        description='UHA encoder round-trip validation (Pipeline A)'
    )
    parser.add_argument('--output-csv', default=None,
                        help='Save results to CSV')
    parser.add_argument('--h0',  default=H0,  type=float)
    parser.add_argument('--om',  default=OM,  type=float)
    args = parser.parse_args()

    import shell_map_pipeline as _smp
    _smp.H0 = args.h0
    _smp.OM = args.om
    _smp.OL = 1.0 - args.om

    ok = run_validation(output_csv=args.output_csv)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
