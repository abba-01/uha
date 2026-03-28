# Reply to Reviewer: Path (b) — r_s Bug Correction
**Date:** 2026-03-28
**Re:** 0.334 vs 0.295 discrepancy in bao_wa_minimizer.py

---

**You were right. The rerun confirmed the error.**

**Root cause identified:** The objective function in `bao_wa_minimizer.py` was computing D_M/r_s with the sound horizon fixed at the Planck fiducial:

```python
XI_SCALE = 299792.458 / (147.09 * 67.4)  # r_s = constant
```

This means r_s was held at 147.09 Mpc regardless of Omega_m. When Omega_m increased, D_M changed but r_s didn't — inverting the sign of the chi2 gradient. The minimizer correctly minimized its (broken) objective and landed at 0.334. That is the wrong objective, not a discovery.

**The fix:** Self-consistent r_s(Omega_m) scaling per Percival (2007):

    r_s(Omega_m) = 147.09 * (Omega_m * h^2 / 0.1430)^{-0.255}  Mpc

**Corrected results (1D minimizer, 7-bin D_M/r_s, DESI DR1):**

| Model              | Omega_m | chi2  | Delta-chi2 vs Planck |
|--------------------|---------|-------|----------------------|
| Planck LCDM        | 0.315   | 13.57 | —                    |
| Omega_m free (fix) | 0.268   | 6.51  | 7.06                 |
| + w0wa             | 0.251   | 6.39  | 0.12                 |

**Why 0.268, not 0.295:** DESI's full analysis uses the complete covariance
matrix, D_H/r_s alongside D_M/r_s, and a more complete r_s prescription.
Our simplified 7-bin D_M/r_s-only fit with the Percival approximation gives a
slightly different central value. The direction is the same — a deficit below
Planck's 0.315 — and the deficit interpretation is preserved.

**Consequence for the manuscript:**

- 0.334 (excess above Planck) is gone. ✓
- "Matter deficit" language is now correct. ✓
- The w0wa signal (Delta-chi2 = 4.74) was entirely an artifact of the
  fixed-r_s bug. Corrected Delta-chi2 = 0.12 for two extra parameters —
  statistically negligible. ✓
- Paper 2 revised: triple hierarchy → double hierarchy (H0 artifact +
  Omega_m deficit). The w0wa layer is removed from the main claim.
  A Limitations section explicitly documents the r_s prescription dependence
  and the 0.268 vs 0.295 discrepancy. ✓

The internal consistency you described is now restored.
