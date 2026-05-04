# Z3 — Track B Pre-Registration: Cross-Survey Ωm Baseline Common-Baseline Audit

**Status:** DRAFT v0.2 — pre-canonical, NOT deposited. Working draft for read-before-deposit cycle. Applies the 2026-05-04 external consistency review (filed alongside as `Z3_consistency_review_outline_and_chat_log_2026-05-04.md`) and the Freedman/Madore-style outreach framing (filed as `Z3_freedman_pressure_test_outline_2026-05-04.md`).

**v0.2 delta from v0.1 (2026-05-01):** Δχ² thresholds normalized to Z0 5/20/49 hierarchy throughout; KS labels deprecated and aliased to canonical K0-Z3…K4-Z3; venue-prestige routing removed from §3.5; κ pre-Phase-3 lock procedure inserted in §3.3; cross-protocol cascade narrowed (Z3 null halts Track B only, not all UHA coordinate-provenance tests); EB three-outcome primitive table added; local-anchor and distance-ladder route stratification controls added (Phase 4); Pantheon+ SN-transfer separation added; "common-baseline audit" language used in decision rules (title preserves "unification" for indexing continuity); explicit non-challenge of SH0ES distance ladder; clean-null = valid publishable outcome surfaced. Full changelog at bottom.

**Working draft note:** This Z3 is a child of the Z0 umbrella pre-registration deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19881689` (concept DOI `10.5281/zenodo.19881688`). It deposits **Track B** of the three-track UHA + EB carrier program. It inherits Z0's hypothesis-lock structure, evidence-class thresholds, kill-switch interpretation preamble, two-stage failure-publication commitment, and deposit chain.

| Self-reference field | Value |
|---|---|
| Version | v0.2 timestamped `2026-05-04T16:55:00Z` |
| Predecessor | v0.1 (2026-05-01T13:09:00Z), preserved in repo |
| Parent (umbrella) | Z0 v1.2-hybrid at hubble-tensor commit `d842691`; deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` |
| Parent (Z2 audit framework) | Z2 deposited 2026-04-29 at DOI `10.5281/zenodo.19908184`; concept `10.5281/zenodo.19908183` |
| Source protocol | `Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md` (commit 77b639c); patent gates removed 2026-05-01 |
| Working filename | `Z3_omega_m_baseline_preregistration_v0_2_DRAFT_2026-05-04.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |
| Pending bookkeeping | Pre-canonical until committed and renamed with bootstrap commit hash. |

**Standing artifact-hash-naming policy (inherited from Z0):** Every artifact carries its commit hash inside AND in filename. No hash, no canonical status. No exceptions.

---

## Zenodo metadata block (deposit-format)

> *Note: "deposit-format" not "deposit-ready" — fields are populated for the eventual deposit but threshold/κ/naming gates must clear before deposit-ready status is asserted (per consult §2.10).*

| Field | Value |
|---|---|
| Title | Z3 Pre-Registration: Cross-Survey Ωm Baseline Unification Test |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint |
| Communities | (TBD — Zenodo community selection at deposit time) |
| Keywords | cosmology, Hubble tension, Ωm, dark matter density, cross-survey systematics, common-baseline audit, EB carrier, UHA, pre-registration |
| Related identifiers (is part of) | `10.5281/zenodo.19881689` (Z0 umbrella v1.2-hybrid) |
| Related identifiers (cites) | `10.5281/zenodo.19908184` (Z2 audit framework); `10.5281/zenodo.19676237` (priority hash); RSOS-260797 r4 (EB carrier characterization theorem, under review); US 63/902,536 (UHA provisional patent) |

---

## 1. Purpose

This deposit pre-registers Track B of the three-track UHA + EB carrier program: the **cross-survey Ωm baseline common-baseline audit** (referred to historically as "Ωm baseline unification" — the title preserves that phrase for indexing continuity, but decision rules in this document use the more neutral "common-baseline audit," "Ωm baseline substitution," and "cross-survey baseline consistency test"). Track B asks whether different cosmological surveys use different Ωm derivation chains and baselines, whether those differences create systematic effects appearing as cosmological tensions, and whether applying a unified UHA-derived Ωm baseline reduces those tensions across surveys.

Track B does NOT test "GPS positioning errors" (factually incorrect framing previously rejected). It tests **whether Ωm baseline inconsistencies across surveys create apparent cosmological tensions, and whether substituting a unified UHA-derived Ωm baseline reduces them.**

Track B does NOT claim Ωm-baseline unification is THE explanation for the Hubble tension. It locks a specific test of one candidate mechanism. Other candidate mechanisms (early dark energy, modified gravity, the cosmopoulous horizon-growth model registered separately as Z*, distance-ladder calibration systematics, etc.) remain open hypotheses for the same observation. An Ωm-unification null result (any of K0-Z3 through K3-Z3) is consistent with multiple alternative explanations.

**Z3 is not a Hubble-tension solution paper.** It is a pre-registered cross-survey common-baseline audit. Its success condition is not "H₀ solved." Its success condition is "a locked Ωm substitution reduces joint tension under identical likelihoods, without extra degrees of freedom, and robustly across local-calibrator routes."

**Z3 does not directly challenge the SH0ES distance-ladder calibration.** It tests whether cross-survey Ωm baseline substitution changes the joint-inference tension after the local-ladder H₀ measurement is held fixed as a public-data constraint. Direct challenges to ladder calibration are out of scope and would require a separate preregistration.

**A clean null result is a valid publishable outcome.** Failure-publication is locked per Z0 §9 (§6 of this document); it is not a fallback, it is a co-equal outcome.

### 1.1 Pre-registered hypotheses and decision locks (Track B)

Inherited from Z0 §1.1 unless narrowed below.

#### Hypotheses (Track B)

- **H0-Z3:** Cosmological surveys (SH0ES R22, Planck 2018, KiDS-1000, DES Y3, DESI DR1, Pantheon+) use Ωm baselines that agree within statistical uncertainty (|ΔΩ_m| < 0.005, the 1σ Planck 2018 threshold). Substituting a unified UHA-derived Ωm baseline produces no significant Δχ² improvement (Δχ² ≤ 5 per Z0 §1.4) in cross-survey joint analysis.

- **H1-Z3:** Cosmological surveys use Ωm baselines that differ systematically beyond statistical agreement (|ΔΩ_m| ≥ 0.005). Applying a unified UHA-derived Ωm baseline produces Δχ² ≥ 20 improvement (per Z0 §1.4 stage-2 threshold) in cross-survey joint analysis under identical likelihoods and no degree-of-freedom inflation, consistent with the hypothesis that Ωm-baseline disagreement contributes materially to apparent cosmological tensions.

#### Shared decision definitions

Inherited from Z0 §1.1. Track B narrowing:

- **Baseline:** original survey-specific Ωm values as published; ΛCDM with Planck 2018 best-fit parameters as null reference
- **Improvement:** Δχ² = χ²(survey-specific Ωm) − χ²(UHA-unified Ωm) computed on identical joint data with identical pipelines, identical covariance treatment, and identical likelihood code, except for the Ωm baseline substitution. **No added degrees of freedom.**
- **Primary success:** Δχ² ≥ 20 with no degree-of-freedom inflation, AND parameter consistency across surveys improved (cross-probe tensions reduced by ≥ 1σ), AND robust across at least two independent local-calibrator routes (§3.4)
- **Analysis start:** the first execution of Phase 1 (Ωm derivation-chain forensics) after this Z3 DOI is deposited and recorded
- **Same-pipeline rule:** Phase 1–6 pipelines locked at deposit; data versions, release dates, and access dates recorded at analysis start
- **Controls:** original survey-specific Ωm as null; UHA-unified Ωm as alternative; both with full covariance treatment per Z2 A3 audit; κ coupling locked pre-Phase-3 per §3.3

#### Data handling locks

Inherited from Z0 §1.1.

### 1.2 What would render Track B unsupported

Track B will be considered unsupported if any of K0-Z3 through K4-Z3 fire (see §4). If any K fires, Track B halts and a negative or narrow-method result is deposited under the failure-publication rule (Z0 §9, two-stage). This summarises §4's termination-criteria table.

**Phase-local labels KS1–KS4 are deprecated aliases.** All adjudication uses canonical K0-Z3 through K4-Z3. Wherever earlier drafts or discussion used "KS1" → "K1-Z3" (and so on for KS2/KS3/KS4 → K2-Z3/K3-Z3/K4-Z3). KS labels appear in this document only inside parenthetical alias hints, never as primary identifiers.

### 1.3 Public-data-first scope

Per Z0 §1.3. Track B uses publicly available data:
- SH0ES R22 supplementary materials (Riess et al. 2022 ApJ 934 L7)
- Planck 2018 results VI cosmological parameters (ESA Planck Legacy Archive)
- KiDS-1000 cosmology data products
- DES Y3 3x2pt cosmology data products
- DESI DR1 BAO measurements
- Pantheon+ supernova sample (Brout et al. 2022, Scolnic et al. 2022)

Dataset versions, release dates, and access dates recorded at analysis start.

### 1.4 Evidence framework

Per Z0 §1.4 — **canonical hierarchy used throughout this document, no Z3-local thresholds:**

- Δχ² ≤ 5: **null** — not significant
- 5 < Δχ² ≤ 20: **stage-1 signal** — description-changelog log only; insufficient for primary success
- 20 < Δχ² < 49: **stage-2 signal** — meets primary-success threshold subject to controls and no degree-of-freedom inflation; eligible for mint per propagation policy
- Δχ² ≥ 49: **divert to fresh pre-reg** — signature too strong to absorb into this Z3; new preregistration required before any strengthened claim

Legacy thresholds in source protocols (`9/20/50`, venue-routing thresholds) are superseded by this Z0 inheritance block. **Bayes factor narrowing:** Z0 treats BF > 1 as support; Z3 narrows for Track B adjudication — BF ≤ 3 is treated as insufficient support, although the raw BF is reported alongside Δχ² in all phase outputs.

---

## 2. Cross-protocol coordination

This Z3 protocol coordinates with the **UHA Coordinate Framework Experiment** companion (`UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md`), which tests the broader UHA coordinate provenance + uncertainty propagation across surveys.

- **This protocol** is the **narrow** test (one specific mechanism: Ωm derivation chain unification)
- **The Coordinate Framework experiment** is the **broad** test (UHA coordinate provenance + uncertainty propagation across surveys)
- Phase 1–3 deliverables of this protocol (Ωm derivation chains, UHA-derived Ωm baseline, substitution test results) are inputs to the broader Coordinate Framework experiment

**Cross-protocol kill-switch cascade — narrowed (v0.2):**

- If K2-Z3 fires (probe-pair Δχ² < 5; Ωm substitution does not produce stage-1 signal anywhere), **Track B halts**. The Coordinate Framework experiment records the Track B null as a negative input for **Ωm-baseline-mediated effects**, but it does NOT automatically halt non-Ωm coordinate-provenance tests unless those tests explicitly require a non-null Ωm substitution effect.
- If the Coordinate Framework's encoding round-trip integrity gate fails (K4-Z3 mirror), this protocol's Phase 2 (UHA-derived Ωm baseline) cannot proceed because the encoding layer is untrustworthy.

The earlier formulation in v0.1 ("Coordinate Framework's Phase 4–5 cross-survey tests halt" on Track B null) was over-broad and is withdrawn. A null for the Ωm-baseline-mediated mechanism is not a null for coordinate-provenance writ large.

---

## 3. Locked observables and pipelines

### 3.1 Phase 1: Ωm derivation-chain forensics

**Observable:** the Ωm value used by each of: SH0ES R22, Planck 2018, KiDS-1000, DES Y3, DESI DR1, Pantheon+. Each survey's derivation method, source citations, treatment as fixed/varied parameter, and propagated uncertainty.

**Method:** parse each survey's published supplementary materials and primary papers; document the Ωm derivation chain end-to-end; compile cross-survey comparison.

**Decision Gate:** if all surveys use identical Ωm to within ±0.001 → **K0-Z3** (alias: KS1) fires; protocol halts.

**Deliverable:** `omega_m_derivation_forensics_<commit>.md` + `omega_m_survey_comparison_<commit>.csv`

### 3.2 Phase 2: UHA-derived Ωm baseline calculation

**Observable:** unified Ωm value derived from multi-probe analysis using UHA coordinate framework + EB carrier uncertainty propagation.

**Method:**
- Apply UHA coordinate framework to CMB (Planck), BAO (BOSS DR12, DESI DR1), structure (KiDS, DES), SN (Pantheon+) constraints
- Run joint MCMC analysis with EB carrier uncertainty propagation
- Extract Ωm best-fit value with EB carrier uncertainty (e_Ωm, b_Ωm)

**Decision Gate:** if UHA-derived Ωm equals existing survey Ωm within |ΔΩ_m| < 0.005 → **K1-Z3** (alias: KS2) fires; no substitution effect to test.

**Deliverable:** UHA-derived Ωm baseline value with EB carrier uncertainty, in (e, b) carrier-state form per §20 recursive pair law cross-link.

### 3.3 Phase 3: Substitution test

**Observable:** χ² values for each survey's joint analysis using (a) survey-specific Ωm vs (b) UHA-unified Ωm.

**Method:**
- Recalculate each survey's cosmological parameter estimates substituting UHA-unified Ωm
- Compute Δχ² = χ²(original) − χ²(UHA-substituted) for each survey
- Compute joint Δχ² across all surveys

**EB carrier three-outcome primitive (added v0.2):**

| Condition | PP input | EB output | Interpretation |
|---|---:|---:|---|
| Agreement | `(v, v)` | `(0, v)` | no expressed disagreement — shared value |
| Disagreement | `(max, min)` | `(max−min, min)` | expressed disagreement in e-rail; shared floor in b-rail |
| Audit failed | unresolved | `(0, max)` | no expressed comparison; maximum bound retained |

**Pairing rule (Z2 A3 + §21.5 application):**
- For two surveys with disagreeing Ωm values v₁, v₂: PP-pair as `(max(v₁,v₂), min(v₁,v₂))` per the disagreement row above
- Π propagation to EB carrier: `(max−min, min)` — disagreement in e-rail, shared floor in b-rail
- Pre-register the κ coupling between surveys (mechanism-justified-off-diagonals per A3) BEFORE Phase 3 executes — see κ-lock rule below

**κ pre-Phase-3 lock rule (added v0.2):**

> Before Phase 3, κᵢⱼ is computed only from pre-analysis documented shared factors: calibration anchors, common covariance products, common likelihood code, shared external priors, shared catalog releases, or shared astrophysical nuisance models. κᵢⱼ = 0 unless at least one such mechanism is documented at deposit. **No empirical post-result tuning of κ is permitted.** κ values for all survey pairs (i,j) are locked in `kappa_lock_<commit>.md` and cited inline in Phase 3 outputs. Any post-deposit κ change requires fresh pre-registration.

**Decision Gate:** if all probe-pair Δχ² < 5 (Z0 null threshold) → **K2-Z3** (alias: KS3) fires; UHA Ωm is not a tension-reducer at the null/stage-1 boundary. (v0.1 used Δχ² < 9, which is below the Z0 hierarchy floor; superseded.)

**Deliverable:** substitution-test Δχ² table; A3-compliant κ documentation; `kappa_lock_<commit>.md`.

### 3.4 Phase 4: Hubble-tension reanalysis with local-anchor and ladder-route stratification

**Observable:** σ-tension between SH0ES H0 and Planck H0 under (a) original Ωm baselines vs (b) UHA-unified Ωm baseline — **stratified by local distance-anchor calibration AND by full distance-ladder route.**

**Method:**
- Re-derive H0 from SH0ES distance ladder under UHA-unified Ωm
- Re-derive H0 from Planck CMB under UHA-unified Ωm
- Compute σ-tension reduction relative to **the precomputed SH0ES R22 vs Planck 2018 ΛCDM baseline σ-tension using the same covariance convention and likelihood treatment used in this Phase**. ("Original 5σ" was generic and is replaced.)

**Local-anchor stratification (added v0.2 — Freedman-style):**

Because local H₀ inferences may differ by distance-indicator calibration, Phase 4 does not treat "local ladder" as a single object. Where public likelihoods or tabulated constraints permit, Phase 4 reports Ωm-substitution outcomes separately for:

- Cepheid-calibrated local H₀
- TRGB-calibrated local H₀
- JAGB-calibrated local H₀

Track B primary success requires that the Δχ² ≥ 20 improvement **not be solely an artifact of selecting one local-anchor calibration**. If improvement appears only under one anchor class, Z3 reports an **anchor-conditional** result, not a general Hubble-tension result.

**Distance-ladder route stratification (added v0.2 — Madore-style):**

Phase 4 also stratifies by full distance-ladder route, not merely by anchor:

- geometric anchor → Cepheids → SN Ia → Hubble-flow SNe → H₀
- geometric anchor → TRGB → SN Ia → Hubble-flow SNe → H₀
- geometric anchor → JAGB → SN Ia → Hubble-flow SNe → H₀

If Δχ² improvement appears only after collapsing these routes into a single local-H₀ prior, Z3 reports the result as **route-mixing-dependent** and does NOT count it as primary Track B success. If improvement is robust across at least two independent local-calibrator routes, the result is reported as **route-stable**.

**SN-transfer / Pantheon+ control (added v0.2):**

Pantheon+ touches SN standardization, local calibration, cosmographic fitting, and global cosmology. Phase 4 separates the local-calibrator route from the supernova Hubble-flow sample. Ωm-substitution effects must be reported separately for the SN standardization/cosmographic layer and the external cosmology layer. **A result that depends on mixing Cepheid/TRGB/JAGB calibration differences into Pantheon+ is not counted as primary Ωm-baseline support.**

**Pre-registered prediction:** if H1-Z3 holds, tension reduces by ≥ 1σ AND the reduction is route-stable across at least two of {Cepheid, TRGB, JAGB} routes. If H0-Z3 holds, tension is unchanged within 0.1σ.

**Decision Gate:** integrated with §4 K-criteria; route-mixing-dependent outcome is non-primary even if Δχ² ≥ 20 in the collapsed analysis.

### 3.5 Phase 5: Multi-probe joint analysis

**Observable:** joint χ² of all surveys; cross-probe tension matrix.

**Method:** joint MCMC with all surveys using UHA-unified Ωm; compare to original.

**Deliverable:** joint analysis Δχ² and Bayes factor reported under the Z0 §1.4 evidence hierarchy (5 / 20 / 49). **Venue-prestige routing removed (v0.2):** v0.1 §3.5 mapped Δχ² ranges to specific journal tiers (Nature/Science, PRL/Nature Astronomy, MNRAS/PRD); this is removed. Evidence classes are neutral per Z0; venue selection is a post-result editorial decision and is not encoded in this preregistration.

### 3.6 Phase 6: Statistical validation

**Observable:** Bayes factor between models {survey-specific Ωm} and {UHA-unified Ωm}, plus AIC/BIC.

**Method:** Bayesian model comparison with full evidence calculation; AIC + BIC.

**Decision Rule:** Bayes factors are interpreted under the Z0 §1.4 evidence hierarchy with Z3's BF-narrowing (§1.4): BF ≤ 3 is treated as insufficient support for Track B adjudication; raw BF is reported. (The 150/20/3 verbal scale from v0.1 is descriptive, not adjudicative; adjudication uses the Δχ² hierarchy + BF>3 narrowing.)

---

## 4. Termination criteria (canonical K0-Z3 … K4-Z3)

KS aliases are deprecated and shown only for cross-reference with v0.1.

| K | Alias (deprecated) | Trigger | Action |
|---|---|---|---|
| K0-Z3 | KS1 | All surveys' Ωm values identical within ±0.001 | Phase 1 halt; null deposited |
| K1-Z3 | KS2 | UHA-derived Ωm equals survey Ωm within `|ΔΩ_m| < 0.005` | Phase 2 halt; null deposited |
| K2-Z3 | KS3 | All probe-pair Δχ² < 5 (Z0 null threshold; v0.1 used <9, superseded) | Phase 3 halt; null deposited |
| K3-Z3 | (KS4) | Survey-specific and UHA-unified Ωm produce statistically indistinguishable joint χ² (Δχ² < 5, BF ≤ 3) | Hypothesis unsupported; null deposited |
| K4-Z3 | — | UHA Coordinate Framework encoding integrity fails | Phase 2 cannot proceed; halt; investigate companion protocol |

If any K fires, two-stage failure-publication per Z0 §9 within 14 days. **A K-firing is a successful preregistered outcome — the test ran and falsified its mechanism cleanly.** A clean null is publishable per §6.

---

## 5. Acknowledged competing hypotheses (Z* cross-reference)

This Z3 deposits the **Ωm-baseline-unification hypothesis as one candidate explanation** for cross-survey cosmological tensions. Other candidate explanations include:

- **Z\* cosmopoulous model:** Hubble tension is horizon-growth structure (universe-inside-black-hole model), not Ωm-baseline disagreement. Pre-registered separately at `Z-star_cosmopoulous_preregistration_v0_1_DRAFT.md`.
- **Distance-ladder calibration / systematics:** local-anchor or ladder-route choice may dominate the residual; Z3's Phase 4 stratification (§3.4) is designed to detect this case explicitly.
- **Early dark energy:** new-physics solution at recombination epoch
- **Modified gravity:** infrared modifications to GR
- **Local-volume effects:** under-dense local region creating biased local H0

A Z3 K0/K1/K2/K3 firing (Ωm-unification null) is **consistent with all of these alternatives**. Z3 does not claim to falsify them; Z3 tests one specific mechanism. Z3 specifically does not adjudicate between Ωm-baseline disagreement and ladder-systematics-dominated explanations for the residual; its Phase 4 stratification makes the difference visible but does not assign it.

---

## 6. Failure-publication template (Z0 §9 inheritance)

If any K fires:

- **Venue:** MNRAS technical note (or Zenodo standalone for purely methodological null). Venue selection is post-result; this preregistration does not lock a specific journal tier.
- **Title format:** `Pre-registration outcome: Ωm baseline unification does not account for [residual quantity] in [data scope]`
- **Length:** ~3000 words target
- **Required content:** methodology recap (cite this Z3 commit hash and DOI), kill-switch trigger (cite K-id with KS alias for cross-reference), data and code (sha256-locked), conclusion with explicit "this hypothesis is not supported" language; if Phase 4 reached, anchor/route stratification table reported even when null
- **Deposit timeline:** within 14 days of kill-switch firing. No extensions.

A failure deposit is not a fallback. It is the co-equal outcome of a falsifiable preregistration and signals scientific seriousness.

---

## 7. What this pre-registration locks

- Hypotheses H0-Z3, H1-Z3 with Z0 §1.4 Δχ² hierarchy (5 / 20 / 49)
- BF > 3 narrowing for Track B adjudication
- Six observables (§3.1–3.6) with locked methods and decision gates
- Five canonical termination criteria K0-Z3 … K4-Z3 (§4); KS aliases deprecated
- Public-data-first scope
- Pairing rule (§21.5 application; A3 invocation); EB three-outcome primitive
- κ pre-Phase-3 lock procedure (§3.3)
- Phase 4 local-anchor and ladder-route stratification + Pantheon+ SN-transfer separation
- Cross-protocol coordination with UHA Coordinate Framework — narrowed cascade
- Failure-publication template
- Title preserves "unification" for indexing; decision rules use "common-baseline audit" / "baseline substitution"
- Explicit non-challenge of SH0ES distance-ladder calibration

After this DOI is deposited, hypothesis-adjudicating analysis begins. Modifications require new pre-reg.

---

## 8. Provenance and dependencies

Z3 draws on:
- **Source protocol:** `Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md` (commit `77b639c`; patent gates removed 2026-05-01)
- **Companion protocol:** `UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md`
- **Z0 umbrella:** DOI `10.5281/zenodo.19881689` (deposited 2026-04-29)
- **Z2 audit framework:** DOI `10.5281/zenodo.19908184` (deposited 2026-04-29) — A3 mechanism-justified-off-diagonals
- **EB carrier theorem:** RSOS-260797 r4 (under review)
- **Recursive pair law (optional cross-link):** `carrier_state_rail_theory_v0_2.md` §20 (postulate-level)
- **Pipeline-stacking + greater-gets-e pairing rule:** `carrier_state_rail_theory_v0_2.md` §21.5
- **v0.2 consult inputs (filed in z-track):**
  - `Z3_consistency_review_outline_and_chat_log_2026-05-04.md` — patch list and reviewer-style critiques
  - `Z3_freedman_pressure_test_outline_2026-05-04.md` — outreach strategy and armor-sentence framing

---

## 9. Pre-deposit checklist

Before GATE:OPEN for deposit:

- [ ] Marketing-language audit (grep for "revolutionary", "Nobel", "100% explained", "completely solves", "definitively", "groundbreaking", "paradigm shift", "Einstein-level", "textbook-level", "resolution", "solves the Hubble tension"; any match fails)
- [ ] Confirm RSOS-260797 r4 current submission status
- [ ] Confirm MN-26-1108-L peer-review status (past first round?)
- [ ] Confirm MN-26-1117-P peer-review status (past first round?)
- [ ] Confirm Z0 DOI canonical
- [ ] Confirm κ values pre-registered in `kappa_lock_<commit>.md` for surveys with shared calibration anchors (A3 application)
- [ ] Hard-print the Z3 v0.2 draft
- [ ] 30-min cool-off (per `feedback_zenodo_publish_gate.md`)
- [ ] Eric reads printed copy and confirms (per `feedback_zenodo_publish_gate.md`)
- [ ] GATE:OPEN cycle: 9 steps per Z2's example
- [ ] Bootstrap commit + filename hash injection
- [ ] Mint Zenodo DOI (cited as child of Z0 concept)
- [ ] Cross-link DOI commit
- [ ] Pre-canonical timestamped predecessor archived

---

## 10. Status

**Pre-canonical, draft v0.2.** NOT deposited. v0.1 preserved alongside.

Outstanding before deposit:
- Status checks (RSOS-260797, MN-26-1108-L, MN-26-1117-P)
- Marketing-language audit
- κ lock document
- Hard print + Eric-read + cool-off + GATE:OPEN
- Bootstrap commit + filename hash

This v0.2 inherits Z0 + Z2, normalizes Δχ² to Z0's 5/20/49 hierarchy, deprecates KS labels in favor of K0-Z3…K4-Z3, removes venue-prestige routing, locks κ pre-Phase-3, narrows the cross-protocol cascade, adds Phase 4 anchor/route/SN-transfer stratification, integrates §21.5 pipeline-stacking + A3 audit invocation, acknowledges Z* and ladder-systematics as competing hypotheses, surfaces clean-null = valid outcome, and explicitly refuses framing as a SH0ES challenge.

---

## 11. Changelog (v0.1 → v0.2, 2026-05-04)

Patches applied from `Z3_consistency_review_outline_and_chat_log_2026-05-04.md` action list. Ordered by consult section.

**Must-fix (consult §10 must-fix block):**

1. Δχ² thresholds normalized to Z0 §1.4 hierarchy (5 / 20 / 49) throughout. Removed v0.1's Δχ² < 9 in K2 trigger, mixed thresholds in §3.3 and §3.5. Now: §1.4 cites Z0; §3.3 uses Δχ² < 5 for K2; §3.6 uses BF > 3 narrowing.
2. K vs KS naming normalized to canonical K0-Z3 … K4-Z3. KS1–KS4 are deprecated phase-local aliases shown only for cross-reference. §3.1–3.4 decision gates updated; §4 table adds alias column.
3. Venue-prestige routing removed from §3.5. v0.1's "Δχ² ≥ 50 → Nature/Science candidate; Δχ² 20–50 → PRL/Nature Astronomy; …" deleted. §6 venue note clarified as post-result editorial.
4. κ pre-Phase-3 lock procedure inserted in §3.3. Locks κᵢⱼ to documented shared mechanisms; forbids post-result tuning.
5. Cross-protocol cascade narrowed in §2. v0.1's "Coordinate Framework's Phase 4–5 cross-survey tests halt" replaced with explicit Track-B-only halt; non-Ωm coordinate-provenance tests not affected unless they require non-null Ωm substitution.

**Should-fix (consult §10 should-fix block):**

6. EB three-outcome primitive table added to §3.3 (agreement / disagreement / audit-failed rows).
7. Local-anchor stratification (Cepheid/TRGB/JAGB) added to §3.4 (Freedman-style).
8. Distance-ladder route stratification added to §3.4 (Madore-style); route-mixing-dependent results disqualified from primary success.
9. SN-transfer / Pantheon+ control added to §3.4; mixing of calibration differences into Pantheon+ disqualified.
10. Bayes-factor narrowing relative to Z0 stated in §1.4 and §3.6 (Z0: BF>1 support; Z3 narrows: BF≤3 insufficient for Track B adjudication; raw BF reported).
11. SH0ES/Planck baseline language tightened in §3.4: "relative to original 5σ" → "relative to the precomputed SH0ES R22 vs Planck 2018 ΛCDM baseline σ-tension using the same covariance convention and likelihood treatment used in this Phase."
12. "Deposit-ready metadata block" → "Deposit-format metadata block" until threshold/κ/naming gates close.

**Style / rhetoric (consult §10 style block):**

13. "Common-baseline audit" / "baseline substitution" used in decision rules; title preserves "Unification" for indexing continuity.
14. "Solves," "explains," "resolution" language not used in decision rules; pre-deposit checklist updated to grep-fail on these.
15. Explicit statement: "Z3 does not directly challenge the SH0ES distance-ladder calibration." (§1)
16. Explicit statement: "A clean null result is a valid publishable outcome." (§1, §4, §6)

**Not applied (out of scope for v0.2):**

- Reviewer-simulation language ("Freedman would say…", "Riess would say…") is treated as adversarial framing input, not as endorsement signal. v0.2 incorporates the *substance* of those critiques (anchor stratification, Pantheon+ control, no-direct-SH0ES-challenge) but does not cite them as authority. The simulated reviewer reactions remain in `Z3_consistency_review_outline_and_chat_log_2026-05-04.md` as reference material; they are not promoted into Z3's body.
- Z3 SMT-solver documentation analysis from a separate AI session: name collision (Microsoft Research Z3 vs Zenodo Z3). Not relevant to this preregistration; not cited.

---

*End of Z3 draft v0.2. Held for read-before-deposit cycle. Hard-print + Eric read + cool-off + GATE:OPEN required before mint.*
