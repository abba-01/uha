# Z0 — Umbrella Pre-Registration: UHA Space-Frame, Coordinate Provenance, and Ωm Baseline Research Program

**Status:** DRAFT v1.2-hybrid — not deposited. Hybrid of v1.1-clean substantive additions and restored rule citation; for hard-print + 30-min cool + GATE:OPEN per `feedback_zenodo_publish_gate.md` and `feedback_submission_print_gate.md`.

**Timestamped hybrid note:** This v1.2-hybrid keeps every substantive addition the v1.1-clean cleanup made (hypothesis locks, decision definitions, data-handling rules, formula-level models, evidence framework sharpening). It restores the `feedback_others_contradict_not_prove.md` rule citation and the contradiction-and-audit framing that v1.1-clean dropped from §2 and §14. Voice markers tied to credentialing or external counsel (J.D. status; patent-counsel specificity in KS7 and §9.1) remain stripped per author decision (2026-04-29). The cleanup pass was performed by an external AI; restoration of the rule citation is required because dropping it silently breaches the rule itself.

| Self-reference field | Value |
|---|---|
| Version | v1.2-hybrid timestamped `2026-04-29T00-54-00-0700` |
| Commit hash (hubble-tensor) | `77b639c` — bootstrap commit (policy block + v1.1 self-reference fields). Subsequent rename commit is bookkeeping only. |
| Base content sha256 | `1378c20b80d292426e5bdb1e1fe8b9e48a8f141ebc9c97b15e74a031a52253a8` (source file content at `77b639c`; verifiable via `git show 77b639c:preregistrations/Z0_umbrella_preregistration_v1.0.md | sha256sum`) |
| Timestamped hybrid note | This working draft is not canonical until committed and renamed with the resulting commit hash under the artifact-hash-naming policy. |
| Working filename | `Z0_umbrella_preregistration_v1.2_hybrid_timestamped_2026-04-29T00-54-00-0700.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |

**Standing artifact-hash-naming policy (locked, propagating):** Every artifact in this research program carries its commit hash both inside the document AND in the filename. No hash, no canonical status. No exceptions. This document follows the policy and propagates it: every artifact derived from, citing, or extending this Z0 inherits the same rule. The policy travels with the artifacts that follow it — exit-document discipline includes the policy itself, not merely the act of compliance. Per `feedback_artifact_hash_naming.md`.

---

## Zenodo metadata block (deposit-ready)

| Field | Value |
|---|---|
| Title | Umbrella Pre-Registration: UHA Space-Frame, Coordinate Provenance, and Ωm Baseline Research Program |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint (Zenodo native vocabulary; subtitle: "Pre-registration umbrella for three-track UHA + EB carrier research program") |
| Communities | (TBD — Zenodo community selection at deposit time) |
| Keywords | UHA, Universal Horizon Address, EB carrier, coordinate provenance, Ωm baseline unification, Hubble tension, cosmological tensions, pre-registration, falsification, public-data cosmology, space-frame, PNT, SPICE, Astropy, frame-stack forensics, kill switch, multi-track program |
| Related identifiers (cites) | 10.5281/zenodo.19676237 (priority hash deposit, RSOS-260797 r1 priority lock; concept-DOI 10.5281/zenodo.19676236 aggregates all versions) ; RSOS-260797 r4 (under review, EB carrier characterization theorem) ; US 63/902,536 (UHA provisional patent) ; AMS Memoirs 260427-umo36 (under preliminary review) |
| Related identifiers (continues) | (none — first deposit in this series) |
| Related identifiers (is part of) | (umbrella; Z1, Z2, Z3, Z4, Z5 are children deposits to be linked when each is created) |

---

## 1. Purpose

This deposit pre-registers the **umbrella** for a three-track research program testing whether the Universal Horizon Address (UHA) coordinate framework, combined with EB carrier uncertainty propagation, can:

1. Operate as an overlay layer for space-operations coordinate handling (Track 0)
2. Improve cross-survey cosmological consistency through better coordinate provenance (Track A)
3. Reduce apparent cosmological tensions by unifying Ωm baselines across surveys (Track B)

The umbrella does not run any analysis itself. It locks the research-program structure, the non-claims, the termination criteria (kill switches), and the deposit chain so that subsequent per-track pre-registrations (Z1, Z2, Z3) inherit a consistent framework and so that post-hoc rescue of any failed branch is structurally impossible.

This pre-registration does not claim that UHA is correct. It defines tests that can support, fail to support, or falsify parts of the framework.

### 1.1 Pre-registered hypotheses and decision locks

These locks apply to Z0 and are inherited by Z1, Z2, and Z3 unless a later child preregistration narrows them further before analysis.

#### Track A — Coordinate provenance

- **H0-A:** Coordinate provenance tracking will not reduce cross-survey disagreement.
- **H1-A:** Coordinate provenance tracking will reduce cross-survey disagreement, measured by lower Δχ² and stronger cross-survey consistency relative to the baseline model.

#### Track B — Ωm baseline alignment

- **H0-B:** Aligning Ωm baselines will not reduce cosmological tension between datasets.
- **H1-B:** Aligning Ωm baselines will reduce cosmological tension between datasets, measured by lower Δχ² and stronger cross-survey consistency relative to the baseline model.

#### Shared decision definitions

- **Baseline model:** the original dataset configuration with no coordinate provenance tracking for Track A and no Ωm alignment for Track B.
- **Improvement:** Δχ² decreases relative to the baseline model in the predicted direction.
- **Primary success:** Δχ² improves in the predicted direction and the Bayes factor favors the adjusted model over baseline.
- **Bayes factor support:** BF > 1 is treated as support for the adjusted model. Strength of evidence is reported under the locked threshold table in §6.
- **AgreementMetric and TensionMetric:** both are defined as Δχ² relative to the baseline model unless a child preregistration defines a narrower metric before analysis begins. No alternative metric will be substituted after results are observed.
- **Analysis start:** the first execution of the locked analysis pipeline after Z0 and the relevant child preregistration DOI are deposited.
- **Same-pipeline rule:** the same analysis pipeline will be used across datasets without modification, except for dataset-specific input adapters documented before analysis start.
- **Controls:** controls include rerunning the analysis with provenance tracking disabled, Ωm alignment disabled where relevant, or dataset labels permuted. Controls may diagnose robustness; they may not redefine primary success.

#### Data handling locks

- Only observations flagged as invalid by the source dataset will be removed.
- No outliers will be removed unless the source dataset already flags them as invalid.
- Missing or incomplete records will be handled by listwise deletion unless the source dataset supplies a documented imputation rule before analysis start.
- Secondary tests use Benjamini-Hochberg FDR correction.
- Primary tests are evaluated under the locked §6 evidence thresholds and are not corrected against exploratory or secondary tests.

### 1.2 What would render the program unsupported

This program will be considered unsupported if any of the following occur: Ωm baselines are statistically consistent across surveys within declared uncertainties; UHA coordinate provenance produces no measurable cross-survey tightening; required coordinate perturbations exceed published uncertainty bounds or require assumptions not present in source documentation; or UHA encode/decode round-trip tests fail. In such cases, the relevant branch halts and a negative or narrow-method result is deposited under the failure-publication rule (§9). This paragraph does not replace the termination-criteria tables in §7; it summarises them in plain language.

### 1.3 Public-data-first scope

"Public-data first" in this pre-registration means that the hypothesis-adjudicating analyses under Z1–Z3 use publicly available datasets (Planck 2018 chains, KiDS-1000, DES Y3, HSC Y3, Pantheon+, BOSS DR12, DESI public BAO results, SH0ES R22, public SPICE/JPL/Astropy/TLE/Gaia products). Proprietary, embargoed, or collaboration-restricted datasets, if ever used, are outside the pre-registered hypothesis test unless covered by a new pre-registered amendment DOI. Dataset versions, release dates, and access dates will be recorded at analysis start. Any later public-data release requires a separate preregistered update before use in hypothesis-adjudicating analysis.

### 1.4 Evidence framework

This pre-registration evaluates evidence within standard likelihood-based and Bayesian model-comparison frameworks (Δχ² + Bayes factor; AIC/BIC may appear in supporting analyses but are not gating thresholds). Δχ² is the primary metric. Bayes factor is confirmatory support, not a substitute for Δχ² movement in the predicted direction. It does not adjudicate philosophical claims about Bayesian versus frequentist optimality.

## 2. Authorship and authority

- Sole author: Eric D. Martin / ORCID 0009-0006-5944-1742 / Independent researcher
- No Co-Authored-By AI. No AI in bibliography as author.
- Disclosure-timing self-review completed by author.
- No external consultation will be used to modify hypotheses, models, thresholds, interpretation rules, or termination criteria after deposit. Any change after deposit requires a new DOI amendment.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md` — drafting support, formatting, and consistency checks. They were not used as authors, data sources, evidence, proof of validity, endorsement, or co-authorship.

## 3. Canonical source documents

The following documents form the locked source manifest for this umbrella. Subsequent per-track deposits may add documents; they may not modify these without an amendment deposited as a new Zenodo record.

| Document | Path (canonical, post-rename) | Bootstrap commit / Content sha256 |
|---|---|---|
| Master roadmap (Research/IP axis) | `nu-algebra/docs/ROADMAP_2026_2027_v0.1_ea08f59.md` | `ea08f59` / `bf4afc3a07e5dc40dcd651eba3511888450f545e4400beeec790fcdb6ce40b48` |
| Track 1 checklist (Research/IP execution pipeline) | `nu-algebra/CHECKLIST_v1.0_ea08f59.md` | `ea08f59` / `9af99cebd92907f6676584847bc3e817ae2e5c8fe7c592de4ac928ada90cef09` |
| Track 2 umbrella (Space-Frame/PNT v0.5) PDF | `hubble-tensor/patent_filing/UHA_Space_Frame_PNT_Roadmap_v0.5_52606f3.pdf` | `52606f3` / `e76fa5f64e494fbcb7d094fec94783640f0ef625bfb8d04b745f8b0ad880ef76` |
| Track 2 umbrella v0.5 markdown | `hubble-tensor/patent_filing/UHA_Space_Frame_PNT_Roadmap_v0.5_52606f3.md` | `52606f3` / `092c0e1bd9d89a9b2f9652807dd05aa52bc839743fb19ab24088bfce393765a9` |
| Track A experiment v1.0 (Coordinate Framework) | `hubble-tensor/research/UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md` | `77b639c` / `5423eeadf5b2052dc04ea51279b03be1d65583851ca4aac28d655ea50a295683` |
| Track B experiment v1.0 (Ωm Baseline Unification) | `hubble-tensor/research/Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md` | `77b639c` / `3dd711f06b0a757c74a4e350d6b6d424ef979de7d8b981fac66907a44b3f0e59` |

**Repository state at pre-registration (bootstrap commits per `feedback_artifact_hash_naming.md`):**
- `nu-algebra` HEAD: `ea08f59` (policy block + 4-file retrofit; CHECKLIST + ROADMAP + carrier-universality + embodied-auditonomy)
- `hubble-tensor` HEAD: `77b639c` (Z0 v1.1 self-reference fields + Track A/B policy block)

**Track 2 retrofit gap closed (2026-04-28):** All entries above now follow the artifact-hash-naming policy. The v0.5 PNT roadmap pair was retrofitted at bootstrap commit `52606f3`. Z0's manifest has no remaining known gaps.

## 4. Three-track program structure

Per the v0.5 roadmap §4:

| Track | Name | Primary question | Public-data first | Output |
|---|---|---|---|---|
| Track 0 | Space-frame / PNT adoption | Can UHA wrap existing space-state systems without breaking them? | Yes | Pre-registered overlay encoder + benchmark + SSA demo |
| Track A | Coordinate-framework experiment | Does UHA coordinate provenance improve cross-survey consistency? | Yes | Pre-registered coordinate-framework paper |
| Track B | Ωm baseline experiment | Do inconsistent Ωm baselines create apparent tensions? | Yes | Pre-registered Ωm unification paper |

Track 0, A, and B are independent pre-registrations (Z1, Z2, Z3 respectively), but they share infrastructure (UHA encoder, EB carrier algebra, public dataset inventory, frame-stack audit) and have explicit cross-track halt-propagation rules (§7 below).

## 5. Non-claims (what this program does NOT assert)

The umbrella locks the following non-claims. Per-track pre-registrations may not contradict them.

1. **Not claiming GPS or spacecraft-position errors cause the Hubble tension.** This is a testable hypothesis under Track A Phase A5; not a result.
2. **Not claiming UHA independently measures positions.** UHA encodes, fingerprints, compares, and audits. Sensors (GNSS, DSN, INS, XNAV, star tracker, optical navigation, VLBI, survey pipeline) produce the estimate.
3. **Not claiming UHA replaces SPICE, GPS, DSN, Astropy, or WCS.** UHA wraps and audits them in this program. Replacement is out of scope.
4. **Not claiming UHA eliminates ephemeris uncertainty.** It carries the uncertainty fields and makes parameter provenance explicit.
5. **Not claiming the residual Hubble tension is fully explained by platform/orbit uncertainty.** This is a falsifiable hypothesis under Track A Phase A5 / Track B Phase B4.
6. **Not claiming a unified UHA-derived Ωm baseline resolves all cosmological tensions.** This is a falsifiable hypothesis under Track B Phases B3–B5.
7. **Not claiming Δχ² improvements from prior companion work (MN-26-1117-P submitted, not peer-reviewed) automatically transfer to these new experiments.** Each experiment computes and validates its own statistics from public data.
8. **Not claiming any specific Bayes factor outcome in advance.** The thresholds in §6 below define the venue routing; they do not assert which venue the outcome will be.

## 6. Pre-registered evidence-class thresholds (locked across tracks)

Per v0.5 §6.8 (Track A) and §7.8 (Track B), the same Bayes-factor + Δχ² thresholds classify the outcome:

| Evidence class | Threshold | Venue route |
|---|---|---|
| Exceptional evidence | Δχ² > 50 AND BF > 150 | *Nature* / *Science* candidate |
| Strong evidence | Δχ² 20–50 AND BF 20–150 | *Physical Review Letters* / *Nature Astronomy* candidate |
| Moderate evidence | Δχ² 9–20 AND BF 3–20 | MNRAS / PRD methods paper |
| Null / unsupported | Δχ² < 9 AND BF < 3 | MNRAS technical note / negative-result deposit |

These thresholds are **locked**. They will not be adjusted post-hoc based on observed Δχ² or BF values. If an outcome falls outside the bands (e.g., Δχ² in the Strong band but BF in the Moderate band), the routing follows the lower of the two evidence-class assignments — i.e., the most conservative venue consistent with both criteria. Worked example: Δχ² = 28 (Strong) and BF = 12 (Moderate) routes to MNRAS / PRD (Moderate venue), not PRL / Nature Astronomy (Strong venue).

### 6.1 Per-track primary endpoints (locked)

| Track | Primary endpoint | Failure endpoint |
|---|---|---|
| Track 0 | UHA wrapper round-trip success + benchmark gain on real public data + zero SSA false negatives under declared bound | Round-trip failure, no benchmark gain, or any SSA false negative |
| Track A | Measurable cross-survey consistency improvement under UHA coordinate provenance | No measurable tightening, or coordinate effect too small to matter |
| Track B | Unified Ωm baseline reduces cross-probe tension, χ², or parameter scatter | Ωm baselines agree across surveys, substitution has no effect, or evidence threshold is not met |

### 6.2 Operational model locks

These model forms are umbrella-level defaults. Child preregistrations may add narrower formulas before analysis starts, but may not loosen these locks.

#### Track 0 — Space-frame / PNT adoption

- **Goal:** Test whether UHA can encode and decode real coordinate systems without breaking round-trip representation.
- **Systems:** ECEF, ECI, WGS84, SPICE frames, Astropy frames, TLE/JPL/Gaia-derived products where source metadata are recoverable.
- **Pass rule:** encode/decode round-trip error must stay within the precision limits documented by the official documentation for the coordinate system, software package, or source product used.
- **Fail rule:** Track 0 fails if encode/decode mismatch occurs, round-trip error exceeds documented precision limits, the coordinate system cannot be represented, no real-data benchmark gain is observed, or any SSA false negative occurs under the declared bound.

#### Track A — Coordinate-framework experiment

Formula-level lock:

```text
AgreementMetric ~ ProvenanceCondition + Dataset
```

Definitions:

- `AgreementMetric` = Δχ² relative to baseline unless narrowed before analysis start.
- `ProvenanceCondition` = baseline vs provenance-tracked.
- `Dataset` = survey/source identifier.

Track A succeeds only if provenance tracking lowers Δχ² relative to baseline under the locked evidence rules. Track A fails if agreement does not improve, agreement worsens, the effect disappears under controls, or coordinate effects are too small to matter under published uncertainty bounds.

#### Track B — Ωm baseline experiment

Formula-level lock:

```text
TensionMetric ~ OmegaBaselineCondition + Dataset
```

Definitions:

- `TensionMetric` = Δχ² relative to baseline unless narrowed before analysis start.
- `OmegaBaselineCondition` = original vs Ωm-aligned.
- `Dataset` = survey/source identifier.

Track B succeeds only if Ωm alignment lowers Δχ² relative to baseline under the locked evidence rules. Track B fails if tension does not decrease, tension increases, required Ωm shifts exceed published uncertainty bounds, or evidence thresholds are not met.

## 7. Termination criteria (kill switches; umbrella-level, locked)

Eighteen primary termination criteria across the two original tracks (`CHECKLIST_v1.0_ea08f59.md` §14 and v0.5 §11), plus four cross-track cascade rules. The shorthand "kill switches" is retained throughout the rest of the document for brevity.

### Track 1 (Research/IP) primary switches

| ID | Trigger | Action |
|---|---|---|
| KS1 | Ωm values agree within uncertainty across surveys | Abort residual-Ωm experiment; deposit negative |
| KS2 | Required δr to close residual exceeds plausible coordinate uncertainty | Abort platform-position branch; reframe |
| KS3 | Ωm_UHA unstable under sensitivity | Reframe Phase 1 as exploratory; do not run substitution as strong test |
| KS4 | Substitution violates pipeline independence | Stop substitution claim; document invalid design |
| KS5 | Cross-survey scatter does not improve | Reframe as pairwise diagnostic only |
| KS6 | Pre-Euclid prediction not numerical/falsifiable | Do not lock; rewrite or do not deposit |
| KS7 | Disclosure restriction prevents public release | Freeze public deposit; private timestamped archive continues until public release is allowed |
| KS8 | Live manuscript contains false claim | Pause new work; correct in place or notify venue |
| KS9 | Repository contains private credential or status URL | Stop and scrub before further commit |

### Track 2 (Space-Frame/PNT) primary switches

| ID | Trigger | Action |
|---|---|---|
| K0 | Source metadata not recoverable | Mark not UHA-wrap-ready per source; partial coverage |
| K1 | UHA encode/decode round-trip failure | Stop wrapper claims; fix encoder before any cosmology test |
| K2 | No real-data benchmark gain | Downgrade operational claim |
| K3 | SSA false negative under declared bound | Stop SSA claim until search rule is corrected |
| K4 | Coordinate effect on cosmology residual is too small | Stop coordinate-precision-causes-tension claim |
| K5 | UHA provenance does not improve cross-survey consistency | Publish null or narrow-method result |
| K6 | No materially different Ωm baselines across surveys | Stop baseline-unification claim; deposit negative |
| K7 | Ωm substitution produces no effect on tensions | Publish negative result |
| K8 | Evidence threshold not met | Route to modest/null venue per §6 |

### Cross-track propagation

Note on axis convention: this table uses the canonical T0/TA/TB axis from §4 (and §12 commit-tag convention) throughout. The earlier "Track 1 / Track 2" labels mapped TA+TB→Track 1 and T0→Track 2; that collision is resolved here by using only T0/TA/TB. Termination criteria IDs (KS1–9, K0–8) retain their original labels for traceability to the source documents.

| Switch fires (in source track) | Effect on other tracks |
|---|---|
| TB.KS1 (identical Ωm baselines across surveys) | TB Phases 2–6 halt; TA Phase 4 Hubble-tension test halts (narrow null implies broad mechanism unlikely to produce detectable Hubble effect) |
| TB.KS2 (δr implausible per back-of-envelope) | TA Phase 5 cosmology-position branch halts |
| T0.K1 (encoder round-trip fails) | TA Phase 2–6 halt; TB Phase 2 (UHA Ωm baseline) cannot proceed (encoding layer untrustworthy) |
| T0.K0 (source metadata not recoverable) | TA Phase 0 marks that source partial-coverage; **mark-and-continue, not halt** (does not abort whole track) |

## 8. Always-active circuit-breakers

These are not phase-bound; they apply at every step in either track:

- **Pre-registration deposit DOI must exist before any analysis runs.** Compute fires only after Z0 + (relevant Z1/Z2/Z3) DOIs are recorded.
- **Print + 30-min cool + GATE:OPEN** required before any ScholarOne or Zenodo submission (`feedback_submission_print_gate.md`).
- **Zenodo deposits gated on hard-print + author-confirmed-read** (`feedback_zenodo_publish_gate.md`).
- **Marketing-language audit** before any deposit: grep for "revolutionary", "Nobel", "100% explained", "completely solves", "definitively", "groundbreaking", "paradigm shift", "Einstein-level", "textbook-level"; any match is a fail and must be replaced with bounded language.

## 9. Failure-publication commitment (pre-locked, two-stage)

If any kill switch fires in either track, the deposit chain is two-stage to preserve the anti-bury rule without forcing premature manuscript quality:

### 9.1 Stage 1 — Negative-outcome notice (within 14 days, no extensions)

A short Zenodo deposit (under 1000 words) identifying:
- Which kill switch fired (KS1–9 / K0–8 / cross-cascade label)
- Observed value vs threshold
- Affected branch (Track and Phase)
- Immediate halt status (which downstream phases stopped)
- Source-document sha256 references (per §3)
- Pointer to the forthcoming Stage 2 deposit

This Stage 1 notice is the anti-rescue commitment. It cannot be extended past 14 days from kill-switch firing, except when KS7 has frozen public release. If KS7 is active when another kill switch fires, the Stage 1 notice is held in a private timestamped archive with sha256 lock. The 14-day public-deposit clock pauses only while public release is blocked. When public release is allowed, the Stage 1 notice is deposited publicly within 7 days. The private timestamped archive is the proof-of-commitment during the freeze period.

### 9.2 Stage 2 — Full negative-result technical note (when code/data packaging is complete)

A full Z5 child deposit follows once code, data, and logs are packaged for reproducibility:
- **Venue:** MNRAS technical note (cosmology nulls) or Zenodo standalone (purely methodological null)
- **Title format:** `Pre-registration outcome: [hypothesis] is not supported by [test]`
- **Length:** ~3000 words target
- **Required content:**
  - Methodology recap (cite source documents from §3 above by sha256)
  - Kill-switch trigger details (which switch, what threshold, what value observed)
  - Data and code (sha256-locked, cited)
  - Conclusion with explicit "this hypothesis is not supported" language
  - Cross-reference to the Stage 1 notice DOI

This two-stage structure preserves the anti-bury rule (Stage 1 cannot be skipped) without creating a quality risk for the technical note (Stage 2 follows when packaging is genuinely complete). Both stages are commitments; both must be deposited.

## 10. Deposit chain (locked sequence)

| ID | Title | Status | Notes |
|---|---|---|---|
| **Z0** | This umbrella | Draft v1.2-hybrid timestamped | This document; deposit before Z1–Z3 |
| **Z1** | Track 0 PNT overlay pre-registration | To draft | Track 0 of v0.5; SPICE/Astropy/TLE/JPL benchmark + SSA demo |
| **Z2** | Track A coordinate-framework pre-registration | To draft | v0.5 §6 + `UHA_Coordinate_Framework_Experiment_Complete_v1.0.md` |
| **Z3** | Track B Ωm baseline pre-registration | To draft | v0.5 §7 + `Omega_M_Baseline_Unification_Experiment_Complete_v1.0.md` |
| **Z4** | Forensic audit results (post Phase 0/A1 + B1) | To draft after Z2/Z3 phases run | Public frame-stack audit + Ωm derivation-chain audit |
| **Z5.0** | Track 0 results deposit | To draft after Track 0 completes | Encoder + benchmark + SSA demo results; null still deposited |
| **Z5.A** | Track A results deposit | To draft after Track A completes | Coordinate-framework cross-survey analysis result; null still deposited |
| **Z5.B** | Track B results deposit | To draft after Track B completes | Ωm baseline unification result; null still deposited |

Each Zi (i ≥ 1) cites this Z0 as `is part of`. If any Zi-phase amendment is needed mid-execution, the amendment is deposited as a new Zenodo DOI before any further analysis runs. The Z5 series is split per track to keep null/positive outcomes per-track unambiguous.

## 11. Non-publication parallel work (not gated by this pre-registration)

The following workstreams continue in parallel and are not gated by Z0 deposit:

- AMS Memoirs source compliance Phase 2 (B1 memo-l.cls when AMS replies; submission 260427-umo36)
- RSOS-260797 r4 status tracking (under review)
- MNRAS pipeline status across MN-26-1108-L (R&R), MN-26-1117-P, MN-26-1198-P, MN-26-1171-P
- Acta Informatica submission `fbc8c519-b2f6-46fb-b3c9-5cd57bee010b` status
- Resurgence paper polish + arXiv preprint + JEAB / Behavioural Processes submission (`martin_2026_off_cycle_bound_width_v01.md`)
- Patent CIP non-provisional drafting toward 2026-10-21 deadline
- Companion-paper claim-alignment audits per `CHECKLIST_v1.0_ea08f59.md` §11.2

## 12. Naming convention (locked)

- Commit messages prefix: `[T0-PhaseN]`, `[T1-PhaseN]` (`CHECKLIST_v1.0_ea08f59.md` axis), `[TA-PhaseN]`, `[TB-PhaseN]` per v0.5
- Zenodo deposit titles include axis tag: `UHA-EB-2026-{T0|T1|TA|TB}-Phase{N}-{topic}-v{ver}` for child deposits; this umbrella is `UHA-EB-2026-Roadmap-v0.5`

## 13. Version history

- v0.1: working draft (none deposited; superseded by v1.0)
- v1.0: prior lock draft; superseded before deposit by v1.1 cleanup.
- v1.1: source uploaded for final cleanup; not deposited.
- v1.1-clean timestamped 2026-04-29T00-25-57-0700: external-AI cleanup pass. Counsel-specific wording removed; hypotheses, metrics, baselines, data-handling rules, and analysis timing locks added. Not deposited; superseded by v1.2-hybrid.
- **v1.2-hybrid timestamped 2026-04-29T00-54-00-0700 (this draft):** preserves every substantive addition from v1.1-clean; restores the `feedback_others_contradict_not_prove.md` rule citation and contradiction-and-audit framing that v1.1-clean dropped from §2 and §14. J.D. credential note and patent-counsel specificity remain stripped per author decision. For print + cool + GATE:OPEN.

## 14. Final attestation

I, Eric D. Martin, ORCID 0009-0006-5944-1742, Independent researcher, certify that:

- This pre-registration is locked at v1.2-hybrid final when deposited and will not be modified post-deposit. Amendments require a new Zenodo DOI.
- The non-claims in §5 are commitments that will not be quietly dropped.
- The kill switches in §7 are commitments that will be honored on firing.
- The two-stage failure-publication commitment in §9 will be honored: Stage 1 (negative-outcome notice) deposited within 14 days of any kill-switch firing with no extensions; Stage 2 (full technical note) deposited when code/data packaging is complete.
- Disclosure-timing self-review completed by author. Any future disclosure restriction affects release timing only and does not modify the scientific rules locked here.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md` — drafting support, formatting, and consistency checks. They were not used as authors, data sources, evidence, proof of validity, endorsement, or co-authorship.

---

## Appendix A — Cleanup + hybrid audit note

The v1.1-clean cleanup pass (external AI) made the following bounded changes to the uploaded v1.1 draft:

1. Removed counsel-specific wording and replaced it with neutral disclosure-restriction language.
2. Preserved the disclosure-freeze mechanism as a timing rule only; it does not alter scientific claims, hypotheses, models, thresholds, or kill switches.
3. Fixed v1.0/v1.1 mismatch language in the deposit chain, version history, final attestation, and end note.
4. Added explicit H0/H1 statements for Track A and Track B.
5. Defined baseline model, improvement, primary success, AgreementMetric, TensionMetric, analysis start, same-pipeline rule, controls, outlier handling, missing-data handling, and multiple-testing correction.
6. Preserved source-manifest hashes, repository commits, evidence thresholds, kill switches, cross-track propagation, circuit-breakers, failure-publication commitment, and deposit chain.

The v1.2-hybrid pass made the following targeted restorations on top of v1.1-clean:

7. Restored the `feedback_others_contradict_not_prove.md` rule citation and the "contradiction-and-audit instrument" framing in §2 and §14. Reason: the v1.1-clean cleanup dropped the citation while doing the cleanup. The rule states that AI agreement is suspicious and contradiction is signal; silently dropping the rule citation while another AI edits the document breaches the rule itself. Restoration is required for consistency.
8. Did NOT restore the J.D. (Inactive 2014) credential note from v1.1. Reason: author confirmed no patent coursework; carrying that credential here would read as borrowed authority in a scientific pre-registration context.
9. Did NOT restore the patent-counsel specificity in KS7 (§7) or §9.1. Reason: author confirmed the generic "disclosure restriction" wording; private patent counsel is not retained.

All other content from v1.1-clean is preserved verbatim.

## Appendix B — Source-manifest sha256 block (verbatim, for deposit metadata)

```
e76fa5f64e494fbcb7d094fec94783640f0ef625bfb8d04b745f8b0ad880ef76  hubble-tensor/patent_filing/UHA_Space_Frame_PNT_Roadmap_v0.5_52606f3.pdf
092c0e1bd9d89a9b2f9652807dd05aa52bc839743fb19ab24088bfce393765a9  hubble-tensor/patent_filing/UHA_Space_Frame_PNT_Roadmap_v0.5_52606f3.md
5423eeadf5b2052dc04ea51279b03be1d65583851ca4aac28d655ea50a295683  hubble-tensor/research/UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md
3dd711f06b0a757c74a4e350d6b6d424ef979de7d8b981fac66907a44b3f0e59  hubble-tensor/research/Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md
9af99cebd92907f6676584847bc3e817ae2e5c8fe7c592de4ac928ada90cef09  nu-algebra/CHECKLIST_v1.0_ea08f59.md
bf4afc3a07e5dc40dcd651eba3511888450f545e4400beeec790fcdb6ce40b48  nu-algebra/docs/ROADMAP_2026_2027_v0.1_ea08f59.md
```

Repository commits at pre-registration freeze (bootstrap, per `feedback_artifact_hash_naming.md`):
- `nu-algebra` HEAD: `ea08f59`
- `hubble-tensor` HEAD: `77b639c`

Note: the v0.5 PNT roadmap retrofit (bootstrap `52606f3`) closed the only known gap in this manifest. All entries now follow the artifact-hash-naming policy.

---

*End of Z0 umbrella pre-registration draft v1.2-hybrid timestamped 2026-04-29T00-54-00-0700. To be hard-printed, cooled 30 minutes, GATE:OPEN per `feedback_zenodo_publish_gate.md`, then deposited on Zenodo with DOI cross-linked back into this repository.*
