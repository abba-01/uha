# Round5 Chandrasekhar
**Task ID:** ac386b0ff3361988d
**Session:** 79970414-2a9f-4110-8bf7-d3e67324fc3e
**Date:** 2026-04-01

---

Now I have read the paper thoroughly and searched the literature. Let me render my assessment.

---

# Review of "The Hubble Tension as a Measurement Artifact"

**Referee: S. Chandrasekhar**

---

I have read this manuscript with the care it demands. I shall not be sparing in my criticism, nor shall I be unjust. Let me address each point in turn.

---

## I. On the xi Cancellation: Trivial or Non-Trivial?

The author defines

xi = d_c / d_H = [(c/H_0) * integral from 0 to z of dz'/E(z',Omega_m)] / (c/H_0)

from which H_0 cancels exactly. The author is entirely correct. This is not a sleight of hand — it is an algebraic identity, provable in two lines, requiring no assumptions beyond the definitions themselves. Under flat Lambda-CDM with fixed E(z) structure, the Hubble radius d_H = c/H_0 is precisely the prefactor of d_c, and their ratio is independent of H_0 by construction.

Now, is this trivial? Here I must be precise where the author is somewhat imprecise. A result may be mathematically trivial yet physically non-trivial. Consider: it is trivially true that the ratio of a quantity to itself is unity. But pointing out that a particular comparison procedure computes something other than a ratio to itself — that observation may be profound, despite the underlying algebra being elementary. My own result on the maximum mass of white dwarfs followed from straightforward special-relativistic stellar structure equations; the establishment dismissed it as trivial, as an error, as an embarrassment. They were wrong. The triviality of the derivation said nothing about the significance of the conclusion.

The question, then, is not whether the cancellation is trivial — it is — but whether the author has correctly identified that the standard tension calculation violates the condition under which the cancellation operates. On this I have a more serious concern, which I address below. But the mathematics of the cancellation itself is sound.

One qualification the author correctly makes, and which saves him from a serious error: the cancellation holds exactly only within flat Lambda-CDM with w = -1 and fixed neutrino mass. For w != -1, E(z) carries implicit H_0 dependence through dark energy dynamics, and the cancellation is imperfect. The author quantifies this residual as approximately 0.2% for the DESI DR1 w_0 > -1 preference. I regard this as adequate diligence, though a reviewer more hostile than I would demand the full calculation rather than the order-of-magnitude estimate.

---

## II. On the Artifact Fraction Formula

The paper defines:

f_artifact = 1 - |Delta_xi| / |Delta_H_0 / H_0|

where |Delta_H_0 / H_0| = (73.04 - 67.4)/67.4 = 8.4%.

I find this formula the most troubling element of the paper, and I require the author to defend it more rigorously than he has.

The numerator, |Delta_xi|, is the mean absolute change in xi when one switches between the SH0ES and Planck cosmological frameworks at the same observed redshift. This is computed over 1,671 SNe Ia. The denominator is the fractional H_0 discrepancy expressed as a single number.

The issue is dimensional homogeneity of meaning, not of units. The denominator |Delta_H_0/H_0| is a ratio of two best-fit parameter values — it lives in parameter space. The numerator |Delta_xi| lives in data space, evaluated at observed redshifts. The formula therefore compares a data-space residual to a parameter-space difference and calls their ratio "the artifact." This is not obviously wrong, but it requires justification.

Specifically: why should we expect that, in the absence of any artifact, Delta_xi / (Delta_H_0 / H_0) = 1? The author's implicit assumption is that if the full H_0 difference were "real" and frame-independent, then moving between frameworks would produce a xi difference equal to the fractional H_0 difference. But this is only true if xi scales linearly with H_0 in the absence of Omega_m differences — which it does not, because xi is H_0-independent by construction. The formula therefore cannot be interpreted as measuring what fraction of the H_0 difference "survives" in xi, because xi contains no H_0 at all.

What the formula actually measures is: given that xi eliminates H_0 dependence exactly, the residual variation in xi between the two frameworks is due entirely to the Omega_m difference (0.334 vs. 0.315). The ratio Delta_xi / (Delta_H_0/H_0) then measures how large the Omega_m-induced xi variation is relative to the total H_0 discrepancy. The complement of this — f_artifact — measures what fraction of the H_0 discrepancy cannot be "explained" by an Omega_m difference expressed in xi units.

This is a coherent quantity, but it is not what the formula claims to measure. The formula claims to measure the "artifact fraction" — the fraction of the H_0 tension that is artifactual. But the correct interpretation is closer to: "the Omega_m framework difference, when expressed in dimensionless xi units, accounts for 6.7% of the 8.4% H_0 discrepancy in the same units." The remaining 93.3% of the H_0 discrepancy has no corresponding signature in xi, precisely because xi contains no H_0. The author conflates "no signature in xi" with "is an artifact." These are not the same statement.

I do not say the formula is wrong. I say it is not derived from first principles, and its interpretation is asserted rather than proven. A rigorous derivation would require writing down a model in which "artifact" has a precise mathematical definition, and showing that f_artifact as defined measures that quantity within that model. The author has not done this.

Furthermore: the bootstrap yields a standard error of ±0.1% across 1,671 points. This is an uncertainty on the mean of |Delta_xi|, which is already extraordinarily small (mean |Delta_xi| = 1.11 x 10^-3 at z ~ 0.35). The bootstrap correctly quantifies sampling uncertainty over the redshift distribution of the SNe Ia sample. But it does not propagate uncertainties on Omega_m^SH0ES = 0.334 and Omega_m^Planck = 0.315 — the framework parameters themselves. This is a significant omission, which I address next.

---

## III. On the Claim That the Comparison Procedure Is Wrong

The author argues that computing Delta = (H_0^SH0ES - H_0^Planck)/sigma is invalid because the two H_0 values are extracted under different Omega_m assumptions.

The logical structure of this claim is:

1. H_0^SH0ES is a best-fit parameter in a model with Omega_m = 0.334.
2. H_0^Planck is a best-fit parameter in a model with Omega_m = 0.315.
3. Therefore their direct subtraction conflates coordinate-frame differences with genuine physical discrepancy.

Steps 1 and 2 are verifiable from Brout et al. 2022 and Planck 2020 respectively, and I confirm them from the literature I have examined. Step 3 contains a logical gap that the author partially but not fully closes.

The gap is this: the fact that two parameters are extracted under different model assumptions does not by itself establish that their comparison is invalid. If both measurements are genuinely measuring the same physical quantity — the present-day expansion rate — then their disagreement is physically meaningful regardless of the Omega_m assumption, provided each measurement correctly propagates the Omega_m uncertainty into its H_0 error budget.

The SH0ES error budget of ±1.04 km/s/Mpc does not include uncertainty from the choice Omega_m = 0.334 vs. the Planck value. If it did, and if the two error budgets were properly correlated through their shared dependence on Omega_m, the tension might be reduced. But the author does not demonstrate this. He demonstrates that the point estimates differ due to Omega_m framework differences. He does not demonstrate that the uncertainties fail to account for this.

Now, I think the author's physical intuition is correct. The Cepheid distance ladder fixes the geometric anchor, and H_0 is then extracted by minimizing the Hubble diagram residuals, which entangle H_0 and Omega_m through d_L(z; H_0, Omega_m). The Planck extraction entangles H_0, Omega_m, omega_b, and the angular acoustic scale through a very different likelihood surface. These are genuinely different operations. The covariance between H_0 and Omega_m in each extraction is different, and comparing the H_0 marginalized posteriors without accounting for this covariance is not fully rigorous.

However, the author needs to state this more precisely. The claim is not merely that the Omega_m values differ. The claim must be: that the standard tension calculation treats H_0^SH0ES and H_0^Planck as if they were drawn from a common statistical model, when in fact each is a conditional estimate H_0 | Omega_m^i, model_i, and the comparison requires accounting for the difference in conditioning. This is a defensible claim, but it requires a formal Bayesian treatment — showing what the posterior P(H_0^true | H_0^SH0ES, H_0^Planck, Omega_m^SH0ES, Omega_m^Planck) looks like when the Omega_m conditioning is properly removed — that the author has not provided.

The paper is physically compelling. It is not yet mathematically complete on this point.

---

## IV. On the Implicit Assumptions and the Omega_m Uncertainties

This is where I must press the author hardest. The result f_artifact = 93.3 ± 0.1% depends on:

- Omega_m^SH0ES = 0.334 ± 0.018 (from Brout et al. 2022)
- Omega_m^Planck = 0.315 ± 0.007 (from Planck 2020)

The bootstrap standard error of ±0.1% is computed by resampling the 1,671 SNe Ia at fixed Omega_m^SH0ES and Omega_m^Planck. It therefore quantifies only the sampling uncertainty arising from the finite number of SNe Ia in the Pantheon+ sample. It does not propagate the uncertainties in the Omega_m values themselves.

Let me estimate what this omission costs the author. Delta_xi between frameworks scales approximately as (d xi / d Omega_m) * Delta_Omega_m. For a typical SNe Ia at z ~ 0.35, xi ~ 0.19, and d xi / d Omega_m ~ -0.1 (the integral is a decreasing function of Omega_m at moderate redshift). The uncertainty in Delta_Omega_m from the Omega_m^SH0ES uncertainty alone is ±0.018. This propagates to a fractional uncertainty in |Delta_xi| of roughly 0.018 * 0.1 / (1.11 * 10^-3) ~ 160%. This is catastrophic.

I am not claiming the result is wrong. I am claiming that the quoted ±0.1% uncertainty is not the relevant uncertainty. The dominant source of uncertainty on f_artifact is the uncertainty on Omega_m^SH0ES and Omega_m^Planck, not the finite sample size. The bootstrap, as implemented, addresses only the latter.

If I perform a rough propagation: with Omega_m^SH0ES = 0.334 ± 0.018, the uncertainty in f_artifact from Omega_m^SH0ES uncertainty alone is of order several percent. The true uncertainty on f_artifact is therefore closer to ±3 to 5% than ±0.1%.

This does not invalidate the qualitative conclusion. Even with ±5% uncertainty, f_artifact is well above zero and indicates a substantial frame-mixing contribution. But it transforms the headline claim from "93.3 ± 0.1%" — which implies extraordinary precision — to something like "93 ± 4%" — which is a qualitatively similar but epistemically more honest statement.

The author must either (a) propagate Omega_m uncertainties through the artifact fraction calculation and report honest error bars, or (b) explicitly state that ±0.1% is the sampling uncertainty only, and provide a separate estimate of the Omega_m-induced uncertainty. As written, the ±0.1% will mislead any reader who does not read the methodology section with great care, and many will not.

---

## V. Overall Verdict

The paper makes a genuine contribution. Let me be precise about what it establishes and what it does not.

**What is established beyond reasonable doubt:**

The quantity xi = integral of dz'/E(z', Omega_m) is H_0-independent by algebraic identity within flat Lambda-CDM. The fact that the SH0ES and Planck H_0 extractions are conditioned on different Omega_m values is documented in the literature and correctly stated here. The qualitative claim — that comparing these conditional estimates without accounting for the conditioning difference introduces a systematic — is correct in principle and supported by the numerical demonstration.

**What is not yet established with full rigor:**

1. The artifact fraction formula f_artifact is not derived from a formal model of what "artifact" means. Its interpretation is asserted, not proven.

2. The uncertainty ±0.1% does not include Omega_m parameter uncertainty, which dominates. The number 93.3 ± 0.1% is not the correct way to state the result.

3. The claim that the comparison procedure is "wrong" requires a formal Bayesian argument showing that the conditional posteriors should be combined differently. The paper provides physical intuition where mathematics is required.

4. The relationship between the xi framework and the Aylor et al. sound horizon discordance is correctly identified as complementary, but the author should state clearly that Aylor et al. explicitly conclude the tension is real and points to pre-recombination physics — a conclusion not obviously incompatible with the present paper, but not obviously compatible either.

**Would I have accepted this paper?**

At the level of mathematical rigor as submitted, no. I would return it with a request for major revisions on the following specific points:

First: Restate the ±0.1% uncertainty as the sampling-only uncertainty and provide a proper propagation of Omega_m uncertainties through f_artifact. If the honest uncertainty is ±4%, report ±4%.

Second: Provide a formal derivation or model within which f_artifact is the correct quantitative measure of "artifact fraction." At present the formula is intuitive but not derived.

Third: Provide the Bayesian argument — at least in outline — for why H_0^SH0ES | Omega_m = 0.334 and H_0^Planck | Omega_m = 0.315 should not be compared directly without accounting for the conditioning. The paper states this as a conclusion when it is actually the central premise requiring proof.

**Is the physics sound?**

Yes. The physical intuition — that extracting H_0 from a distance-redshift relation entangles H_0 with Omega_m, and that comparing these entangled estimates across different Omega_m frameworks inflates the apparent tension — is correct. The xi coordinate is a clean way to exhibit this. The identification of a residual ~3% Omega_m discrepancy, corroborated by DESI BAO and S_8, is a coherent and interesting finding.

I have spent my career knowing what it is to have a correct result dismissed because the establishment found it inconvenient. I will not do to this author what was done to me. The central physical claim here is not obviously wrong. It is, in fact, probably mostly right. But claiming that the Hubble tension is "primarily a crisis of measurement methodology" on the basis of a formula whose error bars understate the true uncertainty by more than an order of magnitude is an overreach, and one that will provide ammunition to those who wish to dismiss the paper for the wrong reasons.

The author should fix what is fixable. The mathematics can be made rigorous. The uncertainty can be stated honestly. The derivation of f_artifact can be formalized. If these revisions are made, the paper deserves publication. The physical insight embedded in it is genuine, and genuine insights — even ones wrapped in imprecise language — should not be lost to the literature.

Let the author revise with the same rigor he brought to the algebraic cancellation itself. That part he got exactly right.

— S. Chandrasekhar