"""
UHA Cepheid ξ Test — Proper Zero-Bias Test
==========================================
Author: Eric D. Martin / All Your Baseline LLC
Date: 2026-03-24

Tests the UHA claim against the ACTUAL source of the Hubble tension.

The tension comes from comparing two independent distance measurements
for the same 77 Cepheid calibrator hosts:
  - CEPH_DIST: geometric distance (Cepheid period-luminosity, anchored to
    LMC eclipsing binaries / MW parallax / NGC 4258 megamaser) — H₀-independent
  - d_c(z): cosmological distance from redshift — depends on Ω_m, H₀

For very nearby objects (z < 0.05), ξ_cosmo ≈ z (essentially model-free).
ξ_ceph = d_c_ceph × H₀ / c — DOES depend on which H₀ you use.

UHA question: is the Cepheid vs cosmological distance discrepancy smaller
in ξ space than in d_L space?

Specifically:
  δ_dL = (d_L_ceph - d_L_cosmo) / d_L_cosmo   [fractional distance residual]
  δ_xi = (ξ_ceph   - ξ_cosmo)  / ξ_cosmo       [fractional ξ residual]

If UHA is right: δ_xi << δ_dL under a correctly-chosen H₀.
The H₀ that minimises δ_xi across all 77 calibrators IS the true H₀.
"""

import numpy as np
import pandas as pd
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
import matplotlib.pyplot as plt
import os

c_kms = 299792.458  # km/s

# ---------------------------------------------------------------------------
# Cosmologies
# ---------------------------------------------------------------------------
SH0ES  = dict(H0=73.04, Om0=0.334)
PLANCK = dict(H0=67.4,  Om0=0.315)
cosmo_shoes  = FlatLambdaCDM(**SH0ES)
cosmo_planck = FlatLambdaCDM(**PLANCK)

# ---------------------------------------------------------------------------
# Load calibrators only
# ---------------------------------------------------------------------------
data_path = os.path.join(os.path.dirname(__file__), '..', 'Pantheon+_Data',
                         '4_DISTANCES_AND_COVAR', 'Pantheon+SH0ES.dat')
df = pd.read_csv(data_path, sep=r'\s+')
cal = df[df['IS_CALIBRATOR'] == 1].copy()
print(f"Calibrators: {len(cal)} rows, {cal['CID'].nunique()} unique SNe")

# ---------------------------------------------------------------------------
# Convert CEPH_DIST (distance modulus μ) → d_c [Mpc]
# μ = 5 log10(d_L / 10 pc) → d_L [Mpc] = 10^((μ-25)/5)
# d_c = d_L / (1 + z)   (luminosity distance → comoving, nearby approx exact)
# ---------------------------------------------------------------------------
z = cal['zCMB'].values
mu_ceph = cal['CEPH_DIST'].values
mu_sn   = cal['MU_SH0ES'].values
mu_err  = cal['MU_SH0ES_ERR_DIAG'].values

d_L_ceph = 10 ** ((mu_ceph - 25) / 5)   # Mpc
d_c_ceph = d_L_ceph / (1 + z)            # Mpc (comoving)

# ---------------------------------------------------------------------------
# Cosmological comoving distance from redshift
# ---------------------------------------------------------------------------
d_c_shoes  = cosmo_shoes.comoving_distance(z).to(u.Mpc).value
d_c_planck = cosmo_planck.comoving_distance(z).to(u.Mpc).value

# Horizon distances
d_H_shoes  = c_kms / SH0ES['H0']
d_H_planck = c_kms / PLANCK['H0']

# ---------------------------------------------------------------------------
# ξ values
# ---------------------------------------------------------------------------
# Cepheid-based ξ under each H₀
xi_ceph_shoes  = d_c_ceph / d_H_shoes
xi_ceph_planck = d_c_ceph / d_H_planck

# Cosmology-based ξ (H₀ cancels → ≈ z for small z)
xi_cosmo_shoes  = d_c_shoes  / d_H_shoes
xi_cosmo_planck = d_c_planck / d_H_planck

# ---------------------------------------------------------------------------
# Residuals
# ---------------------------------------------------------------------------
# Under SH0ES cosmology: Cepheid ξ vs model ξ
delta_xi_shoes  = xi_ceph_shoes  - xi_cosmo_shoes
delta_xi_planck = xi_ceph_planck - xi_cosmo_planck

# Same in d_L space (standard comparison)
d_L_cosmo_shoes  = d_c_shoes  * (1 + z)
d_L_cosmo_planck = d_c_planck * (1 + z)

delta_dL_shoes  = (d_L_ceph - d_L_cosmo_shoes)  / d_L_cosmo_shoes
delta_dL_planck = (d_L_ceph - d_L_cosmo_planck) / d_L_cosmo_planck

# Also compare MU_SH0ES vs CEPH_DIST directly (the calibration residual)
delta_mu = mu_sn - mu_ceph

# ---------------------------------------------------------------------------
# What H₀ minimises the Cepheid vs cosmo residual in ξ space?
# For nearby objects: d_c_cosmo ≈ cz/H₀, d_H = c/H₀ → ξ_cosmo ≈ z
# ξ_ceph = d_c_ceph × H₀ / c
# δξ = 0 when ξ_ceph = ξ_cosmo ≈ z → H₀_implied = c × z / d_c_ceph
# ---------------------------------------------------------------------------
H0_implied = c_kms * z / d_c_ceph   # km/s/Mpc per object

# ---------------------------------------------------------------------------
# Deduplicate by SN (some appear multiple times for different surveys)
# ---------------------------------------------------------------------------
cal_unique = cal.drop_duplicates(subset='CID')
idx = cal.drop_duplicates(subset='CID').index
mask = cal.index.isin(idx)

# Use unique objects for statistics
z_u = z[mask]
H0_u = H0_implied[mask]
d_xi_s = delta_xi_shoes[mask]
d_xi_p = delta_xi_planck[mask]
d_dL_s = delta_dL_shoes[mask]
d_dL_p = delta_dL_planck[mask]

print(f"Unique calibrator SNe: {mask.sum()}")

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
print("\n" + "="*65)
print("UHA Cepheid ξ Test — Proper Zero-Bias Analysis")
print("="*65)

print(f"\nRaw H₀ tension: {SH0ES['H0']} vs {PLANCK['H0']} km/s/Mpc "
      f"= {(SH0ES['H0']-PLANCK['H0'])/PLANCK['H0']*100:.1f}%")

print(f"\nH₀ implied by each Cepheid calibrator (H₀ = cz / d_c_ceph):")
print(f"  Mean:   {H0_u.mean():.2f} ± {H0_u.std():.2f} km/s/Mpc")
print(f"  Median: {np.median(H0_u):.2f} km/s/Mpc")
print(f"  Range:  [{H0_u.min():.1f}, {H0_u.max():.1f}]")

print(f"\n--- Residuals in d_L space (fractional) ---")
print(f"  Under SH0ES (H₀=73.04):  mean={d_dL_s.mean()*100:.2f}%, std={d_dL_s.std()*100:.2f}%")
print(f"  Under Planck (H₀=67.4):  mean={d_dL_p.mean()*100:.2f}%, std={d_dL_p.std()*100:.2f}%")

print(f"\n--- Residuals in ξ space (fractional) ---")
print(f"  Under SH0ES (H₀=73.04):  mean={d_xi_s.mean()/np.mean(xi_cosmo_shoes[mask])*100:.2f}%, "
      f"std={d_xi_s.std()/np.mean(xi_cosmo_shoes[mask])*100:.2f}%")
print(f"  Under Planck (H₀=67.4):  mean={d_xi_p.mean()/np.mean(xi_cosmo_planck[mask])*100:.2f}%, "
      f"std={d_xi_p.std()/np.mean(xi_cosmo_planck[mask])*100:.2f}%")

print(f"\n--- SN Ia calibration residual (MU_SH0ES - CEPH_DIST) ---")
dm = delta_mu[mask]
print(f"  Mean:   {dm.mean():.4f} mag")
print(f"  Std:    {dm.std():.4f} mag")
print(f"  |Mean|: {np.abs(dm).mean():.4f} mag")

print(f"\n--- ξ cross-model comparison ---")
xi_c_s = xi_ceph_shoes[mask]
xi_c_p = xi_ceph_planck[mask]
print(f"  ξ_ceph(SH0ES) / ξ_ceph(Planck) = {(xi_c_s/xi_c_p).mean():.4f}  "
      f"(expected = H₀_SH0ES/H₀_Planck = {SH0ES['H0']/PLANCK['H0']:.4f})")
print(f"  → Cepheid ξ scales directly with H₀ (geometric distances don't cancel)")

print(f"\n--- What UHA actually claims here ---")
xi_best_H0 = H0_u.mean()
d_H_best = c_kms / xi_best_H0
xi_ceph_best = d_c_ceph[mask] / d_H_best
xi_cosmo_best = cosmo_shoes.comoving_distance(z_u).to(u.Mpc).value / d_H_best
delta_xi_best = xi_ceph_best - xi_cosmo_best
print(f"  Implied H₀ (Cepheid-ξ): {xi_best_H0:.2f} km/s/Mpc")
print(f"  At this H₀, ξ residual: mean={delta_xi_best.mean()/xi_cosmo_best.mean()*100:.3f}%, "
      f"std={delta_xi_best.std()/xi_cosmo_best.mean()*100:.3f}%")

# ---------------------------------------------------------------------------
# Honest interpretation
# ---------------------------------------------------------------------------
print(f"\n{'='*65}")
print("Honest Interpretation")
print("="*65)
tension_in_H0 = abs(SH0ES['H0'] - PLANCK['H0']) / PLANCK['H0'] * 100
tension_in_dL_planck = abs(d_dL_p.mean()) * 100
tension_in_xi_planck = abs(d_xi_p.mean()) / np.mean(xi_cosmo_planck[mask]) * 100

print(f"""
Raw H₀ tension:                     {tension_in_H0:.1f}%
d_L residual (Cepheid vs Planck):   {tension_in_dL_planck:.1f}%  (same tension, different units)
ξ residual (Cepheid vs Planck ξ):   {tension_in_xi_planck:.1f}%  (same tension, ξ didn't help here)

For GEOMETRIC distances (Cepheids), ξ = d_c × H₀/c.
H₀ does NOT cancel — it's in the denominator alone.
The tension survives in ξ space for geometric measurements.

UHA's invariance claim holds for REDSHIFT-derived positions only.
For direct-distance measurements, ξ faithfully represents the
physical distance → the tension is real and visible in ξ.

What ξ DOES clarify: the tension is between the geometric distance
scale (Cepheids) and the cosmological model. That residual
{tension_in_xi_planck:.1f}% is clean — it's not contaminated by H₀ arithmetic.
The mean implied H₀ from 77 Cepheid calibrators: {xi_best_H0:.2f} km/s/Mpc.
""")

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].scatter(z_u, H0_u, s=20, alpha=0.7, c='steelblue')
axes[0].axhline(SH0ES['H0'],  color='red',    linestyle='--', label=f'SH0ES {SH0ES["H0"]}')
axes[0].axhline(PLANCK['H0'], color='orange', linestyle='--', label=f'Planck {PLANCK["H0"]}')
axes[0].axhline(H0_u.mean(),  color='green',  linestyle='-',  label=f'Cepheid mean {H0_u.mean():.1f}')
axes[0].set_xlabel('z'); axes[0].set_ylabel('H₀ implied (km/s/Mpc)')
axes[0].set_title('H₀ implied per calibrator')
axes[0].legend(fontsize=8)

axes[1].scatter(z_u, d_xi_s*100, s=20, alpha=0.7, c='steelblue',  label='SH0ES')
axes[1].scatter(z_u, d_xi_p*100, s=20, alpha=0.7, c='darkorange', label='Planck')
axes[1].axhline(0, color='black', linewidth=0.5)
axes[1].set_xlabel('z'); axes[1].set_ylabel('Δξ / ξ_cosmo (%)')
axes[1].set_title('ξ residual: Cepheid vs cosmology model')
axes[1].legend()

bins = np.linspace(60, 85, 30)
axes[2].hist(H0_u, bins=bins, color='steelblue', alpha=0.7, label=f'n={len(H0_u)}')
axes[2].axvline(SH0ES['H0'],  color='red',    linestyle='--', label=f'SH0ES {SH0ES["H0"]}')
axes[2].axvline(PLANCK['H0'], color='orange', linestyle='--', label=f'Planck {PLANCK["H0"]}')
axes[2].axvline(H0_u.mean(),  color='green',  linestyle='-',  linewidth=2,
                label=f'Cepheid mean {H0_u.mean():.1f}±{H0_u.std():.1f}')
axes[2].set_xlabel('H₀ implied (km/s/Mpc)'); axes[2].set_ylabel('Count')
axes[2].set_title('Distribution of per-calibrator H₀')
axes[2].legend(fontsize=8)

plt.tight_layout()
out = os.path.join(os.path.dirname(__file__), 'cepheid_xi_results.png')
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"Plot saved: {out}")
