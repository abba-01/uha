# Z3 Pre-Registration — Gap Survey of Ωm Baseline Protocol v1.0

**Date:** 2026-05-01, 06:08 PDT
**Surveyed:** `/scratch/repos/hubble-tensor/research/Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md` + companion `UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md` + `HUBBLE_RESIDUAL_3PCT_EXPERIMENT_DESIGN_2026-04-28.md`
**Purpose:** Identify gaps between v1.0 protocol and current state before drafting Z3 preregistration. Output: delta-list for inclusion in Z3.

---

## Patent gates — REMOVED 2026-05-01 per Eric directive

Three files cleaned:
- `Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md` §0.3 — replaced with [REMOVED] note
- `UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md` §0.3 — replaced with [REMOVED] note
- `HUBBLE_RESIDUAL_3PCT_EXPERIMENT_DESIGN_2026-04-28.md` (superseded file) — patent gates struck through, timeline rows removed

No patent-counsel gate applies to Z3 deposit.

---

## Required Z3 additions (beyond v1.0 protocol)

### 1. Competing-hypothesis context (NEW)

**Issue:** Protocol asserts "different Ωm derivation chains create cosmological tensions; unifying baselines reduces them." But Z* cosmopoulous reframe (sister preregistration) hypothesizes the Hubble tension is horizon-growth structure, NOT Ωm-baseline disagreement.

**These are competing hypotheses for the same observation.**

**Z3 must:**
- Acknowledge that an Ωm-unification null result (KS3 fires) is consistent with multiple alternatives (cosmopoulous model among them)
- Avoid pre-emptively claiming Ωm-baseline disagreement is THE explanation
- Reference Z* as a parallel-track alternative hypothesis

### 2. Z0 umbrella inheritance (NEW — required by Z-track template)

**Issue:** Protocol v1.0 predates Z0 deposit (2026-04-29). Z3 must inherit from Z0.

**Z3 must:**
- Cite Z0 DOI `10.5281/zenodo.19881689` (concept `10.5281/zenodo.19881688`)
- Inherit Z0 §1.1 hypothesis-lock structure
- Inherit Z0 §1.4 evidence framework (Δχ² thresholds 5/20/49)
- Inherit Z0 §9 two-stage failure-publication rule
- Inherit Z0 §1.3 public-data-first scope

### 3. Recursive pair law cross-link (OPTIONAL)

**Issue:** Protocol uses EB carrier in classical (ℝ × ℝ≥0) form. §20 of `carrier_state_rail_theory_v0_2.md` formalizes the recursive pair law extension.

**Z3 may:**
- Cite §20 as the structural framework underlying EB-carrier uncertainty propagation
- Apply recursive pair law to Ωm-as-domain: R_Ωm(Ωm) = (e_Ωm, b_Ωm)

Optional, not required.

### 4. Pipeline stacking + greater-gets-e pairing rule (NEW — DIRECT APPLICATION)

**Issue:** Phase 3 substitution test combines cross-survey Ωm values. §21.5 of v0.2 formalized the carrier-native pipeline-stacking operation:
- Disagreement-pairing rule: PP-pair as (max, min); Π propagates to (max−min, min) in EB
- Three structurally distinct outcomes: agreement (0, v), disagreement (max−min, min), audit-failed (0, max)

**Z3 must:**
- Use the formal pairing-rule for Phase 3 substitution test instead of generic averaging
- Document the three-outcome structure as the audit framework's primitive operations
- Cross-reference Z2 audit framework (already deposited, DOI `10.5281/zenodo.19908184`)

### 5. A3 mechanism-justified-off-diagonals (NEW)

**Issue:** Phase 3 substitution test implicitly assumes pipelines may share factors (calibration anchors, e.g., TRGB tip, Cepheid LMC). Per Z2 audit framework, A3 demands these shared factors be explicit.

**Z3 must:**
- Explicitly invoke A3: cross-pipeline Ωm coupling κ must be mechanism-justified
- Identify shared factors between SH0ES, Planck, KiDS, DES, DESI, Pantheon+
- Pre-register the κ values (or pre-register the procedure for computing them) before Phase 3 begins

### 6. Marketing-language audit (REQUIRED PRE-DEPOSIT)

Apply §0.5 audit to Z3 draft before deposit:
- grep for: "revolutionary", "Nobel", "100% explained", "completely solves", "definitively", "groundbreaking", "paradigm shift", "Einstein-level", "textbook-level"
- Any match fails; replace with bounded language

---

## Status checks needed before Z3 deposit

| Item | Status | Action |
|---|---|---|
| RSOS-260797 r4 (EB carrier characterization) | "Under review" per protocol — current status uncertain | Verify current submission state |
| MN-26-1108-L peer review | Need confirmation | Verify past first round |
| MN-26-1117-P peer review | Need confirmation | Verify past first round |
| Z0 umbrella DOI | `10.5281/zenodo.19881689` (canonical, deposited 2026-04-29) | Confirm in Z3 inheritance block |
| Companion UHA Coordinate Framework Experiment | Patent gate removed (✓) | No further updates needed for now |

---

## What's clean (no updates required)

- §0.4 Failure-publication template (current; aligned with venues)
- §0.5 Citation discipline (DOIs current; threshold |ΔΩ_m| < 0.005 grounded in Planck 2018)
- §0.6 Commit + deposit naming convention (consistent with Z-track)
- Phase 0–6 definitions structurally sound
- Kill switch thresholds (KS1–KS4) well-defined
- Cross-protocol coordination locked with UHA Coordinate Framework

---

## Pseudocode-to-implementation gap

Phase 1: `extract_riess_omega_m_baseline()`, `extract_kids_omega_m_baseline()`, `extract_des_omega_m_baseline()`, `extract_pantheon_omega_m_baseline()` — placeholders

Phase 2: `UHAJointLikelihood`, `UHAMCMCSampler`, `EBCarrierPair`, `eb_carrier_combination()` — referenced but not implemented

**This is Phase 1 prep work (option D), not a Z3 prereg blocker.** Z3 locks methodology; D implements code.

---

## Delta-list for Z3 draft (to be incorporated)

**ADD to Z3:**
1. Competing-hypothesis acknowledgment (Z* alternative)
2. Z0 inheritance block (§1.1 reference)
3. §20 recursive pair law citation (optional)
4. §21.5 pipeline-stacking + greater-gets-e pairing rule for Phase 3
5. A3 mechanism-justified-off-diagonals invocation

**APPLY pre-deposit:**
6. Marketing-language audit (grep for hype words)
7. Print + 30-min cool-off + GATE:OPEN per `feedback_zenodo_publish_gate.md`

**ALREADY DONE:**
- Patent gates removed from all three files

**STATUS-CHECK before deposit:**
- RSOS-260797 status, MN-26-1108-L status, MN-26-1117-P status

---

## Conclusion

Protocol v1.0 is **structurally sound**. Gaps are **integrative additions** from work since v1.0 (Z0 umbrella, Z2 audit framework, recursive pair law, Z* cosmopoulous reframe), not corrections.

Z3 can be drafted now incorporating items 1–5 above. Marketing-language audit and status checks happen in the GATE:OPEN cycle pre-deposit.

**Next action: A (draft Z3 preregistration).**

---

*End of gap survey. Hash to be added on commit.*
