# Z* Cosmopoulous Pre-Registration — Gap Survey

**Date:** 2026-05-04
**Source:** `Z-star_cosmopoulous_preregistration_v0_1_DRAFT.md` (drafted 2026-05-01)
**Reviewer:** Mae (autonomous gap survey using Z3 v0.2 consult lens)
**Trigger:** Z3 v0.2 deposited 2026-05-04 (DOI 10.5281/zenodo.20028303); Eric authorized exploring Z* as the next Z-track candidate.

---

## Read summary

Z* v0.1 is structurally similar to Z3 v0.1 (drafted same day, 2026-05-01) but is theoretically far more ambitious. Z3 was a narrow public-data audit of one mechanism; Z* claims a fundamental cosmological reframe (universe-inside-black-hole). The preregistration discipline that protects Z3 has to work harder for Z* — the higher the theoretical claim, the tighter the scope discipline must be.

**Bottom line:** Z* v0.1 is NOT deposit-ready by Z3 v0.2 standards. The gap list is more substantive than Z3's was. Deposit-ready v0.2 requires either (a) significant additional work to lock predictions and pipelines, or (b) a deliberate scope-narrowing that defers the quantitative claims to child preregistrations.

---

## What's already aligned with Z3 v0.2 standards (do not change)

- Δχ² hierarchy 5/20/49 inherited from Z0 §1.4 (no Z*-local thresholds)
- K-naming canonical (K0-Z* … K4-Z*) — no KS drift to clean up
- Z0 inheritance for §1.1, §1.3, §1.4
- Public-data-first scope (Planck 2018, JWST DR, Pantheon+, DESI, EHT)
- Failure-publication inherits Z0 §9
- Postulate-level extensions (cyclic cosmology, multi-cosmopoulous transit, PP precursor, recursive pair law) explicitly **NOT** pre-registered — good scope discipline already in place
- Three serious-physics anchors named (Pathria 1972, Stuckey 1994, Popławski recent) — defensible literature footing

---

## Must-fix gaps (deposit-blocking)

### G1. TBD predictions are a preregistration loophole

§3 observables include placeholder language:
- §3.1 "specific value computed from horizon parameters (locked at analysis start using Planck 2018 mass-energy budget)"
- §3.2 "Cosmopoulous: z* corresponds to a specific feature of horizon-emission spectrum (TBD by analysis)"
- §3.4 "Cosmopoulous predicts anisotropy in mass-rail observables at specific multipoles (TBD by analysis)"
- §4 "(to be specified at analysis start; placeholders below)" — Pipelines P1–P5 are entirely placeholders

Pre-registration value comes from locking predictions BEFORE analysis. "TBD by analysis" means the predictions are derivable from the framework after seeing the data — exactly what preregistration is supposed to prevent. **This is the central gap.**

**Two paths to close:**

- **Path A (tighten Z* itself):** lock specific quantitative predictions now (T_CMB target value within the 10% band; z* target value within the 5% band; SH0ES/Planck split target values within 0.5 km/s/Mpc; multipole list for §3.4; age-variance multiplier for §3.5). Computational work required.
- **Path B (split into structural + quant Z**):** Deposit Z* as a *structural* preregistration (claims (a)-(f) as structural commitments; §3 observables named but quantitative predictions explicitly deferred). Spawn Z**-quant-CMB, Z**-quant-multipole, Z**-quant-JWST as child preregistrations once predictions are computed. Each child inherits Z*'s structural lock and adds its own quantitative lock.

Path B is honest about current state. Path A is stronger but requires the prediction work first.

### G2. §2 strong-identity language

§2 claims:
> "The cosmological event horizon **is** the cosmopoulous edge"
> "'Expansion' we measure is **horizon-growth**, not metric stretching"
> "Different cosmopoli have **different local c**"
> "**Universe is finite**"
> "**Single Cosmos contains many cosmopoli**"

These are bold structural identifications presented as facts in the preregistration body. Z3 v0.2 learned to soften: "this preregistration treats X as Y" rather than "X is Y." The same softening applies here. Either:
- Recast as "this preregistration treats the cosmological event horizon as the cosmopoulous edge for the purpose of locking H1-Z* predictions"
- Or move the identity claims into a "Theoretical commitments" subsection clearly labeled as preregistered hypotheses, not facts

### G3. No "does not claim X" armor section

Z3 v0.2 §1 has an explicit armor section:
> "Z3 is not a Hubble-tension solution paper"
> "Z3 does not directly challenge the SH0ES distance-ladder calibration"
> "A clean null result is a valid publishable outcome"

Z* v0.1 has fragments of this scattered (1.0 has "Z* does not claim ΛCDM is wrong in its observational fits") but lacks a consolidated armor section. Add one. Candidates:
- "Z* does not claim cosmopoulous-as-black-hole is established physics — it preregisters a falsifiable test of structural predictions"
- "Z* does not claim universal applicability — it locks specific observables where cosmopoulous and ΛCDM are predicted to differ"
- "Z* does not claim cyclic cosmology, multi-cosmopoulous transit, or PP precursor algebra — those are postulate-level extensions in §5"
- "A K-firing is a co-equal publishable outcome"

### G4. No competing-hypothesis section

Z3 v0.2 §5 names competing hypotheses (Z*, distance-ladder systematics, early dark energy, modified gravity, local-volume effects). Reciprocally, Z* should name:
- ΛCDM with standard parameters (the null reference, already named)
- Z3-style cross-survey baseline systematics
- Early dark energy / modified gravity (alternative new-physics)
- Local-volume effects
- Non-standard inflationary scenarios

A K-firing for Z* (cosmopoulous null) is consistent with multiple alternatives. State that.

### G5. Cross-protocol cascade unspecified

Z* v0.1 says it "sits parallel to the linear Z0–Z5 chain." But it doesn't specify the cascade rules:
- If Z* K-fires (cosmopoulous null), does Z3 halt? **No** — Z3 tests a different mechanism. State this explicitly.
- If Z3 K-fires (Ωm-baseline null), does Z* halt? **No** — Z* tests a different mechanism.
- If carrier-set theorem (RSOS-260797 r4) is rejected, does Z* halt? **Yes (probably)** — Z* depends on the carrier-set theorem as a load-bearing input.

Add a §2-equivalent cross-protocol coordination block.

### G6. No EB three-outcome primitive table

Z3 v0.2 §3.3 has the EB three-outcome table (agreement / disagreement / audit-failed). Z* uses (e,b) algebra throughout (witness-loss, B-flip, e-rail/b-rail) but never lays out the primitive operationally. Add the table — even just for completeness, since Z* observables in §3 implicitly use (e,b) decomposition.

### G7. Self-reference table needs hash-naming conformance at deposit

Same as Z3 v0.1: "Working filename" + "Pending bookkeeping" rows are pre-canonical placeholders. At deposit, replace with: Canonical filename (with hash), Bootstrap commit hash, Hash-injection commit, Zenodo DOI, Status. Mirrors the Z3 v0.2 procedure.

### G8. §3.4 mirror-counter-rotation needs κ specification or pipeline lock

§3.4 claims BOSS/DESI mass-rail correlation tensors should show anisotropy at specific multipoles "TBD by analysis." Cross-survey correlation observables (BOSS × DESI) require A3-style κ coupling locks (mechanism-justified off-diagonals) to avoid post-result tuning. Either lock the multipole list and κ now, or defer to a child Z**-quant-multipole preregistration.

---

## Should-fix gaps (improve before deposit if Path A is chosen)

### G9. Marketing-language audit not yet run

Z3 v0.2 pre-deposit checklist greps for: "revolutionary", "Nobel", "100% explained", "completely solves", "definitively", "groundbreaking", "paradigm shift", "Einstein-level", "textbook-level", "resolution", "solves the Hubble tension". Z* v0.1 contains:
- "strong cosmopoulous evidence" (§3.4) — not in the banned list but uses "strong" as adjudicative word, replace with the Δχ² class language
- "**Universe is finite**" / "**Single Cosmos contains many cosmopoli**" (§2.1) — bold typography signals importance; consider whether the body of an evidence-locked preregistration should typographically emphasize unproven claims
- §3.5 "too mature" galaxies — folksy, replace with quantified standard

Run the full grep before deposit.

### G10. §3.6 Bayes-factor narrowing parity with Z3

Z3 v0.2 §1.4 narrows Z0's BF>1 support rule to BF>3 for Track B adjudication. Z* v0.1 doesn't address Bayes factors at all. If §3 observables will be evaluated with Bayesian model comparison vs ΛCDM (which is the natural framing), pick the BF threshold and lock it now.

### G11. §3.3 (Hubble tension as horizon-growth) overlaps with Z3 mechanism territory

§3.3 predicts SH0ES and Planck H0 differ because of horizon-growth, with quantitative targets (73.04 and 67.40 within 0.5 km/s/Mpc). This overlaps with Z3's target. State the relationship explicitly:
- Z3 attributes the residual to Ωm-baseline disagreement
- Z* attributes the residual to horizon-growth structure
- They are *competing* mechanisms — both could pass observationally, both could fail; observation alone may not distinguish them

If both Z3 and Z* mature to results, expect a third-arbitration document.

### G12. Speed-of-light claim (1f) lacks a distinguishing observable

Structural claim §1.1.H1.(f) — "locally-finite c" — is preregistered as a structural commitment but no §3 observable distinguishes locally-finite-c from universal-c. Either lock such an observable (substrate-level information transit signature?) or move (f) to §5 postulate-level extensions.

---

## Style / rhetoric

### S1. Title preserves "Cosmopoulous Cosmological Model" — fine for indexing

The title "Z* Pre-Registration: Cosmopoulous Cosmological Model" is descriptive and not market-y. Keep.

### S2. Decision-rule language

Z3 v0.2 uses "common-baseline audit" / "baseline substitution" in decision rules even though title preserves "unification." For Z*, the equivalent move is to use "cosmopoulous-as-black-hole structural test" or "horizon-emission predictions test" in decision rules, and reserve "cosmopoulous cosmological model" for indexing/title.

### S3. Provenance section references files that need fixed paths at deposit

§8 references `carrier_state_rail_theory_v0_2.md`, `project_railing_system_discovery.md`, `compile_carrier_set_identity_2026-05-01_v3.md` — these are local-only file references that won't be useful to readers. At deposit, either replace with public-record citations (Zenodo DOIs once those manuscripts deposit) or include the file content as supplementary material.

---

## Recommendation

**Recommend Path B (structural Z* + child quant preregistrations).**

Reasons:
1. Path A requires significant computational work before deposit (T_CMB derivation, z* derivation, horizon-growth function, multipole prediction, age-variance prediction). That work is itself research, not preregistration.
2. Eric is doing his Master's in Psychology in parallel; the cognitive load to lock all five quantitative predictions is non-trivial.
3. Pre-registration value is preserved by Path B: structural claims are locked now, quantitative claims are locked when each prediction is computed but BEFORE the data is queried.
4. Path B mirrors how Z0 (umbrella) → Z1/Z2/Z3 (track-specific) staged. Z* (structural) → Z**-quant-CMB / Z**-quant-multipole / etc. follows the same pattern.

**Path B v0.2 patch list:**

1. (G1) Add §3 narrative explaining that quantitative predictions are deferred to child Z** preregistrations; lock the structural claims (a)-(f) and the *fact* that observable Pi will be computed; do NOT lock specific values.
2. (G2) Soften §2 strong-identity language to "this preregistration treats X as Y" form
3. (G3) Add §1 armor section with three "does not claim" sentences
4. (G4) Add §5 (renumber existing §5 to §5b) competing-hypothesis section naming Z3, EDE, MoG, local-volume, non-standard inflation
5. (G5) Add §2 cross-protocol coordination block (Z* null does not halt Z0-Z3; carrier-set theorem rejection halts Z*)
6. (G6) Add §3.x EB three-outcome primitive table for completeness
7. (G7) Defer to deposit-time hash injection (mirrors Z3 procedure)
8. (G8) Defer §3.4 multipole + κ locks to Z**-quant-multipole child
9. (G9) Run marketing-language grep, scrub
10. (G10) Decide BF threshold: recommend BF>3 narrowing parity with Z3, OR explicitly defer BF adjudication to child quant preregistrations
11. (G11) Add note that Z3 and Z* are competing-mechanism explanations for the same residual
12. (G12) Move (f) "locally-finite c" to §5 postulate-level until a distinguishing observable is locked

Path B v0.2 is light enough to execute in one focused session and would close the Z-track parallel-hypothesis loop cleanly.

**Path A** stays available if Eric prefers full quantitative locking. It's stronger but heavier.

---

## Decision needed from Eric

**Path A, Path B, or defer Z* entirely?**

(No deposit attempted without explicit GATE:OPEN per `feedback_zenodo_publish_gate.md` and `feedback_submission_print_gate.md`.)

---

*End of Z* gap survey 2026-05-04. Filed in z-track alongside Z* v0.1 draft.*
