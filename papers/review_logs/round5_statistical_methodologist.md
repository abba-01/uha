# Round5 Statistical Methodologist
**Task ID:** ae4580f94e98fe6df
**Session:** 79970414-2a9f-4110-8bf7-d3e67324fc3e
**Date:** 2026-04-01

---

I now have a comprehensive picture from the paper searches and cross-checks. Let me deliver the full statistical review.

---

## STATISTICAL AND METHODOLOGICAL REVIEW

**Verdict upfront:** The manuscript has **one foundational methodological error that invalidates the 93.3% headline claim**, plus four serious secondary problems. It is not ready for peer review in its current form. The conceptual question being asked (does frame-mixing affect tension quantification?) is legitimate, but the current execution contains demonstrable errors.

---

## PROBLEM 1 — THE CENTRAL CLAIM IS BUILT ON A CATEGORY ERROR (FATAL)

**The ξ = dc/dH cancellation is correct mathematics applied to the wrong object.**

The paper demonstrates that, for purely redshift-derived distances, ξ(z, Ωm) is H₀-independent. This is trivially true: dc = (c/H₀)∫₀ᶻ dz'/E(z',Ωm), and dividing by dH = c/H₀ cancels H₀ exactly. The mathematics is not in dispute.

The error is in what SH0ES actually measures. As confirmed by R22 (chunk 47, 53): the baseline H₀ measurement uses 277 Hubble-flow SNe Ia at 0.0233 < z < 0.15, with free parameters **{MB, H₀, q₀}**, where MB is the absolute magnitude of SN Ia. H₀ is extracted not from a comparison of two redshift-derived distances, but from the **absolute scale** set by Cepheid-anchored geometric distances to calibrator hosts (rung 2) propagated to the Hubble flow via MB. 

The operational formula is approximately:
> μ_SN = 5 log(cz/H₀) + terms = m_B − MB

H₀ enters through the MB−H₀ degeneracy, which is **broken only by the Cepheid geometric calibration**. The critical point: the ξ transformation does not act on this measurement at all. The paper applies ξ to the comparison of two cosmological model predictions computed at different (H₀, Ωm), then declares 93.3% of the raw H₀ difference is "artifact." But this conflates two completely different operations:

1. **What ξ actually does:** Shows that if you compute ξ under (H₀^SH0ES, Ωm^SH0ES) vs. (H₀^Planck, Ωm^Planck), most of the numerical difference in ξ comes from ΔΩm, not ΔH₀.
2. **What the paper claims ξ does:** Shows that 93.3% of the Hubble tension is an artifact of "frame mixing."

These are not the same claim. The paper is comparing how two cosmological models predict distances, not showing that the SH0ES H₀ measurement procedure conflates anything. SH0ES measures H₀ through a distance ladder with a geometric anchor; it does not perform the comparison in Eq. 4 internally.

**The frame-mixing framing also mischaracterizes what Eq. 4 actually represents.** The tension statistic Δ = (H₀^SH0ES − H₀^Planck)/σ_combined compares two independent measurements of the same physical quantity. These are not "framework-dependent coordinates"—both are measurements of the present-day expansion rate in km/s/Mpc. Planck's H₀ = 67.4 is a derived parameter of the ΛCDM fit; it is not "in a frame defined by Ωm=0.315" in any coordinate sense. The paper needs to demonstrate that SH0ES and Planck are actually measuring different things operationally, which it does not do.

---

## PROBLEM 2 — THE f_artifact FORMULA AND ARITHMETIC (SERIOUS)

**Formula structure:**
f_artifact = 1 − |Δξ| / |ΔH₀/H₀|

There are multiple issues with this formula:

**2a. Denominator ambiguity in the 8.4% claim.** (73.04 − 67.4)/67.4 = 8.37% ≈ 8.4%, confirming the paper uses H₀^Planck as denominator. But |ΔH₀/H₀| in the formula, if evaluated at H₀^SH0ES, gives 7.7%. The paper mixes denominators: 8.4% uses Planck's H₀ as denominator while the ξ numerator is constructed from both frameworks. This is not declared.

**2b. The 93.3% arithmetic does not check out cleanly.** If raw = 8.4% and ξ-space residual = 0.57%, then f = 1 − 0.57/8.4 = 0.932 = 93.2%, not 93.3%. The discrepancy is minor but the paper's internal decomposition (5.5% artifact + 2.9% physical = 8.4%) implies 5.5/8.4 = 65.5%, not 93.3%. This means the paper is reporting two different artifact fractions in two different places (Table 1's decomposition vs. §5.1's f_artifact), and these are **not consistent with each other**. The paper states 93.3% of the "H₀-scaling component of the redshift-derived distance comparison" dissolves—but Table 1 shows only a 5.5% artifact on a total 8.4% discrepancy, implying 65.5%. These cannot both be correct simultaneously without the paper clearly distinguishing between two separate quantities. This distinction is not made explicit, and the 93.3% headline figure is the number that gets remembered.

**2c. The formula can produce misleading results by construction.** Consider what happens at low redshift (z → 0): ξ → 0 for both frameworks, so |Δξ| → 0, and f_artifact → 1 (100%) regardless of any actual physical tension. The formula mechanically approaches 1 as z → 0 not because the tension disappears but because ξ → 0 for all cosmologies. The paper's sample has ⟨z⟩ ≈ 0.35 (plausible), but this redshift-dependence of f_artifact is never examined. A plot of f_artifact(z) would be required to show this is not an artefact of the redshift distribution of the sample.

**2d. Dimensional/conceptual validity of comparing 0.57% to 8.4%.** The 0.57% is the mean fractional ξ-difference across 1,671 SNe: ⟨|ξ^SH0ES − ξ^Planck| / ξ_typical⟩. The 8.4% is |ΔH₀|/H₀^Planck—a ratio in a completely different space. The paper asserts these quantities are directly comparable as fractions of "the same discrepancy," but they measure different things: one is a normalized distance ratio, the other is a parameter ratio. A referee will demand a formal derivation showing these ratios are in the same units and refer to the same physical effect.

---

## PROBLEM 3 — BOOTSTRAP METHODOLOGY VASTLY UNDERSTATES UNCERTAINTY (SERIOUS)

The ±0.1% uncertainty from 10⁴ bootstrap iterations measures **sampling variance only**—i.e., how much f_artifact would change if you drew a different 1,671 SNe from the Pantheon+ population with replacement. This is the least important source of uncertainty in this analysis.

Unquantified systematic uncertainties that dominate and are not captured by bootstrap:

**3a. Choice of Ωm for each framework.** The paper uses Ωm^SH0ES = 0.334. But searching Brout 2022 (chunk 28), the Pantheon+ SNe-only FlatΛCDM constraint is Ωm = 0.306 ± 0.057. The Pantheon+ + SH0ES combined gives a different value. The Brout FlatΛCDM+CMB+BAO gives Ωm = 0.325 (chunk 30). None of these is exactly 0.334. The paper's claim to use "the most complete SH0ES characterisation" is not sourced to a specific table entry in Brout 2022. This Ωm choice alone drives the entire ξ decomposition—ΔΩm is the entire mechanism—and the paper gives it ±0 uncertainty.

**3b. Ωm uncertainty propagation.** Planck gives Ωm = 0.3153 ± 0.0073 (TT,TE,EE+lowE+lensing, Table 2 in Planck 2020). SH0ES/Brout uncertainty on Ωm is ~0.05. The f_artifact computation is entirely controlled by ΔΩm = 0.019 ± ~0.05. The uncertainty on ΔΩm is multiple times larger than ΔΩm itself, meaning f_artifact is consistent with zero at one sigma. This is never stated.

**3c. Cosmological model assumption.** The entire cancellation depends on flat ΛCDM with w = −1. DESI DR1 data (the paper's own citation) shows w₀ ≠ −1 at >2σ. The paper's footnote that residual H₀ dependence is "~0.2% under best-fit DESI dark energy" is not propagated into the 93.3% figure.

**3d. Redshift-dependent systematics.** SALT2 standardization, BEAMS bias corrections, and peculiar velocity corrections all introduce redshift-dependent biases that would differentially affect the two ξ computations. Bootstrap over the same dataset resamples these systematic floors identically—it cannot detect them.

**3e. The covariance matrix is not resampled.** Pantheon+ provides a full covariance matrix C for its 1,701 SNe. The correct bootstrap for correlated data should resample block-structured or use a parametric approach respecting C. Standard IID bootstrap on correlated SN Ia data produces overconfident (too narrow) uncertainty estimates.

---

## PROBLEM 4 — CEPHEID H₀ ANALYSIS IS STATISTICALLY INADMISSIBLE AS PRESENTED (SERIOUS)

**4a. The estimator is wrong.** The paper computes H₀,i = cz_CMB,i / d_c,i for each of 43 Cepheid calibrators, then takes the mean/median. At z ~ 0.001–0.01, the Hubble law d = cz/H₀ is dominated by peculiar velocities of 300–600 km/s (confirmed by Brout 2022 chunk 26 explicitly: "only the distance moduli from such nearby SNe are used in the SN-Cepheid absolute distance calibration in the 2nd rung... only SNe with redshifts z > 0.023 are used in the 3rd rung to limit sensitivity to peculiar velocities"). The paper's own formula is exactly the estimator R22 identifies as unreliable and explicitly avoids for this reason.

**4b. The reported uncertainty is wrong.** σ = 13.97 km/s/Mpc is the sample standard deviation. The standard error on the mean would be 13.97/√43 ≈ 2.13 km/s/Mpc. The paper reports σ = 13.97 as if it is the uncertainty on H₀^Cepheid = 69.78, but this is the spread of the distribution, not the uncertainty on the mean. Reporting "H₀ = 69.78 ± 13.97" in Table 1 without clarifying this is misleading—a reader will interpret ±13.97 as the uncertainty on the central value.

**4c. The comparison to Freedman 2024 TRGB is not valid even as a qualitative check.** The paper states "qualitative directional consistency with TRGB only, not statistical comparison given σ=13.97." However, the mean 69.78 and median 71.51 have a difference of 1.73 km/s/Mpc, indicating right-skew (consistent with peculiar velocity contamination pulling low-z objects down). The Freedman 2024 result (H₀ ≈ 69.96 ± 1.05 from JWST TRGB, per the indexed paper) is a proper error-propagated measurement while the paper's 69.78 ± 13.97 is a naive mean of individually unreliable estimators. Noting they are "consistent" adds no information when σ = 13.97 is 20% of the central value.

**4d. No outlier analysis or redshift cut.** With σ/mean ≈ 20%, any individual object with a peculiar velocity of 200 km/s at z = 0.003 produces H₀,i anywhere from ~0 to ~200 km/s/Mpc. The mean and median are not robust to this contamination without disclosed outlier treatment. R22 explicitly addresses this by excluding z < 0.0233 from the Hubble-flow rung.

---

## PROBLEM 5 — Ωm COMPARISON IS MISCONFIGURED (MODERATE TO SERIOUS)

**5a. The paper compares non-comparable Ωm estimates.** The Brout 2022 Ωm = 0.334 value appears to be from the Pantheon+ + SH0ES FlatΛCDM constraint, but Brout (chunk 28) reports Ωm = 0.306 ± 0.057 for SNe alone, and Brout (chunk 30) reports Ωm = 0.325 for Pantheon+ + Planck + BAO (FlatwCDM). These are different dataset combinations. Using Ωm = 0.334 is not definitively sourced in the manuscript, and it matters: ΔΩm drives the entire calculation.

**5b. Ωm is correlated with H₀, not independent.** In any joint SN Ia + Cepheid analysis, H₀ and Ωm are simultaneously fit. Using the SH0ES Ωm to construct the "SH0ES framework" and the Planck Ωm to construct the "Planck framework," and then treating them as independent inputs to the ξ comparison, ignores the correlated uncertainty between (H₀, Ωm) within each framework. In particular, if H₀^SH0ES were lower (as the paper argues), the best-fit Ωm from the same data would shift, partially invalidating the ΔΩm used to drive f_artifact.

**5c. The paper asserts Ωm discrepancy is "physical residual" without a proper statistical test.** Three probes (DESI DR1, KiDS-1000, DES Y3) are said to be "broadly consistent" with Ωm ≲ 0.310. DES Y3 is quoted as Ωm = 0.289. But Heymans 2021 (KiDS-1000, confirmed by search) gives S₈ = 0.766 with Ωm broadly consistent with Planck at the 2-3σ level, not systematically low. The paper's claim that three probes collectively point toward Ωm ≲ 0.310 is not a properly weighted or statistically formalized combination—it is narrative citation.

---

## PROBLEM 6 — ADDITIONAL FLAGS

**6a. Sample size discrepancy.** The abstract says 1,701 SNe Ia (Pantheon+), with 1,671 redshift-derived and 43 Cepheids. But 1,671 + 43 = 1,714, not 1,701. The 43 Cepheids are not in the Pantheon+ SN Ia count—they are separate calibrators from R22. The math 1,701 − 30 = 1,671 is not explained. The paper should clearly state which 30 objects were excluded from the ξ analysis and why.

**6b. The Aylor 2019 characterization is partially inaccurate.** Aylor 2019 chunk 14 shows their H₀ tension significance as 3.0σ from the WMAP9+SPT+ACT CMB combination. The paper says Aylor "concludes tension is real and requires pre-recombination physics." The actual Aylor conclusion is more nuanced: they recast the tension as a sound horizon discordance (rs discordance at 3.0σ) and argue modifications to late-time physics cannot resolve it—which does require pre-recombination physics. But the paper's summary is close enough to be defensible.

**6c. The DESI paper in the index appears to be DESI EDR (instrument paper, 2024), not the DESI DR1 or DR2 BAO cosmological results paper.** The abstract mentions "DESI BAO" as confirming Ωm ~ 0.295, but the indexed DESI paper is the instrument/technical release, not the cosmological constraints paper. The specific Ωm claim needs to be sourced to the DESI 2024 BAO cosmological results paper (Adame et al. 2024), which is not in the vector index.

**6d. No error propagation from cosmological model uncertainty into f_artifact.** The paper propagates nothing except SN sampling noise. A proper analysis would propagate σ(Ωm^SH0ES), σ(Ωm^Planck), and the w/Ωk uncertainties through the ξ integral and into f_artifact. Given the ~0.05 uncertainty on Ωm^SH0ES, f_artifact is consistent with 0% at ~1σ.

---

## SUMMARY TABLE

| Issue | Severity | Fatal to submission? |
|---|---|---|
| ξ transformation applied to wrong object; H₀ tension is not a coordinate-frame artifact | Fatal | Yes, requires complete reframing |
| 93.3% vs 65.5% internal inconsistency | Serious | Yes |
| f_artifact formula undefined at low-z; redshift dependence unexamined | Serious | Requires new analysis |
| Bootstrap captures only sampling variance; Ωm uncertainty never propagated | Serious | Yes |
| Cepheid H₀ estimator is naively wrong; σ/mean = 20% | Serious | Yes |
| σ = 13.97 reported as uncertainty on mean, not s.d. | Moderate | Yes |
| Ωm = 0.334 not clearly sourced; non-comparable to Planck's 0.315 | Moderate | Requires clarification |
| Ωm−H₀ correlation ignored in ξ decomposition | Serious | Yes |
| DESI EDR instrument paper cited for cosmological Ωm constraint | Minor | Requires correction |

**Overall verdict: Major methodological problems. Not ready for review.**

The paper's core insight—that Ωm differences between frameworks introduce a calculable systematic into the direct H₀ comparison—is scientifically interesting and worth developing. But the current formulation inverts the causal logic (ξ does not remove an artifact in the measurement; it shows a model-comparison effect), overstates the quantitative result by at least a factor of ~10 in the headline figure, and presents the Cepheid analysis in a way that is statistically inadmissible. A substantial revision addressing points 1–4 is required before this could survive referee scrutiny.