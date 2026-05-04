# Z* — Cosmopoulous Pre-Registration: Universe-Inside-Black-Hole Cosmological Model

**Status:** DRAFT v0.1 — pre-canonical, image-mode-derived, NOT deposited. Working draft for review and refinement before any Zenodo deposit. Sits parallel to the linear Z0–Z5 chain (which is tactical UHA + EB carrier work). Z* is the theoretical-cosmology preregistration capturing the cosmopoulous reframe.

**Working draft note:** This Z* is a child of the Z0 umbrella pre-registration deposited 2026-04-29 at Zenodo DOI `10.5281/zenodo.19881689`. It deposits the **cosmopoulous-as-black-hole-interior** model as a formally registered cosmological hypothesis, derived from carrier-set theorem + railing-system framework + B-operator structural asymmetry. It inherits Z0's hypothesis-lock structure and adds cosmology-specific hypotheses, observables, and termination criteria.

| Self-reference field | Value |
|---|---|
| Version | v0.1 timestamped `2026-05-01T05:50:00Z` |
| Parent (umbrella) | Z0 v1.2-hybrid at hubble-tensor commit `d842691`; DOI `10.5281/zenodo.19881689` |
| Working filename | `Z-star_cosmopoulous_preregistration_v0_1_DRAFT.md` |
| Naming-policy authority | `feedback_artifact_hash_naming.md` |
| Pending bookkeeping | Pre-canonical until committed and renamed with bootstrap commit hash. |

**Standing artifact-hash-naming policy (inherited from Z0):** Every artifact carries its commit hash inside AND in filename. No hash, no canonical status.

---

## Zenodo metadata block (deposit-ready)

| Field | Value |
|---|---|
| Title | Z* Pre-Registration: Cosmopoulous Cosmological Model |
| Author | Eric D. Martin |
| ORCID | 0009-0006-5944-1742 |
| Affiliation | Independent researcher |
| License | CC-BY-4.0 |
| Resource type | Publication / Preprint |
| Keywords | cosmology, black hole, cosmopoulous, EB carrier, Hubble tension, recursive pair law |
| Related identifiers (is part of) | `10.5281/zenodo.19881689` (Z0 umbrella v1.2-hybrid) |
| Related identifiers (cites) | `10.5281/zenodo.19676237` (priority hash); RSOS-260797 r4 (EB carrier characterization theorem under review); US 63/902,536 (UHA patent) |

---

## 1. Purpose

This pre-registration locks the **cosmopoulous-as-black-hole-interior** model before any cosmological hypothesis-adjudicating analysis is performed. The model claims our observable universe is the interior of a black hole, with the cosmological event horizon as the edge, and various structural consequences derivable from the carrier-set theorem and EB algebra.

Z* does not claim ΛCDM is wrong in its observational fits. It locks an **alternate cosmological model** with carrier-algebra foundations and tests its predictions against ΛCDM and observation.

Z* does not claim universal applicability to all cosmological observables. It locks a specific set of observables (§3) where the cosmopoulous model and ΛCDM are predicted to differ.

This pre-registration does not claim cyclic cosmology or multi-cosmopoulous transit are established physics. They are postulate-level extensions (per Z*-§5) and tested separately if at all.

### 1.1 Pre-registered hypotheses and decision locks (Z*)

#### Primary hypotheses (Z*)

- **H0-Z\*:** The observable universe's large-scale dynamics are correctly described by ΛCDM with standard cosmological parameters. No cosmopoulous-specific signature exists in the observables locked in §3.
- **H1-Z\*:** The observable universe is the interior of a cosmopoulous (black-hole interior) with structural consequences:
  - (a) **Pull, not push:** apparent expansion is the inevitable forward-direction inside a black-hole geometry
  - (b) **Horizon-growth:** what we measure as Hubble flow is the rate of cosmological event horizon enlargement
  - (c) **Light bent at horizons:** photons at the cosmological event horizon are bent into the b-rail substrate (perpendicular to the e-rail), not destroyed
  - (d) **Substrate-routed light:** some early-universe glow we observe (~280–400 Myr epoch) may be light bent and redirected via substrate routing, not solely original emission
  - (e) **Mirror-counter-rotation at edge:** the edge has counter-rotation that maintains stability (axle-wheel topology); detectable in mass-rail observables but not light-rail observables
  - (f) **Locally-finite c:** the speed of light c is local to our cosmopoulous, not universal across the Cosmos; substrate-level information transit is not bound by c

#### Shared decision definitions

Inherited from Z0 §1.1. Z* narrowing:

- **Baseline:** ΛCDM with Planck 2018 best-fit parameters as the null reference
- **Improvement:** any observable in §3 where the cosmopoulous model predicts a DIFFERENT value than ΛCDM, and the observed value matches the cosmopoulous prediction within stated uncertainty
- **Primary success:** ≥ 2 of the §3 observables show cosmopoulous-predicted value with Δχ² ≥ 20 against ΛCDM, AND no §3 observable shows ΛCDM-favored result with Δχ² ≥ 20 against cosmopoulous
- **Analysis start:** the first execution of the locked observable extraction after Z* DOI is deposited
- **Same-pipeline rule:** observables computed using Planck 2018 maps, JWST DR releases, and existing Pantheon+ SN data with locked extraction pipelines defined in §3
- **Controls:** ΛCDM best-fit predictions as the null; cosmopoulous predictions as the alternative; both with full covariance treatment per Z2's A3 audit

#### Data handling locks

Inherited from Z0 §1.1.

### 1.2 What would render Z* unsupported

Z* will be considered unsupported if any of the following occur:
- **K0-Z\*:** All §3 observables show ΛCDM-favored values within stated uncertainty (no cosmopoulous signature)
- **K1-Z\*:** Cosmopoulous-predicted observables disagree with observation by Δχ² ≥ 49 in any single channel, with no mechanism-justified covariance term explaining the disagreement
- **K2-Z\*:** The model fails to recover BBN abundances when applied with cosmopoulous-equivalent early-time conditions
- **K3-Z\*:** The model fails to predict the observed CMB temperature within 10% under horizon-emission scaling
- **K4-Z\*:** The mirror-counter-rotation prediction (§3) cannot be reconciled with mass-rail observation bounds (e.g., BOSS / DESI structure correlations)

If any of K0–K4 fire, Z* halts and a negative or narrow-method result is deposited under the failure-publication rule (Z0 §9).

### 1.3 Public-data-first scope

Per Z0 §1.3. Z* uses publicly available data:
- **Planck 2018 CMB maps** (ESA Planck Legacy Archive)
- **JWST early-universe galaxy catalog** (STScI MAST)
- **Pantheon+ supernova sample** (Brout et al. 2022)
- **DESI BAO measurements** (DESI Collaboration releases)
- **EHT M87* and Sgr A* images** (EHT Collaboration releases — used for fractal-self-similarity check, not direct cosmological inference)

### 1.4 Evidence framework

Per Z0 §1.4. Z* uses Δχ² with thresholds:
- Δχ² ≤ 5: not significant
- 5 < Δχ² ≤ 20: stage-1 signal (description-changelog log)
- 20 < Δχ² < 49: stage-2 signal (potential mint)
- Δχ² ≥ 49: divert to fresh pre-reg (signature too strong to absorb in current model)

---

## 2. Theoretical Framework

The cosmopoulous model is derived from:

1. **Carrier-set theorem** (RSOS-260797 r4, EB carrier characterization): EB carrier `A_EB = ℝ_e × ℝ_{≥0,b}` is forced unique under axioms A1–A6.
2. **Recursive pair law** (carrier_state_rail_theory_v0_2.md §20): every structured physical domain admits recursive descent into A_EB.
3. **Singular-boundary postulate** (carrier_state_rail_theory_v0_2.md §22): across a singular boundary, e-rail content's sign is destroyed; b-rail magnitude survives.
4. **Railing-system unification** (project_railing_system_discovery.md): time, magnetism, gravity, matter, energy are all (e,b)-decomposable.
5. **Witness-loss principle** (carrier-set theorem corollary): B²(e,b) = (|e|, b); sign on e is destroyed under round-trip; b-rail content preserved.

The cosmopoulous-as-black-hole identification follows from:
- Our observable universe has an event horizon (cosmological horizon)
- We're inside it (light from beyond can't reach us)
- The horizon corresponds to the B-flip locus (e-rail content transitions to b-rail at horizon)
- This identification is structurally consistent with Pathria 1972, Stuckey 1994, Popławski recent
- Black holes throughout our cosmopoulous are smaller-scale instances of the same pattern (fractal self-similarity)

### 2.1 Specific structural claims

- The cosmological event horizon **is** the cosmopoulous edge
- "Expansion" we measure is **horizon-growth**, not metric stretching
- Pull from horizon is thermodynamically forced (entropy increase via Bekenstein-Hawking S = A/4)
- The interior is **stretched in time and space** (gravitational dilation throughout interior)
- Light bent at horizons is **redirected**, not destroyed (transferred to b-rail substrate)
- Different cosmopoli have **different local c** (c is a geometric constant of our specific cosmopoulous)
- **Universe is finite** (bounded by horizon; no infinite space)
- **Single Cosmos contains many cosmopoli** (recursive black-hole-as-universe pattern)

---

## 3. Pre-Registered Observables

### 3.1 CMB temperature from horizon-emission

**Observable:** CMB monopole temperature T_CMB.

**Method:**
- Compute predicted T_CMB given the cosmopoulous's horizon mass-energy content + horizon radius + accretion-disk-equivalent thermal spectrum
- Apply gravitational redshift from horizon to interior observer
- Compare to observed T_CMB = 2.7255 ± 0.0006 K

**Pre-registered prediction:**
- ΛCDM: T_CMB derived from recombination physics; T_CMB ≈ 3000 K at z* ≈ 1090, redshifted to 2.7255 K today
- Cosmopoulous: T_CMB derived from horizon-emission; specific value computed from horizon parameters (locked at analysis start using Planck 2018 mass-energy budget)
- **Test:** does cosmopoulous prediction match observed 2.7255 K within 10%?

### 3.2 z* (decoupling redshift) re-interpretation

**Observable:** the apparent redshift of last-scattering surface, z* ≈ 1090.

**Method:**
- ΛCDM: z* corresponds to recombination at T ≈ 3000 K
- Cosmopoulous: z* corresponds to a specific feature of horizon-emission spectrum (TBD by analysis)
- Compare predicted z* to observed Planck 2018 value

**Pre-registered prediction:**
- The cosmopoulous z* prediction must lie within ±5% of observed z* ≈ 1090 to count as compatible
- Larger deviation = K1-Z* trigger (cosmopoulous fails on CMB epoch)

### 3.3 Hubble tension as horizon-growth structure

**Observable:** SH0ES H0 vs Planck H0; the ~5σ tension.

**Method:**
- ΛCDM: tension is unexplained / new-physics candidate
- Cosmopoulous: H0 measured at different epochs samples different points in horizon-growth profile; SH0ES and Planck legitimately differ because horizon growth isn't constant in cosmic time
- Derive the horizon-growth function and predict the SH0ES vs Planck split quantitatively

**Pre-registered prediction:**
- Cosmopoulous's horizon-growth function predicts SH0ES H0 ≈ 73.04 and Planck H0 ≈ 67.40 within 0.5 km/s/Mpc each
- Failure to match either value within 1 km/s/Mpc = K1-Z* trigger

### 3.4 Mirror-counter-rotation in mass-rail observables

**Observable:** Large-scale structure correlation tensors with handedness; gravitational-wave anisotropy.

**Method:**
- Mass-rail observations should preserve cosmopoulous-edge counter-rotation signature
- Light-rail observations (CMB) are predicted to NOT show it (matter mediation washes it out)
- Specifically: BOSS/DESI structure cross-correlations should show anisotropy at multipoles ℓ where light-rail observations show isotropy

**Pre-registered prediction:**
- Cosmopoulous predicts anisotropy in mass-rail observables at specific multipoles (TBD by analysis)
- ΛCDM predicts isotropy at all scales above the standard model uncertainty
- Detection of anisotropy at predicted multipoles in mass-rail data, while light-rail shows isotropy = strong cosmopoulous evidence

### 3.5 Substrate-routed light at Cosmic Dawn

**Observable:** Apparent maturity of JWST early galaxies at z = 14+.

**Method:**
- ΛCDM: galaxies at z = 14 are 280 Myr old; "too mature" galaxies are a model tension
- Cosmopoulous: some "early epoch" light is substrate-routed (bent and re-emerged), so observed objects' apparent age may include path-length effects
- Test: are there age inconsistencies WITHIN objects at the same apparent epoch?

**Pre-registered prediction:**
- Cosmopoulous predicts age-spread between same-epoch objects is wider than ΛCDM allows
- Statistical test: variance in stellar age estimates for z = 14 galaxy sample
- Larger-than-ΛCDM variance is cosmopoulous evidence

---

## 4. Locked Analysis Pipelines

(to be specified at analysis start; placeholders below)

- **Pipeline P1:** CMB monopole + spectral shape derivation under horizon-emission model
- **Pipeline P2:** z* prediction from horizon-emission peak
- **Pipeline P3:** SH0ES vs Planck H0 prediction from horizon-growth function
- **Pipeline P4:** BOSS/DESI mass-rail anisotropy multipole analysis
- **Pipeline P5:** JWST z = 14 galaxy age-variance statistical test

Each pipeline locks: data version, extraction code commit hash, assumed parameters, statistical test, decision rule. Locked at analysis start; cannot be modified post-deposit.

---

## 5. Postulate-level extensions (NOT pre-registered for this Z*)

These are framework extensions that COULD be tested but are not part of Z*'s primary success criteria:

- **Cyclic cosmology / bounce mechanism** — Z* doesn't test
- **Multi-cosmopoulous transit via decoupling** — Z* doesn't test
- **PP precursor algebra cosmological role** — Z* doesn't test
- **Recursive pair law universality** — Z* doesn't test (separate research target per WT-1 to WT-4)

Each of these may become a separate Z** preregistration in the future.

---

## 6. Termination criteria (K0–K4)

| K | Trigger | Action |
|---|---|---|
| K0 | All §3 observables ΛCDM-favored within stated uncertainty | Z* halts; null result deposited |
| K1 | Single-channel disagreement Δχ² ≥ 49 with no covariance justification | Z* halts; investigate; possible new pre-reg |
| K2 | BBN abundance failure | Z* halts; framework needs revision |
| K3 | T_CMB prediction off by > 10% | Z* halts; horizon-emission model fails |
| K4 | Mirror-counter-rotation rules out by mass-rail bounds | Z* halts; counter-rotation claim retracted |

If any K fires, two-stage failure-publication per Z0 §9.

---

## 7. What this pre-registration locks

- Hypotheses H0-Z*, H1-Z* with structural claims (a)–(f)
- Five observables (§3) and their pre-registered predictions
- Five termination criteria (§6)
- Public-data-first scope
- Δχ² evidence framework with thresholds 5 / 20 / 49

After this DOI is deposited, hypothesis-adjudicating analysis on §3 observables can begin. Any modification to predictions, thresholds, or termination criteria requires a new pre-reg.

---

## 8. Provenance

Z* draws on:
- Image-mode cosmological articulation 2026-05-01 (cosmopoulous-as-black-hole, pull-not-push, light-bending, edge-counter-rotation, etc.)
- Carrier-set theorem (manuscript in review, RSOS-260797 r4)
- Recursive pair law (carrier_state_rail_theory_v0_2.md §20)
- Railing-system unification (project_railing_system_discovery.md)
- Witness-loss principle (compile_carrier_set_identity_2026-05-01_v3.md §6)

Three serious-physics anchors: Pathria 1972, Stuckey 1994, Popławski recent. These are minority-but-defensible cosmological views. Z* operationalizes them by adding the carrier-algebra structure.

---

## 9. Status

**Pre-canonical, image-mode-derived.** Not deposited. Requires:
- Sanity-check pass against existing physics (BBN, structure formation, inflation compatibility)
- Specific prediction values computed (not just structural claims)
- Locked extraction pipelines fully specified
- Print + cool-off + GATE:OPEN per `feedback_zenodo_publish_gate.md`

This draft captures the structural reframe in pre-registration form. Quantitative prediction work and pipeline specification needed before deposit.

---

*End of Z* draft v0.1. Held for review.*
