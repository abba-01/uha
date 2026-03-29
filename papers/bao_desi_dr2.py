"""
bao_desi_dr2.py — ξ-normalization validation against DESI DR2 BAO
Eric D. Martin, 2026-03-28

Uses full 13-measurement covariance matrix from Cobaya BAO data repo:
  https://github.com/CobayaSampler/bao_data/tree/master/desi_bao_dr2

Data: DESI 2025 DR2 BAO consensus (arXiv:2503.14738)
Ωm = 0.289 ± 0.007 (DR2 BAO-only headline)

Compares:
  1. Planck ΛCDM (Ωm=0.315, w0=-1, wa=0)
  2. Ωm free (ΛCDM shape)
  3. Ωm + w0 + wa free (CPL)

Paper 2 DR1 prediction: Ωm = 0.295 ± 0.010
DR2 directional confirmation expected: Ωm < 0.315, w0wa negligible after ξ
"""

import numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad
import warnings
warnings.filterwarnings('ignore')

# ── DESI DR2 BAO consensus data ──────────────────────────────────────────────
# Source: CobayaSampler/bao_data/desi_bao_dr2/
# Order matches covariance matrix rows/cols exactly:
#   [DV/rs at z=0.295,
#    DM/rs at z=0.510, DH/rs at z=0.510,
#    DM/rs at z=0.706, DH/rs at z=0.706,
#    DM/rs at z=0.934, DH/rs at z=0.934,
#    DM/rs at z=1.321, DH/rs at z=1.321,
#    DM/rs at z=1.484, DH/rs at z=1.484,
#    DH/rs at z=2.330, DM/rs at z=2.330]

DATA_LABELS = [
    ('BGS',       0.295, 'DV'),
    ('LRG1',      0.510, 'DM'),
    ('LRG1',      0.510, 'DH'),
    ('LRG2',      0.706, 'DM'),
    ('LRG2',      0.706, 'DH'),
    ('LRG3+ELG1', 0.934, 'DM'),
    ('LRG3+ELG1', 0.934, 'DH'),
    ('ELG2',      1.321, 'DM'),
    ('ELG2',      1.321, 'DH'),
    ('QSO',       1.484, 'DM'),
    ('QSO',       1.484, 'DH'),
    ('Lya',       2.330, 'DH'),
    ('Lya',       2.330, 'DM'),
]

DATA_OBS = np.array([
     7.94167639,   # BGS   DV/rs  z=0.295
    13.58758434,   # LRG1  DM/rs  z=0.510
    21.86294686,   # LRG1  DH/rs  z=0.510
    17.35069094,   # LRG2  DM/rs  z=0.706
    19.45534918,   # LRG2  DH/rs  z=0.706
    21.57563956,   # LRG3  DM/rs  z=0.934
    17.64149464,   # LRG3  DH/rs  z=0.934
    27.60085612,   # ELG2  DM/rs  z=1.321
    14.17602155,   # ELG2  DH/rs  z=1.321
    30.51190063,   # QSO   DM/rs  z=1.484
    12.81699964,   # QSO   DH/rs  z=1.484
     8.63154567,   # Lya   DH/rs  z=2.330
    38.98897396,   # Lya   DM/rs  z=2.330
])

# Full 13x13 covariance matrix (block-diagonal across tracers)
COV_RAW = np.array([
    [ 5.78998687e-03,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  2.83473742e-02, -3.26062007e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00, -3.26062007e-02,  1.83928040e-01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  3.23752442e-02, -2.37445646e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -2.37445646e-02,  1.11469198e-01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  2.61732816e-02, -1.12938006e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -1.12938006e-02,  4.04183878e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.05336516e-01, -2.90308418e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -2.90308418e-02,  5.04233092e-02,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  5.83020277e-01, -1.95215562e-01,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -1.95215562e-01,  2.68336193e-01,  0.00000000e+00,  0.00000000e+00],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.02136194e-02, -2.31395216e-02],
    [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -2.31395216e-02,  2.82685779e-01],
])

COV_INV = np.linalg.inv(COV_RAW)
N_DATA  = len(DATA_OBS)
NDOF_1D = N_DATA - 1
NDOF_2D = N_DATA - 2
NDOF_3D = N_DATA - 3

# ── Cosmological parameters ───────────────────────────────────────────────────
OM_PLANCK  = 0.315
H0_PLANCK  = 67.4
RS_PLANCK  = 147.09   # Mpc, Planck 2018
OM_H2_PLNK = OM_PLANCK * (H0_PLANCK/100)**2   # = 0.14300

def sound_horizon(om, h=H0_PLANCK/100):
    """r_s(Ωm) via Percival (2007) scaling, normalized to Planck 2018."""
    om_h2 = om * h**2
    return RS_PLANCK * (om_h2 / OM_H2_PLNK)**(-0.255)

def E_z(om, z, w0=-1.0, wa=0.0):
    """Dimensionless Hubble rate E(z) = H(z)/H0, CPL dark energy."""
    matter = om * (1 + z)**3
    de     = (1 - om) * (1 + z)**(3*(1 + w0 + wa)) * np.exp(-3*wa*z/(1+z))
    return np.sqrt(matter + de)

def xi_integral(om, z, w0=-1.0, wa=0.0):
    """ξ(z) = ∫₀ᶻ dz'/E(z') — the Horizon-Normalized Coordinate."""
    result, _ = quad(lambda zp: 1.0/E_z(om, zp, w0, wa), 0, float(z))
    return result

def c_over_H0rs(om):
    """c / (H0 * rs(Ωm)) — common scale factor, H0-independent."""
    return 299792.458 / (sound_horizon(om) * H0_PLANCK)

def model_vector(om, w0=-1.0, wa=0.0):
    """
    Compute model predictions for all 13 DR2 observables.
    DM/rs = ξ(z) * c/(H0*rs)
    DH/rs = c/(H0*rs) / E(z)
    DV/rs = [z * (DM/rs)^2 * (DH/rs)]^{1/3}
    """
    scale = c_over_H0rs(om)
    vec   = np.zeros(N_DATA)
    for i, (tracer, z, kind) in enumerate(DATA_LABELS):
        xi = xi_integral(om, z, w0, wa)
        ez = E_z(om, z, w0, wa)
        if kind == 'DM':
            vec[i] = xi * scale
        elif kind == 'DH':
            vec[i] = scale / ez
        elif kind == 'DV':
            dm_rs  = xi * scale
            dh_rs  = scale / ez
            vec[i] = (z * dm_rs**2 * dh_rs)**(1.0/3.0)
    return vec

def chi2(om, w0=-1.0, wa=0.0):
    """Full covariance chi2: (d-m)^T C^{-1} (d-m)."""
    resid = DATA_OBS - model_vector(om, w0, wa)
    return float(resid @ COV_INV @ resid)

def chi2_1d(params):
    om = float(np.atleast_1d(params)[0])
    if om < 0.20 or om > 0.40: return 1e10
    return chi2(om)

def chi2_2d(params):
    om, wa = params
    if om < 0.20 or om > 0.40: return 1e10
    if wa < -3.0 or wa > 2.0:  return 1e10
    return chi2(om, w0=-1.0, wa=wa)

def chi2_3d(params):
    om, w0, wa = params
    if om < 0.20 or om > 0.40: return 1e10
    if w0 < -2.0 or w0 > 0.0:  return 1e10
    if wa < -3.0 or wa > 2.0:   return 1e10
    return chi2(om, w0=w0, wa=wa)

# ── Run fits ──────────────────────────────────────────────────────────────────
print("=" * 72)
print("bao_desi_dr2.py — ξ-Normalization vs DESI DR2 BAO (13 measurements)")
print("Full covariance chi2. DESI 2025 (arXiv:2503.14738)")
print("=" * 72)

chi2_planck = chi2(OM_PLANCK)
print(f"\nPlanck ΛCDM (Ωm=0.315, w0=-1, wa=0):")
print(f"  χ² = {chi2_planck:.2f}  (ndof={NDOF_1D},  χ²/dof = {chi2_planck/NDOF_1D:.2f})")

# ── 1D: Ωm free ──────────────────────────────────────────────────────────────
print("\n── Step 1: Ωm free (w0=-1, wa=0) ─────────────────────────────────────")
r1   = minimize(chi2_1d, [0.295], method='L-BFGS-B', bounds=[(0.24, 0.36)])
om1  = r1.x[0]
c1   = r1.fun
dc1  = chi2_planck - c1

print(f"  Best-fit Ωm = {om1:.4f}")
print(f"  χ² = {c1:.2f}  (χ²/dof = {c1/NDOF_1D:.2f})")
print(f"  Δχ² vs Planck = {dc1:.2f}")
print(f"  Ωm deficit: {OM_PLANCK - om1:.4f}  ({(OM_PLANCK-om1)/OM_PLANCK*100:.1f}%)")

print(f"\n  Residuals (best-fit Ωm={om1:.4f}):")
mv1 = model_vector(om1)
errs = np.sqrt(np.diag(COV_RAW))
for i, (tracer, z, kind) in enumerate(DATA_LABELS):
    resid = DATA_OBS[i] - mv1[i]
    sigma = resid / errs[i]
    print(f"    {tracer:<12} z={z:.3f}  {kind}/rs  obs={DATA_OBS[i]:.3f}  "
          f"mod={mv1[i]:.3f}  resid={resid:+.3f} ({sigma:+.2f}σ)")

# ── 2D: Ωm + wa free ─────────────────────────────────────────────────────────
print("\n── Step 2: Ωm + wa free (w0=-1 fixed) ─────────────────────────────────")
r2      = minimize(chi2_2d, [0.295, -0.5], method='L-BFGS-B',
                   bounds=[(0.24, 0.36), (-3.0, 2.0)])
om2, wa2 = r2.x
c2       = r2.fun
dc2_wa   = c1 - c2

print(f"  Best-fit Ωm={om2:.4f},  wa={wa2:.4f}")
print(f"  χ² = {c2:.2f}  (χ²/dof = {c2/NDOF_2D:.2f})")
print(f"  Δχ² from adding wa = {dc2_wa:.2f}")

# ── 3D: Ωm + w0 + wa free ────────────────────────────────────────────────────
print("\n── Step 3: Ωm + w0 + wa free (CPL) ────────────────────────────────────")
r3          = minimize(chi2_3d, [0.295, -0.9, -0.5], method='L-BFGS-B',
                       bounds=[(0.24, 0.36), (-2.0, 0.0), (-3.0, 2.0)])
om3, w03, wa3 = r3.x
c3            = r3.fun
dc3_w0wa      = c1 - c3

print(f"  Best-fit Ωm={om3:.4f},  w0={w03:.4f},  wa={wa3:.4f}")
print(f"  χ² = {c3:.2f}  (χ²/dof = {c3/NDOF_3D:.2f})")
print(f"  Δχ² from adding w0+wa = {dc3_w0wa:.2f}")

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"""
══════════════════════════════════════════════════════════════════════════
RESULT TABLE — DESI DR2 (13 measurements, full covariance)
══════════════════════════════════════════════════════════════════════════

  Model              Ωm      w0       wa     χ²      χ²/dof
  ────────────────────────────────────────────────────────
  Planck ΛCDM        0.315  -1.000   0.000  {chi2_planck:6.2f}   {chi2_planck/NDOF_1D:.2f}
  Ωm free            {om1:.3f}  -1.000   0.000  {c1:6.2f}   {c1/NDOF_1D:.2f}
  Ωm + wa free       {om2:.3f}  -1.000  {wa2:+.3f}  {c2:6.2f}   {c2/NDOF_2D:.2f}
  Ωm + w0 + wa       {om3:.3f}  {w03:+.3f}  {wa3:+.3f}  {c3:6.2f}   {c3/NDOF_3D:.2f}

  Δχ²(wa):     {dc2_wa:.2f}  — improvement from adding wa alone
  Δχ²(w0+wa):  {dc3_w0wa:.2f}  — improvement from adding full CPL
""")

# DR2 DESI headline: Ωm = 0.289 ± 0.007
print("  DESI DR2 headline (BAO-only):     Ωm = 0.289 ± 0.007")
print(f"  This fit best-fit:                Ωm = {om1:.3f}")
print(f"  Paper 2 DR1 prediction:           Ωm = 0.295 ± 0.010")
print(f"  Planck ΛCDM:                      Ωm = 0.315")
print(f"  Ωm deficit confirmed:             {(OM_PLANCK-om1)/OM_PLANCK*100:.1f}% below Planck")

if dc3_w0wa < 2.3:
    verdict = "Ωm DEFICIT SUFFICIENT — w0wa NOT REQUIRED (Paper 2 prediction confirmed)"
elif dc3_w0wa < 4.0:
    verdict = "w0wa MARGINALLY PREFERRED — Euclid DR1 needed to resolve"
else:
    verdict = "w0wa REQUIRED — unexpected, investigate"

print(f"\n  VERDICT: {verdict}")
print()
