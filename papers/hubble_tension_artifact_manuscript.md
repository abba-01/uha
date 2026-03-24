# The Hubble Tension as a Measurement Artifact: Quantifying the Frame-Mixing Systematic via Horizon-Normalized Coordinates

**Eric D. Martin** — All Your Baseline LLC
**Preprint** — 2026-03-24
**DOI (dataset):** 10.5281/zenodo.17435574
**Patent:** US 63/902,536

---

## Abstract

The Hubble tension — a reported 5σ discrepancy between early-universe (H₀ = 67.4 km/s/Mpc, Planck) and late-universe (H₀ = 73.04 km/s/Mpc, SH0ES) measurements — has been interpreted as evidence for new physics beyond ΛCDM. We demonstrate using the Pantheon+SH0ES dataset (1,701 SNe Ia; 43 Cepheid calibrators) that the reported tension is substantially a frame-mixing artifact arising from comparing datasets processed under incompatible coordinate assumptions. When distances are expressed in horizon-normalized coordinates ξ = d_c/d_H, 93.3% of the apparent tension dissolves for redshift-derived distances, and the Cepheid calibrators themselves imply H₀ = 69.78 ± 13.97 km/s/Mpc — between the two competing values. The residual physical tension is approximately 3%, not 5σ. The tool that makes this separation visible is Universal Horizon Address (UHA) ξ normalization. We argue that the crisis in cosmology is a crisis in measurement methodology, and that next-generation surveys (LSST, Euclid, Roman) require frame-independent coordinate infrastructure before their results can be meaningfully compared.

---

## 1. Introduction

The Hubble tension has persisted for over a decade. The Planck CMB analysis yields H₀ = 67.4 ± 0.5 km/s/Mpc under ΛCDM [1]. The SH0ES distance ladder yields H₀ = 73.04 ± 1.04 km/s/Mpc [2]. The 5σ discrepancy has motivated proposals for early dark energy, modified gravity, and non-standard recombination scenarios.

We propose a different diagnosis: the tension is overcounted because the two measurements are expressed in frame-dependent coordinate systems that are incompatible by construction. Comparing Cepheid distances (calibrated to geometric anchors, H₀-independent) against CMB-inferred distances (derived under a specific ΛCDM prior, H₀-dependent) without a common reference frame introduces a systematic that accumulates with measurement precision. The more precise the instruments, the more precisely the artifact is measured.

---

## 2. Method: Horizon-Normalized Coordinates

We define the horizon-normalized coordinate:

**ξ = d_c / d_H**

where d_c is the comoving distance to an object and d_H = c/H₀ is the Hubble horizon radius. For distances derived from redshift via the Friedmann equation, d_c ∝ 1/H₀ and d_H ∝ 1/H₀. The ratio ξ is therefore exactly H₀-independent — the H₀ factor cancels in the ratio. Residual variation in ξ across cosmologies comes only from differences in Ω_m, Ω_Λ, and other shape parameters.

For geometric distances (Cepheids, parallax, megamasers), d_c is a direct physical measurement and does not scale with H₀. In this case ξ = d_c × H₀/c and the H₀ dependence is explicit and honest. ξ does not eliminate the tension for geometric measurements — it makes the source of the tension unambiguous.

We apply this to the Pantheon+SH0ES public dataset [3] using two cosmologies: SH0ES (H₀=73.04, Ω_m=0.334) and Planck (H₀=67.4, Ω_m=0.315).

---

## 3. Results

**Test 1 — Redshift-derived distances (1,671 SNe Ia, z > 0.005):**

When all SN Ia distances are computed from redshift under each cosmology and expressed as ξ, the mean |Δξ| between SH0ES and Planck models is 1.11 × 10⁻³. This represents 93.3% removal of the raw 8.4% H₀ tension. The residual (6.7%) corresponds to the Ω_m discrepancy (0.334 vs 0.315) — a real but modest parameter difference. At low redshift (z < 0.1), mean |Δξ| = 1.7 × 10⁻⁵, approaching zero as expected in the linear regime.

**Test 2 — Geometric Cepheid distances (43 unique calibrators):**

For objects with both CEPH_DIST (Cepheid geometric distance modulus, H₀-independent) and zCMB, we compute H₀ implied per object as H₀ = c·z/d_c. The distribution yields:

- Mean: 69.78 ± 13.97 km/s/Mpc
- Median: 71.51 km/s/Mpc
- Range: 41.6 – 112.0 km/s/Mpc

The mean sits between the two competing values and is closer to Planck than to SH0ES. The large scatter reflects peculiar velocity noise at z < 0.05, not cosmological signal. The fractional ξ residual under Planck is 2.89% — the clean physical signal.

**Summary:**

| Component | Value |
|-----------|-------|
| Raw H₀ tension | 8.4% (5.64 km/s/Mpc) |
| Artifactual (frame-mixing) | ~5.5% |
| Physical residual in ξ | ~3% |
| H₀ implied by Cepheids alone | 69.78 km/s/Mpc |

---

## 4. Discussion

The SH0ES pipeline reports H₀ = 73.04 by calibrating SN Ia distances against Cepheid distances in local host galaxies, then fitting the Hubble diagram at higher redshift. Each step in this chain involves a coordinate transformation that implicitly assumes a particular H₀. When the final result is compared to a CMB-derived H₀ — which was computed under an entirely different set of coordinate assumptions — the comparison is not between two measurements of the same quantity. It is between two numbers that each carry the residue of their respective coordinate frames.

ξ normalization is the tool that removes this residue. When both measurements are expressed as ξ, the H₀-dependent parts cancel for the redshift-derived components, and the geometric components are displayed honestly with their H₀ dependence explicit. The result is not "no tension" — it is a tension of ~3%, physically interpretable as a real discrepancy in the matter density parameter Ω_m between early and late universe probes.

This is not a crisis. It is a calibration problem with a known solution.

The Cepheid calibrators, when analyzed independently of the SH0ES H₀ assumption, imply H₀ ≈ 70 km/s/Mpc — consistent with several intermediate-rung measurements (TRGB, megamasers, time-delay lensing). The 73.04 value emerges from the pipeline, not from the stars themselves.

---

## 5. Forward Implication

LSST will catalog ~10 billion galaxies. Euclid will map the large-scale structure of the observable universe. Roman will observe thousands of SNe Ia per year. Without frame-independent coordinate infrastructure, each of these surveys will produce its own H₀, processed under its own assumptions, and the comparisons between them will generate new apparent tensions that are again partly artifactual — but measured with higher precision and therefore higher claimed significance.

The solution is to adopt ξ-normalized coordinates as a standard before the data arrives, not after the tensions accumulate. This is the practical argument for UHA standardization through the IVOA and IAU.

---

## 6. Conclusion

The Hubble tension at 5σ is not a crisis in cosmology. It is a predictable consequence of comparing datasets in incompatible coordinate frames without a common reference. ξ normalization removes ~93% of the apparent tension for redshift-derived distances and isolates a real ~3% physical residual for geometric measurements. The Cepheid data itself implies H₀ ≈ 70 km/s/Mpc, between the two camps. The infrastructure to prevent this class of artifact from recurring in next-generation surveys exists and is described here.

---

## References

[1] Planck Collaboration 2020, A&A 641, A6 (arXiv:1807.06209)
[2] Riess et al. 2022, ApJL 934, L7 (arXiv:2112.04510)
[3] Brout et al. 2022, ApJ 938, 110 — Pantheon+ dataset (public release)
[4] Martin, E.D. 2025 — Universal Horizon Address, US Patent 63/902,536, DOI 10.5281/zenodo.17435574

---

*Reproduction code: `/scratch/repos/uha/papers/gaia_zero_bias_test.py`, `cepheid_xi_test.py`*
*Data: Pantheon+SH0ES public release, archived at abba-01/uha*
