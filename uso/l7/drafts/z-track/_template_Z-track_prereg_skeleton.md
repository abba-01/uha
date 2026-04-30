# [Z-id] — [Track-name] Pre-Registration: [Subject]

**Status:** DRAFT v1.0 — not deposited. Working draft for PDF reader-mode + cool-off mode-shift + GATE:OPEN per `feedback_zenodo_publish_gate.md`.

**Working draft note:** This [Z-id] is a child of the Z0 umbrella pre-registration deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19881689` (concept DOI `10.5281/zenodo.19881688`; record https://zenodo.org/records/19881689). It deposits [Track-name] of the three-track UHA + EB carrier program: [Track-purpose-one-line]. It inherits Z0's hypothesis-lock structure, evidence-class thresholds, kill-switch interpretation preamble, two-stage failure-publication commitment, and deposit chain. It adds the [Track-name] specifics: [H0/H1 hypotheses], locked public-data source classes, the [phase-chain] phase chain, and the [K0–K4] termination criteria with cross-track propagation.

| Self-reference field | Value |
|---|---|
| Version | v1.0 timestamped `[ISO-8601-timestamp]` |
| Parent (umbrella) | Z0 v1.2-hybrid at hubble-tensor commit `d842691`; deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` |
| Working filename | `[Z-id]_[track-slug]_preregistration_v1.0_timestamped_[timestamp].md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |
| Pending bookkeeping | This working draft is not canonical until committed and renamed with the resulting commit hash under the artifact-hash-naming policy. |

**Standing artifact-hash-naming policy (locked, propagating, inherited from Z0):** Every artifact in this research program carries its commit hash both inside the document AND in the filename. No hash, no canonical status. No exceptions. This document inherits the policy from Z0 and propagates it: every [Track-name] artifact derived from, citing, or extending this [Z-id] inherits the same rule. Per `feedback_artifact_hash_naming.md`.

---

## Zenodo metadata block (deposit-ready)

| Field | Value |
|---|---|
| Title | [Track-name] Pre-Registration: [Subject] |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint |
| Communities | (TBD — Zenodo community selection at deposit time) |
| Keywords | [comma-separated track-specific keywords] |
| Related identifiers (is part of) | `10.5281/zenodo.19881689` (Z0 umbrella v1.2-hybrid, deposited 2026-04-29) |
| Related identifiers (cites) | `10.5281/zenodo.19676237` (priority hash deposit); RSOS-260797 r4 (under review, EB carrier characterization theorem); US 63/902,536 (UHA provisional patent) |

---

## 1. Purpose

This deposit pre-registers [Track-name] of the three-track UHA + EB carrier program: [Track-purpose-paragraph].

[Track-name] does not [scope-disclaimer-1]. It tests [scope-positive].

[Track-name] does not [scope-disclaimer-2]. It locks [what-the-prereg-locks-before-analysis-starts].

This pre-registration does not claim that [out-of-scope-claim]. Per Z0 §5 non-claims, [Track-name] tests [actual-scope-paragraph].

### 1.1 Pre-registered hypotheses and decision locks ([Track-name])

Inherited from Z0 §1.1 unless narrowed below.

#### Hypotheses ([Track-name])

- **H0-[T-id]:** [null-hypothesis-statement-in-track-specific-form]
- **H1-[T-id]:** [alternative-hypothesis-statement-in-track-specific-form]

#### Shared decision definitions

Inherited from Z0 §1.1. [Track-name] narrowing:

- **Baseline:** [track-specific-baseline-definition]
- **Improvement:** [track-specific-improvement-definition]
- **Primary success:** [track-specific-primary-success-conjunction-of-gates]
- **Analysis start:** the first execution of the locked [pipeline-or-procedure] after this [Z-id] DOI is deposited and recorded.
- **Same-pipeline rule:** [track-specific-same-pipeline-rule]
- **Controls:** [track-specific-controls-definition]

#### Data handling locks

Inherited from Z0 §1.1 in full.

### 1.2 What would render [Track-name] unsupported

[Track-name] will be considered unsupported if any of the following occur: [K0-trigger-summary]; [K1-trigger-summary]; [K2-trigger-summary]; [K3-trigger-summary]; [K4-trigger-summary]. In such cases [Track-name] halts and a negative or narrow-method result is deposited under the failure-publication rule (Z0 §9, two-stage). This paragraph does not replace the termination-criteria tables in §7; it summarises them in plain language.

### 1.3 Public-data-first scope

Per Z0 §1.3. [Track-name] hypothesis-adjudicating analyses use only the publicly available source classes listed in §3 below. Dataset versions, release dates, and access dates will be recorded at analysis start. Any later public-data release requires a separate preregistered update before use in hypothesis-adjudicating analysis.

### 1.4 Evidence framework

Per Z0 §1.4. [Track-specific-evidence-framework-narrowing — Δχ², Bayes factor, etc.]

## 2. Authorship and authority

- Sole author: Eric D. Martin / ORCID 0009-0006-5944-1742 / Independent researcher
- No Co-Authored-By AI. No AI in bibliography as author.
- Disclosure-timing self-review completed by author.
- No external consultation will be used to modify hypotheses, models, thresholds, interpretation rules, or termination criteria after deposit. Any change after deposit requires a new DOI amendment.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md` — drafting support, formatting, and consistency checks. They were not used as authors, data sources, evidence, proof of validity, endorsement, or co-authorship.

## 3. Canonical source documents and locked public-data source classes

[Track-name] inherits Z0 §3 source-document manifest.

Locked [Track-name] public-data source classes:

| Source class | Public path | UHA use |
|---|---|---|
| [class-1] | [public-path-1] | [use-1] |
| [class-2] | [public-path-2] | [use-2] |
| ... | ... | ... |

Source datasets, versions, release dates, and access dates will be recorded at analysis start (cite §1.3 lock).

### 3.1 Data representation locks ([Track-name])

This section pre-commits to *how* the data will be represented at every analysis stage and at deposit time. Rigor of any analytical claim is bounded above by rigor of the representation; pre-registering representation prevents post-hoc downsampling, lossy figure-only deposits, and the kind of machine-unreadable history that forces downstream researchers to digitize from raster scans (e.g., Swensson 1976 figure digitization, the cost case for this lock). This rule maps to FAIR-data and Data-Management-Plan principles already required by NSF/NIH/ESA.

**Tabular data:**
- Format: CSV (UTF-8) and/or parquet for every primary table; XLSX is permitted only as a secondary mirror.
- Schema lock: every table has an explicit column list with types, units, and primary keys named in the data dictionary (Appendix [X]).
- Keyed: at least one primary-key column per table; foreign-key references documented when joining across tables.
- Per-row provenance where applicable: source file, source row, sha256 of the source.

**Figures:**
- Raster floor: 300 DPI minimum at the figure's intended print size; published figures in vector format (PDF, SVG, EPS) where the source software supports it.
- Every figure has a companion machine-readable data file (CSV/parquet) carrying the data points the figure displays; figures alone do not satisfy the data-representation requirement.
- Axis ranges, units, and binning choices recorded in the figure caption AND in the companion file's metadata.

**Database (if used):**
- Schema definition committed before analysis-start; schema changes require a preregistered amendment.
- Export format: SQL dump + CSV-per-table mirror at deposit time.
- Provenance per row.

**File formats (general):**
- Open formats preferred: CSV, parquet, NetCDF, FITS, JSON, YAML, plain text.
- Proprietary formats (XLSX, MAT, SAS, etc.) permitted only as secondary mirrors of open-format primaries.

**Reproducibility block (per analysis run):**
- sha256 of every input data file, recorded at analysis-start.
- Software versions: Python/R/Julia version, package versions (requirements.txt or environment.yml committed).
- Random-seed lock: every stochastic step (MCMC, bootstrapping, train/test split) has a seed declared at analysis-start and recorded with the result.
- Compute environment: OS, CPU/GPU info, total runtime.

**Data dictionary / codebook:**
- One file per primary table.
- Every column documented: name, type, unit, valid range, coded values, missing-value indicator.
- Updated at any schema change with a version stamp.

**Failure mode (what this section prevents):**
- A figure-only deposit that requires downstream digitization to recover the data
- A table without a key, requiring readers to infer join columns
- A 300 DPI raster where vector source existed (information loss for re-typesetting)
- An XLSX with formulas baked in (data and computation entangled, not separable)
- An analysis run with no seed lock (results not exactly reproducible)

Each of the above is grounds for marking a deposit "incomplete representation" rather than "complete." [Track-name] commits to none of these failure modes occurring at the [Z-id] results-deposit stage.

## 4. [Track-name] program structure

| Phase | Name | Output |
|---|---|---|
| [T-id].1 | [phase-name-1] | [phase-output-1] |
| [T-id].2 | [phase-name-2] | [phase-output-2] |
| ... | ... | ... |
| [T-id].N | [results-deposit-phase] | Per Z0 §10; positive, negative, or null per evidence threshold |

## 5. Non-claims ([Track-name]; cite Z0 §5)

Per Z0 §5. [Track-name] specifically does NOT assert:

1. [non-claim-1]
2. [non-claim-2]
...

## 6. Evidence-class thresholds (cite Z0 §6) and [Track-name] endpoints

### 6.1 [Track-name] primary endpoint (locked)

Per Z0 §6.1:

- **Primary success:** [conjunction-of-gates]
- **Primary failure:** [disjunction-of-failure-conditions]

### 6.2 Operational model lock ([Track-name])

[Track-specific operational-model-lock paragraphs]

### 6.3 Threshold-to-venue routing (cite Z0 §6)

Per Z0 §6 evidence-class thresholds. [Track-name] is a [methods/operational/empirical] test; routing follows the conservative-of-two rule per Z0 §6.

## 7. Termination criteria (kill switches; [Track-name]; locked)

### Kill-switch interpretation preamble

Inherited from Z0 §7 verbatim:

The termination criteria ("kill switches") in §7 are defined as auditable decision rules, not descriptive guidelines.

Each kill switch is constructed to satisfy three conditions:

1. Observable trigger — the condition that fires the switch must be detectable from the data, model outputs, or documented pipeline behavior.
2. Defined action — each switch specifies a required response (halt, downgrade, reframe, or deposit), with no discretionary override.
3. Traceable effect — each switch has a defined impact on downstream phases or related tracks, including cross-track propagation where specified.

Where ambiguity arises in determining whether a trigger condition is met, the conservative interpretation applies: halt or downgrade rather than extend or reinterpret the claim.

The purpose of this structure is to minimize researcher degrees of freedom and prevent post-hoc rescue of unsupported results.

### [Track-name] primary switches

| ID | Trigger | Action |
|---|---|---|
| K0 | [K0-trigger-track-specific] | [K0-action-track-specific] |
| K1 | [K1-trigger-track-specific] | [K1-action-track-specific]; cascade per Z0 §7 |
| K2 | [K2-trigger-track-specific] | [K2-action-track-specific] |
| K3 | [K3-trigger-track-specific] | [K3-action-track-specific] |
| K4 | [K4-trigger-track-specific] | [K4-action-track-specific] |

### Cross-track propagation (per Z0 §7)

| Switch fires ([Track-name]) | Effect on other tracks |
|---|---|
| [Z-id].K[n] ([trigger-summary]) | [downstream-track-effect] |

## 8. Always-active circuit-breakers (cite Z0 §8)

Per Z0 §8 in full. Repeating the umbrella circuit-breakers for child-deposit independence:

- **Pre-registration deposit DOIs must exist before any analysis runs.** [Track-name] compute fires only after both (a) Z0 umbrella DOI `10.5281/zenodo.19881689` is recorded and (b) this [Z-id] DOI is recorded.
- **Print + cool + GATE:OPEN required before any Zenodo deposit** (per `feedback_zenodo_publish_gate.md`).
- **Marketing-language audit** before any deposit: per Z0 §8 banned-language list.

## 9. Failure-publication commitment (cite Z0 §9)

Per Z0 §9 in full (two-stage). [Track-name] inherits the Stage 1 (within 14 days) + Stage 2 (when packaging complete) commitment unchanged.

## 10. Deposit chain ([Track-name] position)

Per Z0 §10:

| ID | Title | Status |
|---|---|---|
| Z0 | Umbrella | Deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` |
| Z1 | Track 0 PNT overlay pre-registration | Deposited 2026-04-29 at DOI `10.5281/zenodo.19904395` |
| **[Z-id]** | **[This pre-registration]** | **This document; pending GATE:OPEN + mint** |
| ... | [other-Z-ids-in-chain] | [status] |

## 11. Non-publication parallel work (cite Z0 §11)

Per Z0 §11. [Z-id] deposit does not gate the parallel workstreams listed in Z0 §11.

## 12. Naming convention (cite Z0 §12)

Per Z0 §12. [Track-name] commit prefix: `[[T-id]-PhaseN]`. [Z-id] child Zenodo title: `UHA-EB-2026-[T-id]-[Z-id]-[track-slug]-v{ver}`.

## 13. Version history

- **v1.0 timestamped [ISO-8601] (this draft):** first draft. [Track-name] child of Z0 umbrella v1.2-hybrid (deposited 2026-04-29 at DOI `10.5281/zenodo.19881689`). Locks [Track-name] hypotheses, source-class manifest (§3), program phases (§4), evidence endpoints (§6.1–§6.2), kill switches K0–K4 + cross-track propagation, and failure-publication inheritance from Z0 §9. Pre-canonical (timestamped, no commit hash); cleared for hash-bookkeeping commit cycle and Zenodo mint after gate.

## 14. Final attestation

I, Eric D. Martin, ORCID 0009-0006-5944-1742, Independent researcher, certify that:

- This pre-registration is locked at v1.0 final when deposited and will not be modified post-deposit. Amendments require a new Zenodo DOI.
- The non-claims in §5 are commitments that will not be quietly dropped.
- The kill switches K0–K4 in §7 and the cross-track propagation rules are commitments that will be honored on firing.
- The two-stage failure-publication commitment from Z0 §9 will be honored.
- Disclosure-timing self-review completed by author.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md`.

---

## Appendix A — Drafting note

[Track-specific drafting context]

The draft is pre-canonical: filename uses a timestamp, not a commit hash. Per `feedback_artifact_hash_naming.md`, the draft cannot be canonical until committed to the hubble-tensor repository and renamed with the resulting commit hash.

No analysis runs may begin under [Track-name] until both (a) Z0 deposit DOI is recorded (true: `10.5281/zenodo.19881689`) and (b) this [Z-id] deposit DOI exists.

## Appendix B — Source-manifest sha256 block (verbatim, for deposit metadata)

Inherited from Z0 §3 manifest (see Z1 for the sha256 block). [Track-name]-specific sha256s for source manuscripts in §3:

```
[sha256-1]  [path-1]
[sha256-2]  [path-2]
...
```

Repository commits at pre-registration freeze:

- `nu-algebra` HEAD: `[hash]`
- `hubble-tensor` HEAD at this [Z-id]'s parent state: `[hash]`

---

*End of [Z-id] [Track-name] pre-registration template skeleton. To use: copy, fill all `[PLACEHOLDER]` markers with track-specific content, save with timestamped filename per `feedback_artifact_hash_naming.md`, sanity-pass, print, cool, GATE:OPEN, mint.*

---

## Template provenance

This template is a structural pre-registration of the form all subsequent Z-track pre-registrations will take. Extracted 2026-04-29 from Z1 (Z1_track0_pnt_overlay_preregistration_v1.0_48ea8f4) which inherited from Z0 (Z0_umbrella_preregistration_v1.2_hybrid_d842691). The template locks structure-before-content: every [Z-id] in the chain commits to having these sections in this order, with these inheritance relationships to Z0, before any track-specific content is written.

**Note:** Z5.* (results deposits) and Z4 (forensic audit results) follow a different structural template (results-shaped, not pre-registration-shaped) — to be drafted separately.
