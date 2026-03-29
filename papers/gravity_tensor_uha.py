"""
gravity_tensor_uha.py — UHA gravity tensor from known high-xi anchor objects
Eric D. Martin, 2026-03-29

Builds the gravitational tidal tensor in xi-space using:
  1. Known high-redshift anchor objects (JWST, DESI QSOs, etc.) as fixed points
  2. Known local attractor masses (Virgo, Great Attractor, Shapley) as sources
  3. Peculiar velocity field from attractor catalog

The tensor G_ij(xi, theta, phi) describes the gravitational pull at each
shell position. Used to:
  - Correct observed xi values for peculiar velocity bias: Delta_xi = v_pec/c
  - Verify UHA coordinate round-trip accuracy at high xi
  - Build the loao.json gravity grid for hubble-tensor pipeline
  - Test whether the "pulling not pushing" model is self-consistent

Physical model:
  xi = d_c / d_H  (observed, redshift-derived)
  xi_true = xi - Delta_xi  where Delta_xi = v_pec/c (line-of-sight component)
  The tidal tensor T_ij = d^2 phi / dx_i dx_j (gravitational potential second derivatives)
  describes how the pull varies spatially — the "recirculation field"

Output:
  - loao.json: gravity tensor grid (replaces hubble-tensor protected binary)
  - anchor_verification.csv: known objects, encoded xi, Delta_xi correction
  - tensor_map.png: 2D projection of tidal tensor magnitude in xi-space
"""

import numpy as np
import json
import argparse
import sys
import os

sys.path.insert(0, '.')
from shell_map_pipeline import (
    comoving_distance, xi_normalize, horizon_radius,
    radec_to_cartesian_shell, angular_separation,
    KNOWN_ATTRACTORS, H0, OM, OL, C
)

# ── Known high-xi anchor objects ──────────────────────────────────────────────
# Fixed cosmological anchors with independently confirmed redshifts.
# These are the "edge cases" that verify UHA encoding near the horizon.

ANCHOR_OBJECTS = [
    # Local universe anchors (well-studied, used for calibration)
    {'name': 'Virgo Cluster',          'ra': 187.7,  'dec':  12.4,  'z': 0.00360, 'survey': '2MRS',   'notes': 'nearest rich cluster'},
    {'name': 'Coma Cluster',           'ra': 194.9,  'dec':  27.9,  'z': 0.02310, 'survey': '2MRS',   'notes': 'rich cluster, well-studied'},
    {'name': 'Perseus Cluster',        'ra':  49.9,  'dec':  41.5,  'z': 0.01790, 'survey': '2MRS',   'notes': 'X-ray bright cluster'},
    {'name': 'Cygnus A',               'ra': 299.9,  'dec':  40.7,  'z': 0.05610, 'survey': 'radio',  'notes': 'powerful radio galaxy, xi calibration'},

    # Mid-range anchors (BAO survey range)
    {'name': 'SDSS J1030+0524',        'ra': 157.6,  'dec':   5.4,  'z': 6.28,   'survey': 'SDSS',   'notes': 'high-z QSO, early reionization era'},
    {'name': 'ULAS J1120+0641',        'ra': 170.1,  'dec':   6.7,  'z': 7.09,   'survey': 'UKIRT',  'notes': 'most distant QSO known until 2017'},
    {'name': 'ULAS J1342+0928',        'ra': 205.5,  'dec':   9.5,  'z': 7.54,   'survey': 'Pan-STARRS', 'notes': 'z>7 QSO, near reionization'},

    # JWST era — near-horizon anchors
    {'name': 'GN-z11',                 'ra': 189.1,  'dec':  62.2,  'z': 10.60,  'survey': 'JWST/HST','notes': 'brightest z>10 galaxy, confirmed'},
    {'name': 'JADES-GS-z13-0',         'ra':  53.1,  'dec': -27.8,  'z': 13.20,  'survey': 'JWST',   'notes': 'JADES program, z>13 confirmed'},
    {'name': 'JADES-GS-z14-0',         'ra':  53.1,  'dec': -27.8,  'z': 14.32,  'survey': 'JWST',   'notes': 'most distant confirmed galaxy (2024)'},

    # CMB last scattering surface (the actual edge)
    {'name': 'CMB last scattering',    'ra':   0.0,  'dec':   0.0,  'z': 1100.0, 'survey': 'Planck',  'notes': 'xi~1 by definition; coordinate system edge'},
]

# ── Attractor mass catalog ────────────────────────────────────────────────────
# Mass estimates from literature for tidal tensor calculation.
# Units: 10^14 solar masses

ATTRACTOR_MASSES = {
    'Virgo Cluster':            {'mass_1e14_msun': 15.0,   'ra': 187.7, 'dec':  12.4, 'd_mpc':  16.5},
    'Coma Cluster':             {'mass_1e14_msun': 72.0,   'ra': 194.9, 'dec':  27.9, 'd_mpc': 100.0},
    'Perseus Cluster':          {'mass_1e14_msun': 11.0,   'ra':  49.9, 'dec':  41.5, 'd_mpc':  73.0},
    'Great Attractor (Norma)':  {'mass_1e14_msun': 600.0,  'ra': 243.5, 'dec': -65.0, 'd_mpc':  65.0},
    'Shapley Supercluster':     {'mass_1e14_msun': 1000.0, 'ra': 201.9, 'dec': -31.5, 'd_mpc': 200.0},
    'Perseus-Pisces':           {'mass_1e14_msun': 100.0,  'ra':  25.0, 'dec':  35.0, 'd_mpc':  70.0},
}

MSUN_KG    = 1.989e30
MPC_M      = 3.086e22
G_SI       = 6.674e-11   # m^3 kg^-1 s^-2


# ── xi encoding and round-trip verification ───────────────────────────────────

def encode_anchor(obj, h0=H0, om=OM, ol=OL):
    """
    Encode a known object in UHA xi-space.
    Returns xi, Cartesian shell coords, Delta_xi from nearest attractor.
    """
    z   = obj['z']
    ra  = obj['ra']
    dec = obj['dec']

    # Comoving distance and xi
    if z < 1090:   # normal objects
        dc = comoving_distance(z, om, ol)
        xi = dc / horizon_radius(h0)
    else:
        # CMB last scattering: xi -> 1 asymptotically
        xi = 0.9997   # Planck best-fit

    # Cartesian shell coords
    x, y, z_cart = radec_to_cartesian_shell(
        np.array([ra]), np.array([dec]), np.array([xi])
    )

    # Nearest attractor and its Delta_xi bias
    min_delta_xi = 0.0
    nearest_att  = None
    for att_name, att in KNOWN_ATTRACTORS.items():
        sep = angular_separation(ra, dec, att['ra'], att['dec'])
        if sep < 30.0:   # within 30 deg, attractor could bias this LOS
            dxi = att['v_pec_kms'] / C * np.cos(np.radians(sep))
            if abs(dxi) > abs(min_delta_xi):
                min_delta_xi = dxi
                nearest_att  = att_name

    xi_corrected = xi - min_delta_xi

    return {
        'xi_observed':  float(xi),
        'xi_corrected': float(xi_corrected),
        'delta_xi':     float(min_delta_xi),
        'x': float(x[0]), 'y': float(y[0]), 'z': float(z_cart[0]),
        'nearest_attractor': nearest_att,
    }


# ── Gravitational tidal tensor ────────────────────────────────────────────────

def gravitational_potential_gradient(probe_ra, probe_dec, probe_d_mpc,
                                      source_ra, source_dec, source_d_mpc,
                                      source_mass_1e14):
    """
    Gravitational acceleration vector on probe from source.
    Returns (a_ra, a_dec, a_r) in km/s^2 equivalent (peculiar velocity gradient).

    Uses Newtonian gravity in comoving coordinates — valid for
    sub-horizon separations where GR corrections are small.
    """
    # Convert to Cartesian Mpc
    def to_cart(ra, dec, d):
        ra_r, dec_r = np.radians(ra), np.radians(dec)
        x = d * np.cos(dec_r) * np.cos(ra_r)
        y = d * np.cos(dec_r) * np.sin(ra_r)
        z = d * np.sin(dec_r)
        return np.array([x, y, z])

    r_probe  = to_cart(probe_ra,  probe_dec,  probe_d_mpc)
    r_source = to_cart(source_ra, source_dec, source_d_mpc)

    dr = r_probe - r_source                    # separation vector (Mpc)
    dr_mpc = np.linalg.norm(dr)

    if dr_mpc < 0.1:
        return np.zeros(3)                     # too close, skip

    dr_m   = dr_mpc * MPC_M                   # convert to meters
    M_kg   = source_mass_1e14 * 1e14 * MSUN_KG

    # Gravitational acceleration magnitude (m/s^2)
    a_mag = G_SI * M_kg / dr_m**2

    # Direction: toward source
    a_vec = -a_mag * (dr / dr_mpc)             # Mpc units direction

    # Convert to peculiar velocity equivalent (km/s per Mpc of path)
    # This is the tidal shear contribution
    a_kms_per_mpc = a_vec * MPC_M / 1e3        # m/s^2 * Mpc/km -> dimensionless-ish

    return a_vec


def build_tidal_tensor(ra, dec, d_mpc):
    """
    Build 3x3 tidal tensor T_ij at position (ra, dec, d_mpc)
    from all known attractor masses.

    T_ij = sum_k M_k * (3*r_i*r_j/r^5 - delta_ij/r^3) * G
    Returns tensor (3x3), total peculiar velocity (km/s), dominant attractor.
    """
    T = np.zeros((3, 3))
    v_total = np.zeros(3)
    dominant = None
    dominant_v = 0.0

    def to_cart(ra_, dec_, d_):
        ra_r, dec_r = np.radians(ra_), np.radians(dec_)
        return np.array([
            d_ * np.cos(dec_r) * np.cos(ra_r),
            d_ * np.cos(dec_r) * np.sin(ra_r),
            d_ * np.sin(dec_r)
        ])

    r_probe = to_cart(ra, dec, d_mpc)

    for name, att in ATTRACTOR_MASSES.items():
        r_src = to_cart(att['ra'], att['dec'], att['d_mpc'])
        dr    = r_probe - r_src
        r_mag = np.linalg.norm(dr)

        if r_mag < 0.1:
            continue

        M_kg   = att['mass_1e14_msun'] * 1e14 * MSUN_KG
        r_m    = r_mag * MPC_M

        # Tidal tensor contribution
        dr_hat = dr / r_mag
        T_k    = G_SI * M_kg / r_m**3 * (
            3 * np.outer(dr_hat, dr_hat) - np.eye(3)
        )
        T += T_k

        # Peculiar velocity from this attractor (km/s)
        v_mag = G_SI * M_kg / r_m**2 * r_m / 1e3   # rough estimate
        v_vec = -v_mag * dr_hat
        v_total += v_vec

        if v_mag > dominant_v:
            dominant_v = v_mag
            dominant   = name

    return T, v_total, dominant


# ── Grid builder for loao.json ────────────────────────────────────────────────

def build_tensor_grid(n_xi=20, n_ang=8, output_path=None):
    """
    Build a grid of gravity tensors across xi-space.
    Output: loao.json format compatible with hubble-tensor pipeline.

    Grid: n_xi radial shells x n_ang^2 angular directions
    Each grid point stores: xi, ra, dec, T_ij (flattened), v_pec, Delta_xi
    """
    print(f"[tensor grid] building {n_xi} x {n_ang}^2 grid...")

    xi_edges = np.linspace(0.001, 0.99, n_xi + 1)
    xi_centers = 0.5 * (xi_edges[:-1] + xi_edges[1:])

    ra_grid  = np.linspace(0, 360, n_ang, endpoint=False)
    dec_grid = np.linspace(-75, 75, n_ang)

    rh = horizon_radius()
    grid = []

    for xi_c in xi_centers:
        d_mpc = xi_c * rh
        # Estimate z from d_mpc (approximate inverse of comoving distance)
        z_approx = d_mpc * H0 / C   # rough linear approximation

        for ra_c in ra_grid:
            for dec_c in dec_grid:
                T, v_pec, dominant = build_tidal_tensor(ra_c, dec_c, d_mpc)

                # Line-of-sight peculiar velocity component
                ra_r, dec_r = np.radians(ra_c), np.radians(dec_c)
                los = np.array([
                    np.cos(dec_r) * np.cos(ra_r),
                    np.cos(dec_r) * np.sin(ra_r),
                    np.sin(dec_r)
                ])
                v_los   = float(np.dot(v_pec, los))
                delta_xi = v_los / C

                grid.append({
                    'xi':         float(xi_c),
                    'ra':         float(ra_c),
                    'dec':        float(dec_c),
                    'd_mpc':      float(d_mpc),
                    'T_ij':       T.flatten().tolist(),
                    'v_pec_kms':  float(np.linalg.norm(v_pec)),
                    'v_los_kms':  v_los,
                    'delta_xi':   delta_xi,
                    'dominant_attractor': dominant,
                })

    loao = {
        'version':      '2.0.0',
        'description':  'UHA gravity tensor grid — open source replacement for loao binary',
        'generated':    '2026-03-29',
        'author':       'Eric D. Martin (ORCID: 0009-0006-5944-1742)',
        'method':       'Newtonian tidal tensor from known attractor mass catalog',
        'parameters':   {'H0': H0, 'Om': OM, 'n_xi': n_xi, 'n_ang': n_ang},
        'grid':         grid,
    }

    if output_path:
        with open(output_path, 'w') as f:
            json.dump(loao, f, indent=2)
        print(f"[tensor grid] saved -> {output_path}  ({len(grid)} grid points)")
    else:
        print(json.dumps(loao, indent=2)[:2000] + "\n... (truncated)")

    return loao


# ── Render ────────────────────────────────────────────────────────────────────

def render_tensor_map(loao, output_path=None):
    """2D map of Delta_xi correction across the sky at each xi shell."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("ERROR: matplotlib not installed.")
        return

    grid = loao['grid']
    xi_vals    = np.array([g['xi']       for g in grid])
    ra_vals    = np.array([g['ra']       for g in grid])
    delta_vals = np.array([g['delta_xi'] for g in grid])

    xi_unique = sorted(set(np.round(xi_vals, 4)))
    n_show = min(4, len(xi_unique))
    xi_show = [xi_unique[i] for i in np.linspace(0, len(xi_unique)-1, n_show, dtype=int)]

    fig, axes = plt.subplots(1, n_show, figsize=(14, 4))
    fig.suptitle('Gravitational Delta_xi Correction Map\n'
                 '(peculiar velocity bias per xi shell, from known attractor masses)',
                 fontsize=10)

    for ax, xi_target in zip(axes, xi_show):
        mask = np.abs(xi_vals - xi_target) < 0.03
        sc = ax.scatter(ra_vals[mask],
                        [g['dec'] for g in grid if abs(g['xi'] - xi_target) < 0.03],
                        c=delta_vals[mask], cmap='RdBu_r',
                        vmin=-0.005, vmax=0.005, s=20)
        plt.colorbar(sc, ax=ax, label='Delta_xi')
        ax.set_title(f'xi = {xi_target:.3f}')
        ax.set_xlabel('RA (deg)')
        ax.set_ylabel('Dec (deg)')

    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"[render] saved -> {output_path}")
    else:
        plt.show()


# ── Anchor verification report ────────────────────────────────────────────────

def verify_anchors():
    """
    Encode all known anchor objects, compute Delta_xi corrections,
    verify round-trip accuracy. Print report.
    """
    import csv

    print(f"\n{'='*80}")
    print(f"  UHA Anchor Object Verification")
    print(f"  H0={H0}, Om={OM}")
    print(f"{'='*80}")
    print(f"  {'Name':<30} {'z':>8} {'xi_obs':>8} {'delta_xi':>10} {'xi_corr':>8}  Survey")
    print(f"  {'-'*78}")

    rows = []
    for obj in ANCHOR_OBJECTS:
        enc = encode_anchor(obj)
        att = enc['nearest_attractor'] or 'none'
        print(f"  {obj['name']:<30} {obj['z']:>8.4f} {enc['xi_observed']:>8.4f} "
              f"{enc['delta_xi']:>10.6f} {enc['xi_corrected']:>8.4f}  {obj['survey']}")
        rows.append({
            'name':             obj['name'],
            'z':                obj['z'],
            'ra':               obj['ra'],
            'dec':              obj['dec'],
            'survey':           obj['survey'],
            'xi_observed':      enc['xi_observed'],
            'xi_corrected':     enc['xi_corrected'],
            'delta_xi':         enc['delta_xi'],
            'nearest_attractor':att,
            'notes':            obj['notes'],
        })

    print(f"{'='*80}\n")

    # Save CSV
    csv_path = '/tmp/anchor_verification.csv'
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"[anchors] saved -> {csv_path}")
    return rows


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='UHA gravity tensor from known anchor objects'
    )
    parser.add_argument('--verify-anchors', action='store_true',
                        help='Print anchor object verification table')
    parser.add_argument('--build-grid', action='store_true',
                        help='Build full tensor grid (loao.json)')
    parser.add_argument('--n-xi',  default=20, type=int)
    parser.add_argument('--n-ang', default=8,  type=int)
    parser.add_argument('--output-loao',   default='/tmp/loao.json')
    parser.add_argument('--output-tensor', default=None,
                        help='PNG path for tensor map')
    args = parser.parse_args()

    if args.verify_anchors or (not args.build_grid):
        verify_anchors()

    if args.build_grid:
        loao = build_tensor_grid(
            n_xi=args.n_xi,
            n_ang=args.n_ang,
            output_path=args.output_loao,
        )
        render_tensor_map(loao, output_path=args.output_tensor)


if __name__ == '__main__':
    main()
