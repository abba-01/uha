# Paper 4 Execution Memo
## "Shell Geometry of the Observable Universe: A Selection-Corrected xi-Density Profile"
**Eric D. Martin — 2026-03-29**

Pre-registration DOI: 10.5281/zenodo.19322304

---

## Current Status

| Task | Status |
|---|---|
| Pipeline A (UHA round-trip validation) | **COMPLETE** — all tests pass, committed, DOI minted |
| SDSS DR16 shell map (raw) | **COMPLETE** — 4 figures, 500k galaxies, ξ∈[0.001,0.653] |
| Pipeline B — SDSS 1/V_max correction | **RUNNING** — V_max loop for 500k galaxies |
| DESI DR1 LRG download | **COMPLETE** — 2.8 GB on disk |
| DESI DR1 BGS download | **IN PROGRESS** — ~4.8 GB of ~5 GB |
| Paper 4 LaTeX skeleton | Pending — all pieces exist |

---

## Dataset Hierarchy (locked 2026-03-29)

### Tier 1 — 2MRS
- **Purpose:** Debug and stabilize the completeness machinery
- **Limits:** K_s < 11.75, |b| > 5°, ξ < 0.17
- **On disk:** `/scratch/repos/galaxy-survey-data/galaxy_catalogs/2mrs/`
- **What it proves:** Mask handling, magnitude-limit logic, radial completeness, raw vs corrected shell plots work
- **What it does NOT prove:** The 3% residual question (too shallow, ξ ceiling too low)

### Tier 2 — SDSS DR16 (500k galaxies)
- **Purpose:** Bridge — corrected shell density at intermediate depth
- **Limits:** r < 17.77, z ∈ [0.001, 0.80], ξ ∈ [0.001, 0.653]
- **On disk:** `/scratch/repos/galaxy-survey-data/galaxy_catalogs/sdss_dr16/sdss_dr16_galaxies.csv`
- **Key result so far:** 6.0% attractor-flagged (30,147/500,000 objects); compare-masked panel is primary Paper 4 diagnostic
- **What it proves:** Corrected shell method scales beyond local universe; attractor masking sensitivity visible
- **Completeness method:** 1/V_max (Schmidt 1968), extinction-corrected r-band

### Tier 3 — DESI DR1 BGS + LRG (main science)
- **Purpose:** Decisive — where the residual physics from Papers 1 & 2 already lives
- **BGS:** z < 0.40, ξ < 0.32, ~10M targets; on disk at `desi_dr1/BGS_BRIGHT_full.fits`
- **LRG:** z < 1.10, ξ < 0.73; on disk at `desi_dr1/LRG_full.fits`
- **Why DESI is the main event:** Papers 1 & 2 already place the surviving residual signal here:
  - Ω_m ≈ 0.290 deficit (DESI DR2 confirmed prediction)
  - Δχ²(w0wa) = 13.13 from DH/rs at z = 0.51–0.71
  - DESI is not just "more galaxies" — it is the dataset where the claimed physics already lives
- **Next:** Port same corrected shell-density pipeline once BGS download completes

### Named Anchor Object — CDG-2
- **Full name:** Candidate Dark Galaxy-2
- **Reference:** arXiv:2506.15644, ApJL 986(2):L18 (2025); ESA Hubble press release heic2605
- **Dark matter fraction:** 99.94–99.99% (press: "99.8%")
- **Location:** Perseus cluster, ~75 Mpc
- **Coordinates:** α = 3h17m12.61s, δ = +41°20'51.5"
- **ξ position:** z ≈ 0.0179 → **ξ ≈ 0.017**
- **Detection:** First galaxy found solely via globular cluster population (4 GCs; HST + Euclid + Subaru)
- **Stellar mass:** ~1.2 × 10⁷ M☉; halo mass ~2–5.7 × 10¹⁰ M☉
- **Paper 4 role:** Named extreme dark-matter object overlay on the local shell map; case-study for DM-dominated halo in dense environment; Euclid contribution to its detection ties it to the Oct 2026 validation lane
- **What it does NOT replace:** Survey completeness machinery, DESI/SDSS corrected profiles, Euclid DR1 falsification

### Validation Target — Euclid DR1 (October 2026)
- **Purpose:** Decisive external falsification/confirmation
- **Pre-registered predictions (from Paper 2 / partition analysis):**
  1. S8 < 0.820
  2. Euclid + DESI dark-energy preference consistent with w0wa signal
  3. Ly-α / QSO BAO consistency near z ~ 2.4
- **Status:** Eclipse date — October 2026

---

## What "Publishable Evidence" Looks Like

Paper 4 clears the bar when it has all of the following:

1. **Pipeline A validation** — ξ coordinate operationally confirmed across full range including ξ > 1 ✓ DONE
2. **Corrected shell-density profile (at least one major survey)** — SDSS in progress; DESI next
3. **Attractor masking sensitivity test** — does the residual persist after removing attractor-cone objects? Compare-masked panel from SDSS already computed
4. **At least two independent depth regimes** — SDSS (ξ < 0.65) + DESI BGS (ξ < 0.32) + DESI LRG (ξ < 0.73) = three overlapping windows
5. **Named anchor object(s)** — CDG-2 at ξ ≈ 0.017 provides an extreme-DM case study
6. **Consistency with Papers 1 & 2 residual** — shell-density residual direction should align with Ω_m ≈ 0.290 and w0wa signal in DESI DR1

---

## Immediate Next Actions (priority order)

1. **Wait for SDSS Pipeline B to finish** — then inspect corrected shell-density profile and compare-masked panel
2. **Complete DESI BGS download** — then run same Pipeline B on BGS
3. **Run Pipeline B on DESI LRG** — already on disk
4. **Add CDG-2 as named overlay** — annotate shell map at ξ ≈ 0.017, Perseus cluster region
5. **Write Paper 4 LaTeX skeleton** — intro ready from G5 gap analysis; sections: Coordinate, Validation, Selection, SDSS Result, DESI Result, Anchor Objects, Discussion
6. **Zenodo: upload updated pipeline package** — after DESI results are committed

---

## Key Files

| File | Location | Status |
|---|---|---|
| shell_map_pipeline.py | `/scratch/repos/uha/papers/` | Production |
| pipeline_b_completeness.py | `/scratch/repos/uha/papers/` | Production |
| uha_roundtrip_validation.py | `/scratch/repos/uha/papers/` | Complete |
| shell_map_sdss_dr16_*.png | `/scratch/repos/uha/papers/` | Complete (4 figures) |
| pipeline_b_sdss.png/csv | `/scratch/repos/uha/papers/` | Pending (Pipeline B running) |
| sdss_dr16_galaxies.csv | `/scratch/repos/galaxy-survey-data/galaxy_catalogs/sdss_dr16/` | 500k galaxies |
| BGS_BRIGHT_full.fits | `/scratch/repos/galaxy-survey-data/galaxy_catalogs/desi_dr1/` | Download in progress |
| LRG_full.fits | `/scratch/repos/galaxy-survey-data/galaxy_catalogs/desi_dr1/` | Complete |
| loao.json | `/scratch/repos/hubble-tensor/` | Complete (gravity tensor grid) |

---

## Connection to Papers 1 & 2

- **Paper 1** ("The Hubble Tension as a Measurement Artifact"): established ξ coordinate removes ~90% H₀ tension as frame artifact
- **Paper 2** ("Three Separable Components in DESI DR1 and DR2 BAO"): partitions residual into Ω_m deficit (0.290) + w0wa dark energy signal (Δχ²=13.13 in DR2)
- **Paper 4** closes the loop: if the corrected shell-density profile shows a residual signal at DESI depths that is:
  - directionally coherent (not isotropic noise)
  - reduced but not eliminated by attractor masking
  - consistent with Ω_m ≈ 0.290 direction
  - then Paper 4 provides the spatial/structural face of what Papers 1 & 2 found in aggregate statistics

---

*Last updated: 2026-03-29*
