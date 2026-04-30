# Z-Track — Workflow Snapshot

**The stable overall look at the Z-track program.** Open this file any time to see where we stand. Updated as gates fire.

**Last updated:** 2026-04-29 (Z2 GATE:OPEN fired 22:41 PDT; minted Zenodo DOI 10.5281/zenodo.19908184; concept DOI 10.5281/zenodo.19908183; canonical at hubble-tensor commit e6d8f9f / cross-link commit 38502cd. Earlier same day: Z1 GATE:OPEN at 19:33 PDT minted DOI 10.5281/zenodo.19904395)

------------------------------

## What is the Z-track?

The Z-track is the chain of pre-registration deposits + results deposits that gate the UHA + EB-carrier research program. Each Z is a Zenodo deposit. Pre-registrations lock hypotheses BEFORE analysis. Results follow.

**Print + cool + GATE:OPEN required before each Zenodo deposit** (per `feedback_zenodo_publish_gate.md`).

------------------------------

## Chain status

| ID | Title | Status | DOI / commit |
|---|---|---|---|
| **Z0** | Umbrella pre-registration | 🟢 **DEPOSITED 2026-04-29** | `10.5281/zenodo.19881689` (concept `19881688`); commit `d842691` (canonical, hubble-tensor) |
| **Z1** | Track 0 — UHA Space-Frame / PNT overlay | 🟢 **DEPOSITED 2026-04-29** | `10.5281/zenodo.19904395` (concept `19904394`); commit `48ea8f4` / cross-link `3f2a346` (canonical, hubble-tensor) |
| **Z2** | Track A — UHA coordinate provenance / cross-survey consistency | 🟢 **DEPOSITED 2026-04-29** | `10.5281/zenodo.19908184` (concept `19908183`); commit `e6d8f9f` / cross-link `38502cd` (canonical, hubble-tensor) |
| **Z3** | Track B — Ω_m baseline | 🟡 **NEXT TO DRAFT** | source: `hubble-tensor/research/Omega_M_Baseline_Unification_Experiment_*` |
| **Z4** | Forensic audit results (post Phase A0 + B1) | ⬜ to draft after Z2/Z3 phases run | — |
| **Z5.0** | Track 0 results deposit | ⬜ after Track 0 phases complete | — |
| **Z5.A** | Track A results deposit | ⬜ after Track A phases complete | — |
| **Z5.B** | Track B results deposit | ⬜ after Track B phases complete | — |

------------------------------

## What's in this directory

******************************

```
drafts/z-track/
└── README.md      ← this file (workflow snapshot)

(Z1 working files moved to canonical location at hubble-tensor/preregistrations/
on GATE:OPEN; pre-canonical timestamped predecessors archived at
uha/uso/l6/_manuscripts/preregistrations/ for provenance.)
```

******************************

------------------------------

## Next gate

**Z1: DEPOSITED.** All nine GATE:OPEN steps completed 2026-04-29 19:33–19:39 PDT:

1. ✅ Moved Z1 .md/.pdf → `hubble-tensor/preregistrations/`
2. ✅ Bootstrap commit `48ea8f4`
3. ✅ Renamed files with bootstrap hash per `feedback_artifact_hash_naming.md`
4. ✅ Injected self-ref hash + Z0-DOI parent fields inside doc
5. ✅ Regenerated PDF with hash-name; second commit `fc293be`
6. ✅ Minted Zenodo: DOI `10.5281/zenodo.19904395`, concept `10.5281/zenodo.19904394` (child of Z0 concept `19881688`)
7. ✅ Cross-link DOI commit `3f2a346`
8. ✅ Pre-canonical timestamped predecessor archived at `uha/uso/l6/_manuscripts/preregistrations/`
9. ✅ This README updated; Z1 flipped to 🟢; Z2 marked NEXT

**Next gate: Z2 (Track A — coordinate framework)** — source manuscripts are in `hubble-tensor/research/UHA_Coordinate_Framework_Experiment_*`. Apply the sanity-pass routine (below) before GATE:OPEN.

------------------------------

## Parallel work (not Z-track but related)

- **EB-Gravity Inversion** (discovery 2026-04-29) — `../eb-gravity-inversion/README.md` — image-mode discovery of EB b-rail gravity propagation + UHA dual-witness Earth-hulling framework. Same phenomenology as N/U algebra 2025-09-21. Pre-canonical working draft. May become Z6 or stand-alone deposit pending Eric's direction.

------------------------------

## Where Z-track sits in the framework

The Z-track operationalizes the railing-system discovery (per memory `project_railing_system_discovery.md`) in the UHA / PNT-overlay domain. Z0 umbrella locks the hypothesis-frame and gate machinery; Z1 locks the operational test for whether UHA can wrap public coordinate systems without breaking round-trip representation; Z2 (Track A) and Z3 (Track B) lock the cosmology applications. The chain is structured so no later track inherits encoding-layer errors as cosmology confounds — Z1 is the encoder lock, Z2/Z3 are the science.

The railing-system framing is **structural background**, not deposit content: Z deposits are formally about UHA + N/U-derived-cosmology results, not about the (e,b) carrier-set theorem (which is deposited separately at Zenodo `10.5281/zenodo.19676237` and lives in RSOS-260797). Z-track is the cosmology operationalization; the carrier-set / EB algebra work is its substrate, and the railing-system framing is the genus the substrate instantiates.

------------------------------

## Working-mode notes (for any future session)

- **Pre-canonical vs canonical**: drafts in this directory carry timestamps in their filenames (e.g., `2026-04-29T02-30-00-0700`). Per `feedback_artifact_hash_naming.md`, no artifact is canonical until committed and renamed with the resulting commit hash. The timestamped name is a working anchor, not an authority claim.
- **Sanity-pass tightening vs version bump**: small clarifying edits before deposit (no semantic claim changes — phrasing, control language, kill-switch wording) are recorded in the version history but don't bump the version number. Version bumps are reserved for changes that affect locked claims, hypotheses, thresholds, or termination criteria.
- **PDF font**: STIX Two Text (mainfont) + STIX Two Math (mathfont) — chosen for full Greek + math Unicode coverage. The Latin Modern Roman default lacks χ in some configurations; STIX renders Δχ² cleanly.
- **Symmetry-break rule** (per `feedback_eb_symmetry_break.md`): when a deposit hits an asymmetric situation where public-facing convention has no functor for the actual structure, the deposit language breaks symmetry to match the structure rather than collapsing to convention. Applied here: kill-switch criteria are auditable rules, not descriptive guidelines, even though most pre-registration conventions stay descriptive.

------------------------------

## Cross-references

- **Master roadmap (program-level, IP-side):** `hubble-tensor/patent_filing/UHA_Space_Frame_PNT_Roadmap_v0.5_52606f3.md`
- **Master roadmap (research-side):** `nu-algebra/docs/ROADMAP_2026_2027_v0.1_ea08f59.md`
- **Z0 canonical:** `hubble-tensor/preregistrations/Z0_umbrella_preregistration_v1.2_hybrid_d842691.md`
- **Forward queue (what comes after Z-cycle clears):** memory `project_post_z0_queue.md`
- **Gate rules:** memory `feedback_zenodo_publish_gate.md`, `feedback_submission_print_gate.md`
- **Hash-naming rule:** memory `feedback_artifact_hash_naming.md`

------------------------------

## Sanity-pass routine

**Purpose:** Catch overclaim, contradiction, and convention-fold before any pre-registration deposit. Run after the draft is structurally complete and PDF has been rendered, but before GATE:OPEN. First applied to Z1 v1.0 on 2026-04-29.

**When to run:**
- Before the first GATE:OPEN on any Z deposit
- After any subsequent tightening, before reprint + cool + GATE:OPEN

**Checklist — "what looks solid" (verify present, no action needed if all green):**
1. Parent (umbrella) DOI is included for child deposits
2. Timestamped versioning is present in filename until canonical commit-hash naming applies
3. Artifact-hash-naming policy text is preserved (`feedback_artifact_hash_naming.md`)
4. No external-consultation language for hypothesis modification post-deposit
5. Disclosure-restriction language is neutral and time-only-not-content
6. AI-use language is bounded (no co-authorship, no endorsement, no proof-of-validity, no data-source role)
7. Hypotheses are explicit, locked, separated from non-claims
8. Kill switches are clear (auditable rules with observable trigger / defined action / traceable effect)
9. "No analysis before DOI" rule is preserved
10. Marketing-language banned-list returns no matches

**Things to tighten before deposit (if found):**
- **Benchmark-gain definition** — axis-only gain must not allow degradation on other axes; provenance-only gain requires explicit non-degradation lock on memory and throughput
- **Cascade-threshold rules** — per-class vs whole-track effects of single vs multi-class kill-switch fires must be unambiguous
- **Controls wording** — precise pass/fail per control type (geometric round-trip vs provenance-completeness vs benchmark stand-in)
- **Editorial sentences** — sentences that don't carry adjudication weight should be cut (e.g., "exceptional outcome unlikely" venue-routing prose)
- **K0 / primary-success interaction** — partial-coverage continuation under K0 must explicitly preclude full-manifest primary success claims

**Patch policy:**
- Tightening edits that DO NOT change locked claims/hypotheses/thresholds/termination-criteria are recorded in version history but DO NOT bump the version number
- Each tightening entry in version history records: timestamp, sections affected, one-line summary per change
- Reprint after each tightening cycle is required; the prior printout is stale

**Output sequence after sanity-pass:**
1. Apply edits to `.md`
2. Append entry to version history bullet
3. Regenerate PDF: `pandoc <file>.md -o <file>.pdf --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=11pt -V mainfont="STIX Two Text" -V mathfont="STIX Two Math"`
4. Print to default printer: `lp <file>.pdf`
5. Cool-off (mode-shift substance per `feedback_zenodo_publish_gate.md`)
6. Read hardcopy
7. `DONEREAD` signal — state becomes STOP until handwritten notes uploaded OR explicit bypass per `magic_words.md`
8. `GATE:OPEN <Z-id>` to proceed to commit + Zenodo mint

Applied 2026-04-29: 16:24 PDT first-pass tightening (4 edits); 16:42 PDT continuation (1 edit, K0/primary-success interaction). PDFs regenerated and reprinted at each cycle.

------------------------------

## Recent edits log (this directory)

- **2026-04-29T16:24 PDT — Z1 sanity-pass tightening** (no version bump; pre-canonical preserved). Four edits applied:
  - §1.1 Improvement: provenance-field-gain non-degradation lock added (provenance-only gain counts only if memory + throughput don't worsen)
  - §1.1 Controls: softened to allow geometric round-trip pass while requiring provenance-completeness failure
  - §6.3: removed "exceptional unlikely" editorial sentence; routing language tightened to methods/operational + conservative-of-two only
  - §7 K1 row: cascade threshold clarified — single K1 invalidates source-class claim only; more than one K1 invalidates the general Track 0 wrapper claim and triggers halt + cross-track cascade

  PDF regenerated 16:25 PDT (STIX Two Text font; 65170 bytes). Print job 167 to Xerox_Phaser_3260.

- **2026-04-29T16:42 PDT — Z1 sanity-pass continuation** (no version bump; pre-canonical preserved). One edit applied:
  - §7 K0/primary-success interaction: clarification paragraph added — K0 fire on any source class allows partial-coverage continuation but precludes full-manifest primary success claims under §6.1 (which requires every locked source class in §3 to pass)

  PDF regenerated 16:42 PDT (66117 bytes). Print job 168 to Xerox_Phaser_3260 (supersedes job 167).

- **2026-04-29T19:33 PDT — Z1 GATE:OPEN fired**. Cool-off elapsed ~2.75h (well past 30-min floor). All nine gate steps completed by 19:39 PDT:
  - Files moved from this working directory to `hubble-tensor/preregistrations/`
  - Three commits in hubble-tensor: bootstrap `48ea8f4`, canonical-hash + internals `fc293be`, DOI cross-link `3f2a346`
  - Files renamed under artifact-hash-naming policy: `Z1_track0_pnt_overlay_preregistration_v1.0_48ea8f4.md` (and .pdf)
  - Zenodo deposit minted: DOI `10.5281/zenodo.19904395`, concept DOI `10.5281/zenodo.19904394`, record at https://zenodo.org/records/19904395 (child of Z0 concept `10.5281/zenodo.19881688`)
  - Pre-canonical timestamped predecessor archived at `uha/uso/l6/_manuscripts/preregistrations/`
  - This README flipped Z1 to 🟢; Z2 marked NEXT

------------------------------

## How to use this README

**Eric:** open it when you want to know "where are we." Don't read the pre-reg files unless you're about to GATE:OPEN. This README is the project's stable overall look.

**Mae:** update the table on every gate event (mint, draft, supersede). Date the "Last updated" line at top. Treat this as the program's HEAD pointer.
