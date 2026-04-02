# Round5 Vera Rubin
**Task ID:** a74938cbb6dba12fc
**Session:** 79970414-2a9f-4110-8bf7-d3e67324fc3e
**Date:** 2026-04-01

---

I now have enough material from the actual papers to write a thorough, grounded review. Here is Vera Rubin's assessment.

---

# Vera Rubin Reviews: "The Hubble Tension as a Measurement Artifact"

*A referee report by Vera C. Rubin*

---

I have spent the better part of my career telling people that what you think you know about the universe, and what the universe is actually doing, are not always the same thing. Before I discovered that galaxy rotation curves refused to flatten the way anyone predicted, I was told dark matter was a theorist's contrivance. So I come to this paper with genuine sympathy for an author who says: look at the data differently, and the problem changes shape. That is sometimes exactly right. But sympathy does not replace rigor. Let me tell you what the data actually says.

---

## On the ~3% Ωm Discrepancy: Does the Physics Make Sense?

I went to the papers. The KiDS-1000 3x2pt analysis — Heymans and collaborators, 2021 — reports from their full multi-probe analysis: **Ωm = 0.305, σ₈ = 0.76**. Those are their best-fit values from combining weak lensing with BOSS spectroscopic clustering. Planck 2018 gives Ωm = 0.3111 ± 0.0056 at its tightest. That gap — roughly 0.006 to 0.010 in Ωm — is real and persistent across datasets. Planck's own executive summary in that paper is careful to note that its S₈ = 0.831 ± 0.013 is "in modest tension" with weak lensing results.

Now: does a 4–6% matter density deficit between early and late universe make physical sense?

I want to be honest here, because I have spent decades watching people propose explanations for small signals that then vanish. A 4–6% deficit in Ωm between CMB epoch and the late universe is not obviously impossible, but it is not obviously easy either. Matter in ΛCDM is conserved — it dilutes as a⁻³, the same in early and late epochs. A genuine discrepancy of this magnitude would require one of the following:

**First:** Dark matter is not perfectly cold and collisionless. If a fraction of it decays, self-annihilates at an appreciable rate, or couples weakly to radiation or baryons at scales we have not probed, the effective Ωm measured by low-redshift geometry (BAO, lensing) could be lower than what the CMB sound horizon records. The Aubourg 2015 BAO paper, which I searched, explicitly considers models where "dark matter decays into radiation" and finds these models are constrained but not ruled out at the level of their data.

**Second:** The Ωm difference may not be a matter density difference at all. It may be that dark energy is not a cosmological constant — that w ≠ −1, or that there is early dark energy that shifts the calibration of the sound horizon. If the sound horizon inferred from Planck is slightly off, everything downstream changes coherently. This is, of course, the Poulin early dark energy argument.

**Third:** It is a systematic artifact in either direction — in the CMB extraction, in the lensing shape catalog, or in the BAO analysis. I do not dismiss this.

I note with some interest that the Planck 2020 parameter table shows that Ωm shifts significantly depending on what data combination you use: TT-only gives Ωm = 0.321, while the full TT+TE+EE+lowE+lensing+BAO gives 0.3111. That is already a 3% internal variation within Planck itself. So when Martin says the discrepancy between SH0ES's assumed Ωm = 0.334 and Planck's 0.315 is itself a measurable quantity worth accounting for — he is not wrong in principle.

---

## On the S₈ Tension: What the Papers Actually Say

The vector search against the actual papers gives me this picture:

**KiDS-1000 (Heymans 2021):** The 3x2pt analysis finds Ωm = 0.305 (+0.012/−0.013) and σ₈ = 0.759 (+0.020/−0.024). The suspiciousness statistic ln S = −2.0 ± 0.1 in tension with Planck. For Gaussian posteriors, d − 2 ln S is distributed as χ²_d, and Heymans et al. explicitly state they find tension at roughly **3σ** in the combined multi-probe analysis. This is real. This is not a marginal result.

**Planck's own assessment of DES:** The Planck 2020 paper itself states that S₈ = 0.831 ± 0.013 is "in modest tension with DES results that also include galaxy clustering." The word "modest" in Planck's vocabulary means they're worried about it but not ready to declare a crisis.

**What the paper under review says about these:** Martin characterizes the lensing surveys as finding "matter clustering below Planck prediction." That characterization is accurate. The KiDS numbers I retrieved — σ₈ ≈ 0.76 versus Planck's σ₈ ≈ 0.811 — represent a ~6% deficit in σ₈, and Ωm ≈ 0.305 versus Planck's 0.311. The S₈ tension is real and has been replicated independently. Martin's use of these results as corroborating evidence is legitimate.

Where I would push back: DES Y3 Ωm = 0.289 with uncertainties of +0.036/−0.056 is a wide posterior. The DES central value is consistent with both Planck and KiDS at less than 1σ. Citing the central value of 0.289 as evidence for the Ωm deficit without noting that the error bars span 0.233 to 0.325 — that is cherry-picking the mean. The paper should quote the full constraint.

---

## On the Three-Probe Convergence: Real Signal or Coincidence?

Let me be direct, because in my experience this is where people go wrong.

Three probes pointing in the same direction is suggestive. It is not proof. The question I always ask is: **do these probes share a systematic error?**

The ξ-residual (the Cepheid distance ladder residual after applying the coordinate correction) depends on the Planck Ωm as an input. DESI BAO constrains Ωm geometrically but still uses rd from the early universe. The lensing S₈ comes from shear catalogues with known issues — intrinsic alignments, shape noise, photometric redshift calibration. These are not fully independent measurements. They share CMB priors in various ways. That is not a fatal objection, but it means the "three independent probes" argument is softer than it appears.

That said — I have to be honest about the other side of this ledger. When I was measuring rotation curves flat where Newtonian gravity said they should fall, nobody wanted to believe me either. The most common response was "it must be a systematic." Eventually, enough independent methods — radio hydrogen, optical spectra, different galaxies, different inclinations — all said the same thing. The evidence accumulated.

The situation here reminds me of that, in miniature. BAO measures geometry. Weak lensing measures structure growth. The Cepheid residual comes from the distance ladder. They all point low for Ωm. That convergence is not nothing.

---

## On Dark Matter: Is This Paper Accidentally Finding Something?

This is the question I find most compelling, and I wish the paper had engaged with it directly.

Here is what interests me: weak lensing measures the **projected mass** along the line of sight — it is sensitive to the total matter power spectrum at low and intermediate redshift. The CMB measures the matter density at recombination via the acoustic peaks and the damping tail. If dark matter has even a small self-interaction cross-section that is velocity-dependent — which is entirely possible and has been discussed in the context of the "too-big-to-fail" problem and the "core-cusp" problem — then structure at late times could be subtly suppressed relative to what you predict from the early universe.

The Aubourg 2015 BAO paper I searched considers dark matter that "decays into radiation" and finds that the current data constrains but does not eliminate such scenarios. A decay fraction of even a few percent, spread over the Hubble time, could look exactly like what Martin is seeing: late-universe Ωm slightly below early-universe Ωm, with suppressed σ₈.

There is another possibility I find less exotic: **massive neutrinos**. Neutrinos suppress structure growth at small scales, and their contribution to Ωm is not negligible. If the neutrino mass sum is toward the upper end of current constraints — the Planck+BAO 95% limit is around 0.12 eV, but the actual sum is unknown — the effective Ωm in matter clustering at z ~ 0.5 would be slightly lower than the total Ωm measured by the CMB. This is a known effect, not new physics, but it could account for part of what Martin is calling a "discrepancy."

The paper would benefit substantially from explicitly discussing neutrino mass as a confound and from engaging with scale-dependent dark matter models. The Ωm deficit it identifies may be real, but the explanation space is wider than the paper acknowledges.

---

## Overall Verdict: Should This Be Published?

Let me say something direct, because I believe in directness more than diplomatic hedging.

**The core observation is valid.** When you compare H₀ values extracted under different assumed cosmologies without accounting for the implicit Ωm difference, you are not comparing like with like. This is a real issue. The field has been somewhat sloppy about it. Martin is right to flag it, and the ξ ≡ dc/dH normalization is a sensible tool for making the comparison dimensionally honest.

**The 93.3% figure is too precise to be trusted.** A claim that the tension is "93.3% artifact" requires that the residual decomposition is exact, that no other parameters co-vary, and that the assumed Planck-vs-SH0ES Ωm difference is itself well-characterized. None of those conditions is fully satisfied. The calculation may be directionally right while being numerically overconfident.

**The ~3% Ωm residual is the real contribution of this paper.** And here Martin does something I respect: he follows the data. Rather than claiming to have solved the Hubble tension, he decomposes it and finds that the genuine residual — after removing the frame artifact — is a matter density discrepancy. That residual has independent support from KiDS and DESI. That is a testable, falsifiable, observationally grounded claim.

**What the paper needs before publication:**

1. The DES Y3 Ωm = 0.289 central value should be accompanied by its full posterior range. Central values without uncertainties are not evidence.

2. The paper must engage with neutrino mass as an alternative explanation for the Ωm deficit. This is the simplest physics explanation and has to be excluded before exotic mechanisms are invoked.

3. The "93.3% artifact" claim needs uncertainty quantification. What are the error bars on that fraction? How sensitive is it to the assumed Ωm inputs?

4. The discussion of dark matter evolution is entirely absent. If an Ωm deficit between early and late universe is real, this is arguably the most profound implication of the paper, and it is not discussed at all.

**Final judgment:** This paper identifies a genuine methodological issue, performs a reasonable decomposition, and arrives at a physically interesting residual that is consistent with other data. The strongest version of its claim — that 93.3% of the Hubble tension is artifact — is overconfident. But the underlying observation — that the comparison of H₀ across different Ωm frameworks conflates a coordinate artifact with physics — deserves to be published, read, and argued with.

Publish it, with revisions. The community needs to have this argument out in the open.

I have seen the universe confound confident theorists before. I am not confident in any direction about what Ωm is really doing between z=1100 and today. But I am confident that dismissing this paper without engaging with its core decomposition would be a mistake.

---

*V.C. Rubin*
*Referee report, April 2026*