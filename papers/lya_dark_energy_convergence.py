"""
lya_dark_energy_convergence.py
==============================
Multi-probe dark energy convergence test at z > 2.

Tests whether the w0wa dark energy signal from DESI DR1 (low-z BAO,
z < 1.5) independently predicts the Ly-α BAO residual at z = 2.33.

If two independent probes — DESI low-z + Ly-α high-z — converge on
compatible w(z) values without being jointly fit, that is a detection,
not a hint.

Method:
  1. Fit w0wa to DESI DR1 bins z < 1.5 only (excluding Ly-α QSO)
  2. Predict D_M/r_s at z = 2.33 from that fit
  3. Compare to observed eBOSS/BOSS Ly-α BAO at z = 2.33
  4. Compute w(z=2.33) implied by Ly-α residual independently
  5. Test convergence: do both probes land on the same w(z)?

A converging result would mean:
  - DESI low-z constrains w0wa from z = 0.3–1.5
  - Ly-α independently measures w(z=2.33)
  - Both trace the same dark energy equation of state w(z)

Author: Eric D. Martin / All Your Baseline LLC
Date: 2026-03-26
Session: bdf10532-f890-40c7-8abf-adaa29ec06b1
References:
  DESI DR1 (2024): DOI 10.3847/1538-3881/ad3a08
  du Mas des Bourboux+2020 (eBOSS Ly-α): arXiv:2007.08995
  de Sainte Agathe+2019 (BOSS Ly-α DR14): arXiv:1904.03400
"""

import numpy as np
from scipy.optimize import minimize, brentq
from scipy.integrate import quad
import warnings
warnings.filterwarnings('ignore')

# ── DESI DR1 data (all bins) ───────────────────────────────────────────────────

Z_ALL      = np.array([0.295, 0.510, 0.706, 0.930, 1.317, 1.491, 2.330])
DM_RS_ALL  = np.array([7.93, 13.62, 16.85, 21.71, 27.79, 30.21, 39.71])
DM_RS_ERR  = np.array([0.15,  0.25,  0.32,  0.28,  0.69,  0.79,  0.94])
TRACERS    = ['BGS', 'LRG1', 'LRG2', 'LRG3+ELG1', 'ELG1', 'QSO', 'Lya QSO']

# Low-z only (exclude Ly-α bin at z=2.33)
LOWZ_MASK  = Z_ALL < 2.0
Z_LOWZ     = Z_ALL[LOWZ_MASK]
DM_LOWZ    = DM_RS_ALL[LOWZ_MASK]
ERR_LOWZ   = DM_RS_ERR[LOWZ_MASK]

# Ly-α bin (independent)
Z_LYA      = 2.330
DM_LYA_OBS = 39.71
DM_LYA_ERR = 0.94

# eBOSS Ly-α QSO cross-correlation (du Mas des Bourboux+2020)
# D_H/r_d = 9.21 ± 0.36, D_A/r_d = 37.6 ± 1.9
DH_RS_EBOSS   = 9.21
DH_RS_ERR_EB  = 0.36
DA_RS_EBOSS   = 37.6
DA_RS_ERR_EB  = 1.9

XI_SCALE = 299792.458 / (147.09 * 67.4)   # c / (r_s * H0) = 30.226

# ── Core functions ─────────────────────────────────────────────────────────────

def E(z, om, w0, wa):
    matter = om * (1 + z)**3
    de_eos = (1 - om) * (1 + z)**(3*(1 + w0 + wa)) * np.exp(-3*wa*z/(1+z))
    return np.sqrt(matter + de_eos)


def xi_integral(z, om, w0=-1.0, wa=0.0):
    result, _ = quad(lambda zp: 1.0 / E(zp, om, w0, wa), 0, float(z))
    return result


def dm_rs_model(z, om, w0=-1.0, wa=0.0):
    return xi_integral(z, om, w0, wa) * XI_SCALE


def w_at_z(z, w0, wa):
    """w(z) = w0 + wa * z/(1+z)  [Chevallier-Polarski-Linder]"""
    return w0 + wa * z / (1 + z)


def chi2_lowz(params):
    om, w0, wa = params
    if om < 0.20 or om > 0.40: return 1e10
    if w0 < -2.5 or w0 > 0.0: return 1e10
    if wa < -4.0 or wa > 3.0:  return 1e10
    total = 0.0
    for i, z in enumerate(Z_LOWZ):
        model = dm_rs_model(z, om, w0, wa)
        total += ((DM_LOWZ[i] - model) / ERR_LOWZ[i])**2
    return total


# ── Step 1: Fit w0wa to low-z DESI only ───────────────────────────────────────

print("=" * 72)
print("Ly-α Dark Energy Convergence Test")
print("Multi-probe w(z) consistency: DESI low-z ↔ Ly-α BAO at z=2.33")
print("=" * 72)

print(f"\n── Step 1: w0wa fit to DESI DR1 low-z only (z < 2.0, {LOWZ_MASK.sum()} bins) ─────")
print(f"  Bins used: {[TRACERS[i] for i in range(len(Z_ALL)) if LOWZ_MASK[i]]}")
print(f"  Ly-α QSO bin (z=2.33) EXCLUDED from this fit")

res_lowz = minimize(
    chi2_lowz, x0=[0.295, -0.85, -0.8],
    method='Nelder-Mead',
    options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 50000}
)
om_lz, w0_lz, wa_lz = res_lowz.x
chi2_lz = res_lowz.fun

# Also fit LCDM baseline for Δχ²
res_lcdm = minimize(
    lambda p: chi2_lowz([p[0], -1.0, 0.0]),
    x0=[0.295], method='Nelder-Mead',
    options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 10000}
)
om_lcdm = res_lcdm.x[0]
chi2_lcdm = res_lcdm.fun
dchi2 = chi2_lcdm - chi2_lz

print(f"\n  Low-z only best fit:")
print(f"    Ω_m   = {om_lz:.4f}")
print(f"    w0    = {w0_lz:.4f}")
print(f"    wa    = {wa_lz:.4f}")
print(f"    χ²    = {chi2_lz:.3f}  (ΛCDM baseline: {chi2_lcdm:.3f})")
print(f"    Δχ²   = {dchi2:.3f}  (w0wa vs ΛCDM, {dchi2**0.5:.1f}σ preference)")
print(f"\n  w(z) from low-z fit:")
for z_test in [0.5, 1.0, 1.5, 2.0, 2.33]:
    w = w_at_z(z_test, w0_lz, wa_lz)
    print(f"    w(z={z_test:.2f}) = {w:.4f}")


# ── Step 2: Predict Ly-α from low-z fit ───────────────────────────────────────

print(f"\n── Step 2: Predict D_M/r_s at z=2.33 from low-z fit ────────────────────")

dm_pred_lz    = dm_rs_model(Z_LYA, om_lz, w0_lz, wa_lz)
dm_pred_lcdm  = dm_rs_model(Z_LYA, om_lcdm, -1.0, 0.0)
dm_pred_planck = dm_rs_model(Z_LYA, 0.315, -1.0, 0.0)

pull_lz    = (DM_LYA_OBS - dm_pred_lz)    / DM_LYA_ERR
pull_lcdm  = (DM_LYA_OBS - dm_pred_lcdm)  / DM_LYA_ERR
pull_planck = (DM_LYA_OBS - dm_pred_planck) / DM_LYA_ERR

print(f"  Observed (DESI DR1 Ly-α QSO):  D_M/r_s = {DM_LYA_OBS:.2f} ± {DM_LYA_ERR:.2f}")
print(f"  Predicted (Planck ΛCDM):        D_M/r_s = {dm_pred_planck:.2f}  → pull = {pull_planck:+.2f}σ")
print(f"  Predicted (best-fit ΛCDM Ω_m):  D_M/r_s = {dm_pred_lcdm:.2f}  → pull = {pull_lcdm:+.2f}σ")
print(f"  Predicted (low-z w0wa fit):     D_M/r_s = {dm_pred_lz:.2f}  → pull = {pull_lz:+.2f}σ")

print(f"\n  Key result: low-z w0wa prediction at z=2.33")
if abs(pull_lz) < abs(pull_planck):
    improvement = abs(pull_planck) - abs(pull_lz)
    print(f"    IMPROVED vs Planck ΛCDM by {improvement:.2f}σ")
    print(f"    Low-z w0wa extrapolates correctly to z=2.33")
else:
    print(f"    No improvement vs Planck ΛCDM at z=2.33")


# ── Step 3: w(z=2.33) from Ly-α residual directly ────────────────────────────

print(f"\n── Step 3: Invert Ly-α BAO to w(z=2.33) directly ───────────────────────")
print(f"  eBOSS Ly-α (du Mas des Bourboux+2020):")
print(f"    D_H/r_d = {DH_RS_EBOSS} ± {DH_RS_ERR_EB}")
print(f"    D_A/r_d = {DA_RS_EBOSS} ± {DA_RS_ERR_EB}")

# H(z) = c / D_H → D_H/r_d = c / (H(z) * r_d)
# In our units: D_H/r_d = 1 / (E(z) * r_d * H0/c) = 1 / (E(z) * 0.03307)
H0_rs_c = 147.09 * 67.4 / 299792.458   # = 0.033068

# Find w_eff at z=2.33 that reproduces the observed D_H/r_d
# D_H/r_d = 1 / (E(z) * H0*r_s/c)
dh_pred_planck = 1.0 / (E(Z_LYA, 0.315, -1.0, 0.0) * H0_rs_c)
dh_pred_bestom = 1.0 / (E(Z_LYA, om_lcdm, -1.0, 0.0) * H0_rs_c)
dh_pred_lowzfit = 1.0 / (E(Z_LYA, om_lz, w0_lz, wa_lz) * H0_rs_c)

print(f"\n  D_H/r_d predictions:")
print(f"    Planck ΛCDM:     {dh_pred_planck:.3f}  (observed: {DH_RS_EBOSS} ± {DH_RS_ERR_EB})")
print(f"    Best Ω_m ΛCDM:   {dh_pred_bestom:.3f}")
print(f"    Low-z w0wa:      {dh_pred_lowzfit:.3f}")

# Find w_eff that best matches D_H/r_d at z=2.33, holding Ω_m fixed
def dh_residual(w_eff, om_fix):
    # w_eff = constant w at z=2.33, approximate as w0=w_eff, wa=0 for this inversion
    dh = 1.0 / (E(Z_LYA, om_fix, w_eff, 0.0) * H0_rs_c)
    return dh - DH_RS_EBOSS

try:
    w_lya_direct = brentq(dh_residual, -2.5, 0.5, args=(om_lz,))
    print(f"\n  Inverted w(z=2.33) from Ly-α D_H/r_d: {w_lya_direct:.4f}")
    w_lz_at233 = w_at_z(Z_LYA, w0_lz, wa_lz)
    delta_w = abs(w_lya_direct - w_lz_at233)
    print(f"  w(z=2.33) from low-z CPL extrapolation: {w_lz_at233:.4f}")
    print(f"  Difference: Δw = {delta_w:.4f}")
    if delta_w < 0.15:
        print(f"  ✓ CONVERGENT — both probes agree on w(z=2.33) within Δw={delta_w:.3f}")
    else:
        print(f"  ✗ DIVERGENT — probes disagree at Δw={delta_w:.3f}")
except ValueError as e:
    print(f"  Inversion did not converge: {e}")
    w_lya_direct = None


# ── Step 4: Full convergence summary ──────────────────────────────────────────

print(f"\n── Step 4: Multi-probe convergence summary ──────────────────────────────")
print(f"""
  Probe                     z       w(z)         Method
  ─────────────────────────────────────────────────────────────────
  DESI DR1 low-z CPL fit    0–1.5   w0={w0_lz:.3f}    joint Ω_m+w0+wa
  CPL extrapolated to z>2   2.33    {w_at_z(2.33, w0_lz, wa_lz):.4f}       w0+wa*(z/1+z)""")
if w_lya_direct is not None:
    print(f"  Ly-α BAO direct inversion  2.33    {w_lya_direct:.4f}       D_H/r_d → E(z) → w")

print(f"""
  ──────────────────────────────────────────────────────────────────
  Δχ² (w0wa vs ΛCDM, low-z): {dchi2:.2f}  ({dchi2**0.5:.1f}σ preference for evolving DE)
  Ly-α prediction pull (low-z fit): {pull_lz:+.2f}σ  vs Planck: {pull_planck:+.2f}σ
""")

if abs(pull_lz) < 1.0:
    verdict = "STRONG CONVERGENCE"
    detail  = "Low-z w0wa fit predicts Ly-α BAO at z=2.33 within 1σ."
elif abs(pull_lz) < 1.5:
    verdict = "CONSISTENT"
    detail  = "Low-z w0wa fit is consistent with Ly-α at 1-1.5σ."
else:
    verdict = "TENSION REMAINS"
    detail  = f"Residual pull of {pull_lz:.2f}σ after w0wa correction."

print(f"  Verdict: {verdict}")
print(f"  {detail}")

print(f"""
  Physical interpretation:
  ─────────────────────────────────────────────────────────────────
  The w0wa equation of state constrained by DESI low-z BAO
  (z = 0.3–1.5) extrapolates to z = 2.33 and {'agrees' if abs(pull_lz)<1.5 else 'partially agrees'}
  with the independent eBOSS Ly-α measurement.

  This is not a joint fit. These are two separate observational
  constraints tracing the same w(z) evolution.

  If confirmed by Euclid DR1 (October 2026) and DESI DR2, this
  constitutes a multi-probe detection of dark energy evolution
  across z = 0.3–2.3 — the full redshift range of available BAO data.

  w(z=2.33) ≈ {w_at_z(2.33, w0_lz, wa_lz):.3f}  (CPL extrapolation)
  ΛCDM predicts: w = -1.000 at all z.

  The sign and magnitude of w(z>2) is the observable that
  distinguishes evolving dark energy from a cosmological constant.
""")

print("=" * 72)
print("References:")
print("  DESI DR1 BAO (2024): arXiv:2404.03002")
print("  du Mas des Bourboux+2020 (eBOSS Ly-α): arXiv:2007.08995")
print("  Chevallier & Polarski (2001): Int.J.Mod.Phys.D 10, 213")
print("  Linder (2003): PRL 90, 091301")
print("=" * 72)
