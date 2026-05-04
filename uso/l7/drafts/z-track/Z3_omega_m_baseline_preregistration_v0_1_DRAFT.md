# Z3 — Track B Pre-Registration: Ωm Baseline Unification

**Status:** DRAFT v0.1 — pre-canonical, NOT deposited. Working draft for review and refinement before GATE:OPEN cycle. Drafted 2026-05-01 from `Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md` + Z-track template + gap-survey delta list.

**Working draft note:** This Z3 is a child of the Z0 umbrella pre-registration deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19881689` (concept DOI `10.5281/zenodo.19881688`). It deposits **Track B** of the three-track UHA + EB carrier program: cross-survey Ωm baseline unification test. It inherits Z0's hypothesis-lock structure, evidence-class thresholds, kill-switch interpretation preamble, two-stage failure-publication commitment, and deposit chain. It adds Track B specifics: H0/H1 hypotheses on Ωm-baseline disagreement vs unified UHA-derived Ωm, locked public-data source classes, the Phase 0–6 phase chain, and the K0–K4 termination criteria with cross-protocol propagation.

| Self-reference field | Value |
|---|---|
| Version | v0.1 timestamped `2026-05-01T13:09:00Z` |
| Parent (umbrella) | Z0 v1.2-hybrid at hubble-tensor commit `d842691`; deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` |
| Parent (Z2 audit framework) | Z2 deposited 2026-04-29 at DOI `10.5281/zenodo.19908184`; concept `10.5281/zenodo.19908183` |
| Source protocol | `Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md` (commit 77b639c); patent gates removed 2026-05-01 |
| Working filename | `Z3_omega_m_baseline_preregistration_v0_1_DRAFT.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |
| Pending bookkeeping | Pre-canonical until committed and renamed with bootstrap commit hash. |

**Standing artifact-hash-naming policy (inherited from Z0):** Every artifact carries its commit hash inside AND in filename. No hash, no canonical status. No exceptions.

---

## Zenodo metadata block (deposit-ready)

| Field | Value |
|---|---|
| Title | Z3 Pre-Registration: Cross-Survey Ωm Baseline Unification Test |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint |
| Communities | (TBD — Zenodo community selection at deposit time) |
| Keywords | cosmology, Hubble tension, Ωm, dark matter density, cross-survey systematics, EB carrier, UHA, pre-registration |
| Related identifiers (is part of) | `10.5281/zenodo.19881689` (Z0 umbrella v1.2-hybrid) |
| Related identifiers (cites) | `10.5281/zenodo.19908184` (Z2 audit framework); `10.5281/zenodo.19676237` (priority hash); RSOS-260797 r4 (EB carrier characterization theorem, under review); US 63/902,536 (UHA provisional patent) |

---

## 1. Purpose

This deposit pre-registers Track B of the three-track UHA + EB carrier program: the **cross-survey Ωm baseline unification test**. Track B asks whether different cosmological surveys use different Ωm derivation chains and baselines, whether those differences create systematic effects appearing as cosmological tensions, and whether applying a unified UHA-derived Ωm baseline reduces those tensions across surveys.

Track B does NOT test "GPS positioning errors" (factually incorrect framing previously rejected). It tests **whether Ωm baseline inconsistencies across surveys create apparent cosmological tensions, and whether unified UHA-derived Ωm baseline reduces them.**

Track B does NOT claim Ωm-baseline unification is THE explanation for the Hubble tension. It locks a specific test of one candidate mechanism. Other candidate mechanisms (early dark energy, modified gravity, the cosmopoulous horizon-growth model registered separately as Z*, etc.) remain open hypotheses for the same observation. An Ωm-unification null result (KS3 fires) is consistent with multiple alternative explanations.

This pre-registration does not claim that Ωm inconsistencies are the unique source of Hubble tension. Per Z0 §5 non-claims, Track B tests one specific mechanism with pre-registered observables, kill switches, and decision rules.

### 1.1 Pre-registered hypotheses and decision locks (Track B)

Inherited from Z0 §1.1 unless narrowed below.

#### Hypotheses (Track B)

- **H0-Z3:** Cosmological surveys (SH0ES R22, Planck 2018, KiDS-1000, DES Y3, DESI DR1, Pantheon+) use Ωm baselines that agree within statistical uncertainty (|ΔΩ_m| < 0.005, the 1σ Planck 2018 threshold). Unifying Ωm baselines via UHA-derived value produces no significant Δχ² improvement (Δχ² ≤ 5) in cross-survey joint analysis.

- **H1-Z3:** Cosmological surveys use Ωm baselines that differ systematically beyond statistical agreement (|ΔΩ_m| ≥ 0.005). Applying a unified UHA-derived Ωm baseline produces Δχ² ≥ 20 improvement in cross-survey joint analysis, consistent with the hypothesis that Ωm-baseline disagreement contributes materially to apparent cosmological tensions.

#### Shared decision definitions

Inherited from Z0 §1.1. Track B narrowing:

- **Baseline:** original survey-specific Ωm values as published; ΛCDM with Planck 2018 best-fit parameters as null reference
- **Improvement:** Δχ² = χ²(survey-specific Ωm) − χ²(UHA-unified Ωm) computed on identical joint data with identical pipelines except for the Ωm baseline substitution
- **Primary success:** Δχ² ≥ 20 with no degree-of-freedom inflation, AND parameter consistency across surveys improved (cross-probe tensions reduced by ≥ 1σ)
- **Analysis start:** the first execution of Phase 1 (Ωm derivation-chain forensics) after this Z3 DOI is deposited and recorded
- **Same-pipeline rule:** Phase 1–6 pipelines locked at deposit; data versions, release dates, and access dates recorded at analysis start
- **Controls:** original survey-specific Ωm as null; UHA-unified Ωm as alternative; both with full covariance treatment per Z2 A3 audit

#### Data handling locks

Inherited from Z0 §1.1.

### 1.2 What would render Track B unsupported

Track B will be considered unsupported if any of the following occur:

- **K0-Z3:** All surveys use identical Ωm value to within ±0.001 (sub-Planck-1σ). Hypothesis falsified at Phase 1; no substitution test possible.
- **K1-Z3:** UHA-derived Ωm equals existing survey Ωm within statistical uncertainty (|ΔΩ_m| < 0.005). No substitution effect to test.
- **K2-Z3:** Substitution test produces Δχ² < 9 across all probe pairs. No significant improvement; UHA Ωm is not a tension-reducer.
- **K3-Z3:** Survey-specific Ωm and UHA-unified Ωm both pass joint analysis at comparable χ²; the difference is statistically indistinguishable.
- **K4-Z3:** Cross-protocol coordination failure (UHA Coordinate Framework Experiment Phase encoding-round-trip integrity gate fails). Phase 2 cannot proceed because the encoding layer is untrustworthy.

If any of K0–K4 fire, Track B halts and a negative or narrow-method result is deposited under the failure-publication rule (Z0 §9, two-stage). This summarises §7's termination-criteria tables.

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

Per Z0 §1.4. Δχ² thresholds:
- Δχ² ≤ 5: not significant
- 5 < Δχ² ≤ 20: stage-1 signal (description-changelog log)
- 20 < Δχ² < 49: stage-2 signal (potential mint per propagation policy)
- Δχ² ≥ 49: divert to fresh pre-reg (signature too strong to absorb)

---

## 2. Cross-protocol coordination

This Z3 protocol coordinates with the **UHA Coordinate Framework Experiment** companion (`UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md`), which tests the broader UHA coordinate provenance + uncertainty propagation across surveys.

- **This protocol** is the **narrow** test (one specific mechanism: Ωm derivation chain unification)
- **The Coordinate Framework experiment** is the **broad** test (UHA coordinate provenance + uncertainty propagation across surveys)
- Phase 1–3 deliverables of this protocol (Ωm derivation chains, UHA-derived Ωm baseline, substitution test results) are inputs to the broader Coordinate Framework experiment
- Cross-protocol kill-switch cascade:
  - If KS3 of Track B fires (Ωm values agree within uncertainty), the Coordinate Framework's Phase 4–5 cross-survey tests halt because the narrow null implies the broad mechanism is unlikely to produce detectable effects
  - If the Coordinate Framework's encoding round-trip integrity gate fails, this protocol's Phase 2 (UHA-derived Ωm baseline) cannot proceed because the encoding layer is untrustworthy

---

## 3. Locked observables and pipelines

### 3.1 Phase 1: Ωm derivation-chain forensics

**Observable:** the Ωm value used by each of: SH0ES R22, Planck 2018, KiDS-1000, DES Y3, DESI DR1, Pantheon+. Each survey's derivation method, source citations, treatment as fixed/varied parameter, and propagated uncertainty.

**Method:** parse each survey's published supplementary materials and primary papers; document the Ωm derivation chain end-to-end; compile cross-survey comparison.

**Decision Gate (KS1):** if all surveys use identical Ωm to within ±0.001 → KS1 fires; protocol halts.

**Deliverable:** `omega_m_derivation_forensics_<commit>.md` + `omega_m_survey_comparison_<commit>.csv`

### 3.2 Phase 2: UHA-derived Ωm baseline calculation

**Observable:** unified Ωm value derived from multi-probe analysis using UHA coordinate framework + EB carrier uncertainty propagation.

**Method:**
- Apply UHA coordinate framework to CMB (Planck), BAO (BOSS DR12, DESI DR1), structure (KiDS, DES), SN (Pantheon+) constraints
- Run joint MCMC analysis with EB carrier uncertainty propagation
- Extract Ωm best-fit value with EB carrier uncertainty (e_Ωm, b_Ωm)

**Decision Gate (KS2):** if UHA-derived Ωm equals existing survey Ωm within |ΔΩ_m| < 0.005 → KS2 fires; no substitution effect to test.

**Deliverable:** UHA-derived Ωm baseline value with EB carrier uncertainty, in (e, b) carrier-state form per §20 recursive pair law cross-link.

### 3.3 Phase 3: Substitution test

**Observable:** χ² values for each survey's joint analysis using (a) survey-specific Ωm vs (b) UHA-unified Ωm.

**Method:**
- Recalculate each survey's cosmological parameter estimates substituting UHA-unified Ωm
- Compute Δχ² = χ²(original) − χ²(UHA-substituted) for each survey
- Compute joint Δχ² across all surveys

**Pairing rule (Z2 A3 + §21.5 application):**
- For two surveys with disagreeing Ωm values v₁, v₂: PP-pair as (max(v₁,v₂), min(v₁,v₂))
- Π propagation to EB carrier: (max−min, min) — disagreement in e-rail, shared floor in b-rail
- Pre-register the κ coupling between surveys (mechanism-justified-off-diagonals per A3) BEFORE Phase 3 executes

**Decision Gate (KS3):** if all probe-pair Δχ² < 9 → KS3 fires; UHA Ωm is not a tension-reducer.

**Deliverable:** substitution-test Δχ² table; A3-compliant κ documentation.

### 3.4 Phase 4: Hubble tension reanalysis

**Observable:** σ-tension between SH0ES H0 and Planck H0 under (a) original Ωm baselines vs (b) UHA-unified Ωm baseline.

**Method:**
- Re-derive H0 from SH0ES distance ladder under UHA-unified Ωm
- Re-derive H0 from Planck CMB under UHA-unified Ωm
- Compute σ-tension reduction relative to original 5σ

**Pre-registered prediction:** if H1-Z3 holds, tension reduces by ≥ 1σ. If H0-Z3 holds, tension is unchanged within 0.1σ.

**Decision Gate (KS4 partial):** integrated with KS3.

### 3.5 Phase 5: Multi-probe joint analysis

**Observable:** joint χ² of all surveys; cross-probe tension matrix.

**Method:** joint MCMC with all surveys using UHA-unified Ωm; compare to original.

**Deliverable:** joint analysis Δχ² with publication-venue routing per §0.5 of source protocol (Δχ² ≥ 50 → Nature/Science candidate; Δχ² 20–50 → PRL/Nature Astronomy; Δχ² 9–20 → MNRAS/PRD; Δχ² < 9 → technical note / negative deposit).

### 3.6 Phase 6: Statistical validation

**Observable:** Bayes factor between models {survey-specific Ωm} and {UHA-unified Ωm}.

**Method:** Bayesian model comparison with full evidence calculation; AIC + BIC.

**Decision Rule:** Bayes factor > 150 → very strong evidence; > 20 → strong; > 3 → moderate; ≤ 3 → null.

---

## 4. Termination criteria (K0–K4)

| K | Trigger | Action |
|---|---|---|
| K0-Z3 | All surveys' Ωm values identical within ±0.001 | Phase 1 halt; null deposited |
| K1-Z3 | UHA-derived Ωm equals survey Ωm within |ΔΩ_m| < 0.005 | Phase 2 halt; null deposited |
| K2-Z3 | All probe-pair Δχ² < 9 | Phase 3 halt; null deposited |
| K3-Z3 | Survey-specific and UHA-unified Ωm produce statistically indistinguishable joint χ² | Hypothesis unsupported; null deposited |
| K4-Z3 | UHA Coordinate Framework encoding integrity fails | Phase 2 cannot proceed; halt; investigate companion protocol |

If any K fires, two-stage failure-publication per Z0 §9 within 14 days.

---

## 5. Acknowledged competing hypotheses (Z* cross-reference)

This Z3 deposits the **Ωm-baseline-unification hypothesis as one candidate explanation** for cross-survey cosmological tensions. Other candidate explanations include:

- **Z\* cosmopoulous model:** Hubble tension is horizon-growth structure (universe-inside-black-hole model), not Ωm-baseline disagreement. Pre-registered separately at `Z-star_cosmopoulous_preregistration_v0_1_DRAFT.md`.
- **Early dark energy:** new-physics solution at recombination epoch
- **Modified gravity:** infrared modifications to GR
- **Local-volume effects:** under-dense local region creating biased local H0

A Z3 K0/K1/K2/K3 firing (Ωm-unification null) is **consistent with all of these alternatives**. Z3 does not claim to falsify them; Z3 tests one specific mechanism.

---

## 6. Failure-publication template (Z0 §9 inheritance)

If any K fires:

- **Venue:** MNRAS technical note (or Zenodo standalone for purely methodological null)
- **Title format:** `Pre-registration outcome: Ωm baseline unification does not account for [residual quantity] in [data scope]`
- **Length:** ~3000 words target
- **Required content:** methodology recap (cite this Z3 commit hash and DOI), kill-switch trigger, data and code (sha256-locked), conclusion with explicit "this hypothesis is not supported" language
- **Deposit timeline:** within 14 days of kill-switch firing. No extensions.

---

## 7. What this pre-registration locks

- Hypotheses H0-Z3, H1-Z3 with Δχ² thresholds
- Six observables (§3.1–3.6) with locked methods and decision gates
- Five termination criteria (§4)
- Public-data-first scope
- Pairing rule (§21.5 application; A3 invocation)
- Cross-protocol coordination with UHA Coordinate Framework
- Failure-publication template

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

---

## 9. Pre-deposit checklist

Before GATE:OPEN:

- [ ] Marketing-language audit (grep for "revolutionary", "Nobel", "100% explained", "completely solves", "definitively", "groundbreaking", "paradigm shift", "Einstein-level", "textbook-level"; any match fails)
- [ ] Confirm RSOS-260797 r4 current submission status
- [ ] Confirm MN-26-1108-L peer-review status (past first round?)
- [ ] Confirm MN-26-1117-P peer-review status (past first round?)
- [ ] Confirm Z0 DOI canonical
- [ ] Confirm κ values pre-registered (pipeline-stacking A3 application) for surveys with shared calibration anchors
- [ ] Hard-print the Z3 draft
- [ ] 30-min cool-off (per `feedback_zenodo_publish_gate.md`)
- [ ] GATE:OPEN cycle: 9 steps per Z2's example
- [ ] Bootstrap commit + filename hash injection
- [ ] Mint Zenodo DOI (cited as child of Z0 concept)
- [ ] Cross-link DOI commit
- [ ] Pre-canonical timestamped predecessor archived

---

## 10. Status

**Pre-canonical, draft v0.1.** NOT deposited. Requires:
- Status checks (RSOS-260797, MN-26-1108-L, MN-26-1117-P)
- Marketing-language audit
- Hard print + cool-off + GATE:OPEN
- Bootstrap commit + filename hash

This draft inherits Z0 + Z2, removes patent gates, integrates §21.5 pipeline-stacking + A3 audit invocation, acknowledges Z* as competing-hypothesis context, and locks Phase 1–6 with K0–K4 termination criteria.

---

*End of Z3 draft v0.1. Held for review and gap-survey integration verification.*
