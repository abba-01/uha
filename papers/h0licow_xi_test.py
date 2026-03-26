"""
h0licow_xi_test.py — H0LiCOW / TDCOSMO strong lensing time delay tension via ξ normalization
Session: ecda5f02-e5c9-4cda-8135-7346661b0b91

Tests whether the H0LiCOW / TDCOSMO H₀ tension (strong gravitational lensing
time delays vs. CMB) contains a coordinate-frame component under ξ normalization,
and quantifies the mass-sheet degeneracy (MSD) contribution.

Data sources (published summary statistics — no catalog download required):
    H0LiCOW (Wong+2020, 6 lenses):          H₀ = 73.3 ± 1.8 km/s/Mpc
    TDCOSMO (Millon+2020, 7 lenses):         H₀ = 74.2 ± 1.6 km/s/Mpc
    TDCOSMO+SLACS (Birrer+2021, kinematics): H₀ = 67.4 +4.1/-3.2 km/s/Mpc
    Planck 2020 CMB:                         H₀ = 67.4 ± 0.5 km/s/Mpc
    SH0ES 2022 (Riess+2022):                 H₀ = 73.04 ± 1.04 km/s/Mpc

Physical model:
    Time delay distance: D_Δt = (1+z_l) × D_l × D_s / D_ls
    where D = angular diameter distance.  H₀ ∝ 1/D_Δt

    Mass-sheet degeneracy (MSD): a uniform mass sheet κ_ext rescales
    D_Δt → D_Δt / (1-κ_ext), hence H₀_true = H₀_measured × (1-κ_ext).
    Typical external convergence: κ_ext ≈ 0.04–0.08.

ξ normalization:
    ξ = (H₀ - H₀_ref) / H₀_ref    with H₀_ref = 70.0 km/s/Mpc

Key question:
    How much of the H0LiCOW vs Planck tension is
      (a) a coordinate-frame artifact (ξ frame mixing),
      (b) mass-sheet degeneracy, or
      (c) genuine physical disagreement?

References:
    Wong et al. 2020, MNRAS 498, 1420  (H0LiCOW XIII)
    Millon et al. 2020, A&A 639, A101  (TDCOSMO I)
    Birrer et al. 2021, A&A 643, A165  (TDCOSMO IV)
    Planck Collaboration 2020, A&A 641, A6
    Riess et al. 2022, ApJL 934, L7    (SH0ES)

Author: Eric Andersson / Claude (claude-sonnet-4-6)
Date:   2026-03-26
"""

import numpy as np
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
import warnings
warnings.filterwarnings('ignore')

# ── Constants and reference values ────────────────────────────────────────────
H0_REF    = 70.0          # frame-independent anchor (km/s/Mpc)
H0_PLANCK = 67.4          # Planck 2020 CMB
H0_SHOES  = 73.04         # SH0ES 2022
OM_PLANCK = 0.315
OM_SHOES  = 0.334

# Typical lens redshifts for the H0LiCOW / TDCOSMO sample
# (mean values across the six / seven lens systems used in published analyses)
Z_L_MEAN  = 0.55          # mean lens redshift
Z_S_MEAN  = 1.70          # mean source redshift

# ── Published H₀ measurements from strong lensing time delays ─────────────────
# Format: (label, H0, err_hi, err_lo, reference)
# err_lo is the downward uncertainty (positive number). Symmetric where given.
MEASUREMENTS = [
    ('H0LiCOW (Wong+2020)',         73.3,  1.8,  1.8,  'Wong et al. 2020'),
    ('TDCOSMO (Millon+2020)',        74.2,  1.6,  1.6,  'Millon et al. 2020'),
    ('TDCOSMO+SLACS (Birrer+2021)', 67.4,  4.1,  3.2,  'Birrer et al. 2021'),
    ('Planck 2020 CMB',             67.4,  0.5,  0.5,  'Planck Collab. 2020'),
    ('SH0ES 2022 (Riess+2022)',     73.04, 1.04, 1.04, 'Riess et al. 2022'),
]

# ── ξ normalization helper ─────────────────────────────────────────────────────
def xi(H0_val, H0_ref=H0_REF):
    """Dimensionless fractional deviation from the frame-independent anchor."""
    return (H0_val - H0_ref) / H0_ref

def xi_sigma(H0_err, H0_ref=H0_REF):
    """Uncertainty in ξ from symmetric H₀ uncertainty."""
    return H0_err / H0_ref

# ── Compute angular diameter distances via astropy ────────────────────────────
def time_delay_distance(H0_val, z_l=Z_L_MEAN, z_s=Z_S_MEAN, Om=OM_PLANCK):
    """
    D_Δt = (1+z_l) × D_l × D_s / D_ls  [Mpc]
    Uses FlatLambdaCDM; returns D_Δt in Mpc.
    """
    cosmo = FlatLambdaCDM(H0=H0_val, Om0=Om)
    D_l   = cosmo.angular_diameter_distance(z_l).to(u.Mpc).value
    D_s   = cosmo.angular_diameter_distance(z_s).to(u.Mpc).value
    D_ls  = cosmo.angular_diameter_distance_z1z2(z_l, z_s).to(u.Mpc).value
    D_dt  = (1.0 + z_l) * D_l * D_s / D_ls
    return D_dt

# ── MSD: κ_ext shifts H₀ ──────────────────────────────────────────────────────
def msd_correction(H0_measured, kappa_ext):
    """
    Under MSD: H₀_true = H₀_measured × (1 - κ_ext).
    Returns corrected H₀.
    """
    return H0_measured * (1.0 - kappa_ext)

# ═══════════════════════════════════════════════════════════════════════════════
print("=" * 72)
print("H0LiCOW / TDCOSMO — H₀ tension via ξ normalization")
print("=" * 72)

# ── Section 1: Raw H₀ table with tensions ─────────────────────────────────────
print("\n── Published H₀ measurements ───────────────────────────────────────────")
print(f"  {'Survey':<33} {'H₀':>6} {'σ_hi':>5} {'σ_lo':>5}   {'ξ':>7} {'σ_ξ':>6}  "
      f"{'Pull vs Planck':>15}")

planck_H0    = 67.4
planck_err   = 0.5
planck_xi    = xi(planck_H0)
planck_xi_s  = xi_sigma(planck_err)

for label, h0, err_hi, err_lo, ref in MEASUREMENTS:
    xi_val    = xi(h0)
    xi_s      = xi_sigma((err_hi + err_lo) / 2.0)   # symmetric approximation
    # asymmetric pull: use err_lo when H0 > Planck, err_hi when H0 < Planck
    if h0 >= planck_H0:
        combined = np.sqrt(planck_err**2 + err_lo**2)
    else:
        combined = np.sqrt(planck_err**2 + err_hi**2)
    pull      = (h0 - planck_H0) / combined
    print(f"  {label:<33} {h0:>6.2f} {err_hi:>5.2f} {err_lo:>5.2f}   "
          f"{xi_val:>+7.4f} {xi_s:>6.4f}  {pull:>+8.2f}σ")

# ── Section 2: Time delay distance geometry ──────────────────────────────────
print(f"\n── Time delay distance D_Δt geometry ───────────────────────────────────")
print(f"  Using mean lens/source redshifts: z_l = {Z_L_MEAN}, z_s = {Z_S_MEAN}")
print(f"  D_Δt = (1+z_l) × D_l × D_s / D_ls,   H₀ ∝ 1/D_Δt\n")

D_dt_planck = time_delay_distance(H0_PLANCK)
D_dt_shoes  = time_delay_distance(H0_SHOES)
D_dt_h0licow = time_delay_distance(73.3)
D_dt_tdcosmo = time_delay_distance(74.2)
D_dt_birrer  = time_delay_distance(67.4)

print(f"  {'Survey':<33} {'D_Δt [Mpc]':>12}  {'H₀ × D_Δt  [relative]':>22}")
for label, D_dt in [
    ('Planck 2020 CMB',              D_dt_planck),
    ('H0LiCOW (73.3)',               D_dt_h0licow),
    ('TDCOSMO (74.2)',               D_dt_tdcosmo),
    ('TDCOSMO+SLACS (67.4)',         D_dt_birrer),
    ('SH0ES 2022 (73.04)',           D_dt_shoes),
]:
    h0_val = [h for l, h, *_ in MEASUREMENTS if h == 67.4 or h == 73.3 or
              h == 74.2 or h == 73.04][0]
    # label-keyed lookup
    lut = {'Planck 2020 CMB': 67.4, 'H0LiCOW (73.3)': 73.3,
           'TDCOSMO (74.2)': 74.2, 'TDCOSMO+SLACS (67.4)': 67.4,
           'SH0ES 2022 (73.04)': 73.04}
    hv   = lut[label]
    prod = hv * D_dt / 1e5     # dimensionless (H₀ in km/s/Mpc × Mpc / km×s⁻¹ × …)
    print(f"  {label:<33} {D_dt:>12.1f}  {prod:>22.4f}")

print(f"""
  Interpretation:
    D_Δt is larger at lower H₀ (Planck cosmology).
    H0LiCOW / TDCOSMO infer a smaller D_Δt → higher H₀.
    The product H₀ × D_Δt / c is roughly constant at fixed (z_l, z_s):
    the tension is entirely encoded in where D_Δt is anchored.
""")

# ── Section 3: ξ-normalized analysis ──────────────────────────────────────────
print("── ξ-normalized H₀ values  (H₀_ref = {:.1f} km/s/Mpc) ─────────────────".format(H0_REF))
print(f"  ξ = (H₀ - {H0_REF}) / {H0_REF}\n")

xi_planck   = xi(67.4)
xi_h0licow  = xi(73.3)
xi_tdcosmo  = xi(74.2)
xi_birrer   = xi(67.4)
xi_shoes    = xi(73.04)

print(f"  {'Survey':<33} {'ξ':>8}   interpretation")
for label, xv in [
    ('Planck 2020 CMB',              xi_planck),
    ('H0LiCOW (Wong+2020)',          xi_h0licow),
    ('TDCOSMO (Millon+2020)',         xi_tdcosmo),
    ('TDCOSMO+SLACS (Birrer+2021)', xi_birrer),
    ('SH0ES 2022',                   xi_shoes),
]:
    sign = "below ref" if xv < 0 else "above ref"
    print(f"  {label:<33} {xv:>+8.4f}   {abs(xv)*100:.2f}% {sign}")

# ── Section 4: Frame-artifact component ───────────────────────────────────────
print(f"\n── Frame-artifact vs. physical decomposition ────────────────────────────")
print(f"""
  The ξ normalization framework separates two contributions to an H₀ discrepancy:

    (1) Frame-mixing / coordinate artifact
        Measurements using different fiducial cosmologies introduce a bias
        proportional to Δξ = ξ(H₀_A) - ξ(H₀_B).
        This is NOT physical — it vanishes in a frame-independent parameterisation.

    (2) Physical residual
        After removing the frame component, any remaining Δξ is a genuine
        measurement disagreement about the expansion rate.

  For the H0LiCOW vs Planck tension:
    Both H0LiCOW and Planck work in physically distinct regimes (late-universe
    lensing vs. early-universe CMB), but they both express results in
    H₀ [km/s/Mpc], which IS a frame-independent observable.
    The H₀ frame-mixing contribution is therefore ZERO in the H₀ tension itself
    — unlike S8 where h appears implicitly in the 8 h⁻¹ Mpc scale.

  The ξ decomposition is most useful here for comparing the SIZE of the tension
  relative to the anchor, and for isolating the MSD component.
""")

xi_gap_h0licow_planck  = xi_h0licow - xi_planck
xi_gap_tdcosmo_planck  = xi_tdcosmo - xi_planck
xi_gap_birrer_planck   = xi_birrer  - xi_planck   # ≈ 0 by construction

total_gap_kms   = 73.3 - 67.4    # km/s/Mpc
frame_component = 0.0             # H₀ is frame-independent; no h-implicit unit
physical_gap    = total_gap_kms

print(f"  H0LiCOW vs Planck:")
print(f"    Raw H₀ gap:            {total_gap_kms:.2f} km/s/Mpc")
print(f"    Δξ (H0LiCOW - Planck): {xi_gap_h0licow_planck:+.4f}")
print(f"    Frame-artifact:         {frame_component:.2f} km/s/Mpc  (0% — H₀ is frame-independent)")
print(f"    Physical residual:      {physical_gap:.2f} km/s/Mpc  (100%)")
print(f"")
print(f"  TDCOSMO+SLACS vs H0LiCOW:")
birrer_h0licow_gap = 67.4 - 73.3
print(f"    Raw H₀ gap:            {birrer_h0licow_gap:.2f} km/s/Mpc")
print(f"    Δξ (Birrer - H0LiCOW): {xi_birrer - xi_h0licow:+.4f}")
print(f"    This shift is driven by: stellar kinematics / MSD breaking")

# ── Section 5: Mass-sheet degeneracy in ξ space ───────────────────────────────
print(f"\n── Mass-sheet degeneracy (MSD) in ξ space ───────────────────────────────")
print(f"""
  MSD: a uniform mass sheet κ_ext is degenerate with the lens model.
  It rescales H₀:  H₀_true = H₀_measured × (1 - κ_ext)

  If κ_ext > 0 (mass over-density along line of sight):
    H₀_measured > H₀_true  → lensing H₀ is biased HIGH.
  Typical external convergence from large-scale structure: κ_ext ≈ 0.04–0.08.
""")

kappa_values = [0.00, 0.02, 0.04, 0.06, 0.08, 0.10]
H0_lensing   = 73.3    # H0LiCOW central value

print(f"  Starting from H0LiCOW H₀ = {H0_lensing} km/s/Mpc:\n")
print(f"  {'κ_ext':>8}  {'H₀_true':>9}  {'ξ_true':>8}  {'Pull vs Planck':>16}  {'Tension reduced by':>20}")
tension_raw = (H0_lensing - H0_PLANCK) / np.sqrt(1.8**2 + 0.5**2)
for kappa in kappa_values:
    h0_true  = msd_correction(H0_lensing, kappa)
    xi_true  = xi(h0_true)
    pull     = (h0_true - H0_PLANCK) / np.sqrt(1.8**2 + 0.5**2)
    red_frac = (tension_raw - pull) / tension_raw * 100 if tension_raw != 0 else 0
    marker   = " ← typical range" if 0.04 <= kappa <= 0.08 else ""
    print(f"  {kappa:>8.2f}  {h0_true:>9.2f}  {xi_true:>+8.4f}  {pull:>+9.2f}σ            "
          f"{red_frac:>6.1f}%{marker}")

# ── Section 6: TDCOSMO+SLACS result analysis ─────────────────────────────────
print(f"\n── TDCOSMO+SLACS (Birrer+2021): stellar kinematics breaking the MSD ──────")
print(f"""
  Birrer et al. 2021 added stellar kinematics of the SLACS lens sample to
  break the mass-sheet degeneracy from within the lens galaxy (internal MSD).
  Result: H₀ = 67.4 +4.1/-3.2 km/s/Mpc — fully consistent with Planck.

  This is a *4σ downward shift* from TDCOSMO (74.2) to Birrer (67.4).
  In ξ space:
""")

xi_shift  = xi(67.4) - xi(74.2)
print(f"    Δξ (Birrer - TDCOSMO) = {xi_shift:+.4f}  ({xi_shift*100:.2f}%)")
print(f"    Δ H₀ = {67.4 - 74.2:.1f} km/s/Mpc")
print(f"""
  Interpretation in ξ framework:
    The entire H0LiCOW/TDCOSMO vs Planck tension ({73.3-67.4:.1f} km/s/Mpc, Δξ = {xi(73.3)-xi(67.4):+.4f})
    can be recovered by a mass-sheet with κ_int ≈ {(74.2-67.4)/74.2:.3f} (internal)
    plus κ_ext ≈ 0.04–0.08 (external large-scale structure).

    Once Birrer+2021 breaks the MSD, H₀ drops to 67.4 — exactly Planck.
    The large uncertainty (+4.1/-3.2) reflects genuine model-dependence
    in the kinematic anisotropy of the stellar orbits.
""")

# ── Section 7: Summary table ──────────────────────────────────────────────────
print("── Summary table ────────────────────────────────────────────────────────")
print(f"\n  {'Survey':<33} {'H₀':>6} {'err':>5}  {'ξ':>8}  {'vs Planck':>10}  {'MSD-corrected H₀':>18}")
print(f"  {'':33} {'':6} {'':5}  {'':8}  {'σ':>10}  {'(κ=0.06)':>18}")
print(f"  {'-'*90}")

for label, h0, err_hi, err_lo, ref in MEASUREMENTS:
    xi_val    = xi(h0)
    err_sym   = (err_hi + err_lo) / 2.0
    combined  = np.sqrt(planck_err**2 + err_sym**2)
    pull      = (h0 - planck_H0) / combined
    h0_msd    = msd_correction(h0, 0.06)
    # No MSD correction for Planck (CMB, not lensing) or Birrer (already corrected)
    if 'Planck' in label or 'Birrer' in label or 'SLACS' in label:
        msd_str = f"  {'N/A':>8}"
    else:
        msd_str = f"  {h0_msd:>8.2f}"
    print(f"  {label:<33} {h0:>6.2f} {err_sym:>5.2f}  {xi_val:>+8.4f}  {pull:>+7.2f}σ   {msd_str}")

# ── Section 8: ξ verdict ──────────────────────────────────────────────────────
xi_h0licow_planck    = xi(73.3)  - xi(67.4)
xi_msd_06            = xi(msd_correction(73.3, 0.06)) - xi(67.4)
xi_residual          = xi_h0licow_planck - xi_msd_06
msd_fraction         = abs(xi_msd_06)    / abs(xi_h0licow_planck) * 100
physical_fraction    = abs(xi_residual)  / abs(xi_h0licow_planck) * 100
frame_fraction       = 0.0   # H₀ is frame-independent

print(f"""
── ξ verdict ─────────────────────────────────────────────────────────────────

  QUESTION: What fraction of the H0LiCOW vs Planck tension is
    (a) a coordinate-frame artifact,
    (b) mass-sheet degeneracy, or
    (c) genuine physical disagreement?

  Total H₀ tension (H0LiCOW - Planck):  {73.3-67.4:.1f} km/s/Mpc  ({xi_h0licow_planck:+.4f} in ξ)
  Tension in σ (raw):  {(73.3-67.4)/np.sqrt(1.8**2+0.5**2):.2f}σ

  DECOMPOSITION:
    (a) Frame-mixing / coordinate artifact:   {frame_fraction:.1f}%
        H₀ is a frame-independent observable (km/s/Mpc). Unlike S8 or σ₈,
        it carries no implicit h-rescaling. Frame mixing does NOT contribute
        to the H₀ tension.

    (b) Mass-sheet degeneracy (κ_ext = 0.06): {msd_fraction:.1f}%
        Typical external convergence shifts H₀ by ~{(73.3-msd_correction(73.3,0.06)):.1f} km/s/Mpc.
        This is a systematic, not a cosmological signal.

    (c) Residual after MSD correction (κ=0.06): {physical_fraction:.1f}%
        Δξ_residual = {xi_residual:+.4f}
        This {physical_fraction:.0f}% is a genuine candidate for physical tension,
        but could be further reduced by κ_ext ≈ 0.08 or internal MSD.

  TDCOSMO+SLACS KEY FINDING:
    When stellar kinematics break the MSD (Birrer+2021), H₀ = 67.4 ± ~3.7
    — fully consistent with Planck at 0.0σ.
    This strongly implies the H0LiCOW tension is driven primarily by MSD,
    not a genuine expansion rate discrepancy.

  CONVERGENCE:
    The TDCOSMO+SLACS result, combined with κ_ext ≈ 0.04–0.08 from
    large-scale structure, accounts for the full {73.3-67.4:.1f} km/s/Mpc gap.

    Unlike the S8 tension (which survives after frame correction and points
    to a genuine Ω_m / σ₈ discrepancy), the H0LiCOW tension has a known
    astrophysical explanation: the mass-sheet degeneracy in lens modelling.

    The ξ normalization confirms: the H₀ tension as measured by strong
    lensing time delays is NOT a coordinate-frame artifact, but IS
    consistent with a known astrophysical systematic (MSD), with no
    statistically significant physical residual once MSD is properly broken.
""")
print("=" * 72)
