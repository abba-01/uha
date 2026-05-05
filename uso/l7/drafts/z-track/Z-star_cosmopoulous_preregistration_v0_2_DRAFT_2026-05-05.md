# Z* — Pre-Registration: Cosmopoulous Cosmological Model (Structural)

**Status:** DRAFT v0.2 — pre-canonical, NOT deposited. Working draft for read-before-deposit cycle. Applies the 2026-05-04 gap-survey action list (Path B: structural Z* + child quant preregistrations).

**v0.2 delta from v0.1 (2026-05-01):** Path B chosen — Z* is preregistered as a *structural* cosmological hypothesis only; quantitative predictions are deferred to child Z** preregistrations to be locked when each prediction is computed but BEFORE that prediction's data is queried. §2 strong-identity language softened to "this preregistration treats X as Y" form. §1 armor section added with explicit "does not claim" sentences. §5 competing-hypothesis cross-references expanded (Z3, EDE, modified gravity, local-volume, non-standard inflation). §2 cross-protocol cascade made bidirectional + explicit (Z* null does not halt Z0–Z3; carrier-set theorem rejection halts Z*). EB three-outcome primitive table added to §3. Locally-finite-c claim moved to §5 postulate-level pending a distinguishing observable. BF>3 narrowing inherited from Z0/Z3. Marketing-language audit pass. Full changelog at §11.

**Working draft note:** This Z* is a child of the Z0 umbrella pre-registration deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19881689` (concept DOI `10.5281/zenodo.19881688`). It preregisters the **cosmopoulous-as-black-hole-interior structural model** as a formally registered cosmological hypothesis, derived from carrier-set theorem + railing-system framework + B-operator structural asymmetry. It inherits Z0's hypothesis-lock structure, evidence-class thresholds, kill-switch interpretation preamble, two-stage failure-publication commitment, and deposit chain. Quantitative tests are deferred to child Z** preregistrations.

| Self-reference field | Value |
|---|---|
| Version | v0.2 timestamped `2026-05-05T17:10:00Z` |
| Path | Path B (structural; quantitative claims deferred to child Z** preregistrations) |
| Predecessor | v0.1 (2026-05-01T05:50:00Z), preserved in repo |
| Parent (umbrella) | Z0 v1.2-hybrid at hubble-tensor commit `d842691`; DOI `10.5281/zenodo.19881689` |
| Working filename | `Z-star_cosmopoulous_preregistration_v0_2_DRAFT_2026-05-05.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |
| Pending bookkeeping | Pre-canonical until committed and renamed with bootstrap commit hash. |

**Standing artifact-hash-naming policy (inherited from Z0):** Every artifact carries its commit hash inside AND in filename. No hash, no canonical status.

---

## Zenodo metadata block (deposit-format)

> *Note: "deposit-format" not "deposit-ready" — fields are populated for the eventual deposit but read-before-deposit gate must clear before deposit-ready status is asserted.*

| Field | Value |
|---|---|
| Title | Z* Pre-Registration: Cosmopoulous Structural Cosmological Model |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint |
| Communities | (TBD — Zenodo community selection at deposit time) |
| Keywords | cosmology, black hole interior, cosmopoulous, structural preregistration, EB carrier, Hubble tension, recursive pair law |
| Related identifiers (is part of) | `10.5281/zenodo.19881689` (Z0 umbrella v1.2-hybrid) |
| Related identifiers (cites) | `10.5281/zenodo.19676237` (priority hash); `10.5281/zenodo.20028303` (Z3 cross-survey Ωm baseline audit); RSOS-260797 r4 (EB carrier characterization theorem, under review); US 63/902,536 (UHA provisional patent) |

---

## 1. Purpose

This pre-registration locks the **cosmopoulous-as-black-hole-interior structural model** before any cosmological hypothesis-adjudicating analysis is performed. The model claims our observable universe is treatable as the interior of a black hole, with the cosmological event horizon as the structural boundary, and various structural consequences derivable from the carrier-set theorem and EB algebra.

**Path B (structural-only) commitment:** This v0.2 preregisters STRUCTURAL claims (a)–(f) of §1.1 and the FACT that observables Pi will be computed in a follow-on study. It does NOT lock specific quantitative values. Each quantitative prediction will be locked in its own child Z** preregistration, once the prediction is computed, but BEFORE that prediction's data is queried. This preserves preregistration discipline at each step without forcing premature commitment to numerical values that may turn out to be analytically derivable from the framework.

### 1.1 Armor — what Z* does not claim

- **Z\* does not claim cosmopoulous-as-black-hole is established physics.** It preregisters a falsifiable structural test of structural predictions.
- **Z\* does not claim universal applicability** to all cosmological observables. It locks a specific set of observables (§3) where the cosmopoulous model and ΛCDM are predicted to differ structurally.
- **Z\* does not claim cyclic cosmology, multi-cosmopoulous transit, or PP precursor algebra cosmological role.** Those are postulate-level extensions in §5; not preregistered in this Z*.
- **Z\* does not claim to falsify ΛCDM or any competing cosmological model.** It tests one specific mechanism. A K-firing for Z* is consistent with multiple alternative explanations remaining viable.
- **A K-firing is a co-equal publishable outcome.** Failure-publication is locked per Z0 §9 (this document §6); it is not a fallback, it is the structural pair of any falsifiable preregistration.

### 1.2 Pre-registered hypotheses and decision locks (Z*)

Inherited from Z0 §1.1 unless narrowed below.

#### Primary structural hypotheses (Z*)

- **H0-Z\*:** This preregistration treats the observable universe's large-scale dynamics as correctly described by ΛCDM with standard cosmological parameters. No cosmopoulous-specific structural signature exists in the observables locked in §3.
- **H1-Z\*:** This preregistration treats the observable universe as the interior of a cosmopoulous (black-hole interior) with structural consequences:
  - (a) **Pull-not-push:** apparent expansion is treated as the inevitable forward-direction inside a black-hole geometry, not as metric stretching.
  - (b) **Horizon-growth:** what we measure as Hubble flow is treated as the rate of cosmological event horizon enlargement.
  - (c) **Light bent at horizons:** photons at the cosmological event horizon are treated as bent into the b-rail substrate (perpendicular to the e-rail), not destroyed.
  - (d) **Substrate-routed light:** some early-universe glow we observe (~280–400 Myr epoch) is treated as light bent and redirected via substrate routing, not solely original emission.
  - (e) **Mirror-counter-rotation at edge:** the edge is treated as carrying counter-rotation that maintains stability (axle-wheel topology); detectable in mass-rail observables but not light-rail observables.

(Claim (f) "locally-finite c" — moved to §5 postulate-level — see §5 below.)

#### Shared decision definitions

Inherited from Z0 §1.1. Z* narrowing:

- **Baseline:** ΛCDM with Planck 2018 best-fit parameters as the null reference
- **Improvement:** any §3 observable where the cosmopoulous model predicts a structurally DIFFERENT outcome than ΛCDM, and the observed value matches the cosmopoulous prediction within the stated quantitative threshold of that observable's child Z** preregistration
- **Primary success:** ≥ 2 of the §3 observables show cosmopoulous-predicted outcomes with Δχ² ≥ 20 against ΛCDM (per Z0 §1.4 stage-2 threshold), AND no §3 observable shows ΛCDM-favored result with Δχ² ≥ 20 against cosmopoulous, AND the supporting child Z** preregistrations clear before each respective analysis
- **Analysis start:** the first execution of a child Z**-locked observable extraction after Z* DOI is deposited and the child preregistration is itself deposited
- **Same-pipeline rule:** §3 observable extraction pipelines locked at child Z** deposit time; data versions, release dates, and access dates recorded at child analysis start
- **Controls:** ΛCDM best-fit predictions as the null; cosmopoulous predictions as the alternative; both with full covariance treatment per Z2 A3 audit

#### Data handling locks

Inherited from Z0 §1.1.

### 1.3 What would render Z* unsupported

Z* will be considered unsupported if any of the following K-criteria fire:
- **K0-Z\*:** All §3 observables show ΛCDM-favored values within stated child-Z**-locked uncertainty (no cosmopoulous structural signature)
- **K1-Z\*:** Cosmopoulous-predicted observables disagree with observation by Δχ² ≥ 49 in any single channel (Z0 stage-3 divert), with no mechanism-justified covariance term explaining the disagreement
- **K2-Z\*:** The model fails to recover BBN abundances when applied with cosmopoulous-equivalent early-time conditions
- **K3-Z\*:** The model fails to predict the observed CMB temperature within 10% under horizon-emission scaling
- **K4-Z\*:** The mirror-counter-rotation prediction (§3.4) cannot be reconciled with mass-rail observation bounds (e.g., BOSS / DESI structure correlations) under any consistent §3.4 child Z** locking
- **K5-Z\*:** Carrier-set theorem (RSOS-260797 r4 or its successor) is rejected. Since Z* depends on the carrier-set theorem as a load-bearing input, theorem rejection halts Z*.

If any of K0–K5 fire, Z* halts and a negative or narrow-method result is deposited under the failure-publication rule (Z0 §9, two-stage). This summarises §6's termination-criteria table.

### 1.4 Public-data-first scope

Per Z0 §1.3. Z* uses publicly available data:
- **Planck 2018 CMB maps** (ESA Planck Legacy Archive)
- **JWST early-universe galaxy catalog** (STScI MAST)
- **Pantheon+ supernova sample** (Brout et al. 2022)
- **DESI BAO measurements** (DESI Collaboration releases)
- **EHT M87\* and Sgr A\* images** (EHT Collaboration releases — used for fractal-self-similarity check, not direct cosmological inference)
- **BOSS / DESI structure correlations** (for mass-rail anisotropy diagnostics under child Z** locking)

Dataset versions, release dates, and access dates recorded at child Z** analysis start.

### 1.5 Evidence framework

Per Z0 §1.4 — canonical hierarchy used throughout this document:
- Δχ² ≤ 5: not significant
- 5 < Δχ² ≤ 20: stage-1 signal (description-changelog log)
- 20 < Δχ² < 49: stage-2 signal (potential mint per propagation policy)
- Δχ² ≥ 49: divert to fresh pre-reg

**Bayes-factor narrowing (parity with Z3):** Z0 treats BF > 1 as support; Z* narrows for adjudication — BF ≤ 3 is treated as insufficient support, although the raw BF is reported alongside Δχ² in all phase outputs. Per-observable BF thresholds may be further narrowed in the child Z** preregistration for that observable.

---

## 2. Cross-protocol coordination (bidirectional)

This Z* protocol coordinates with the linear Z0–Z3 chain (Z0 umbrella, Z1 Track-0 PNT overlay, Z2 Track-A coordinate provenance, Z3 cross-survey Ωm baseline common-baseline audit) and with the carrier-set theorem (RSOS-260797 r4).

**Cross-protocol cascade (v0.2 — bidirectional, narrowed):**

- **Z\* null does NOT halt Z0–Z3.** Z3 (cross-survey Ωm baseline) tests a different mechanism. A Z* null (K0-Z* through K3-Z*) is consistent with Z3 succeeding, and vice versa. The two are **competing-mechanism explanations for the same residual** (cross-survey cosmological tension); both could pass, both could fail, or either could pass while the other fails. Observation alone may not always distinguish them; a third arbitration document is expected if both mature to results.
- **Z\* halt on carrier-set theorem rejection (K5-Z*).** Z* depends on the carrier-set theorem as a load-bearing input (claims (a)–(e) of §1.2 invoke EB algebra structurally). If the theorem is rejected by independent review, Z* halts.
- **Z\* halt on UHA Coordinate Framework encoding integrity failure.** Mirrors Z3's K4 cascade. If UHA encoding round-trip integrity fails, §3 observables that rely on UHA-derived coordinates cannot be evaluated; Z* halts pending companion-protocol resolution.

The earlier formulation in v0.1 (silence on bidirectional cascade) is replaced. Cascade rules are now bidirectional and explicit.

### 2.1 Relationship to Z3 specifically

Z3 attributes a measurable fraction of the Hubble residual to **cross-survey Ωm-baseline disagreement** (a calibration / coordinate effect). Z* attributes the residual to **horizon-growth structural difference** (a substrate/geometry effect). They are competing-mechanism explanations:

- Both passing: the residual decomposes; some fraction is Ωm-baseline-mediated (Z3-explained), some is horizon-growth-mediated (Z*-explained).
- Z3 passes, Z* fails: the residual is dominated by cross-survey calibration; cosmopoulous structure is unsupported.
- Z* passes, Z3 fails: the residual is dominated by structural geometry; cross-survey calibration is not the active mechanism.
- Both fail: the residual is something else (early dark energy, modified gravity, local-volume, non-standard inflation, or unidentified).

Z* does NOT adjudicate between these scenarios; its Phase-equivalent observables make the decomposition visible.

---

## 3. Pre-Registered Observables (structural; quantitative locks deferred to child Z**)

### 3.1 EB carrier three-outcome primitive (added v0.2)

For comparing model predictions to observations, the EB carrier algebra provides a three-outcome primitive applicable to every §3 observable:

| Condition | PP input | EB output | Interpretation |
|---|---:|---:|---|
| Agreement | `(v, v)` | `(0, v)` | no expressed disagreement; cosmopoulous structurally consistent with observation at this observable |
| Disagreement | `(max, min)` | `(max−min, min)` | expressed disagreement in e-rail; shared floor in b-rail; cosmopoulous structurally distinguished from ΛCDM at this observable |
| Audit failed | unresolved | `(0, max)` | no expressed comparison; observable's child Z** locking did not produce extractable data |

Each §3 observable, under its child Z** preregistration, evaluates to one of these three primitive outcomes plus a Δχ² magnitude.

### 3.2 CMB temperature from horizon-emission

**Observable:** CMB monopole temperature T_CMB.

**Structural method:**
- Compute predicted T_CMB given the cosmopoulous's horizon mass-energy content + horizon radius + accretion-disk-equivalent thermal spectrum.
- Apply gravitational redshift from horizon to interior observer.
- Compare to observed T_CMB = 2.7255 ± 0.0006 K.

**Structural prediction (locked):** T_CMB derives from horizon-emission, not recombination physics. The prediction has an extractable closed form once horizon parameters are locked.

**Quantitative threshold:** deferred to child preregistration `Z**-quant-CMB` (to be deposited before extraction).

### 3.3 z\* (decoupling redshift) re-interpretation

**Observable:** the apparent redshift of last-scattering surface, z\* ≈ 1090.

**Structural method:**
- Cosmopoulous: z\* corresponds to a specific feature of horizon-emission spectrum.
- Compare predicted z\* to observed Planck 2018 value.

**Structural prediction (locked):** z\* corresponds to a horizon-emission spectrum feature, not recombination at T ≈ 3000 K.

**Quantitative threshold:** deferred to child preregistration `Z**-quant-zstar`.

### 3.4 Hubble tension as horizon-growth structure

**Observable:** SH0ES H0 vs Planck H0; the residual ~5σ tension.

**Structural method:**
- Cosmopoulous: H0 measured at different epochs samples different points in horizon-growth profile; SH0ES and Planck differ structurally because horizon growth isn't constant in cosmic time.
- Derive the horizon-growth function predicted by cosmopoulous structure.

**Structural prediction (locked):** The residual is structurally attributable to horizon-growth profile differences across measurement epochs.

**Quantitative threshold:** deferred to child preregistration `Z**-quant-Hubble`.

**Cross-reference to Z3:** Z3 locked the cross-survey Ωm-baseline mechanism for a measurable fraction of this same residual. Z* and Z3 are competing-mechanism preregistrations for the same residual; see §2.1.

### 3.5 Mirror-counter-rotation in mass-rail observables

**Observable:** Large-scale structure correlation tensors with handedness; gravitational-wave anisotropy.

**Structural method:**
- Mass-rail observations are predicted to preserve cosmopoulous-edge counter-rotation signature.
- Light-rail observations (CMB) are predicted NOT to show it (matter mediation washes it out).

**Structural prediction (locked):** Mass-rail observables exhibit anisotropy at multipoles where light-rail observables show isotropy.

**Quantitative threshold + multipole list + κ coupling:** deferred to child preregistration `Z**-quant-multipole`. (Per gap-survey G8: cross-survey BOSS×DESI κ coupling locks live with the quantitative child, not in this structural Z*.)

### 3.6 Substrate-routed light at Cosmic Dawn

**Observable:** Apparent maturity of JWST early galaxies at z = 14+.

**Structural method:**
- Cosmopoulous: some "early epoch" light is substrate-routed (bent and re-emerged), so observed objects' apparent age may include path-length effects.
- Statistical test: variance in stellar age estimates for z = 14 galaxy sample.

**Structural prediction (locked):** Age-spread between same-epoch objects is structurally larger than ΛCDM allows.

**Quantitative threshold:** deferred to child preregistration `Z**-quant-JWST`.

---

## 4. Locked Analysis Pipelines

(Pipeline specifics deferred to per-observable child Z** preregistrations. This Z* locks only the FACT that each pipeline will be specified before its data is queried.)

- **Pipeline P1** → `Z**-quant-CMB`: CMB monopole + spectral shape derivation under horizon-emission model
- **Pipeline P2** → `Z**-quant-zstar`: z\* prediction from horizon-emission peak
- **Pipeline P3** → `Z**-quant-Hubble`: SH0ES vs Planck H0 prediction from horizon-growth function
- **Pipeline P4** → `Z**-quant-multipole`: BOSS/DESI mass-rail anisotropy multipole analysis + κ coupling
- **Pipeline P5** → `Z**-quant-JWST`: JWST z = 14 galaxy age-variance statistical test

Each child preregistration locks: data version, extraction code commit hash, assumed parameters, statistical test, decision rule, BF threshold (≥ 3 narrowing, possibly tighter). Locked at child deposit time; cannot be modified post-child-deposit.

---

## 5. Postulate-level extensions (NOT pre-registered for this Z*)

These are framework extensions that COULD be tested but are not part of Z*'s primary success criteria:

- **Cyclic cosmology / bounce mechanism** — Z* doesn't test
- **Multi-cosmopoulous transit via decoupling** — Z* doesn't test
- **PP precursor algebra cosmological role** — Z* doesn't test
- **Recursive pair law universality** — Z* doesn't test (separate research target per WT-1 to WT-4)
- **Locally-finite c** — claim (f) of v0.1 H1 — moved here because no §3 observable in v0.1 distinguishes locally-finite-c from universal-c. Until such an observable is locked in a future child Z** preregistration, locally-finite-c is structurally postulated but not tested.

Each may become a separate Z\*\* preregistration in the future.

### 5.1 Acknowledged competing hypotheses (added v0.2)

This Z* preregisters the **cosmopoulous structural model as one candidate explanation** for the observed residuals. Other candidate explanations include:

- **Z3 cross-survey Ωm-baseline disagreement** (DOI `10.5281/zenodo.20028303`) — calibration-mediated mechanism for the same residual; competing-mechanism with Z*.
- **Distance-ladder calibration / systematics** — local-anchor or ladder-route choice may dominate the residual; Z3 stratifies for this.
- **Early dark energy** — new-physics solution at recombination epoch.
- **Modified gravity** — infrared modifications to GR.
- **Local-volume effects** — under-dense local region creating biased local H0.
- **Non-standard inflationary scenarios** — affecting CMB and large-scale structure observables.

A Z* K-firing (K0-Z* through K3-Z*) is **consistent with all of these alternatives**. Z* does not claim to falsify them; Z* tests one specific structural mechanism.

---

## 6. Termination criteria (canonical K0-Z\* … K5-Z\*)

| K | Trigger | Action |
|---|---|---|
| K0-Z\* | All §3 observables ΛCDM-favored within child-Z**-locked uncertainty | Z* halts; null result deposited |
| K1-Z\* | Single-channel Δχ² ≥ 49 disagreement with no covariance justification | Z* halts; investigate; possible new pre-reg |
| K2-Z\* | BBN abundance failure | Z* halts; framework needs revision |
| K3-Z\* | T_CMB prediction off by > 10% | Z* halts; horizon-emission model fails |
| K4-Z\* | Mirror-counter-rotation ruled out by mass-rail bounds | Z* halts; counter-rotation claim retracted |
| K5-Z\* | Carrier-set theorem rejected | Z* halts; structural foundation gone |

If any K fires, two-stage failure-publication per Z0 §9 within 14 days. **A K-firing is a successful preregistered outcome** — the test ran and falsified its mechanism cleanly.

---

## 7. What this pre-registration locks

- Hypotheses H0-Z*, H1-Z* with structural claims (a)–(e); claim (f) moved to §5 postulate-level
- Five observable categories (§3) with structural predictions; quantitative thresholds deferred to child Z**
- Six canonical termination criteria K0-Z* … K5-Z*
- Public-data-first scope
- EB three-outcome primitive table for observable evaluation
- Bidirectional cross-protocol cascade with Z0–Z3 + carrier-set theorem
- Failure-publication template
- Path B commitment: child Z** preregistrations will be deposited before each quantitative analysis begins

After this DOI is deposited, structural-claim-adjudicating analysis can begin under each child Z**'s additional locks. Modifications to structural claims require new pre-reg.

---

## 8. Provenance

Z* draws on:
- **Image-mode cosmological articulation 2026-05-01** (cosmopoulous-as-black-hole, pull-not-push, light-bending, edge-counter-rotation)
- **Carrier-set theorem** (manuscript in review, RSOS-260797 r4)
- **Recursive pair law** (carrier_state_rail_theory_v0_2.md §20)
- **Railing-system unification** (project_railing_system_discovery.md)
- **Witness-loss principle** (compile_carrier_set_identity_2026-05-01_v3.md §6)
- **(1,1) primitive conversion witness** (project_eb_primitive_conversion_witness_2026-05-05.md — Eric, 2026-05-05) — exhaustive-scan formal grounding for B-flip fixed-point selection
- **Z0 umbrella:** DOI `10.5281/zenodo.19881689` (deposited 2026-04-29)
- **Z3 cross-survey audit:** DOI `10.5281/zenodo.20028303` (deposited 2026-05-04) — competing-mechanism preregistration for the same residual; see §2.1

Three serious-physics anchors: Pathria 1972, Stuckey 1994, Popławski recent. These are minority-but-defensible cosmological views. Z* operationalizes them by adding the carrier-algebra structure.

---

## 9. Pre-deposit checklist

Before GATE:OPEN for deposit:

- [ ] Marketing-language audit pass (grep for "revolutionary", "Nobel", "100% explained", "completely solves", "definitively", "groundbreaking", "paradigm shift", "Einstein-level", "textbook-level", "resolution", "solves the Hubble tension"; any match fails)
- [ ] Confirm RSOS-260797 r4 current submission status
- [ ] Confirm Z3 deposit DOI (`10.5281/zenodo.20028303`) is live and citable
- [ ] Confirm Z0 DOI canonical
- [ ] Hard-print the Z* v0.2 draft
- [ ] 30-min cool-off (per `feedback_zenodo_publish_gate.md`)
- [ ] Eric reads printed copy and confirms (per `feedback_zenodo_publish_gate.md`)
- [ ] GATE:OPEN cycle: 9 steps per Z2's example
- [ ] Bootstrap commit + filename hash injection (rename to `v0_2_2026-05-05_<hash>.md`)
- [ ] Mint Zenodo DOI (cited as child of Z0 concept)
- [ ] Cross-link DOI commit
- [ ] Pre-canonical timestamped predecessor archived

---

## 10. Status

**Pre-canonical, draft v0.2 (Path B — structural).** NOT deposited. v0.1 preserved alongside.

Outstanding before deposit:
- Marketing-language audit
- Hard print + Eric-read + cool-off + GATE:OPEN
- Bootstrap commit + filename hash

This v0.2 inherits Z0 + Z2, applies Path B (structural-only with deferred quantitative children), softens strong-identity language, adds armor section, expands competing-hypothesis cross-references, makes cross-protocol cascade bidirectional, integrates EB three-outcome primitive, defers locally-finite-c to postulate-level, narrows BF adjudication parity with Z3, and explicitly cites Z3 as competing-mechanism preregistration.

After this Z* mints, child Z** quantitative preregistrations are deposited per observable as the prediction extractions are computed. Each child preregistration locks its own data, code, threshold, and BF criterion before its observation is queried.

---

## 11. Changelog (v0.1 → v0.2, 2026-05-05)

Path B chosen per `Z-star_cosmopoulous_gap_survey_2026-05-04.md` recommendation. Patches applied by gap number:

**Must-fix (gap survey §"Must-fix"):**

1. **G1 — TBD predictions.** v0.1 had "TBD by analysis" predictions in §3 — preregistration loophole. v0.2 chooses Path B: structural claims locked here, quantitative claims deferred to child Z** preregistrations; §3 narrative updated; §4 pipeline list now points to per-observable children.
2. **G2 — Strong-identity language.** v0.1 §2 said "the cosmological event horizon **is** the cosmopoulous edge". v0.2 softens to "this preregistration treats X as Y" form throughout §1.2.
3. **G3 — Armor section.** Added §1.1 with three explicit "does not claim" sentences plus K-firing co-equal-outcome statement.
4. **G4 — Competing-hypothesis section.** Added §5.1 naming Z3, distance-ladder systematics, EDE, modified gravity, local-volume, non-standard inflation. Z3 specifically called out as competing-mechanism preregistration for the same residual.
5. **G5 — Cross-protocol cascade narrowed.** §2 now bidirectional: Z* null does NOT halt Z0–Z3; carrier-set theorem rejection halts Z* (added K5-Z*).

**Should-fix:**

6. **G6 — EB three-outcome primitive.** Added §3.1 table.
7. **G7 — Hash-naming.** Mirrors Z3 procedure; bootstrap commit + filename hash injection at deposit time.
8. **G8 — §3.4 multipole + κ.** Multipole list and κ coupling locks deferred to `Z**-quant-multipole` per Path B.
9. **G9 — Marketing-language scrub.** Pre-deposit checklist retains the grep gate.
10. **G10 — BF narrowing.** Inherited Z3's BF > 3 narrowing; child Z** may further narrow per observable.
11. **G11 — Z3 / Z\* relationship.** Made explicit in §2.1 — competing-mechanism preregistrations for the same residual.
12. **G12 — Locally-finite c.** Claim (f) moved from §1.2 H1 to §5 postulate-level; stays there until a distinguishing observable is locked in a child Z**.

**Style / rhetoric:**

- "Conversion witness" / "first inhabited rail-symmetric state" framing for (1,1) added in §8 provenance, citing the 2026-05-05 exhaustion claim. Strengthens the algebraic ground for claims (a)–(e) without overstating.
- "K-firing is a co-equal publishable outcome" surfaced in §1.1 + §6.

---

*End of Z* draft v0.2 (Path B structural). Held for read-before-deposit cycle. Hard-print + Eric read + cool-off + GATE:OPEN required before mint.*
