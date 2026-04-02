# Round4 Hubble
**Task ID:** a944de27623a910a3
**Session:** 79970414-2a9f-4110-8bf7-d3e67324fc3e
**Date:** 2026-04-01

---

Now I have what I need to give a thorough assessment. Let me render my verdict.

---

# Referee Report on "The Hubble Tension as a Measurement Artifact"

*Reviewed by Edwin Powell Hubble, Mount Wilson Observatory*

---

## Preliminary Remarks

I have spent the better part of my career peering through the 100-inch Hooker telescope, measuring the apparent magnitudes of Cepheid variables in what the theorists then called "spiral nebulae," later established to my satisfaction as island universes wholly external to our own. The velocity-distance relation I published in 1929 rested on exactly thirty-one nebulae and the best photographic plates I could obtain. I say this not from vanity but to establish my standing: I know something about what it means to measure a distance, and about what assumptions quietly enter the measurement before a single number appears in the ledger.

This paper deserves a careful reading. It is not crankery, and its central concern is legitimate. But it requires qualification in several important places.

---

## 1. On the Distance Ladder — Does the Paper Understand How It Actually Works?

The paper correctly identifies the three-rung architecture of the SH0ES pipeline: geometric anchor, Cepheid period-luminosity calibration, and SN Ia standardizable candles into the Hubble flow. That much is accurate. And I will grant that the fundamental insight — that the *Hubble flow* rung of that ladder depends on an assumed cosmological model to convert redshifts into comoving distances — is not wrong.

But I must be precise about *where* this dependence actually bites, because the paper's treatment is too sweeping.

My searches of the Riess et al. (2022) and Brout et al. (2022) Pantheon+ papers confirm an essential point that the manuscript appears to appreciate but does not fully articulate: the SH0ES measurement of H₀ is conducted, deliberately, in a way that is largely insulated from the Ωm question at the Hubble-flow stage. Riess and his colleagues use only SNe Ia at z > 0.023 for the Hubble flow, and the quantity they are fitting is the *intercept* of the magnitude-redshift relation — which is MB, the absolute magnitude of the SN Ia standard candle. H₀ emerges from the combination of that intercept with the Cepheid-anchored absolute distance scale. At low redshift (z < 0.15, where most of the constraining power lies), the comoving distance integral is barely sensitive to Ωm — the first-order correction goes as Ωm/6 times z squared. For z ~ 0.05, a shift of ΔΩm = 0.02 moves distances by less than 0.01%. The paper's claim that 93.3% of the Hubble-flow H₀-scaling dissolves in ξ space may be technically defensible for the full Pantheon+ redshift range out to z ~ 2, but it vastly overstates the practical leverage on the *local* H₀ measurement, which is anchored in the low-z portion of that sample.

This is not a minor quibble. The paper's headline claim — 93.3% of the tension is an artifact — rests on applying a horizon-normalization that has near-zero effect at the redshifts where the Cepheid-anchored H₀ is actually extracted. The framework dependence the author is pointing to is real, but it is overwhelmingly a concern at z > 0.5, not at z ~ 0.05.

**Verdict on this section:** The directional argument is sound. The magnitude of the claimed effect is substantially overstated for the measurement as it is actually performed.

---

## 2. On the Cepheid Analysis — 43 Calibrators, H₀ = 69.78 ± 13.97

I must be candid here, and I will be, because I spent years measuring Cepheids one by one and I know what their scatter means.

A dispersion of ±13.97 km/s/Mpc from 43 calibrators is not a result — it is a confession that the pipeline has been removed. The Cepheid period-luminosity relation is not a theoretical construct; it is an empirical regularity that I used in the Small Magellanic Cloud data from Miss Leavitt and subsequently applied to NGC 6822, M33, and M31. When that relation is properly applied, the distance uncertainty per galaxy drops below 5%. The scatter in a pipeline-free analysis of z ~ 0.001-0.01 calibrators is dominated by peculiar velocities — a galaxy at cz = 1,500 km/s with a peculiar velocity of 300 km/s has a 20% error in its recession velocity before a single Cepheid magnitude has been measured.

The authors are correct that this scatter is expected and does not impugn the pipeline. But the pipeline-free result of 69.78 is then used to argue that the "true" value is intermediate between Planck and SH0ES. I am skeptical of this reading. The result is consistent with both 67.4 and 73.04 within its enormous uncertainty. It demonstrates only that the peculiar velocity problem is severe — something that has been known since long before the current controversy and is precisely why SH0ES uses z > 0.023 as a low-redshift cutoff.

What the Cepheid scatter does tell us, and what the paper might have emphasized more forcefully, is that H₀ cannot be reliably extracted from any single rung of the ladder in isolation. It requires the full apparatus. This is the argument for the pipeline, not against it.

**Verdict on this section:** The analysis is honest about its own limitations. The interpretation that 69.78 is somehow a more "framework-free" result is misleading — it is simply an imprecise result. The large scatter reflects peculiar velocities exactly as expected.

---

## 3. On H₀ as a Parameter — Did I Start a Measurement Tradition with a Conceptual Flaw?

This is the most philosophically interesting part of the paper, and I confess it gives me pause.

When I published the velocity-distance relation, I was measuring apparent recession velocities — Doppler shifts in spectra — and distances estimated from Cepheid luminosities and angular sizes. The "constant" that emerged from that work (which Lemaître had anticipated on theoretical grounds, a priority I did not adequately acknowledge at the time) described the *local* proportionality between those two observables. It was an empirical number, extracted from data, with no cosmological model assumed beyond approximate isotropy.

The paper argues that the modern problem arises because SH0ES and Planck are measuring the same label — H₀ — but within frameworks with different Ωm values, and that this difference in the assumed expansion history contaminates the comparison. There is something to this. Planck does not measure H₀ directly. It infers it from the angular scale of the acoustic peaks under the assumption of ΛCDM with specific parameter values. The comoving sound horizon at recombination depends on ωm and ωb, and the angular diameter distance to last scattering depends on the full expansion history. So Planck's H₀ = 67.4 is not a direct measurement — it is a consistency inference within a model. That is not a criticism; it is a description of what CMB cosmology does.

The paper's ξ construction — dc/dH, normalizing comoving distance by the Hubble radius — is a reasonable attempt to extract a quantity that is model-independent in a specific sense: it absorbs the H₀ scaling. The claim that this reveals the tension as fundamentally an Ωm discrepancy rather than an H₀ discrepancy is interesting. The Aylor et al. (2019) paper in our index, "Sounds Discordant," makes a related point: that the tension can be partially decomposed into a disagreement in the shape of D_A(z) as much as in its overall amplitude.

But I am cautious about the conclusion that H₀ as a concept is therefore flawed. The Hubble constant, as I measured it, was precisely a *local* quantity — the slope of the velocity-distance relation in the nearby universe, extracted at scales small enough that the expansion is linear and Ωm corrections are negligible. The measurement tradition I started is not contaminated by framework dependence in the way the paper implies, because at z << 1, the comoving distance is simply cz/H₀ to first order, and the Ωm sensitivity is second-order. The framework dependence the paper identifies is a feature of how the Planck inference works, not of how the distance ladder works.

**Verdict on this section:** The concern about H₀ as a "framework parameter" is more applicable to the CMB side of the tension than to the distance ladder side. The paper would benefit from a clearer asymmetry in its treatment — the ladder measures H₀ more directly; the CMB infers it more indirectly.

---

## 4. On TRGB — What Does H₀ ≈ 69.96 Tell Us?

The tip of the red giant branch is a useful check precisely because it does not share the potential systematic biases of the Cepheid scale — it is not sensitive to metallicity corrections in the same way, does not depend on the period-luminosity slope, and uses a different stellar population. That Freedman's TRGB work (2024) gives an intermediate value of roughly 69-70 km/s/Mpc is significant.

My searches of the Freedman (2024) paper confirm that the TRGB disagreement with Cepheids is not primarily about framework dependence — it is about how the LMC anchor is calibrated and how reddening corrections are applied. Freedman notes explicitly that the two main sources of difference between TRGB and Cepheid-based H₀ values are: (1) the LMC calibration, and (2) corrections for dust in the inner regions of host galaxies. These are observational systematics in the classical sense — not coordinate-system artifacts.

If the paper's framework-mixing hypothesis were the primary driver of the tension, we would expect TRGB to agree with Cepheids at the rung level (both are local anchors using the same geometric base) and disagree only at the Hubble-flow comparison. But the TRGB and Cepheid methods diverge before the Hubble flow is reached — they give different calibrations of the SN Ia absolute magnitude. This tells us that at least part of what we are seeing is a genuine calibration disagreement between first-rung distance indicators, not merely a consequence of comparing pipelines built in different Ωm frameworks.

The intermediate TRGB value could mean several things: the true answer is between 68 and 73, there are unresolved systematics on one or both distance scales, or both. What it does not straightforwardly support is the paper's claim that 93% of the discrepancy is a comparison artifact. If it were, TRGB and Cepheids would agree with each other (both being direct, model-light measurements) and both would disagree with Planck by the residual ~3%. That is not what we observe.

**Verdict on this section:** The TRGB intermediate value actually argues against the paper's strong claim, because the disagreement exists before the Hubble flow is invoked at all.

---

## 5. Overall Verdict

This paper identifies a real methodological concern: that quoting two values of H₀ from measurements made within different cosmological frameworks and calling their discrepancy a "tension in H₀" conflates a framework parameter with a direct observable. This is worth saying clearly, and it has been said in adjacent forms by Aylor et al. (2019) and the inverse-distance-ladder literature. The ξ coordinate is a clean way to formalize this.

However, the paper overreaches in three ways that undermine the headline claim:

**First**, the 93.3% figure applies across the full Pantheon+ redshift range, but the H₀ measurement from the distance ladder is anchored at z < 0.15 where Ωm sensitivity is negligible — perhaps one to two percent at most, not 93%. The paper does not adequately account for the fact that the SH0ES pipeline was designed to be insensitive to this exact concern by operating in the linear-regime redshift range.

**Second**, the intermediate Cepheid result of 69.78 ± 13.97 is not meaningful evidence for a preferred H₀ value. It is what you get when peculiar velocities dominate and the pipeline constraints are removed. This is expected and uninformative about the true tension.

**Third**, and most importantly: the TRGB/Cepheid disagreement occurs below the Hubble-flow rung of the ladder. Framework dependence in the Hubble-flow calculation cannot explain a difference that emerges between two local calibration methods before any model-dependent distance conversion is applied. This is the strongest observational evidence that something other than frame-mixing is at work.

What remains after these corrections is still interesting: perhaps 5-10% of the tension (not 93%) may reflect genuine Ωm-framework dependence in the comparison, particularly for analyses that extend to higher redshift. The residual is a real astrophysical or physical discrepancy between early-universe and late-universe probes.

I do not find this paper suitable for publication in its present form. The core idea deserves a careful revision in which the ξ-space formalism is applied specifically to the redshift ranges actually used in the distance-ladder H₀ determination, not to the full Pantheon+ sample, and in which the TRGB observational result is reckoned with honestly. A revised paper that claims "a few percent of the Hubble tension may be a comparison artifact" rather than "93.3% of it is" would be both more accurate and more defensible.

I built the first rung of this ladder with photographic plates and a wire micrometer. I know that distances are hard to measure and that systematic errors are patient enemies. The author has identified a real systematic. He has not yet demonstrated that it is the dominant one.

*E. P. Hubble*
*Referee*

---

**Summary of key findings drawn from the literature:**

- Riess et al. 2022 confirms the SH0ES Hubble-flow cutoff at z > 0.023 specifically to avoid peculiar-velocity contamination — the model-sensitivity at these redshifts is negligible.
- Brout et al. (Pantheon+) confirms that the low-z Hubble diagram residuals at z < 0.008 show ~5% scatter from peculiar velocities even after correction — exactly the noise that drowns the 43-calibrator pipeline-free result.
- Freedman 2024 locates the Cepheid/TRGB discrepancy at the calibration level (LMC anchor, dust), not at the Hubble-flow level — undermining the frame-mixing hypothesis as the primary explanation.
- Aubourg et al. 2015 (inverse distance ladder) shows that the BAO/SN Ia path to H₀, which does have significant model dependence, gives ~67 km/s/Mpc — consistent with Planck — indicating the framework dependence runs in the right direction but quantitatively explains far less than 93% of the gap.