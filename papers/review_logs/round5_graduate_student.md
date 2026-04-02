# Round5 Graduate Student
**Task ID:** ad86c194a33bfb6f4
**Session:** 79970414-2a9f-4110-8bf7-d3e67324fc3e
**Date:** 2026-04-01

---

Good. I now have everything I need to give a full, honest journal club reaction. Here it is.

---

# Journal Club Reaction: "The Hubble Tension as a Measurement Artifact"

*Eric D. Martin, preprint 2026-03-24. Written from the perspective of a first-year PhD student.*

---

## 1. The Core Argument in My Own Words

The paper claims that the 5-sigma Hubble tension is mostly an illusion produced by comparing two numbers that were computed in incompatible coordinate systems.

The central technical move is this: define xi = d_c / d_H, where d_c is comoving distance and d_H = c/H_0 is the Hubble radius. If d_c was computed from a redshift integral — that is, d_c = (c/H_0) * integral(dz/E(z)) — then H_0 appears in both numerator and denominator and cancels exactly. So xi depends only on the shape of the cosmology (Omega_m, Omega_Lambda), not on H_0. The paper then says: when you compare SH0ES and Planck in xi space, the difference shrinks by 93.3%, leaving only a ~3% residual that is a real Omega_m discrepancy, not an H_0 crisis.

For Cepheid distances, the paper correctly notes that H_0 does NOT cancel in xi, because d_c there is a directly measured physical distance. So xi = d_c_physical * H_0 / c. The paper uses the 43 Cepheid calibrators to compute H_0 implied per object as H_0 = cz / d_c, getting a mean of 69.78 km/s/Mpc — between the Planck and SH0ES values — and says this is evidence the "true" H_0 is closer to 70.

That's the argument. Now here's where I got confused and where I think it breaks.

---

## 2. Every Point I Could Not Follow

### Confusion A — The cancellation is real, but is it the right question?

The H_0 cancellation in xi is mathematically correct. I verified it myself. If you define d_c = (c/H_0) * f(z, Omega_m) and d_H = c/H_0, the ratio is just f(z, Omega_m). H_0 cancels. That is not in dispute.

But here is my problem: this is exactly what the existing literature already does. The quantity the SH0ES pipeline actually measures is the distance modulus mu = 5 log10(d_L / 10 pc). Riess et al. are not reporting H_0 by computing d_c and then dividing by d_H. They are calibrating the absolute magnitude M_B of Type Ia supernovae using Cepheid host galaxies, then reading off H_0 from the intercept of the Hubble diagram. The H_0 that comes out of SH0ES is NOT computed as a ratio of two redshift-derived distances — it is anchored to geometric distances (LMC eclipsing binaries, MW parallax, NGC 4258 megamaser). Those geometric anchors fix M_B. Then M_B fixes the distance scale. Then the Hubble diagram gives H_0.

So my question is: **the paper's xi cancellation applies to redshift-derived distances, but the whole point of SH0ES is that they are NOT using redshift-derived distances for the calibration step.** When the paper says "93.3% of the tension dissolves for redshift-derived distances" — yes, mathematically, but the tension exists precisely because one side is using geometric distances. The paper seems to treat this as a disclosure rather than a problem. I am not sure it is that clean.

### Confusion B — The 93.3% figure: what is it actually measuring?

I read the code carefully (gaia_zero_bias_test.py). The computation is:

1. Take the 1,671 non-calibrator SNe Ia.
2. Compute d_c for each from its redshift, under SH0ES parameters (H0=73.04, Om=0.334) and Planck parameters (H0=67.4, Om=0.315).
3. Compute xi for each under each cosmology.
4. The mean |delta_xi| is 1.11e-3. The raw H_0 fractional tension is ~8.4%. The paper says 1.11e-3 / 8.4% = ~1.3%, so 93.3% removed.

But I have a conceptual objection. Step 2 computes d_c from the SAME redshifts in both cosmologies, just plugging in different parameters. Of course the xi values are nearly identical at low redshift — at z << 1, xi ≈ z regardless of any parameters. The H_0 cancellation is a mathematical identity, not an empirical result. You are not "discovering" that 93.3% of the tension dissolves — you are demonstrating a tautology.

The actual SH0ES measurement of H_0 does not work by computing d_c from redshifts and comparing to Planck's d_c from redshifts. It works by comparing geometric distance anchor → SN absolute magnitude → Hubble diagram intercept. You can't wash away the tension by showing that a redshift-to-distance conversion is H_0-invariant, because that conversion is not what causes the tension.

**The MNRAS editor said exactly this, and I think the editor is right:** "The use of the horizon-normalised coordinate is simply a redefinition after which no properly-calculated observable result could change."

### Confusion C — "Unimodal, centered well below 73"

The paper reports H_0 implied per Cepheid calibrator: mean 69.78, sigma 13.97, range 41.6 to 112.0. With sigma = 13.97, you cannot say this distribution is "centered well below 73." That is a 0.23-sigma statement. The mean is 69.78, and 73 is within 0.23 sigma of it. The median is 71.51 — also within 0.1 sigma of both competing values. This is noise, and the paper is overinterpreting it.

Why is sigma = 13.97? I read the code. The computation is H_0 = c*z / d_c per object. At very low redshift (z < 0.05), peculiar velocities v_pec of order 300 km/s contribute an error of delta_H_0 ~ v_pec / d_c. For a galaxy at 10 Mpc, that's 300/10 = 30 km/s/Mpc uncertainty on H_0 from a single galaxy. These objects are too nearby for this computation to be meaningful as a cosmological H_0 measurement. SH0ES knows this — it's why they use the full Hubble diagram fit rather than per-galaxy naive estimates.

So the paper is computing H_0 in the way it is specifically wrong to compute it (naive cz/d), getting enormous scatter, and then claiming the mean is meaningful. The 13.97 km/s/Mpc sigma is not a quirk — it signals that the estimator is dominated by peculiar velocity noise.

### Confusion D — The f_artifact formula

The paper's table says "Artifactual (frame-mixing) ~ 5.5%" and "Physical residual in xi ~ 3%." These don't add up to 8.4% exactly — they add to 8.5%, fine, rounding. But I could not find the formula f_artifact = 1 - |delta_xi| / |delta_H_0/H_0| explicitly derived anywhere. It appears to be just the complement of the xi residual fraction. That's a tautology dressed as a measurement.

### Confusion E — Which Omega_m for SH0ES?

The paper uses SH0ES Omega_m = 0.334. This comes from the Pantheon+ dataset metadata. But the prompt mentions R22 uses q_0 = -0.51, implying Omega_m ≈ 0.327 (from q_0 = Omega_m/2 - Omega_Lambda). The paper never flags this discrepancy. And I note from the reviewer_reply file that an earlier version of the code had Omega_m = 0.334 from a *buggy BAO fitter* (fixed r_s, wrong gradient), not from the literature. The submission uses 0.334 from Pantheon+SH0ES.dat — that is legitimate, it is in the Brout et al. data release. But the fact that the same number appeared in a buggy computation earlier is worth noting.

### Confusion F — The JWST objection section

The paper says the JWST 8-sigma result "measures the artifact more precisely." This is the key claim and I'm genuinely unsure whether it is right or circular. JWST reduced the known HST systematic (crowded fields, blending) and still got H_0 = 73.17. If the "artifact" were due to a systematic in Cepheid photometry, JWST would have reduced it. If the "artifact" is purely the mathematical frame-mixing, then yes, better data cannot remove a mathematical incompatibility.

But the paper's answer to the JWST objection is: "the frame-mixing argument holds for JWST data for precisely the same mathematical reason." That's not an answer — it just re-asserts the tautology. What it would need to show is that the JWST geometric distance ladder, when treated as geometric (not redshift-derived), does NOT close the tension — and indeed the code finds median JWST-implied H_0 of 68.66 km/s/Mpc. But that's the same peculiar-velocity-dominated estimator that gives sigma ~ 14 on the HST calibrators. It tells me very little.

---

## 3. Verifying the 93.3% Calculation

Let me work through this myself.

xi = d_c / d_H = [∫dz/E(z)] (dimensionless)

For SH0ES: xi = ∫_0^z dz' / sqrt(0.334*(1+z')^3 + 0.666)

For Planck: xi = ∫_0^z dz' / sqrt(0.315*(1+z')^3 + 0.685)

At z = 0.1: the integral is dominated by the linear term, xi ≈ z = 0.1 regardless. Delta_xi ~ 0.

At z = 0.5: the Omega_m term matters more. The difference in E(z) between Omega_m=0.334 and 0.315 is roughly delta_E/E ~ (0.019 * (1.5)^3) / (2 * E^2) ~ (0.064) / (2 * ~1.24) ~ 2.6%. The integrated effect over z = 0 to 0.5 gives delta_xi / xi of order 1-2%.

The raw H_0 tension is (73.04 - 67.4)/67.4 = 8.4%.

So the xi residual from the Omega_m difference alone is ~1-2% of an 8.4% tension, leaving ~6-7% dissolved. The paper claims 93.3% dissolved, leaving 6.7% as the xi residual. That is consistent with this estimate.

**So the arithmetic is defensible.** The 93.3% is a real number derived from a real calculation. My objection is not to the arithmetic — it is to whether the arithmetic measures what the paper claims it measures.

The H_0 cancellation in xi is not removing a systematic from the SH0ES measurement. It is demonstrating that if you had computed both distances from redshifts using different Omega_m, the redshift-only comparison would differ only by the Omega_m amount. SH0ES does not compute its calibration distances from redshifts. The calculation is internally consistent but externally irrelevant to the actual source of the tension.

---

## 4. Questions I Would Ask in Journal Club

These are the ones that would make the speaker pause:

**Q1.** "You show H_0 cancels in d_c/d_H when d_c is redshift-derived. But SH0ES's key innovation is that their calibration distances are NOT redshift-derived — they are anchored to Cepheid period-luminosity, which is anchored to geometric parallax and eclipsing binaries. How does your xi cancellation apply to those steps?"

**Q2.** "Your 93.3% figure comes from comparing xi values computed from the same redshifts under two cosmologies. Since xi is by construction H_0-independent, isn't the 93.3% just a demonstration that xi is H_0-independent — which is true by definition — rather than evidence that 93.3% of the observed tension is artifactual?"

**Q3.** "Your Cepheid-implied H_0 has sigma = 13.97 km/s/Mpc. This is dominated by peculiar velocity scatter at z < 0.05. SH0ES uses 43 hosts precisely because you need to fit the full Hubble diagram to average over peculiar velocities, not compute cz/d per object. Why is your per-object naive estimator informative when it gives a range of 41 to 112?"

**Q4.** "MNRAS's editor says xi normalization is 'simply a redefinition after which no properly-calculated observable result could change.' Your reply to JWST says the same — that measuring Cepheids more precisely 'measures the artifact more precisely.' How would you distinguish this prediction from one that says your framework cannot be falsified?"

**Q5.** "You say the 73.04 value 'emerges from the pipeline, not from the stars themselves.' Freedman's TRGB gets ~70. But the Carnegie-Chicago Hubble Program using TRGB also anchored to the geometric distance to NGC 4258 gets H_0 ≈ 69.8. Meanwhile, Blakeslee et al. using surface brightness fluctuations gets 73.3. If the artifact is in the 'pipeline,' why do methods with completely different pipelines land on both sides of the split?"

**Q6.** "The paper references a Omega_m = 0.334 for SH0ES throughout. But your own reviewer_reply file shows that this number appeared earlier in your work from a broken BAO fitter with fixed r_s. The Pantheon+ dataset does use 0.334, but can you clarify the provenance so a reader can be sure these are not accidentally the same value for different reasons?"

**Q7.** "The MNRAS rejection says there is no indication of statistical methodology — no error propagation, no Fisher matrix, no MCMC posterior. The 93.3% and 3% numbers come from mean |delta_xi| divided by raw fractional H_0 tension. What is the uncertainty on 93.3%? Could it be 80% or 99%? How would we know?"

---

## 5. My Overall Impression

I want to be honest here because I am genuinely trying to understand, not to be harsh.

The mathematical core is correct and clearly stated. xi = d_c/d_H is H_0-independent when d_c is computed from redshifts. That is a true statement and the code confirms it. The residual |delta_xi| between cosmologies is driven by Omega_m differences. Also true.

But the paper conflates "xi is H_0-independent" with "93.3% of the tension is a coordinate artifact." These are not the same claim. The tension exists because geometric distances (Cepheid calibration) and CMB-inferred distances disagree. The paper correctly notes that xi does NOT eliminate the tension for geometric distances. So the "93.3% removal" is calculated exclusively in the regime where the cancellation is an identity — and then used to characterize the tension that lives in the other regime. That is a gap in the logic that I cannot close.

The Cepheid analysis has a real problem. Naive cz/d at z < 0.05 is not a measurement of H_0 — it is peculiar velocity noise. Reporting 69.78 ± 13.97 and saying it sits "between the two camps" without noting that the uncertainty is so large it is compatible with any value from 42 to 112 is presenting noise as signal.

The JWST objection section is the weakest. The paper says better data "measures the artifact more precisely." This is unfalsifiable as stated. A genuine systematic goes away with better data. A coordinate frame incompatibility (if real) does not — but the paper has not ruled out that what JWST is actually measuring is a genuine astrophysical signal. The section needs a stronger engagement with why we should believe the frame-mixing interpretation over the new-physics interpretation.

The forward section about LSST and Euclid is speculative in a way that is not grounded by the analysis. The analysis is of 1,671 SNe Ia in the existing Pantheon+ dataset. Whether xi normalization should be adopted as a standard by the IVOA is a much larger claim that needs community engagement, not a single preprint.

The MNRAS rejection is, in my reading, fair. The editor's two main points are correct:

- The xi redefinition cannot, by itself, change any properly-calculated observable result. The paper needs to point to a specific equation in SH0ES or Planck that contains an error caused by frame-mixing. It does not do this.
- The statistical methodology is absent. There are no error bars on the 93.3%, no covariance treatment, no comparison to established tension metrics.

**My overall verdict: interesting idea, fatally underspecified.** The core mathematical insight — that xi is H_0-independent for redshift-derived distances — is correct and worth knowing. The claim that this resolves 93.3% of the observed tension is not supported by the analysis as written, because the analysis computes the cancellation in a regime that is not where the tension lives. The Cepheid result is dominated by noise and does not support the claimed conclusion.

This is not something I would dismiss at first glance — there is a real thought here about coordinate frame dependencies in cosmological measurements, and the Omega_m convergence section is the most compelling part of the paper. But as currently written, I would agree with MNRAS: the paper does not demonstrate what it claims to demonstrate, and a smart referee (or a first-year PhD student preparing a journal club) will see that gap on a first read.

The path to a publishable version, in my view, would require: (1) identifying a specific, concrete equation in the Riess or Planck pipeline that introduces the frame-dependence; (2) showing by direct calculation that using xi removes a bias in an actual observable, not just in a mathematical redefinition; (3) replacing the naive cz/d H_0 estimate with a proper posterior; and (4) computing uncertainties on every headline number.