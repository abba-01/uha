# Z2 — Track A Pre-Registration: UHA Coordinate Provenance Cross-Survey Consistency Test

**Status:** DRAFT v1.0 — not deposited. Working draft for PDF reader-mode + cool-off mode-shift + GATE:OPEN per `feedback_zenodo_publish_gate.md`.

**Working draft note:** This Z2 is a child of the Z0 umbrella pre-registration deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19881689` (concept DOI `10.5281/zenodo.19881688`; record https://zenodo.org/records/19881689). It is also a child of Z1 (Track 0) deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19904395` (concept DOI `10.5281/zenodo.19904394`) — Z2 inherits Z1's encoder lock as its operational dependency. It deposits Track A of the three-track UHA + EB carrier program: testing whether **UHA coordinate provenance tracking improves cross-survey consistency** by making coordinate provenance explicit and improving uncertainty propagation. It inherits Z0's hypothesis-lock structure, evidence-class thresholds, kill-switch interpretation preamble, two-stage failure-publication commitment, and deposit chain. It adds the Track A specifics: H0-TA / H1-TA hypotheses, locked public-data source classes (coordinate frames + survey datasets), the TA.0–TA.7 phase chain, and the K0–K4 (optional K5) termination criteria with cross-track propagation.

| Self-reference field | Value |
|---|---|
| Version | v1.0 timestamped `2026-04-29T21-21-00-0700` |
| Parent (umbrella) | Z0 v1.2-hybrid at hubble-tensor commit `d842691`; deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` |
| Parent (Track 0 dependency) | Z1 v1.0 at hubble-tensor commit `48ea8f4`; deposited 2026-04-29 at DOI `10.5281/zenodo.19904395` |
| Working filename | `Z2_track_A_coordinate_provenance_preregistration_v1.0_timestamped_2026-04-29T21-21-00-0700.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |
| Pending bookkeeping | This working draft is not canonical until committed and renamed with the resulting commit hash under the artifact-hash-naming policy. Staged structural changes accumulating per `feedback_zenodo_propagation_policy.md`: (1) §3.1 data representation lock; (2) EB layer ontology disambiguation (forward-applicable; see `project_eb_layer_ontology.md`); (3) agency hull doctrine as interpretive bridge (forward-applicable; see `project_agency_hull_doctrine.md`); (4) literature engagement (Brout 2021, Casertano 2026, Macri 2006); (5) propagation-policy + scope-risk-primary rules locked in-session. Mint when count + significance gates both trip. |

**Standing artifact-hash-naming policy (locked, propagating, inherited from Z0/Z1):** Every artifact in this research program carries its commit hash both inside the document AND in the filename. No hash, no canonical status. No exceptions. This document inherits the policy from Z0/Z1 and propagates it: every Track A artifact derived from, citing, or extending this Z2 inherits the same rule. Per `feedback_artifact_hash_naming.md`.

---

## Zenodo metadata block (deposit-ready)

| Field | Value |
|---|---|
| Title | Track A Pre-Registration: UHA Coordinate Provenance Cross-Survey Consistency Test |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint |
| Communities | (TBD — Zenodo community selection at deposit time) |
| Keywords | UHA, Universal Horizon Address, coordinate provenance, cross-survey consistency, Hubble tension, frame-stack audit, ICRS, J2000, GCRS, ITRS, WCS, SH0ES, Planck, KiDS, DES, HSC, Pantheon+, BOSS, DESI, pre-registration, falsification, kill switch |
| Related identifiers (is part of) | `10.5281/zenodo.19881689` (Z0 umbrella v1.2-hybrid, deposited 2026-04-29) |
| Related identifiers (is supplemented by) | `10.5281/zenodo.19904395` (Z1 Track 0 PNT overlay pre-registration; encoder dependency for Track A) |
| Related identifiers (cites) | `10.5281/zenodo.19676237` (priority hash deposit, RSOS-260797 r1 priority lock); RSOS-260797 r4 (under review, EB carrier characterization theorem); US 63/902,536 (UHA provisional patent) |

---

## 1. Purpose

This deposit pre-registers Track A of the three-track UHA + EB carrier program: testing whether UHA coordinate provenance tracking improves cross-survey consistency by making coordinate provenance explicit and improving uncertainty propagation through the analysis pipeline.

Track A does not test UHA's encoder fidelity or round-trip representation — that is Z1 / Track 0 territory, already locked. Track A tests what changes downstream when coordinate provenance is held under UHA discipline at the cosmology-relevant cross-survey-comparison level.

Track A does not run the full cosmology comparison; it locks the audit-of-frame-stack, the encoder application across the cosmology dataset stack, the cross-survey consistency test, the cosmological-tension-specific tests, the error-propagation analysis, and the statistical validation, so that the results-deposit (Z5.A) can report findings against pre-registered locks rather than retrofitted criteria.

This pre-registration does not claim that UHA resolves the Hubble tension. Per Z0 §5 non-claims, Track A tests whether coordinate-provenance discipline reduces cross-survey disagreement under the locked Δχ² + Bayes-factor evidence framework — a measurable methodological claim, not a cosmological-tension claim.

### 1.1 Pre-registered hypotheses and decision locks (Track A)

Inherited from Z0 §1.1 unless narrowed below.

#### Hypotheses (Track A)

- **H0-TA:** UHA coordinate provenance tracking will not reduce cross-survey disagreement relative to the baseline dataset configuration.
- **H1-TA:** UHA coordinate provenance tracking will reduce cross-survey disagreement relative to the baseline dataset configuration, measured by lower Δχ² and stronger cross-survey consistency under the locked evidence rules.

#### Shared decision definitions

Inherited from Z0 §1.1. Track A narrowing:

- **Baseline:** the source coordinate-provenance configuration as published by each survey, without UHA-explicit provenance tracking.
- **Improvement:** UHA-explicit provenance tracking reduces cross-survey Δχ² OR strengthens cross-survey consistency on the same data, without loss on the other axes. Per `feedback_zenodo_propagation_policy.md` significance gate language, "lower Δχ²" means a measurable reduction past noise; thresholds are set in §6.
- **Primary success:** all of (TA-G1 frame-stack audit clean) AND (TA-G2 positioning-precision verification clean) AND (TA-G3 encoder application clean) AND (TA-G4 cross-survey consistency improvement measurable) AND (TA-G5 cosmological-tension-specific tests pass) AND (TA-G6 error-propagation clean) AND (TA-G7 statistical validation thresholds met) hold simultaneously on the locked source-class manifest in §3.
- **Analysis start:** the first execution of the locked encoder + provenance-tracking pipeline after this Z2 DOI is deposited and recorded.
- **Same-pipeline rule:** the same encoder (from Z1) and the same provenance-tracking layer is used across all source datasets; per-dataset adapters are documented before analysis start.
- **Controls:** controls include rerunning consistency tests with provenance tracking disabled (must NOT pass TA-G4 if provenance tracking is the load-bearing operation) and substituting random dataset labels (must NOT pass TA-G4). Provenance-disabled controls may pass geometric round-trip but must fail provenance-completeness checks. Controls may diagnose robustness; they may not redefine primary success.

#### Data handling locks

Inherited from Z0 §1.1 in full.

### 1.2 What would render Track A unsupported

Track A will be considered unsupported if any of the following occur: required frame / epoch / provenance metadata is not recoverable for a dataset or source class (K0); Z1 encoder dependency fails or Track A cannot preserve required provenance through the analysis pipeline (K1); UHA coordinate provenance produces no measurable cross-survey tightening (K2); coordinate effect is too small to matter under published uncertainty bounds OR required coordinate perturbation exceeds published bounds / requires undocumented assumptions (K3); provenance effect disappears under controls, dataset-label permutation, or provenance-disabled rerun (K4); evidence threshold not met under locked Δχ² + BF rules (K5, optional). In such cases Track A halts and a negative or narrow-method result is deposited under the failure-publication rule (Z0 §9, two-stage). This paragraph does not replace the termination-criteria tables in §7; it summarises them in plain language.

### 1.3 Public-data-first scope

Per Z0 §1.3. Track A hypothesis-adjudicating analyses use only the publicly available source classes listed in §3 below. Dataset versions, release dates, and access dates will be recorded at analysis start. Any later public-data release requires a separate preregistered update before use in hypothesis-adjudicating analysis.

### 1.4 Evidence framework

Per Z0 §1.4. Δχ² primary; Bayes factor confirmatory. AIC/BIC may appear in supporting analyses but are not gating thresholds. For Track A, the cross-survey consistency improvement is reported as a measured Δχ² difference between the baseline dataset configuration and the UHA-provenance-tracking configuration; the Bayes factor is a confirmatory readout. The Z0 §6 evidence-class table maps the Δχ² magnitude tiers to venue routing.

**Methodology references engaged.** Track A's cross-survey-consistency framing sits in an active 2025–2026 literature on systematic-error budgets and multi-probe combination. Brout et al. (2021) ("Binning is Sinning, Supernova Version") demonstrate that systematic error budgets in cosmological analyses with Type Ia supernovae can be improved by approximately 1.5x via unbinned and unsmoothed covariance matrices, and that data-driven self-calibration of systematics is hindered when information is binned in redshift space. The Pantheon+ binning choice that SH0ES adopts therefore interacts with Track A's A3-equivalent (mechanism-justified off-diagonals) at the SN rung. Casertano et al. (2026) (the H0 Distance Network collaboration) report a community-consensus measurement of H0 = 73.50 +/- 0.81 km/s/Mpc at ~1% precision using explicit covariance-weighted combination of eleven distance indicators; this is exactly the kind of multi-probe accounting Track A's framework should be applicable to, and the H0DN result is treated here as a parallel methodological reference rather than a competitor. Macri et al. (2006) note that background subtraction in crowded HST fields carries calibration-dependent uncertainties at a level that may exceed the formal model; Track A's TA.0 frame-stack forensic audit explicitly opens this calibration question per source class. These references are engaged here to position Track A in the active cosmology-methodology discussion; full literature engagement at the results stage is the burden of Z5.A.

## 2. Authorship and authority

- Sole author: Eric D. Martin / ORCID 0009-0006-5944-1742 / Independent researcher
- No Co-Authored-By AI. No AI in bibliography as author.
- Disclosure-timing self-review completed by author.
- No external consultation will be used to modify hypotheses, models, thresholds, interpretation rules, or termination criteria after deposit. Any change after deposit follows the propagation policy (`feedback_zenodo_propagation_policy.md`): description-changelog accumulates; mint when count + significance gates both trip.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md` — drafting support, formatting, and consistency checks. They were not used as authors, data sources, evidence, proof of validity, endorsement, or co-authorship.

## 3. Canonical source documents and locked public-data source classes

Track A inherits Z0 §3 source-document manifest. Source protocol: `hubble-tensor/research/UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md`.

Locked Track A public-data source classes:

### Coordinate / frame classes

| Frame class | Purpose |
|---|---|
| ICRS | International Celestial Reference System; baseline celestial frame |
| J2000 | Equatorial frame at J2000.0 epoch; legacy reference |
| GCRS | Geocentric Celestial Reference System |
| ITRS | International Terrestrial Reference System |
| WCS-derived survey frames | Per-survey World Coordinate System frames as published |
| Mission-specific celestial / spacecraft frames | HST, Planck L2, Gaia, JWST as documented per mission |
| SPICE / Astropy frame transforms (via Z1 dependency) | Frame composition where required |

### Survey / dataset classes

| Source class | Public path | Track A use |
|---|---|---|
| HST / SH0ES R22 | Riess et al. 2022 public release | Cepheid/SN ladder cross-survey anchor |
| Planck 2018 | Planck Legacy Archive chains/likelihoods | CMB-derived cosmology comparison |
| KiDS-1000 | KiDS public DR | S₈ / weak-lensing cross-survey |
| DES Y3 | Dark Energy Survey Y3 public | Cross-survey weak-lensing/clustering |
| HSC Y3 | Hyper Suprime-Cam Y3 public | Cross-survey weak-lensing |
| Pantheon+ | SN Ia public release with covariance | SN cosmology cross-survey |
| BOSS DR12 BAO | SDSS DR12 BAO consensus | BAO cross-probe anchor |
| DESI public BAO | DESI public release if included under Z0 public-data scope | BAO cross-probe (conditional) |
| Gaia / MAST / JPL / mission metadata | Public via mission archives | Frame-stack and provenance audit only; not hypothesis-adjudicating |

Source datasets, versions, release dates, and access dates will be recorded at analysis start (cite §1.3 lock).

### 3.1 Data representation locks (Track A)

Per the data-representation lock template in `_template_Z-track_prereg_skeleton.md` §3.1 (FAIR-compliant; Swensson cost-case driven). Track A specifically commits:

- **Tabular data** — every cross-survey consistency comparison output as CSV (UTF-8) + parquet; primary keys per table; columns documented in companion data dictionary (Appendix C).
- **Figures** — 300 DPI minimum raster; vector PDF/SVG where matplotlib supports it; companion CSV/parquet for every figure displaying measured data.
- **Reproducibility block** — sha256 of every input file at analysis-start; locked software versions (Python >=3.12, numpy >=2.0, astropy >=7.0; specific versions to be locked at TA.1 freeze); random-seed lock for any MCMC or bootstrap; compute-environment record (OS, CPU/GPU, total runtime).
- **Data dictionary** — one CSV per primary table, schema in Appendix C.
- **Failure mode prevention** — no figure-only deposits; no XLSX-only primaries; no missing seed locks on stochastic steps.

## 4. Track A program structure

Per Z0 §4 + the source protocol's Phase 0–6 structure (zero-indexed in source; 1-indexed mapping shown for template-template alignment):

| Phase | Name | Output |
|---|---|---|
| TA.0 | Frame-stack forensic audit | Per-survey frame-stack provenance recovery; gap log; goes to Z4 forensic-audit results deposit |
| TA.1 | Positioning-precision verification | Per-survey positioning-precision floor recovered and locked |
| TA.2 | UHA overlay encoder application (depends on Z1) | UHA-encoded coordinate provenance applied to each survey dataset |
| TA.3 | Cross-survey parameter consistency test | Δχ² and parameter-scatter measurements baseline-vs-UHA-provenance |
| TA.4 | Cosmological-tension specific tests | Hubble-tension and S₈-tension-specific Δχ² readouts under UHA provenance |
| TA.5 | Error-propagation analysis | Per-pipeline error budget under UHA provenance; comparison to baseline |
| TA.6 | Statistical validation | Bootstrap, leave-one-out, sensitivity-permutation; evidence-class verdict |
| TA.7 | Z5.A results deposit | Per Z0 §10; positive, negative, or null per evidence threshold; uses common Z5 results template |

## 5. Non-claims (Track A; cite Z0 §5)

Per Z0 §5. Track A specifically does NOT assert:

1. UHA resolves the Hubble tension.
2. UHA replaces standard frame-transform pipelines (ICRS, J2000, GCRS, ITRS) — UHA is a provenance overlay layer.
3. Track A independently measures cosmological parameters; it audits provenance and tests whether explicit provenance reduces cross-survey disagreement.
4. The Track A cross-survey consistency improvement transfers automatically to other tension claims.
5. Track A's positive verdict on a subset of surveys generalises to the survey universe.
6. UHA-derived parameter values are correct in the absolute sense — only that they are more cross-survey-consistent under explicit provenance.

## 6. Evidence-class thresholds (cite Z0 §6) and Track A endpoints

### 6.1 Track A primary endpoint (locked)

Per Z0 §6.1:

- **Primary success:** all seven gates (TA-G1 through TA-G7 per §1.1) pass on the locked source-class manifest, with cross-survey Δχ² improvement measurable past noise.
- **Primary failure:** any single gate fails, OR no measurable Δχ² improvement, OR effect disappears under controls.

### 6.2 Operational model lock (Track A)

- **Goal:** Test whether explicit UHA coordinate provenance tracking improves cross-survey consistency, measured by Δχ² reduction and stronger cross-survey agreement under the locked evidence rules.
- **Systems:** ICRS, J2000, GCRS, ITRS, WCS-derived survey frames; SH0ES, Planck, KiDS, DES, HSC, Pantheon+, BOSS BAO, DESI BAO (conditional).
- **Pass rule:** the cross-survey Δχ² with UHA provenance must be measurably lower than without, **in the same fitted parameter space and likelihood definition**, by an amount meeting the locked threshold of **Δχ² >= 9 (~3σ improvement past noise)**. Per `feedback_zenodo_propagation_policy.md`, the propagation-policy floor of Δχ² >= 20 (~4.5σ) is reserved for batched re-mint events, not single-gate primary success; the Δχ² 20-49 range is significance-gate territory and Δχ² >= 49 (~7σ) routes to a separate cosmology-claim deposit per the ceiling-diversion rule. Controls must NOT replicate the improvement.
- **Fail rule:** Track A fails if Δχ² with UHA does not improve, worsens, ties, OR if controls replicate the effect (suggesting the effect is not UHA-specific).
- **Evidence metric:** Δχ² primary; Bayes factor confirmatory. Per-survey contribution decomposition required for the results deposit.
- **Provenance metric:** every coordinate transform applied during TA.2 must carry a provenance record (frame, epoch, transform-type, software-version) traceable end-to-end.

### 6.3 Threshold-to-venue routing (cite Z0 §6)

Per Z0 §6 evidence-class thresholds. Track A is a methods/empirical test; routing follows the conservative-of-two rule per Z0 §6. If Δχ² >= 49 (~7σ improvement OR ~7σ degradation), per `feedback_zenodo_propagation_policy.md` ceiling-diversion rule, the result may warrant a separate cosmology-claim deposit rather than a Track A results deposit.

## 7. Termination criteria (kill switches; Track A; locked)

### Kill-switch interpretation preamble

Inherited from Z0 §7 verbatim (auditable decision rules, observable trigger / defined action / traceable effect; conservative interpretation under ambiguity).

### Track A primary switches

| ID | Trigger | Action |
|---|---|---|
| TA.K0 | Required frame / epoch / provenance metadata not recoverable for a dataset or source class | Mark that source not UHA-wrap-ready; partial coverage; **mark-and-continue (does not halt whole track)**; gap logged for Z4 forensic audit |
| TA.K1 | Z1 encoder dependency fails, OR Track A cannot preserve required provenance through the analysis pipeline | Halt TA.2–TA.6; cascade to Z3 (Track B depends on TA encoder application); deposit narrow methods note (Z0 §9 Stage 1 within 14 days); do not deposit positive Track A result |
| TA.K2 | UHA coordinate provenance produces no measurable cross-survey tightening (Δχ² improvement below noise threshold) | Publish null or narrow-method result; deposit Z5.A as null per Z0 §10; do not claim positive Track A |
| TA.K3 | Coordinate effect too small to matter under published uncertainty bounds, OR required coordinate perturbation exceeds published bounds / requires undocumented assumptions | Halt coordinate-effect explanation branch; reframe Track A as scope-narrowed exploratory result |
| TA.K4 | Provenance effect disappears under controls (dataset-label permutation, provenance-disabled rerun, random-substitution) | Stop positive Track A claim; route to null or diagnostic result; deposit Z5.A as null |
| **TA.K5 (optional)** | Locked Δχ² + BF evidence threshold not met (insufficient evidence for either H0-TA or H1-TA) | Route to modest/null venue per Z0 thresholds; deposit Z5.A with evidence-class verdict |

If exactly K0–K4 required, K5 merges into K2 or K4: K2 broadened to "no measurable cross-survey tightening OR evidence threshold not met"; K4 broadened to "effect disappears under controls OR evidence threshold not met."

### Cross-track propagation (per Z0 §7)

| Switch fires (Track A) | Effect on other tracks |
|---|---|
| TA.K0 (some source class metadata not recoverable) | Z4 forensic audit logs the gap; Z3 (Track B) Phase TB.1 must mark inheritance |
| TA.K1 (Z1 encoder dependency fails OR provenance-preservation fails) | Z3 (Track B) Phase 2+ halt; cosmology-tension claims cannot proceed (encoding/provenance untrustworthy); Z1 results-deposit (Z5.0) referenced for cause |
| TA.K2 (no measurable tightening) | Z3 may still proceed independently if Ωm-baseline test does not depend on Track A's provenance result |
| TA.K3 (coordinate effect too small) | Z3 informed; the Ωm-baseline test path remains available |
| TA.K4 (effect disappears under controls) | Z3 informed; positive Track A claim withdrawn before Z3 mint if pending |

## 8. Always-active circuit-breakers (cite Z0 §8)

Per Z0 §8 in full. Repeating the umbrella circuit-breakers for child-deposit independence:

- **Pre-registration deposit DOIs must exist before any analysis runs.** Track A compute fires only after (a) Z0 umbrella DOI `10.5281/zenodo.19881689` is recorded, (b) Z1 Track 0 DOI `10.5281/zenodo.19904395` is recorded, AND (c) this Z2 DOI is recorded.
- **Print + cool + GATE:OPEN required before any Zenodo deposit** (per `feedback_zenodo_publish_gate.md`).
- **Marketing-language audit** before any deposit.

## 9. Failure-publication commitment (cite Z0 §9)

Per Z0 §9 in full (two-stage). Track A inherits the Stage 1 (within 14 days) + Stage 2 (when packaging complete) commitment unchanged.

## 10. Deposit chain (Track A position)

Per Z0 §10:

| ID | Title | Status |
|---|---|---|
| Z0 | Umbrella | Deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` |
| Z1 | Track 0 PNT overlay pre-registration | Deposited 2026-04-29 at DOI `10.5281/zenodo.19904395` |
| **Z2** | **Track A coordinate-provenance pre-registration** | **This document; pending GATE:OPEN + mint** |
| Z3 | Track B Ωm baseline pre-registration | To draft after Z2 deposit |
| Z4 | Forensic audit results (post Phase TA.0 + TB.1) | Results-shaped; to draft after Z2/Z3 phases run |
| Z5.0 | Track 0 results deposit | To draft after Track 0 completes |
| Z5.A | Track A results deposit | To draft after Track A completes (this Z2's results-deposit child) |
| Z5.B | Track B results deposit | To draft after Track B completes |

## 11. Non-publication parallel work (cite Z0 §11)

Per Z0 §11. Z2 deposit does not gate the parallel workstreams listed in Z0 §11.

## 12. Naming convention (cite Z0 §12)

Per Z0 §12. Track A commit prefix: `[TA-PhaseN]`. Z2 child Zenodo title: `UHA-EB-2026-TA-Z2-coordinate-provenance-v{ver}`.

## 13. Version history

- **v1.0 timestamped 2026-04-29T21-21-00-0700 (this draft):** first draft. Track A child of Z0 umbrella v1.2-hybrid (deposited 2026-04-29) and Z1 (deposited 2026-04-29). Locks Track A hypotheses (H0-TA / H1-TA), source-class manifest (§3 + §3.1 data representation), program phases (§4, TA.0–TA.7), evidence endpoints (§6.1–§6.2), kill switches K0–K4 (optional K5) + cross-track propagation, failure-publication inheritance from Z0 §9, and propagation policy from `feedback_zenodo_propagation_policy.md`. Pre-canonical (timestamped, no commit hash); cleared for hash-bookkeeping commit cycle and Zenodo mint after sanity-pass + gate. Note: §3.1 data-representation lock is one staged change since Z1 mint; below the count gate threshold of >=2; description-changelog will accumulate per propagation policy.

- **Sanity-pass tightening 2026-04-29T22:23 PDT (pre-canonical, no version bump):** five edits applied — (a) literature engagement in §1.4 (Brout 2021, Casertano/H0DN 2026, Macri 2006); (b) TA-G4 Δχ² threshold value locked at >=9 (~3σ) in §6.2; (c) self-reference table "Pending bookkeeping" line lists staged structural changes per propagation policy; (d) §13 version history records this sanity-pass cycle (this entry); (e) §6.2 Pass rule clarifying parenthetical "in the same fitted parameter space and likelihood definition" added per Copilot cross-check audit. Forward-applicable EB layer ontology (`project_eb_layer_ontology.md`) and agency hull doctrine (`project_agency_hull_doctrine.md`) acknowledged as staged structural changes for next-mint cycle but not back-fixed into Z2 vocabulary. PDF regenerated with DejaVu Sans Mono monofont for Unicode glyph integrity in code blocks; Greater-equal (U+2265) and approximately-equal (U+2248) replaced with ASCII >= and ~ in source for renderer-agnostic stability.

## 14. Final attestation

I, Eric D. Martin, ORCID 0009-0006-5944-1742, Independent researcher, certify that:

- This pre-registration is locked at v1.0 final when deposited and will not be modified post-deposit. Amendments follow the propagation policy in `feedback_zenodo_propagation_policy.md` (description-changelog accumulation; mint when count + significance gates both trip).
- The non-claims in §5 are commitments that will not be quietly dropped.
- The kill switches K0–K4 (optional K5) in §7 and the cross-track propagation rules are commitments that will be honored on firing.
- The two-stage failure-publication commitment from Z0 §9 will be honored.
- Disclosure-timing self-review completed by author.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md`.

---

## Appendix A — Drafting note

This Z2 v1.0 draft was authored 2026-04-29T21-21 PDT immediately after Z1 deposit and after the propagation-policy + scope-risk rules were locked in session 63806bef. The draft inherits Z0's structural commitments and Z1's encoder lock, and adds the Track A specifics: cross-survey-consistency hypothesis, frame + dataset source classes, Phase TA.0–TA.7 chain (zero-indexed per source protocol), and Track-A-specific kill switches.

The corrected hypothesis (H0-TA / H1-TA) frames Track A as a coordinate-provenance test, not as round-trip preservation (which is Z1 territory). Authoring note: the original template-fill guess used round-trip language inherited from Z1; this was caught and corrected before draft commit per Eric's 2026-04-29 21:19 PDT correction.

The draft is pre-canonical: filename uses a timestamp, not a commit hash. Per `feedback_artifact_hash_naming.md`, the draft cannot be canonical until committed to the hubble-tensor repository and renamed with the resulting commit hash.

No analysis runs may begin under Track A until (a) Z0 deposit DOI is recorded (true: `10.5281/zenodo.19881689`), (b) Z1 deposit DOI is recorded (true: `10.5281/zenodo.19904395`), AND (c) this Z2 deposit DOI exists.

## Appendix B — Source-manifest sha256 block (verbatim, for deposit metadata)

Inherited from Z0 §3 manifest. Track A-specific source-manuscript sha256 to be added at canonicalization commit:

```
[Track A source manuscript sha256]  hubble-tensor/research/UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md
[Track A source manuscript PDF sha256]  hubble-tensor/research/UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.pdf
```

Z0 umbrella content sha256:
```
ebc22922d1277a1c080c0dda4166b031aa0d33d9313530152b713ee520a78957  hubble-tensor/preregistrations/Z0_umbrella_preregistration_v1.2_hybrid_d842691.md
```

Z1 Track 0 content sha256 (canonical at 48ea8f4):
```
[Z1 .md sha256]  hubble-tensor/preregistrations/Z1_track0_pnt_overlay_preregistration_v1.0_48ea8f4.md
[Z1 .pdf sha256]  hubble-tensor/preregistrations/Z1_track0_pnt_overlay_preregistration_v1.0_48ea8f4.pdf
```

Repository commits at pre-registration freeze (to be filled at canonicalization):

- `nu-algebra` HEAD: `[hash]`
- `hubble-tensor` HEAD at this Z2's parent state: `[hash]` (post Z1 cross-link `3f2a346`)

## Appendix C — Data dictionary (Track A primary tables)

(Schema definitions for cross-survey consistency tables, per-survey provenance records, and the per-figure companion CSVs. To be expanded at TA.1 freeze.)

```
Table: cross_survey_consistency
Columns:
  survey_pair_id (str, primary key) — pair of survey-class identifiers (e.g., "SH0ES_x_Planck")
  baseline_chi2 (float, dimensionless) — Δχ² baseline configuration
  uha_chi2 (float, dimensionless) — Δχ² with UHA provenance tracking
  delta_chi2 (float, dimensionless) — uha_chi2 − baseline_chi2; negative = improvement
  control_chi2 (float, dimensionless) — Δχ² with provenance tracking disabled (control)
  random_label_chi2 (float, dimensionless) — Δχ² with random dataset labels (control)
  bayes_factor (float, dimensionless) — log10 BF baseline-vs-UHA
  notes (str) — free-text per-pair notes

Table: per_survey_provenance
Columns:
  survey_id (str, primary key) — survey class identifier
  frame_input (str) — declared source frame (ICRS, J2000, etc.)
  frame_output (str) — UHA-encoded provenance frame
  transform_chain (str) — ordered list of transforms applied
  software_version (str) — software stack and version locked
  source_release (str) — survey public-release identifier
  access_date (str, ISO-8601) — date dataset accessed at TA.0
  access_sha256 (str) — sha256 of accessed dataset file
  provenance_status (enum: COMPLETE | PARTIAL | UNRECOVERABLE) — TA.K0 status
```

(Additional tables to be added at TA.1 freeze.)

---

*End of Z2 Track A pre-registration draft v1.0 timestamped 2026-04-29T21-21-00-0700. Pre-canonical (pending hash bookkeeping). For PDF reader-mode + cool-off mode-shift + GATE:OPEN per `feedback_zenodo_publish_gate.md`, then deposit on Zenodo with DOI cross-linked back into this repository.*
