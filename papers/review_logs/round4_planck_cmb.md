# Round4 Planck Cmb
**Task ID:** a7b54d141fb2d3fa3
**Session:** 79970414-2a9f-4110-8bf7-d3e67324fc3e
**Date:** 2026-04-01

---

I now have sufficient information to write a thorough, grounded review. Here is my assessment:

---

## Referee Report: "The Hubble Tension as a Measurement Artifact"

**Reviewer position:** Planck/CMB specialist, skeptical of artifact explanations.
**Verdict summary at top:** The paper identifies a real and discussable methodological point, but it is substantially overstated. The treatment of the Planck side of the comparison contains a fundamental conceptual error that undermines the central quantitative claim. The paper is not ready for publication in its current form, but the residual issue it identifies — the Ωm discrepancy — is real and deserves a narrower, more honest treatment.

---

### Critical Issue 1: The Paper Fundamentally Mischaracterises How Planck Derives H₀

This is the most serious problem in the manuscript.

The paper writes (Section 2, around Eq. 3): "The Planck H₀ is derived from the angular acoustic scale... both computed self-consistently within the Planck ΛCDM model with Ωm^Planck = 0.315." This framing treats Ωm = 0.315 as if it is an input assumption — a "prior" or "fixed framework parameter" — analogous to the way Riess et al. fix Ωm = 0.30 in their Hubble-flow fit.

This is wrong, and it is wrong in a way that is fatal to the frame-mixing argument as currently stated.

Planck does not input Ωm = 0.315 and then derive H₀. Planck samples the six primary ΛCDM parameters: ωb, ωcdm, 100θMC (the acoustic angular scale), τ, As, and ns. H₀ and Ωm are **both derived (posterior) quantities** — they emerge from the posterior chains after the likelihood has been evaluated. The actual sampled parameter that pins the acoustic peak positions is 100θMC, constrained to 1.04092 ± 0.00031 (Planck 2020, Table 1 retrieved from the search results). This is a 0.03% measurement. From it, H₀ and Ωm are jointly inferred with the full posterior covariance. Ωm = 0.3158 is the posterior mean that falls out; it is not a framework assumption that goes in.

This matters enormously for the paper's argument. The paper claims there is a "frame-mixing systematic" because the two H₀ values are extracted under different Ωm assumptions (0.334 vs 0.315). But the correct description is:

- **SH0ES**: H₀ is fit with Ωm fixed at 0.30 (Hubble-flow only) or jointly preferred at 0.334 (full Pantheon+). This genuinely is a framework assumption in the sense the paper describes.
- **Planck**: H₀ and Ωm are jointly constrained — the posterior joint distribution of (H₀, Ωm) from Planck is a correlated 2D ellipse. The Ωm = 0.315 figure is the mean of the marginalized posterior, not a held-fixed value.

The paper's entire quantitative structure — f_artifact = 93.3% — depends on treating these as symmetric "framework parameters." They are not symmetric. Planck's constraint is a full multiparameter posterior fit; SH0ES uses Ωm as an external prior input to the Hubble-flow fit. The asymmetry is the paper's blind spot.

Furthermore: Planck's actual sensitivity to H₀ comes almost entirely through the angular acoustic scale θ* = rs(z*)/DA(z*), which is primarily sensitive to **ωm h² = Ωm h²**, not Ωm alone. The degeneracy direction in Planck parameter space is not "H₀ vs Ωm" in isolation — it is the well-known (H₀, Ωm) degeneracy ridge where Ωm h² stays approximately constant (confirmed by the Planck 2020 search result chunk 40: "the CMB constraint can be expressed as a tight 0.04%-precision relation"). If you hold ωm h² constant and change H₀, you must change Ωm in the same direction. This is a self-consistent simultaneous constraint, not two separate framework assumptions that can be "mixed."

**Requested fix:** The paper must explicitly distinguish between (a) Ωm as a sampled parameter with a posterior mean, and (b) Ωm as a fixed external prior input. The two cases require completely different treatments in the frame-mixing argument. The claim that Planck uses "Ωm = 0.315 as a framework" should be removed or severely qualified.

---

### Critical Issue 2: The ξ Framework Does Not Apply to the Planck Side of the Comparison

The ξ = dc/dH construction (Eq. 4) cancels H₀ exactly for distances computed from redshift via the Friedmann equation:

ξ(z, Ωm) = ∫₀ᶻ dz'/E(z', Ωm)

This is mathematically correct and internally consistent. But notice what it requires: **a redshift-derived comoving distance dc(z; H₀, Ωm)**. This is precisely how SN Ia Hubble flow distances are computed. The construction is valid on the SH0ES/Pantheon+ side.

The problem is that Planck does not compute dc at all. Planck does not measure the comoving distance to anything in the low-redshift universe. The Planck measurement chain is:

1. Observe the CMB temperature and polarization power spectra (angular data, dimensionless multipoles)
2. Fit the angular acoustic scale θ* = rs(z*)/DA(z*) to 0.03% precision — this is an angular ratio, not a distance
3. From the fitted values of ωb, ωcdm, ns, As, τ: compute the sound horizon rs and the angular diameter distance to recombination DA(z*≈1090) from known early-universe physics
4. Derive H₀ as the value needed to make the inferred geometry consistent

At no point does Planck compute a dc(z; H₀, Ωm) for z in the range of the Pantheon+ SN sample (z ~ 0.01–2.3). The ξ transformation is defined on redshift-derived low-z distances. It has no natural application to the Planck observable, which lives at z ~ 1090 and is an angular measurement, not a distance measurement.

The paper partially acknowledges this by focusing f_artifact = 93.3% on the "1,671 Hubble flow SNe Ia" component. But the claim is still that this removes a "frame-mixing systematic" from the H₀ comparison — which requires the Planck H₀ to also be subject to the same coordinate-frame analysis. It is not. The ξ framework dissolves the H₀ scaling in the SH0ES portion of the comparison. What it does to the Planck portion is undefined, because Planck's H₀ is not a redshift-integrated distance ratio.

Put differently: the paper shows that ξ(z, Ωm_SH0ES) ≈ ξ(z, Ωm_Planck) for the Hubble flow SNe. This is true and interesting. But this does not constitute a "frame-mixing" between the two H₀ measurements, because Planck's H₀ is not derived by computing ξ at any redshift. The supposed equivalence of the two frames in ξ-space applies only to one side of the comparison.

**Requested fix:** The paper needs a careful discussion of what the ξ framework actually proves: that within the SN Ia Hubble flow, the H₀ scaling is nearly degenerate with Ωm, and that 93.3% of the apparent H₀ discrepancy when comparing two SN Ia analyses under different Ωm is attributable to this degeneracy. This is a valid SN-internal statement. It is not a valid statement about the SN vs CMB comparison without additional justification.

---

### Critical Issue 3: The Ωm Uncertainty Is Treated as a Point Estimate When It Matters Most

The paper treats Ωm^Planck = 0.315 and Ωm^SH0ES = 0.334 as if they are fixed framework parameters with no uncertainty. But Planck 2020 reports Ωm = 0.315 ± 0.007 (the search confirmed: "matter density parameter Ωm = 0.315 ± 0.007"). Brout 2022 reports Ωm = 0.334 ± 0.018.

The ΔΩm = 0.019 central value difference is less than 1σ when propagating the Brout uncertainty alone (0.019/0.018 = 1.06σ), and less than 2σ when accounting for both:

σ_combined ≈ √(0.007² + 0.018²) ≈ 0.019 → ΔΩm/σ_combined ≈ 1.0σ

This is barely a 1σ difference. The paper builds an entire "frame-mixing" argument on an Ωm difference that is consistent with zero within measurement uncertainties. If the paper acknowledges this, it should quantify how f_artifact varies when ΔΩm is drawn from its uncertainty distribution. A significant fraction of bootstrap realizations would give ΔΩm ≈ 0, which would drive f_artifact toward undefined (0/0 type limit). The 93.3% figure is computed at the central value of the parameters; the uncertainty on f_artifact from Ωm uncertainty is almost certainly much larger than the quoted ±0.1% (which is purely bootstrap on the SN sample, holding Ωm fixed).

**Requested fix:** Propagate the Ωm uncertainties into the f_artifact calculation. The ±0.1% statistical uncertainty on f_artifact is not the relevant uncertainty; the uncertainty from the Ωm values themselves dominates and has not been computed.

---

### Critical Issue 4: The Aylor 2019 Engagement Is Incomplete and Arguably Self-Contradictory

The paper's §7.3 engagement with Aylor et al. (2019) is its most sophisticated move, but it contains a logical problem.

The paper correctly states that Aylor et al. reframe the tension as a 3.0σ discordance in the inferred sound horizon rs (CDL-derived: 137.6 ± 3.45 Mpc vs ΛCDM-predicted), and that Aylor conclude "it is real and points to pre-recombination modifications." The paper then claims this is "orthogonal" to the ξ diagnosis and that "both analyses converge on the conclusion that the raw 5σ H₀ subtraction is the wrong quantity to optimise."

But Aylor's conclusion actively contradicts the paper's central claim. The paper argues the tension is primarily a comparison methodology artifact (93.3% artifactual). Aylor et al. argue it is a genuine physical signal in the early-universe sound horizon. These are not "orthogonal diagnoses" — they are competing explanations. If Aylor are right, then the tension is not primarily a comparison artifact; the measurement methodology is correct and the physics is wrong. The paper cannot simultaneously credit Aylor as supporting evidence while also claiming the tension is 93.3% artifactual.

Moreover, the Aylor 2019 rs analysis is precisely the kind of CMB-grounded measurement that is immune to the ξ coordinate transformation. rs is an early-universe physical scale determined from ωb and ωcdm — not a late-universe redshift-integrated distance. The fact that the rs tension is 3σ even before any ξ analysis means there is a genuine physical discrepancy somewhere in the early universe that the paper's coordinate redefinition cannot dissolve.

**Requested fix:** The paper must either (a) claim that Aylor et al. are wrong and explain why the rs tension is artifactual — which would require substantial additional analysis — or (b) acknowledge that the Aylor 2019 result establishes that at least some component of the tension is genuinely early-universe in origin, independent of the comparison methodology, and revise the abstract/conclusion accordingly.

---

### Critical Issue 5: The Cepheid-Only H₀ Analysis Is a Diagnostic, Not Evidence

The paper reports H₀ = 69.78 ± 13.97 km/s/Mpc from 43 Cepheid calibrators via the naïve H₀,i = cz_CMB/dc,i estimator. The paper correctly notes this is dominated by peculiar velocities and is "qualitative only."

However, the paper then uses the median (71.51 km/s/Mpc) as corroborating evidence for an intermediate H₀ value, and argues that the JWST Cepheids "imply a median H₀ = 68.66 km/s/Mpc" from the same estimator. Both of these are deeply unreliable. At z ~ 0.001–0.01, peculiar velocities of 300–600 km/s contribute H₀ uncertainties of 30–100 km/s/Mpc **per object**. A median of 13 realizations at these scales is not informative about H₀ at the 1 km/s/Mpc level.

More problematically, the paper claims this median is "consistent with TRGB results" at H₀ ≈ 70. But H₀ = 70 ± 14 is consistent with virtually everything — including both 67 and 73. The agreement with Freedman 2024 is not a meaningful consistency check given the uncertainty.

The suggestion in §7.1 that the JWST result "emerges from the pipeline, not from the Cepheids or redshifts in isolation" is a significant claim that requires more justification than is provided. The Riess et al. 2023 JWST result uses exactly the same H₀,i type analysis but at 5–40 Mpc distances where peculiar velocities are properly accounted for within the pipeline. Dismissing the pipeline-derived result as artifactual while crediting the scatter-dominated naïve estimator as a diagnostic is circular.

---

### Critical Issue 6: The q₀ Argument is a Circular Conflation

The paper uses R22's best-fit q₀ = -0.51 to infer an "effective Ωm ≈ 0.327" for the SH0ES framework (§2). But this conversion assumes flat ΛCDM with w = -1. If q₀ is being used as a model-independent parameterisation of the Hubble flow (which is why R22 uses it — to avoid assuming Ωm), then converting it back to an Ωm via the ΛCDM relation q₀ = (3/2)Ωm - 1 is circular: it assumes the very model-dependent relationship that q₀ was introduced to avoid. The paper then uses this circular Ωm = 0.327 as evidence for a "frame-mixing" Ωm discrepancy.

---

### Secondary Issues

**On the EDE discussion (§7.4):** The paper claims EDE models attempting to bridge the "full 8.4% gap without first removing the frame-mixing component require scalar field parameters more extreme than necessary." This has the logic backwards. EDE resolves the H₀ tension by shrinking rs and raising H₀ in the CMB framework — it operates entirely in the early-universe physics domain. The "frame-mixing" the paper identifies operates in the late-universe comparison. These are in different places in the causal chain. EDE does not use or reference the coordinate comparison methodology.

**On the abstract:** The abstract states the Hubble crisis is "primarily a crisis of measurement methodology." The f_artifact = 93.3% figure applies only to the Hubble flow component of the SN Ia comparison, not to the full tension including the CMB anchoring through the sound horizon. The abstract overstates what the analysis actually shows.

**On DESI corroboration:** DESI's Ωm ≈ 0.295–0.304 is cited as independently confirming the late-universe Ωm deficit. This is a real result. But DESI measures Ωm primarily through DM/rs — an H₀-independent ratio where rs is calibrated from the CMB. If the CMB-inferred rs is itself part of the tension (as Aylor 2019 argues), then DESI's Ωm and Planck's Ωm are not independently anchored. The paper treats them as if they are.

---

### Verdict

**The paper makes one legitimate methodological point:** when comparing two Hubble flow SN Ia analyses computed under different Ωm assumptions, a significant fraction of the apparent H₀ discrepancy is due to Ωm-dependent shape differences in the distance-redshift relation rather than a clean H₀ signal. This is discussable at peer review.

**The paper does not establish its central claim:** that the 5σ Hubble tension is "primarily a measurement artifact." This claim requires that the Planck H₀ be subject to the same coordinate-frame analysis as the SH0ES H₀, which it is not — Planck measures an angular acoustic scale at z~1090 through a self-consistent multiparameter fit in which Ωm is a posterior output, not a framework input. The ξ construction simply does not apply to the CMB side of the comparison. The f_artifact = 93.3% quantifies something real within SN Ia Hubble-flow distance modelling, but it cannot be interpreted as dissolving 93.3% of the CMB vs distance-ladder tension.

The paper should be substantially revised to (1) restrict its claims to what the ξ framework actually proves — a statement about SN Ia internal Ωm-H₀ degeneracy; (2) correctly describe Planck's H₀ determination as a self-consistent posterior from a multiparameter CMB fit rather than an extraction at a fixed Ωm; (3) propagate Ωm uncertainties into f_artifact; and (4) reconcile the Aylor 2019 engagement with the paper's central conclusion. The Aylor 2019 result, taken seriously, implies the tension has an early-universe physical component that no late-time coordinate redefinition can address.

---

**Summary of issues by severity:**

| Issue | Severity |
|---|---|
| Planck H₀ mischaracterised as "extracted at fixed Ωm=0.315" | Fatal to central claim |
| ξ framework inapplicable to CMB-side of comparison | Fatal to central claim |
| Ωm uncertainties not propagated into f_artifact | Major |
| Aylor 2019 engagement logically inconsistent with central claim | Major |
| Cepheid naïve H₀ median used as corroborating evidence | Moderate |
| q₀ → Ωm conversion is circular | Moderate |
| EDE discussion has causal chain backwards | Minor |
| Abstract overstates scope of analysis | Minor |