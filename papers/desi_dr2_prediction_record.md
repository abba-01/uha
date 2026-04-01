# Pre-Registration: ξ-Normalization Predictions for DESI DR2 BAO

**Author:** Eric D. Martin
**ORCID:** 0009-0006-5944-1742
**Date:** 2026-03-31
**Framework:** Horizon-Normalized Coordinates (UHA), Patent US 63/902,536

---

## Context

This record documents the quantitative predictions of the ξ-normalization framework
applied to DESI DR2 BAO data (arXiv:2503.14738), independently of the full Paper 2
manuscript. The predictions are recorded here as a standalone citable record so that
the framework's outputs are not buried in a longer paper.

DR1 corrected analysis (bao_wa_minimizer.py, self-consistent r_s(Ωm) scaling):

- Ωm = 0.268 (Δχ²_Planck = 7.06; 1D minimizer, 7 DM-only bins)
- w0wa negligible (Δχ²(w0wa) = 0.12 — statistically unsupported)

Note: an earlier pre-registration (DOI: 10.5281/zenodo.19232340, UHA v2.0.0) used a
fixed r_s formulation that produced a spurious Δχ²(w0wa) = 4.74 with Ωm = 0.295.
With self-consistent r_s(Ωm) scaling (Percival 2007, as used in Paper 2 and this
record), the w0wa signal collapses to Δχ² = 0.12 and the best-fit Ωm shifts to 0.268.
The pre-registration result is superseded by the corrected analysis.

DESI DR2 (arXiv:2503.14738) was published with a headline BAO-only result of
Ωm = 0.289 ± 0.007.

---

## DR2 Analysis

**Script:** `bao_desi_dr2.py` (included in this record)
**Data:** DESI DR2 BAO consensus, 13 measurements (DM/rs and DH/rs at 6 redshifts
plus BGS DV/rs), full 13×13 covariance matrix from CobayaSampler/bao_data.
**Source:** arXiv:2503.14738

---

## Results

| Model                   | Ωm     | w0      | wa      | χ²    | χ²/dof |
|-------------------------|--------|---------|---------|-------|--------|
| Planck ΛCDM             | 0.315  | −1.000  |  0.000  | 28.97 |  2.41  |
| Ωm free (ΛCDM)          | 0.290  | −1.000  |  0.000  | 20.99 |  1.75  |
| Ωm + wa free            | 0.290  | −1.000  | +0.202  |  9.82 |  0.89  |
| Ωm + w0 + wa (CPL)      | 0.333  | −0.710  | −1.075  |  7.86 |  0.79  |

**Δχ²(wa) = 11.17** — improvement from adding wa alone.
**Δχ²(w0+wa) = 13.13** — improvement from adding full CPL over Ωm-only fit.

---

## Key Findings

### 1. Ωm Deficit — Confirmed

The DR1 prediction of Ωm < 0.315 is confirmed. Best-fit Ωm = 0.290 matches the
DESI DR2 headline of 0.289 ± 0.007 to within 0.001 (< 0.1σ).

This represents a 7.9% deficit below Planck (Ωm = 0.315).

### 2. w0wa Signal — Unexpected, Driven by DH/rs Data

The DR1 analysis used 7 DM-only bins. DR2 adds DH/rs measurements (Hubble
parameter ratios) at each redshift, which carry independent sensitivity to H(z).

Δχ²(w0wa) = 13.13 is statistically significant (>>4.61 threshold for 2 dof at 90%).

The signal is driven by DH/rs residuals at z = 0.51 and z = 0.71:
- LRG1 DH/rs (z=0.510): −1.84σ below ΛCDM
- LRG2 DH/rs (z=0.706): −2.21σ below ΛCDM

DH/rs = c / (H(z) · rs) — these measurements directly constrain the expansion rate.
The DR1 null result (Δχ² = 0.12) was correct for the DM-only data available then.
The DR2 DH measurements expose a distinct line-of-sight residual.

### 3. Planck ΛCDM Rejected

χ²/dof = 2.41 for Planck ΛCDM against the 13-measurement DR2 dataset.
The Ωm-free fit reduces this to χ²/dof = 1.75. The CPL fit reaches χ²/dof = 0.79.

---

## Interpretation

Within the ξ-normalization framework, the BAO tension decomposes into three
separable layers:

1. **~90% coordinate artifact** — H₀ cancels in ξ = dc/dH (confirmed Paper 1)
2. **~8% Ωm deficit** — Ωm = 0.290 vs Planck 0.315 (confirmed DR1 and DR2)
3. **Provisional DH/rs signal** — Δχ² = 13.13, driven by z=0.51–0.71 line-of-sight
   measurements absent from DR1; requires Euclid DR1 (October 2026) for confirmation

The third layer was NOT predicted from DR1 data. It was discovered upon applying the
framework to the DR2 DH measurements. This record documents the discovery date and
computational method transparently.

---

## Prior Records

| Record | DOI |
|--------|-----|
| Paper 1 (Hubble tension artifact) | 10.5281/zenodo.19230366 |
| Paper 2 pre-registration (UHA v2.0.0) | 10.5281/zenodo.19232340 |
| Paper 2 corrected PDF (triple hierarchy) | 10.5281/zenodo.19304441 |

---

## Computational Record

The analysis script `bao_desi_dr2.py` is included in this record. It is
self-contained: hardcoded DR2 data values and covariance matrix, reproducible
with standard Python (numpy, scipy). No external data files required.

To reproduce:
```bash
python bao_desi_dr2.py
```

---

## Citation

Eric D. Martin (2026). *ξ-Normalization Predictions for DESI DR2 BAO: Matter-Density
Deficit and DH/rs Signal*. Zenodo. https://doi.org/10.5281/zenodo.19361407

ORCID: 0009-0006-5944-1742
