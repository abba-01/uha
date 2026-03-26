"""
kbc_void_xi_test.py — KBC void / bulk flow tension via ξ normalization
Session: 2026-03-26

Tests whether the KBC void and bulk flow can account for the H₀ tension,
and how much of the residual is a coordinate-frame artifact under ξ normalization.

Data sources (published summary statistics — no catalog download required):
    SH0ES 2022 (Riess+22):     H₀ = 73.04 ± 1.04 km/s/Mpc
    Planck 2020 (Aghanim+20):  H₀ = 67.4  ± 0.5  km/s/Mpc
    KBC void (Keenan+13):      δ  = -0.46  ± 0.06, R_void ≈ 300 Mpc
    Kenworthy+2019:            ΔH₀/H₀ boost ≈ 2.0 ± 0.6 km/s/Mpc from void
    Watkins+2023 (2Mpz):       v_bulk ≈ 290 ± 45 km/s toward (l=295°, b=10°)
    Freedman+2021 (TRGB):      H₀ = 69.8 ± 0.8 km/s/Mpc (intermediate anchor)

KBC void context:
    Keenan, Barger & Cowie (2013) identified a ~300 Mpc local under-density.
    If we live inside an under-dense region, local H₀ measurements (Cepheids,
    SNe Ia) would be biased high relative to the global CMB value because
    the local expansion rate is faster inside a void.

Method:
    1. Quantify raw H₀ tension (SH0ES vs Planck)
    2. Apply KBC void correction (Kenworthy+2019 estimate)
    3. Apply ξ normalization to separate coordinate-frame artifacts from physics
    4. Test bulk flow contribution at SNe Ia redshift range (z ~ 0.01-0.05)
    5. Compute combined residual and fraction decomposition

Author: Eric D. Martin
Date:   2026-03-26
References: Keenan+2013, Kenworthy+2019, Watkins+2023, Freedman+2021
"""

import numpy as np
from astropy.cosmology import FlatLambdaCDM
import warnings
warnings.filterwarnings('ignore')

# ── Physical constants ────────────────────────────────────────────────────────
C_KM_S = 299792.458  # speed of light, km/s

# ── H₀ measurements ──────────────────────────────────────────────────────────
H0_SHOES   = 73.04;  SIG_SHOES   = 1.04   # Riess+2022
H0_PLANCK  = 67.40;  SIG_PLANCK  = 0.50   # Planck 2020
H0_TRGB    = 69.80;  SIG_TRGB    = 0.80   # Freedman+2021 (TRGB, intermediate)

# ── KBC void parameters ───────────────────────────────────────────────────────
DELTA_KBC      = -0.46   # density contrast (Keenan+2013)
DELTA_KBC_ERR  =  0.06
R_VOID_MPC     = 300.0   # void radius, Mpc

# ── Kenworthy+2019 void-induced H₀ boost ─────────────────────────────────────
DH0_VOID       = 2.0     # km/s/Mpc expected H₀ boost from KBC void
DH0_VOID_ERR   = 0.6

# ── Bulk flow (Watkins+2023, 2Mpz survey) ────────────────────────────────────
V_BULK         = 290.0   # km/s
V_BULK_ERR     =  45.0
BULK_L_DEG     = 295.0   # Galactic longitude, deg
BULK_B_DEG     =  10.0   # Galactic latitude, deg

# ── SNe Ia survey redshift range (typical local H₀ anchor sample) ────────────
Z_SN_LOW   = 0.01
Z_SN_HIGH  = 0.05
Z_SN_MID   = 0.023   # representative midpoint

# ── ξ normalization parameters ────────────────────────────────────────────────
# ξ is the frame-mixing parameter from the Hubble tension framework.
# It captures the fractional H₀ frame shift between local and CMB observers.
# ξ = (H0_local / H0_global) - 1
XI_OBSERVED  = (H0_SHOES - H0_PLANCK) / H0_PLANCK   # raw observed
XI_ERR       = np.sqrt((SIG_SHOES / H0_PLANCK)**2 + (H0_SHOES * SIG_PLANCK / H0_PLANCK**2)**2)

# ── Reference cosmologies ─────────────────────────────────────────────────────
cosmo_planck = FlatLambdaCDM(H0=H0_PLANCK, Om0=0.315)
cosmo_shoes  = FlatLambdaCDM(H0=H0_SHOES,  Om0=0.334)

# =============================================================================
print("=" * 70)
print("KBC void / bulk flow — H₀ tension via ξ normalization test")
print("=" * 70)

# ── 1. Raw H₀ tension ─────────────────────────────────────────────────────────
print("\n── 1. Raw H₀ tension ───────────────────────────────────────────────")
H0_DIFF_RAW  = H0_SHOES - H0_PLANCK
SIG_COMBINED = np.sqrt(SIG_SHOES**2 + SIG_PLANCK**2)
TENSION_RAW  = H0_DIFF_RAW / SIG_COMBINED

print(f"  SH0ES 2022:       H₀ = {H0_SHOES:.2f} ± {SIG_SHOES:.2f} km/s/Mpc")
print(f"  Planck 2020:      H₀ = {H0_PLANCK:.2f} ± {SIG_PLANCK:.2f} km/s/Mpc")
print(f"  TRGB (Freedman):  H₀ = {H0_TRGB:.2f} ± {SIG_TRGB:.2f} km/s/Mpc  [intermediate anchor]")
print(f"  Observed boost:   ΔH₀ = {H0_DIFF_RAW:.2f} km/s/Mpc")
print(f"  Raw tension:      {TENSION_RAW:.2f}σ  (SH0ES - Planck)")

trgb_diff = H0_TRGB - H0_PLANCK
trgb_sig  = np.sqrt(SIG_TRGB**2 + SIG_PLANCK**2)
print(f"  TRGB - Planck:    {trgb_diff:.2f} km/s/Mpc  ({trgb_diff/trgb_sig:.2f}σ)")

# ── 2. KBC void correction ───────────────────────────────────────────────────
print("\n── 2. KBC void correction (Kenworthy+2019) ─────────────────────────")

print(f"""
  KBC void (Keenan, Barger & Cowie 2013):
    Density contrast:  δ_KBC = {DELTA_KBC:.2f} ± {DELTA_KBC_ERR:.2f}
    Void radius:       R     = {R_VOID_MPC:.0f} Mpc
    Interpretation:    local Universe is ~{abs(DELTA_KBC)*100:.0f}% under-dense
                       relative to the cosmic mean

  Mechanism: inside a void, the local Hubble flow is faster than global.
  Local distance indicators (Cepheids, SNe Ia) sit in a region where
  peculiar velocities add to the Hubble expansion → H₀_local biased high.

  Kenworthy+2019 estimated the H₀ boost from the KBC void profile:
    ΔH₀_KBC = {DH0_VOID:.1f} ± {DH0_VOID_ERR:.1f} km/s/Mpc
""")

H0_CORRECTED      = H0_SHOES - DH0_VOID
SIG_CORRECTED     = np.sqrt(SIG_SHOES**2 + DH0_VOID_ERR**2)
H0_DIFF_AFTER_KBC = H0_CORRECTED - H0_PLANCK
TENSION_AFTER_KBC = H0_DIFF_AFTER_KBC / np.sqrt(SIG_CORRECTED**2 + SIG_PLANCK**2)

print(f"  SH0ES corrected for KBC: {H0_CORRECTED:.2f} ± {SIG_CORRECTED:.2f} km/s/Mpc")
print(f"  Residual vs Planck:      {H0_DIFF_AFTER_KBC:.2f} km/s/Mpc")
print(f"  Tension after KBC:       {TENSION_AFTER_KBC:.2f}σ")
KBC_FRACTION = DH0_VOID / H0_DIFF_RAW
print(f"  KBC accounts for:        {KBC_FRACTION*100:.1f}% of raw ΔH₀ = {H0_DIFF_RAW:.2f} km/s/Mpc")

# ── 3. ξ normalization of the void effect ────────────────────────────────────
print("\n── 3. ξ normalization of the void effect ───────────────────────────")

print(f"""
  ξ = (H₀_local / H₀_global) - 1  [fractional frame shift]

  Raw observed:  ξ_obs  = {XI_OBSERVED:.4f} ± {XI_ERR:.4f}
               = {XI_OBSERVED*100:.2f}% fractional H₀ excess

  The void produces a coordinate-frame effect on local measurements:
    H₀_local = H₀_global × (1 + δH/H)
  where δH/H is the local expansion perturbation from the void.

  In ξ space:
    ξ_local  = ξ_global + δ_void × f_corr
  where f_corr accounts for the void profile shape and observer position.

  For a top-hat void of radius R with δ_KBC:
    δH/H ≈ -f_Ω × δ_KBC / 3  (linear perturbation theory)
  where f_Ω = Ω_m^0.55 ≈ 0.47 (growth rate at z≈0, Planck cosmology)
""")

f_Omega = cosmo_planck.Om0 ** 0.55
dH_over_H_tophat = -f_Omega * DELTA_KBC / 3.0
XI_VOID = dH_over_H_tophat
XI_VOID_ERR = f_Omega * DELTA_KBC_ERR / 3.0

print(f"  Growth rate f_Ω = Ω_m^0.55  = {f_Omega:.4f}")
print(f"  ξ_void (top-hat) = -f_Ω × δ_KBC / 3 = {XI_VOID:.4f}  ({XI_VOID*100:.2f}%)")
print(f"  In km/s/Mpc: ΔH₀_ξ_void = {XI_VOID * H0_PLANCK:.2f} ± {XI_VOID_ERR * H0_PLANCK:.2f} km/s/Mpc")
print()

# ξ correction to H₀ from void
DH0_XI_VOID     = XI_VOID * H0_PLANCK
DH0_XI_VOID_ERR = XI_VOID_ERR * H0_PLANCK

print(f"  Compare to Kenworthy+2019 empirical estimate:")
print(f"    ξ linear theory:   {DH0_XI_VOID:.2f} ± {DH0_XI_VOID_ERR:.2f} km/s/Mpc")
print(f"    Kenworthy+2019:    {DH0_VOID:.2f} ± {DH0_VOID_ERR:.2f} km/s/Mpc")
print(f"    Agreement:         {'good' if abs(DH0_XI_VOID - DH0_VOID) < max(DH0_XI_VOID_ERR, DH0_VOID_ERR) else 'modest'}")

# Residual ξ after removing void component
XI_RESIDUAL     = XI_OBSERVED - XI_VOID
XI_RESIDUAL_ERR = np.sqrt(XI_ERR**2 + XI_VOID_ERR**2)
H0_XI_RESIDUAL  = XI_RESIDUAL * H0_PLANCK

print(f"\n  ξ_obs:       {XI_OBSERVED:.4f}  ({XI_OBSERVED * H0_PLANCK:.2f} km/s/Mpc)")
print(f"  ξ_void:      {XI_VOID:.4f}  ({DH0_XI_VOID:.2f} km/s/Mpc)  [frame artifact]")
print(f"  ξ_residual:  {XI_RESIDUAL:.4f}  ({H0_XI_RESIDUAL:.2f} km/s/Mpc)  [after void correction]")

# ── 4. Bulk flow contribution in ξ space ─────────────────────────────────────
print("\n── 4. Bulk flow contribution (Watkins+2023) ─────────────────────────")

print(f"""
  Bulk flow:  v_bulk = {V_BULK:.0f} ± {V_BULK_ERR:.0f} km/s  toward (l={BULK_L_DEG:.0f}°, b={BULK_B_DEG:.0f}°)

  A bulk flow at the observer position creates a dipole anisotropy in
  the local Hubble flow. For SNe Ia used in local H₀ measurements
  (z ~ {Z_SN_LOW:.2f} – {Z_SN_HIGH:.2f}), the recession velocity is:
    cz ≈ c × {Z_SN_MID:.3f} = {C_KM_S * Z_SN_MID:.0f} km/s  (at z = {Z_SN_MID:.3f})

  The maximum fractional contribution from bulk flow:
    δH/H ≈ v_bulk / cz  (worst case: all SNe in bulk flow direction)
""")

cz_mid = C_KM_S * Z_SN_MID
cz_low = C_KM_S * Z_SN_LOW
cz_high = C_KM_S * Z_SN_HIGH

xi_bulk_mid  = V_BULK / cz_mid
xi_bulk_low  = V_BULK / cz_low   # maximum contamination (nearby SNe)
xi_bulk_high = V_BULK / cz_high

dH0_bulk_mid  = xi_bulk_mid  * H0_PLANCK
dH0_bulk_high = xi_bulk_high * H0_PLANCK
dH0_bulk_low_z = xi_bulk_low  * H0_PLANCK  # labelled by z, not magnitude

print(f"  At z = {Z_SN_MID:.3f}: cz = {cz_mid:.0f} km/s,  ξ_bulk = {xi_bulk_mid:.4f}  → ΔH₀ ≈ {dH0_bulk_mid:.2f} km/s/Mpc")
print(f"  At z = {Z_SN_LOW:.3f}: cz = {cz_low:.0f} km/s,   ξ_bulk = {xi_bulk_low:.4f}  → ΔH₀ ≈ {dH0_bulk_low_z:.2f} km/s/Mpc")
print(f"  At z = {Z_SN_HIGH:.3f}: cz = {cz_high:.0f} km/s,  ξ_bulk = {xi_bulk_high:.4f}  → ΔH₀ ≈ {dH0_bulk_high:.2f} km/s/Mpc")

# Realistic average: SH0ES uses z > 0.023 cut; Pantheon+ extends to z ~ 0.15
# The dipole averages down over sky coverage. Use a conservative sky-average factor.
SKY_AVG_FACTOR = 1.0 / np.sqrt(3.0)  # RMS of cos θ over hemisphere
xi_bulk_avg     = xi_bulk_mid * SKY_AVG_FACTOR
dH0_bulk_avg    = xi_bulk_avg * H0_PLANCK
dH0_bulk_avg_err = (V_BULK_ERR / V_BULK) * dH0_bulk_avg

print(f"""
  Realistic estimate (sky-averaged, z ~ {Z_SN_MID:.3f}):
    ξ_bulk_avg  ≈ {xi_bulk_avg:.4f}  (includes sky-average factor 1/√3 = {SKY_AVG_FACTOR:.3f})
    ΔH₀_bulk    ≈ {dH0_bulk_avg:.2f} ± {dH0_bulk_avg_err:.2f} km/s/Mpc

  Note: SH0ES uses a z > 0.023 cut specifically to reduce bulk flow contamination.
  Residual bulk flow effect after their cut is < {dH0_bulk_high:.1f} km/s/Mpc.
""")

# ── 5. Combined decomposition ─────────────────────────────────────────────────
print("\n── 5. Combined decomposition of H₀ tension ─────────────────────────")

# Total observed tension
H0_OBS_BOOST = H0_DIFF_RAW  # 5.64 km/s/Mpc

# Components
H0_KBC_COMPONENT   = DH0_VOID          # Kenworthy+2019 void boost
H0_BULK_COMPONENT  = dH0_bulk_avg      # sky-averaged bulk flow
H0_KBC_ERR         = DH0_VOID_ERR
H0_BULK_ERR        = dH0_bulk_avg_err

# ξ residual = physical signal not explained by KBC or bulk flow
H0_XI_FRAME_EXTRA  = max(0.0, H0_XI_RESIDUAL - H0_KBC_COMPONENT - H0_BULK_COMPONENT)
H0_PHYSICAL        = H0_OBS_BOOST - H0_KBC_COMPONENT - H0_BULK_COMPONENT
H0_PHYSICAL_ERR    = np.sqrt(SIG_SHOES**2 + SIG_PLANCK**2 + H0_KBC_ERR**2 + H0_BULK_ERR**2)

TENSION_PHYSICAL   = H0_PHYSICAL / H0_PHYSICAL_ERR

# Fractions
frac_kbc    = H0_KBC_COMPONENT  / H0_OBS_BOOST
frac_bulk   = H0_BULK_COMPONENT / H0_OBS_BOOST
frac_phys   = H0_PHYSICAL       / H0_OBS_BOOST

print(f"  Total observed ΔH₀ = {H0_OBS_BOOST:.2f} km/s/Mpc  ({TENSION_RAW:.2f}σ)")
print()
print(f"  Component breakdown:")
print(f"    KBC void (Kenworthy+2019):   {H0_KBC_COMPONENT:+.2f} ± {H0_KBC_ERR:.2f} km/s/Mpc  ({frac_kbc*100:.1f}%)")
print(f"    Bulk flow (Watkins+2023):    {H0_BULK_COMPONENT:+.2f} ± {H0_BULK_ERR:.2f} km/s/Mpc  ({frac_bulk*100:.1f}%)")
print(f"    Physical residual:           {H0_PHYSICAL:+.2f} ± {H0_PHYSICAL_ERR:.2f} km/s/Mpc  ({frac_phys*100:.1f}%)")
print(f"    ─────────────────────────────────────────────────────")
print(f"    Sum (check):                 {H0_KBC_COMPONENT + H0_BULK_COMPONENT + H0_PHYSICAL:+.2f} km/s/Mpc")
print()
print(f"  Physical residual tension:  {TENSION_PHYSICAL:.2f}σ  (after KBC + bulk flow removal)")

# ── 6. Results table ─────────────────────────────────────────────────────────
print("\n── 6. Results table ────────────────────────────────────────────────")
print()
print(f"  {'Step':<40} {'H₀ residual':>12}  {'Tension':>10}")
print(f"  {'─'*40} {'─'*12}  {'─'*10}")

raw_tension_str   = f"{TENSION_RAW:.2f}σ"
kbc_tension_str   = f"{TENSION_AFTER_KBC:.2f}σ"
phys_tension_str  = f"{TENSION_PHYSICAL:.2f}σ"

after_both        = H0_SHOES - DH0_VOID - H0_BULK_COMPONENT
after_both_sig    = np.sqrt(SIG_SHOES**2 + DH0_VOID_ERR**2 + H0_BULK_ERR**2)
after_both_diff   = after_both - H0_PLANCK
after_both_comb   = np.sqrt(after_both_sig**2 + SIG_PLANCK**2)
tension_after_both = after_both_diff / after_both_comb

print(f"  {'Raw SH0ES - Planck':<40} {H0_OBS_BOOST:>+8.2f} km/s  {TENSION_RAW:>7.2f}σ")
print(f"  {'After KBC void correction':<40} {H0_DIFF_AFTER_KBC:>+8.2f} km/s  {TENSION_AFTER_KBC:>7.2f}σ")
print(f"  {'After KBC + bulk flow correction':<40} {after_both_diff:>+8.2f} km/s  {tension_after_both:>7.2f}σ")
print(f"  {'Physical residual (ξ framework)':<40} {H0_PHYSICAL:>+8.2f} km/s  {TENSION_PHYSICAL:>7.2f}σ")
print()

# Status assessment
if TENSION_PHYSICAL < 2.0:
    status = "RESOLVED  (< 2σ physical residual)"
elif TENSION_PHYSICAL < 3.0:
    status = "PARTIALLY RESOLVED  (2–3σ physical residual)"
else:
    status = "NOT RESOLVED  (> 3σ physical residual remains)"

print(f"  Status: {status}")

# ── 7. ξ verdict ─────────────────────────────────────────────────────────────
print(f"""
── ξ verdict ─────────────────────────────────────────────────────────

  FRACTION DECOMPOSITION OF H₀ TENSION (ΔH₀ = {H0_OBS_BOOST:.2f} km/s/Mpc):

    Local structure / KBC void:  {frac_kbc*100:.1f}%  ({H0_KBC_COMPONENT:.2f} km/s/Mpc)
      → coordinate-frame artifact: observer inside under-dense region
         inflates local expansion rate (Kenworthy+2019)

    Bulk flow / peculiar velocity: {frac_bulk*100:.1f}%  ({H0_BULK_COMPONENT:.2f} km/s/Mpc)
      → coordinate-frame artifact: our ~290 km/s bulk motion adds
         anisotropic Doppler bias to SNe Ia Hubble diagram

    Physical residual:            {frac_phys*100:.1f}%  ({H0_PHYSICAL:.2f} km/s/Mpc)
      → genuine H₀ tension not explained by local structure or kinematics
      → tension level: {TENSION_PHYSICAL:.2f}σ after both corrections

  ξ NORMALIZATION ASSESSMENT:

    ξ_observed  = {XI_OBSERVED:.4f}  (total fractional H₀ excess)
    ξ_void      = {XI_VOID:.4f}  (KBC void, linear perturbation theory)
    ξ_bulk      = {xi_bulk_avg:.4f}  (sky-averaged bulk flow at z = {Z_SN_MID:.3f})
    ξ_residual  = {XI_OBSERVED - XI_VOID - xi_bulk_avg:.4f}  (physical, unexplained by frame effects)

  CONVERGENCE CHECK:
    TRGB (Freedman+2021) sits between SH0ES and Planck:
      H₀ = {H0_TRGB:.1f} km/s/Mpc  →  residual vs Planck = {trgb_diff:.2f} km/s/Mpc  ({trgb_diff/trgb_sig:.2f}σ)
    TRGB is less sensitive to local SNe Ia systematics → lower tension
    consistent with KBC/bulk flow biasing SH0ES upward.

  CONCLUSION:
    The KBC void + bulk flow together account for
    ~{(frac_kbc + frac_bulk)*100:.0f}% of the raw ΔH₀ = {H0_OBS_BOOST:.2f} km/s/Mpc tension.
    A physical residual of {H0_PHYSICAL:.2f} ± {H0_PHYSICAL_ERR:.2f} km/s/Mpc ({TENSION_PHYSICAL:.2f}σ) remains.
    This residual is {'below' if TENSION_PHYSICAL < 3.0 else 'above'} the conventional 3σ discovery threshold.

    The ξ framework classifies {(frac_kbc + frac_bulk)*100:.0f}% of the tension as
    coordinate-frame artifacts (local structure + bulk flow) and
    {frac_phys*100:.0f}% as a genuine physical signal requiring new cosmology
    (early dark energy, modified gravity, or calibration systematics).

References:
  Keenan, Barger & Cowie (2013), ApJ 775, 62        [KBC void discovery]
  Kenworthy, Scolnic & Riess (2019), ApJ 875, 145   [void H₀ boost estimate]
  Riess et al. (2022), ApJL 934, L7                  [SH0ES H₀]
  Aghanim et al. / Planck (2020), A&A 641, A6        [Planck H₀]
  Watkins et al. (2023), MNRAS 524, 1885             [bulk flow]
  Freedman et al. (2021), ApJ 919, 16                [TRGB H₀]
""")
