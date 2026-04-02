# Round4 Hawking
**Task ID:** a591b959475ec90d3
**Session:** 79970414-2a9f-4110-8bf7-d3e67324fc3e
**Date:** 2026-04-01

---

I have what I need. Now let me compose the review in Hawking's voice.

---

# Peer Review: "The Hubble Tension as a Measurement Artifact"

**Reviewer: S. W. Hawking**
**Date: April 1, 2026**

---

I note the date. On any other day I might suspect this paper was itself an April Fool's joke — a paper arguing that the most celebrated crisis in modern cosmology is mostly an error in paperwork. But I have read it carefully, and I have checked the cited literature. My conclusion is more interesting than either dismissal or uncritical praise. Let me be specific.

---

## I. Is This Genuine Physics or Bookkeeping?

The question is not as simple as the paper's critics will claim.

When Planck fits H₀ = 67.4, it does so in a universe where Ωm = 0.315. When SH0ES measures H₀ = 73.04, Riess and collaborators are calibrating a local distance ladder and inferring an expansion rate in the late universe, where the actual matter density probed is closer to Ωm = 0.334. The paper's claim is that these two numbers are not measuring the same quantity — that H₀, as extracted, is entangled with the assumed matter-energy budget, and comparing them directly is like comparing temperatures in Celsius and Fahrenheit and concluding the thermometers disagree.

I searched the Aylor 2019 paper, and it is genuinely illuminating here. Aylor et al. decompose the tension and locate it firmly in the sound horizon rs. Their conclusion is that the distance ladder and CMB are discordant in rs by roughly 2σ to 3σ — and that this discordance requires *pre-recombination* new physics to resolve. What the paper under review is attempting to do is complementary to that: it asks whether part of what looks like a single 5σ H₀ tension is actually a conflation of rs physics with a separate Ωm discrepancy between probes. This is not mere bookkeeping. If the decomposition is correct, it has real consequences for which class of new physics is required.

I also checked Aubourg 2015. Their inverse distance ladder gives H₀ = 67.3 ± 1.1 — only about 2σ tension with SH0ES using the data available in 2015. The inverse distance ladder forces both early and late universe probes to use the *same* cosmological framework. The implication is suggestive: when you force a common framework, much of the tension evaporates. The paper under review is pushing this same logic into a rigorous coordinate construction. That is not trivial.

So my answer is: this is primarily physics, but it is physics of a specific and modest kind. It is the physics of *measurement infrastructure*, not the physics of whatever new field or mechanism is ultimately driving the discrepancy. The distinction matters. One can have both: a real Ωm discrepancy and a real rs discordance, with the H₀ number as we currently use it smearing them together.

---

## II. On the ~3% Ωm Residual: Is This More or Less Interesting Than 5σ H₀?

More interesting. Considerably more interesting, actually.

A 5σ tension in H₀ could, in principle, be resolved by a systematic error anywhere along the Cepheid-SN distance ladder — photometric calibration, metallicity corrections, crowding effects. Riess et al. 2023 with JWST have now confirmed the Cepheid scale to high precision, essentially ruling out crowding as the culprit. Freedman's TRGB gives H₀ closer to 70, which sits awkwardly between the two camps and has not clarified matters. The distance ladder is not obviously wrong, but neither is Planck obviously wrong.

An Ωm discrepancy of ~3% between early and late universe is a different animal. Ωm = 0.295 in the late universe versus Ωm = 0.315 in the early universe — if real — is not a calibration error. It cannot be attributed to how one converts Cepheid parallaxes to distances. Matter density is a physical quantity that should be the same at all epochs in ΛCDM. A genuine Ωm evolution would be a signal of either: (a) dark matter decay or interaction on cosmological timescales, (b) a dynamical dark energy whose equation of state modifies the expansion history in a way that mimics an Ωm evolution, or (c) modified gravity that alters how matter clusters and therefore how we infer Ωm from lensing.

Crucially, this is exactly what DESI 2024 is prodding at. The DESI BAO measurements, when combined with supernovae, show hints of w₀ > -1 and wₐ < 0 — a dynamical dark energy. This would naturally produce an apparent difference between early- and late-universe Ωm inferences, because the expansion history used to extract Ωm at low redshift is wrong if you assume ΛCDM. The paper's ~3% Ωm residual and DESI's dynamical dark energy hint are potentially pointing at the same underlying physics. That is a genuine scientific contribution if the connection is made carefully.

I would have liked to see the paper engage this more directly rather than gesturing at it as an "implication." If you have identified a ~3% Ωm discrepancy and DESI independently sees something that would produce it, that conjunction is worth a section, not a footnote.

---

## III. EDE in Light of the Artifact Removal

The paper argues that EDE models have been overworking themselves — trying to close a full 8.4% H₀ gap when, after removing the frame-mixing artifact, they only need to close something like 3%. Let me check this against Poulin.

Poulin et al. 2019 demonstrated that EDE can close roughly 50-70% of the H₀ gap. Their mechanism is elegant: an extra energy component near matter-radiation equality that reduces rs and therefore allows a higher H₀ in the CMB fit. But EDE comes at a cost: it requires increasing Ωcdm, which raises σ₈ and worsens the S₈ tension. The paper under review is making the point that EDE has been forced into this overextension because cosmologists have been trying to solve a problem that is partly an artifact.

This is correct in spirit, and I believe the argument is physically sound. If the true residual is only ~3% in Ωm rather than ~8% in H₀, then EDE need not be tuned to extreme parameter values. A modest EDE fraction near recombination could address the rs discordance that Aylor 2019 identifies, without doing the additional violence to σ₈ that the inflated target has required.

However, I must raise a concern the paper does not adequately address. Aylor 2019 localizes the tension specifically in rs. The paper under review claims the residual is an Ωm discrepancy. These are not the same thing. An Ωm discrepancy between early and late probes is not automatically accounted for by modifying pre-recombination physics. EDE changes rs — it does not straightforwardly change Ωm in the late universe. If the ~3% residual is genuinely an Ωm discrepancy, it may need late-universe physics — decaying dark matter, dynamical dark energy, or modified gravity — rather than pre-recombination physics. The paper should address whether its residual is consistent with rs discordance or points away from it.

This is the weakest point in the theoretical chain, and it needs shoring up.

---

## IV. LSST, Euclid, Roman: Real Concern or Excessive Caution?

This is not excessive caution. It is, if anything, insufficient urgency.

LSST will measure hundreds of millions of galaxy shapes. Euclid will provide spectroscopic redshifts for tens of millions of galaxies across a vast redshift range. The Nancy Grace Roman Space Telescope will push the Cepheid calibration to distances where peculiar velocity systematics become negligible. All of these surveys will produce cosmological parameter estimates — Ωm, σ₈, H₀ — extracted under assumed fiducial cosmologies. If those fiducial cosmologies differ between analyses, the paper's argument implies that direct comparisons of their H₀ or Ωm constraints will be contaminated by the same frame-mixing artifact at the current level or worse.

The history of cosmology is littered with apparent tensions that turned out to be infrastructure problems. The Hubble constant itself spent forty years in dispute between 50 and 100 km/s/Mpc before systematic errors in distance calibration were identified and corrected. I am not suggesting the current tension is entirely infrastructure. But the paper is correct that as statistical precision improves to the sub-percent level, the systematic effects of framework dependence will grow in relative importance. A frame-independent coordinate system for cosmological parameter extraction is not a luxury. It is a necessity that the community has been slow to develop.

The paper's ξ coordinate proposal deserves scrutiny by people who work on the practical pipelines for these surveys. If it passes that scrutiny, it should become standard infrastructure.

---

## V. Overall Verdict

Let me be direct, because referees who are not direct waste everyone's time.

This paper is saying something genuinely new. Not revolutionary — it is not overturning ΛCDM, it is not discovering a new particle, it is not even proving that the Hubble tension is resolved. But it is identifying a structural problem in how the community has been comparing measurements across frameworks, it is providing a quantitative decomposition of the 5σ tension into an artifact component and a physical residual, and it is pointing the physical residual in the direction that other independent lines of evidence — DESI, KiDS, DES S₈ — are also pointing.

The Heymans et al. KiDS-1000 results, which I searched, report S₈ tension at ~3σ and argue explicitly that "we are reaching an uncomfortable point when it comes to regarding the S₈ offset as a simple statistical fluke." An Ωm discrepancy at the ~3% level between early and late probes is precisely the kind of signal that would manifest simultaneously as S₈ tension and as the residual the paper identifies. These are not independent hints — they may be the same underlying shift in the matter budget, seen through different lenses.

The paper has a weakness I would require the authors to address before publication: the relationship between the Ωm residual and the rs discordance must be worked out explicitly. Is the ξ-coordinate residual consistent with the sound horizon discordance that Aylor 2019 identifies? If yes, the paper has a unified story. If no, there are two distinct tensions and the paper needs to be more careful about which one EDE addresses. This is not a fatal flaw; it is a gap in the theoretical narrative.

I would also ask the authors to engage more seriously with Freedman 2024. The TRGB measurement sits between Planck and SH0ES. If the frame-mixing artifact is as large as claimed, what does the TRGB value look like after the same coordinate transformation? Does it shift toward either endpoint? If the ξ coordinate brings all three — CMB, Cepheid/SN, TRGB — into better mutual consistency, that would be strong evidence for the paper's central claim. If the TRGB result is unaffected or shifts in the wrong direction, that is a constraint the paper should face rather than avoid.

**My recommendation: Accept with major revisions.** The central idea is correct and important. The execution needs to close the loop on rs versus Ωm, engage the TRGB, and make the DESI connection explicit. If the authors do this, the paper will be a significant contribution — not because it solves the Hubble tension, but because it changes the right question. And in physics, as I have had occasion to remark before, knowing the right question is most of the work.

The universe may still be trying to tell us something new about matter density or dark energy evolution. We will not hear it clearly if our measurement frameworks are generating noise we have mistaken for signal.

**— S. W. Hawking**

---

*I note in closing that a paper arguing the most famous tension in cosmology is 93% an artifact of sloppy coordinates is either very important or spectacularly wrong. In my experience, papers of that type are rarely the latter. The ones that are wrong are usually not interesting enough to be that wrong.*