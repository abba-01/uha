# UHA Data Repository — Single Source of Truth

**Repo:** abba-01/uha (PRIVATE)
**Source data:** Pantheon+/SH0ES DataRelease (original: PantheonPlusSH0ES/DataRelease)
**Clone date:** 2025-10-10
**Original commit:** c447f0f
**Status:** Data archive — cosmological observational datasets for UHA analysis
**Last Updated:** 2026-03-24

---

## What This Is

This is the cosmological data archive underpinning UHA-based Hubble tension analysis. It holds the observational datasets (Pantheon+ supernovae and SH0ES distance ladder) that are encoded into UHA coordinate space for tension analysis.

This is a **data repo**, not a theory repo. The UHA theory lives in `uha-blackbox` and `uha-api-service`.

---

## Contents

| Directory | Contents |
|-----------|---------|
| `Pantheon+_Data/` | Pantheon+ Type Ia supernovae compilation |
| `SH0ES_Data/` | SH0ES distance ladder calibration data |
| `Cosmology/` | MCMC chains, cosmology inputs, CosmoSIS likelihoods |

---

## Data Provenance

Full git history preserved from original DataRelease repository. Complete provenance trail for peer review. Data is from public scientific repository with proper attribution.

---

## Role in UHA Research

These datasets are the primary input to:
1. **uha_hubble** — Hubble tension analysis in UHA coordinate space
2. **uha-blackbox / uha-api-service** — encoding these measurements as UHA addresses
3. **Hubble tension repos** — all statistical analyses in the Hubble cluster draw from this data

---

## UHA and the Cosmological Tensions

UHA (Universal Horizon Address) provides a framework that addresses both:
- **Hubble tension** (H₀ discrepancy): Planck CMB vs. SH0ES distance ladder
- **S8 tension**: σ₈ × √(Ω_m/0.3) discrepancy between CMB and weak lensing

The coordinate system's cosmology-portable invariant (ξ = horizon-normalized position) provides a frame-agnostic way to compare measurements that are traditionally made in incompatible reference frames. UHA encodes *where* in horizon space a measurement was made — and the early/late universe tension may reflect genuine horizon-scale geometry rather than systematic error.

---

## Publications / DOIs

| Paper | DOI |
|-------|-----|
| Hubble Tension as Measurement Artifact (Martin 2026) | 10.5281/zenodo.19154280 |
| Universal Horizon Address theory (Martin 2025) | 10.5281/zenodo.17435574 |
| Hubble tension resolution validation package | 10.5281/zenodo.17435578 |

**Reproduction code:**
- `papers/gaia_zero_bias_test.py` — Gaia zero-bias parallax test (mean |Δξ| ≈ 0)
- `papers/cepheid_xi_test.py` — Cepheid ξ normalization (Pantheon+/SH0ES)
- `papers/jwst_xi_test.py` — JWST Cepheid hosts ξ test (Riess 2023, 8 hosts)
- `papers/bao_xi_test.py` — DESI DR1 BAO tension (physical Ω_m residual confirmed)
- `papers/s8_sigma8_xi_test.py` — S8/σ₈ tension (physical, ~2-3σ, Ω_m driven)
- `papers/age_tension_xi_test.py` — Age of universe tension (dissolves at H₀≈69-70)
- `papers/al_lensing_xi_test.py` — A_L lensing amplitude tension (12–24% coordinate + statistical)

**Patent:** US 63/902,536

---

## Cosmological Tension Test Results (Session ecda5f02)

All five major cosmological tensions tested via ξ normalization. Results as of 2026-03-24:

| Tension | H₀ frame component | Physical residual | Key finding |
|---------|-------------------|-------------------|-------------|
| **H₀ (Hubble)** | ~93% artifact | ~7% real (Ω_m) | ξ cancels on Pantheon+/JWST; stars alone → H₀≈68.7 |
| **BAO (DESI DR1)** | ~0% | 100% real | D_M/r_s invariant to H₀; DESI Ω_m=0.295 vs Planck 0.315 |
| **S8 / σ₈** | ~0–3% | ~97% real | Both surveys use H₀≈67.4 — genuine Ω_m/σ₈ discrepancy |
| **Age of universe** | Large (SH0ES → 12.5 Gyr) | Small at H₀≈70 | 4/7 GCs exceed SH0ES age; dissolves at H₀≈69-70 |
| **A_L lensing** | 12–24% minor | Mostly statistical | ACT A_L=1.01 (same sky, no anomaly) — weakest tension |

**Convergent signal:** All late-universe probes point to Ω_m ≈ 0.295 vs Planck 0.315 (~6%). This is the genuine physical residual after ξ removes the frame-mixing artifact from the H₀ tension.
