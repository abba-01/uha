# Z1 — Track 0 Pre-Registration: UHA Space-Frame / PNT Overlay

**Status:** DRAFT v1.0 — not deposited. Working draft for PDF reader-mode + cool-off mode-shift + GATE:OPEN per `feedback_zenodo_publish_gate.md` calibration of 2026-04-29 (cool-off is mode-shift substance; PDF satisfies print).

**Working draft note:** This Z1 is a child of the Z0 umbrella pre-registration deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19881689` (concept DOI `10.5281/zenodo.19881688`; record https://zenodo.org/records/19881689). It deposits Track 0 of the three-track UHA + EB carrier program: UHA as a non-replacing overlay layer for public ephemerides, state-vector representations, telemetry products, and space-situational-awareness (SSA) workflows. It inherits Z0's hypothesis-lock structure, evidence-class thresholds, kill-switch interpretation preamble, two-stage failure-publication commitment, and deposit chain. It adds the Track 0 specifics: H0-T0 / H1-T0 hypotheses, locked public-data source classes, the T0.1–T0.7 phase chain, and the K0–K4 termination criteria with cross-track propagation.

| Self-reference field | Value |
|---|---|
| Version | v1.0 timestamped `2026-04-29T02-30-00-0700` |
| Parent (umbrella) | Z0 v1.2-hybrid at hubble-tensor commit `d842691`; deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` |
| Working filename | `Z1_track0_pnt_overlay_preregistration_v1.0_timestamped_2026-04-29T02-30-00-0700.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |
| Pending bookkeeping | This working draft is not canonical until committed and renamed with the resulting commit hash under the artifact-hash-naming policy. |

**Standing artifact-hash-naming policy (locked, propagating, inherited from Z0):** Every artifact in this research program carries its commit hash both inside the document AND in the filename. No hash, no canonical status. No exceptions. This document inherits the policy from Z0 and propagates it: every Track 0 artifact derived from, citing, or extending this Z1 inherits the same rule. Per `feedback_artifact_hash_naming.md`.

---

## Zenodo metadata block (deposit-ready)

| Field | Value |
|---|---|
| Title | Track 0 Pre-Registration: UHA Space-Frame / PNT Overlay |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint |
| Communities | (TBD — Zenodo community selection at deposit time; may be skipped per Z0 deposit pattern) |
| Keywords | UHA, Universal Horizon Address, PNT, space-frame overlay, SPICE, Astropy, TLE, JPL, Gaia, ephemeris, state vector, SSA, situational awareness, proximity query, encode/decode round-trip, public-data, pre-registration, falsification, kill switch |
| Related identifiers (is part of) | `10.5281/zenodo.19881689` (Z0 umbrella v1.2-hybrid, deposited 2026-04-29) |
| Related identifiers (cites) | `10.5281/zenodo.19676237` (priority hash deposit, RSOS-260797 r1 priority lock); RSOS-260797 r4 (under review, EB carrier characterization theorem); US 63/902,536 (UHA provisional patent) |

---

## 1. Purpose

This deposit pre-registers Track 0 of the three-track UHA + EB carrier program: testing whether UHA can operate as a non-replacing overlay layer for public ephemerides, state-vector representations, telemetry products, and space-situational-awareness (SSA) workflows.

Track 0 does not test cosmology. It tests whether the encoding layer is sound enough that downstream cosmological tests (Tracks A and B) can rely on it without inheriting encoding errors as confounds.

Track 0 does not run the cosmological analyses. It locks the encoder, the public-data source classes, the round-trip pass/fail rules, the benchmark posture, the SSA endpoint, and the kill-switch tree, so that subsequent per-track child deposits (Z2, Z3) can use the encoder without post-hoc rescue.

This pre-registration does not claim that UHA is a better orbit dynamics engine. Per Z0 §5 non-claims and v0.5 §5.4 benchmark posture, Track 0 tests UHA as: (a) a compact state-record format; (b) a high-throughput proximity-screening representation; (c) a provenance-carrying telemetry object; (d) a wrapper that preserves source, epoch, frame, units, parameter set, and uncertainty.

### 1.1 Pre-registered hypotheses and decision locks (Track 0)

Inherited from Z0 §1.1 unless narrowed below.

#### Hypotheses (Track 0)

- **H0-T0:** UHA does not encode and decode public state-vector / ephemeris data within documented precision limits without breaking round-trip representation. Equivalently, UHA does not provide measurable benchmark gain (memory, speed, or provenance) on real public vectors, OR UHA produces SSA false negatives under declared bounds.
- **H1-T0:** UHA encodes and decodes public state-vector / ephemeris data within documented precision limits without breaking round-trip representation, AND provides measurable benchmark gain on real public vectors, AND produces zero SSA false negatives under declared bounds.

#### Shared decision definitions

Inherited from Z0 §1.1. Track 0 narrowing:

- **Baseline:** the source coordinate system, software package, or source product as published, without UHA wrapping.
- **Improvement:** UHA wrapping reduces memory footprint, increases proximity-query throughput, OR strengthens provenance fields, relative to baseline, on the same data, without loss on the other axes. Provenance-field gain is treated as benchmark gain only if memory footprint and throughput do not worsen relative to baseline.
- **Primary success:** all four of (G0-2 round-trip pass) AND (G0-3 benchmark gain on real public data) AND (G0-4 zero SSA false negatives) AND (G0-5 overlay posture confirmed) hold simultaneously on the locked source-class manifest in §3.
- **Analysis start:** the first execution of the locked encoder pipeline after this Z1 DOI is deposited and recorded.
- **Same-pipeline rule:** the same encoder/decoder is used across source classes; per-source adapters are documented before analysis start.
- **Controls:** controls include rerunning round-trip with provenance fields disabled (provenance-disabled controls may pass geometric round-trip but must fail provenance-completeness checks) and substituting random data on benchmark step (must NOT pass G0-3). Controls may diagnose robustness; they may not redefine primary success.

#### Data handling locks

Inherited from Z0 §1.1 in full.

### 1.2 What would render Track 0 unsupported

Track 0 will be considered unsupported if any of the following occur: source metadata is not recoverable for the locked source classes in §3 (K0); UHA encode/decode round-trip exceeds documented precision (K1); UHA produces no measurable benchmark gain on real public data (K2); UHA produces any SSA false negative under declared bound (K3); or the wrapper requires a replacement-first posture incompatible with the §1 overlay claim (K4). In such cases Track 0 halts and a negative or narrow-method result is deposited under the failure-publication rule (Z0 §9, two-stage). This paragraph does not replace the termination-criteria tables in §7; it summarises them in plain language.

### 1.3 Public-data-first scope

Per Z0 §1.3. Track 0 hypothesis-adjudicating analyses use only the publicly available source classes listed in §3 below. Dataset versions, release dates, and access dates will be recorded at analysis start. Any later public-data release requires a separate preregistered update before use in hypothesis-adjudicating analysis.

### 1.4 Evidence framework

Per Z0 §1.4. Δχ² primary; Bayes factor confirmatory. AIC/BIC may appear in supporting analyses but are not gating thresholds. For Track 0, the round-trip and SSA gates are pass/fail, not likelihood-class; the benchmark gate (G0-3) is reported as a measured quantity (memory bytes per record; queries per second; provenance fields per record) compared against baseline. The Z0 §6 evidence-class table maps the benchmark-magnitude tiers to venue routing.

## 2. Authorship and authority

- Sole author: Eric D. Martin / ORCID 0009-0006-5944-1742 / Independent researcher
- No Co-Authored-By AI. No AI in bibliography as author.
- Disclosure-timing self-review completed by author.
- No external consultation will be used to modify hypotheses, models, thresholds, interpretation rules, or termination criteria after deposit. Any change after deposit requires a new DOI amendment.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md` — drafting support, formatting, and consistency checks. They were not used as authors, data sources, evidence, proof of validity, endorsement, or co-authorship.

## 3. Canonical source documents and locked public-data source classes

Track 0 inherits Z0 §3 source-document manifest (Z0 umbrella roadmap v0.5 at hubble-tensor `52606f3`; CHECKLIST at `ea08f59`; ROADMAP at `ea08f59`; Z0 umbrella v1.2-hybrid at `d842691`).

Locked Track 0 public-data source classes (per v0.5 §5.3, license-compliant per v0.5 §P-9):

| Source class | Public path | UHA use |
|---|---|---|
| SPICE example kernels | NAIF sample kernels (public, redistributable) | State-vector encoding and provenance |
| Astropy ephemerides | Astropy / JPL ephemeris path (public, redistributable) | Frame-transform comparison |
| Public TLEs | Permitted public satellite catalogs (per v0.5 §P-9 license lock) | SSA / conjunction screening |
| Gaia sample | Gaia astrometric products (public DR releases) | Celestial-coordinate wrapping |
| JPL Horizons states | Solar-system body state vectors (public via Horizons web/API) | Ephemeris-provenance test |
| HST/MAST metadata | HST observation/orbit/pointing metadata (public via MAST) | Frame-stack audit target |
| Mission docs (Planck/Gaia/JWST) | Public navigation/orbit products | Deep-space / L2 audit target |

Source datasets, versions, release dates, and access dates will be recorded at analysis start (cite §1.3 lock).

## 4. Track 0 program structure

Per Z0 §4 + v0.5 §5:

| Phase | Name | Output |
|---|---|---|
| T0.1 | Source audit | Confirm metadata recoverability per source class (G0-1 / K0 gate); per-source manifest with sha256 |
| T0.2 | Encoder build | Locked UHA encoder/decoder for the source classes in §3; commit hash recorded at lock |
| T0.3 | Round-trip test | Encode-then-decode each source class; verify within documented precision (G0-2 / K1 gate) |
| T0.4 | Benchmark | Compare memory / speed / provenance on real public vectors vs baseline (G0-3 / K2 gate) |
| T0.5 | SSA demo | Proximity-query screen with declared uncertainty bound; verify zero false negatives (G0-4 / K3 gate) |
| T0.6 | Overlay posture verification | Confirm wrapper composes with existing tools without replacement-first posture (G0-5 / K4 gate) |
| T0.7 | Z5.0 results deposit | Per Z0 §10; positive, negative, or null per evidence threshold |

## 5. Non-claims (Track 0; cite Z0 §5)

Per Z0 §5. Track 0 specifically does NOT assert:

1. UHA is a better orbit dynamics engine.
2. UHA replaces SPICE, GPS, DSN, Astropy, or WCS.
3. UHA independently measures positions; it encodes / fingerprints / compares / audits.
4. UHA eliminates ephemeris uncertainty; it carries the uncertainty fields.
5. The Track 0 round-trip pass result transfers automatically to cosmological tracks (Z2, Z3 must validate the encoder under their own pipelines).
6. The benchmark gain on one source class transfers to other source classes; benchmark is reported per source class.
7. The SSA-safety result transfers to operational SSA workflows; this is a public-data demo, not a deployed system.

## 6. Evidence-class thresholds (cite Z0 §6) and Track 0 endpoints

### 6.1 Track 0 primary endpoint (locked)

Per Z0 §6.1:

- **Primary success:** UHA wrapper round-trip success on every locked source class in §3 + benchmark gain on real public data + zero SSA false negatives under declared bound + overlay posture confirmed.
- **Primary failure:** any single round-trip failure outside documented precision, no benchmark gain on real public data, any SSA false negative under declared bound, or replacement-first posture required.

### 6.2 Operational model lock (Track 0)

Per Z0 §6.2 Track 0 sub-section, repeated here for child-deposit independence:

- **Goal:** Test whether UHA can encode and decode real coordinate systems without breaking round-trip representation, with measurable benchmark gain on real public data, and zero SSA false negatives under declared bound.
- **Systems:** ECEF, ECI, WGS84, SPICE frames, Astropy frames, TLE/JPL/Gaia-derived products where source metadata are recoverable.
- **Pass rule:** encode/decode round-trip error must stay within the precision limits documented by the official documentation for the coordinate system, software package, or source product used.
- **Fail rule:** Track 0 fails if encode/decode mismatch occurs, round-trip error exceeds documented precision limits, the coordinate system cannot be represented, no real-data benchmark gain is observed, or any SSA false negative occurs under the declared bound.
- **Benchmark metric:** memory footprint per state-vector record; proximity-query throughput per second on real public vectors; provenance-field count carried per record. Each metric is reported vs baseline. Gain = better-on-at-least-one-axis-without-loss-on-others.
- **SSA metric:** zero false negatives on the locked test set under the declared uncertainty bound. Any false negative is K3 fire.
- **Overlay posture:** wrapper composes with existing tools; downstream consumers can call source software (SPICE / Astropy / etc.) directly through the wrapper without UHA-specific reconstruction. K4 fires if any source class requires replacement-first integration.

### 6.3 Threshold-to-venue routing (cite Z0 §6)

Per Z0 §6 evidence-class thresholds. Track 0 is a methods/operational test; routing follows the conservative-of-two rule per Z0 §6.

## 7. Termination criteria (kill switches; Track 0; locked)

### Kill-switch interpretation preamble

Inherited from Z0 §7 verbatim:

The termination criteria ("kill switches") in §7 are defined as auditable decision rules, not descriptive guidelines.

Each kill switch is constructed to satisfy three conditions:

1. Observable trigger — the condition that fires the switch must be detectable from the data, model outputs, or documented pipeline behavior.
2. Defined action — each switch specifies a required response (halt, downgrade, reframe, or deposit), with no discretionary override.
3. Traceable effect — each switch has a defined impact on downstream phases or related tracks, including cross-track propagation where specified.

Where ambiguity arises in determining whether a trigger condition is met, the conservative interpretation applies: halt or downgrade rather than extend or reinterpret the claim.

The purpose of this structure is to minimize researcher degrees of freedom and prevent post-hoc rescue of unsupported results. The number of switches reflects coverage across independent failure modes, not an attempt to imply unwarranted precision.

### Track 0 primary switches

| ID | Trigger | Action |
|---|---|---|
| K0 | Source metadata not recoverable for a given source class | Mark not UHA-wrap-ready per source; partial coverage; **mark-and-continue (does not halt whole track)** |
| K1 | UHA encode/decode round-trip failure (exceeds documented precision) for any source class | A single K1 failure invalidates claims for that source class only. More than one K1 failure invalidates the general Track 0 wrapper claim — halt T0.4–T0.7 and cascade to Tracks A, B per Z0 §7. |
| K2 | No real-data benchmark gain (memory, speed, or provenance) on the locked source-class set | Downgrade operational claim; deposit narrow methods note (Z0 §9 Stage 1 within 14 days); do not deposit positive Track 0 result |
| K3 | SSA false negative under declared bound | Stop SSA claim until search rule is corrected; deposit narrow methods note (Z0 §9 Stage 1 within 14 days) |
| K4 | Replacement-first posture required for any source class | Stop overlay claim for that class; if K4 fires on more than one class, halt T0.6–T0.7; deposit revised scope or null |

**K0 / primary-success interaction (clarification):** If K0 fires for any source class, Track 0 may continue over recoverable source classes, but full-manifest primary success cannot be claimed. Primary success per §6.1 requires that every locked source class in §3 pass; partial-coverage continuation under K0 yields a partial-coverage result, not a full-manifest pass.

### Cross-track propagation (per Z0 §7)

| Switch fires (Track 0) | Effect on other tracks |
|---|---|
| T0.K1 (encoder round-trip fails for >1 class) | TA Phase 2–6 halt; TB Phase 2 (UHA Ωm baseline) cannot proceed (encoding layer untrustworthy) |
| T0.K0 (source metadata not recoverable for some class) | TA Phase 0 marks that source partial-coverage; **mark-and-continue, not halt** (does not abort whole track) |

## 8. Always-active circuit-breakers (cite Z0 §8)

Per Z0 §8 in full. Repeating the umbrella circuit-breakers for child-deposit independence:

- **Pre-registration deposit DOIs must exist before any analysis runs.** Track 0 compute fires only after both (a) Z0 umbrella DOI `10.5281/zenodo.19881689` (already recorded) and (b) this Z1 DOI are recorded.
- **Print + cool + GATE:OPEN required before any Zenodo deposit** (per `feedback_zenodo_publish_gate.md` calibration of 2026-04-29: cool-off is mode-shift substance; PDF satisfies print when paper is impractical; mode-shift is the substance).
- **Marketing-language audit** before any deposit: per Z0 §8 banned-language list. Any match in this Z1 (or any Z5.0 results deposit derived from it) is a fail and must be replaced with bounded language before deposit.

## 9. Failure-publication commitment (cite Z0 §9)

Per Z0 §9 in full (two-stage). Track 0 inherits the Stage 1 (within 14 days) + Stage 2 (when packaging complete) commitment unchanged. The KS7 carve-out language in Z0 §9.1 (private-archive / pause-clock when public release is blocked) applies if Track 0 work is ever subject to disclosure restriction.

## 10. Deposit chain (Track 0 position)

Per Z0 §10:

| ID | Title | Status |
|---|---|---|
| Z0 | Umbrella | Deposited 2026-04-29 at DOI `10.5281/zenodo.19881689` (concept `10.5281/zenodo.19881688`) |
| **Z1** | **Track 0 PNT overlay pre-registration** | **This document; pending GATE:OPEN + mint** |
| Z2 | Track A coordinate-framework pre-registration | To draft after Z1 deposit |
| Z3 | Track B Ωm baseline pre-registration | To draft after Z2 deposit |
| Z4 | Forensic audit results (post Phase A0 + B1) | To draft after Z2/Z3 phases run |
| Z5.0 | Track 0 results deposit | To draft after Track 0 completes (positive, negative, or null per evidence threshold) |
| Z5.A | Track A results deposit | To draft after Track A completes |
| Z5.B | Track B results deposit | To draft after Track B completes |

This Z1 cites Z0 (`10.5281/zenodo.19881689`) as `is part of`. If any Z1 phase amendment is needed mid-execution, the amendment is deposited as a new Zenodo DOI before any further analysis runs. The Z5.0 results deposit is the Track 0 result-of-record; null still deposits per Z0 §9.

## 11. Non-publication parallel work (cite Z0 §11)

Per Z0 §11. Z1 deposit does not gate the parallel workstreams listed in Z0 §11 (AMS Memoirs Phase 2; RSOS-260797 r4; MNRAS pipeline; Acta Informatica; Resurgence; patent CIP non-provisional; companion-paper claim-alignment audits).

## 12. Naming convention (cite Z0 §12)

Per Z0 §12. Track 0 commit prefix: `[T0-PhaseN]`. Z1 child Zenodo title: `UHA-EB-2026-T0-Z1-track0-pnt-overlay-v{ver}`.

## 13. Version history

- **v1.0 timestamped 2026-04-29T02-30-00-0700 (this draft):** first draft. Track 0 child of Z0 umbrella v1.2-hybrid (deposited 2026-04-29 at DOI `10.5281/zenodo.19881689`). Locks Track 0 hypotheses (H0-T0 / H1-T0), source-class manifest (§3), program phases (§4, T0.1–T0.7), evidence endpoints (§6.1–§6.2), kill switches K0–K4 + cross-track propagation, and failure-publication inheritance from Z0 §9. Pre-canonical (timestamped, no commit hash); cleared for hash-bookkeeping commit cycle and Zenodo mint after gate.
- **Sanity-pass tightening 2026-04-29T16:24 PDT (pre-deposit, no version bump, pre-canonical):** §1.1 Improvement — added provenance-field gain non-degradation lock (provenance-only gain counts only if memory footprint and throughput do not worsen). §1.1 Controls — softened "must NOT pass G0-2" to allow geometric round-trip pass while requiring provenance-completeness failure. §6.3 — removed "exceptional is unlikely" editorial sentence; routing language tightened to methods/operational + conservative-of-two only. §7 K1 row — clarified cascade threshold: single K1 invalidates source-class claim only; more than one K1 invalidates the general Track 0 wrapper claim and triggers halt + cross-track cascade.
- **Sanity-pass continuation 2026-04-29T16:42 PDT (pre-deposit, no version bump, pre-canonical):** §7 K0 / primary-success interaction — added explicit clarification that K0 fire on any source class allows partial-coverage continuation but precludes full-manifest primary success claims (§6.1 requires every locked source class in §3 to pass).

## 14. Final attestation

I, Eric D. Martin, ORCID 0009-0006-5944-1742, Independent researcher, certify that:

- This pre-registration is locked at v1.0 final when deposited and will not be modified post-deposit. Amendments require a new Zenodo DOI.
- The non-claims in §5 are commitments that will not be quietly dropped.
- The kill switches K0–K4 in §7 and the cross-track propagation rules are commitments that will be honored on firing.
- The two-stage failure-publication commitment from Z0 §9 will be honored: Stage 1 (negative-outcome notice) deposited within 14 days of any kill-switch firing with no extensions; Stage 2 (full technical note) deposited when code/data packaging is complete.
- Disclosure-timing self-review completed by author. Any future disclosure restriction affects release timing only and does not modify the scientific rules locked here.
- AI tools were used as a contradiction-and-audit instrument per `feedback_others_contradict_not_prove.md` — drafting support, formatting, and consistency checks. They were not used as authors, data sources, evidence, proof of validity, endorsement, or co-authorship.

---

## Appendix A — Drafting note

This Z1 v1.0 draft was authored 2026-04-29T02-30 PDT immediately after Z0 v1.2-hybrid was deposited at DOI `10.5281/zenodo.19881689`. The draft inherits Z0's structural commitments (kill-switch interpretation preamble, two-stage failure-publication, evidence-class thresholds, public-data-first scope, AI-use disclosure rule) and adds the Track 0 specifics (H0-T0 / H1-T0 hypotheses, source-class manifest, T0.1–T0.7 phases, kill switches K0–K4).

The draft is pre-canonical: filename uses a timestamp, not a commit hash. Per `feedback_artifact_hash_naming.md`, the draft cannot be canonical until committed to the hubble-tensor repository and renamed with the resulting commit hash.

No analysis runs may begin under Track 0 until both (a) Z0 deposit DOI is recorded (already true: `10.5281/zenodo.19881689`) and (b) this Z1 deposit DOI exists.

## Appendix B — Source-manifest sha256 block (verbatim, for deposit metadata)

Inherited from Z0 §3 manifest:

```
e76fa5f64e494fbcb7d094fec94783640f0ef625bfb8d04b745f8b0ad880ef76  hubble-tensor/patent_filing/UHA_Space_Frame_PNT_Roadmap_v0.5_52606f3.pdf
092c0e1bd9d89a9b2f9652807dd05aa52bc839743fb19ab24088bfce393765a9  hubble-tensor/patent_filing/UHA_Space_Frame_PNT_Roadmap_v0.5_52606f3.md
5423eeadf5b2052dc04ea51279b03be1d65583851ca4aac28d655ea50a295683  hubble-tensor/research/UHA_Coordinate_Framework_Experiment_Complete_v1.0_77b639c.md
3dd711f06b0a757c74a4e350d6b6d424ef979de7d8b981fac66907a44b3f0e59  hubble-tensor/research/Omega_M_Baseline_Unification_Experiment_Complete_v1.0_77b639c.md
9af99cebd92907f6676584847bc3e817ae2e5c8fe7c592de4ac928ada90cef09  nu-algebra/CHECKLIST_v1.0_ea08f59.md
bf4afc3a07e5dc40dcd651eba3511888450f545e4400beeec790fcdb6ce40b48  nu-algebra/docs/ROADMAP_2026_2027_v0.1_ea08f59.md
```

Z0 umbrella content sha256 (the parent of this Z1):

```
ebc22922d1277a1c080c0dda4166b031aa0d33d9313530152b713ee520a78957  hubble-tensor/preregistrations/Z0_umbrella_preregistration_v1.2_hybrid_d842691.md (file content at d842691; deposited DOI 10.5281/zenodo.19881689)
```

Repository commits at pre-registration freeze (bootstrap, per `feedback_artifact_hash_naming.md`):

- `nu-algebra` HEAD: `ea08f59`
- `hubble-tensor` HEAD at this Z1's parent state: `8d39ad2` (post-DOI-cross-link commit of Z0 v1.2-hybrid)

---

*End of Z1 Track 0 pre-registration draft v1.0 timestamped 2026-04-29T02-30-00-0700. Pre-canonical (pending hash bookkeeping). For PDF reader-mode + cool-off mode-shift + GATE:OPEN per `feedback_zenodo_publish_gate.md` calibration of 2026-04-29, then deposit on Zenodo with DOI cross-linked back into this repository.*
