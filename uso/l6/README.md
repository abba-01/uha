# l6 — Provenance Archive ("trash bin that never empties")

**Role:** Things we read, used, or worked on that are no longer active but must not be deleted. Drops here from l7 when no longer being actively edited or referenced for live work.

**Flow:** desktop → `l7/` (active workspace) → `l6/` (cold archive).

------------------------------

## `_*` sub-directory taxonomy (canary v1.0, derived from `carrier-set/uso/l6/` corpus)

a) **`_conversations/`** — chat / discussion captures (e.g. `conversation_eb_*.uso.md`)

b) **`_handoffs/`** — agent or persona handoff records (e.g. `handoff_identity_classification_cc_v2_*.md`)

c) **`_manuscripts/`** — manuscript snapshots, canon-scrubs, pre-rewrite freezes (e.g. `manuscript_*_canon_scrub_*.md`, `*_pre-rewrite_*.tex`)

d) **`_publications/<venue>/`** — per-venue bundles: returned proofs, editor emails, paperpal/browser views, DOI-claim records. One subdir per venue/manuscript-id (e.g. `_publications/rsos_260797/`, `_publications/mn261117p/`).

e) **`_audits/`** — cold reads, translation audits, validation runs (e.g. `cold_read_validation_*.uso.md`, `translation_audit_*.uso.md`)

f) **`_superseded_ssot/`** — predecessor SSOT versions and errata documents

g) **`_consultations/<engagement>/`** — per-engagement consultation bundles. One subdir per engagement (e.g. `_consultations/sit-g5-binary-carrier/`, `_consultations/unkin-reviewer/`)

h) **`_unclassified/`** — catch-all; mirrors `l7/_unclassified/` convention

**Reserved (create on first use):** `_external_literature/<topic>/` — third-party journal articles, books, and external reference material the author has read and wants archived (e.g. `_external_literature/sh0es/riess_2024_*.pdf`).

------------------------------

## Naming inside each `_*` dir

Date-stamped, lowercase, underscore-separated, descriptive:

```
<topic-or-id>_<short-name>_<YYYY-MM-DD>.<ext>
```

Examples (from corpus):
- `conversation_eb_sh0es_manuscript_2026-04-19.uso.md`
- `manuscript_shoes_six_axiom_reading_canon_scrub_2026-04-21.md`
- `rsos_260797_returned_proof_2026-04-20.pdf`

------------------------------

## How to route

**If it was actively edited in this repo's l7 last week and isn't anymore →** drop to the matching `_*` bin.

**If it's a third-party PDF you read once and want kept →** `_external_literature/<topic>/` (create on first use).

**If it doesn't fit anywhere →** `_unclassified/`. Don't force a fit. The catch-all is honest.

**If it's a venue-specific bundle (proof + editor email + paperpal view) →** group all under `_publications/<venue>/`.

------------------------------

## Status

- **Canary:** this repo (`uha`), 2026-04-29
- **Authority:** corpus pattern in `/scratch/repos/carrier-set/uso/l6/` (the files that survived v1.0 testing-phase chaos)
- **Propagation:** held until Eric's green light. On green: copy this README and the `_*` skeleton to all USO-bearing repos.
- **SSOT cross-ref:** also documented in memory `project_uso_v2.2.0.md` (l6 underscore taxonomy section).
