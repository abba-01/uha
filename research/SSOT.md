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

**Reproduction code:** `papers/gaia_zero_bias_test.py`, `papers/cepheid_xi_test.py`
**Patent:** US 63/902,536
