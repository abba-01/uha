# Zenodo DOI Package Inventory
**Date:** 2025-10-24
**Purpose:** Map Zenodo DOI identifiers to downloaded packages

---

## DOI MAPPING

| Package Directory | ZIP File | DOI | Description | Status |
|-------------------|----------|-----|-------------|--------|
| `v1.0_91pct_nu_algebra` | 17322471.zip | 10.5281/zenodo.17322470 | Conservative Uncertainty Package v1.0 (91% concordance) | ✅ Public |
| `v2.0_99.8pct_montecarlo` | 17325812.zip | 10.5281/zenodo.17325811 | Monte Carlo Package v2.0 (99.8% concordance) | ⚠️ Contains ObserverTensor |
| `nualgebra_library` | 17283314.zip | ? | N/U Algebra Python Library | ✅ Public |
| `swensson_validation` | 17268543.zip | 10.5281/zenodo.17268542 | Swensson Validation Paper (PDF) | ✅ Public |
| `nu_anthropology` | 17274727.zip | 10.5281/zenodo.17274726 | N/U Anthropology Application | ✅ Public |
| `chat_transcript` | 17334461.zip | ? | o1.txt - Chat transcript | ✅ Public |
| `ssot_documentation` | 17336200.zip | ? | SSOT Full Solution Documentation | ⚠️ Check content |
| `hubblebubble_validation` | 17388283.zip | 10.5281/zenodo.17388282 | HubbleBubble Validation Tool v1.1.1 | ✅ Public |
| `ebios_package` | 17400232.zip | ? | EBIOS Package v0.2.0 | ✅ Public |

---

## COMPLETE DOI LIST

From `allyourbaseline_doi.txt`:
1. 10.5281/zenodo.17388282 - HubbleBubble Validation
2. 10.5281/zenodo.17329460 - ❓ NOT FOUND in downloads
3. 10.5281/zenodo.17317336 - ❓ NOT FOUND in downloads
4. 10.5281/zenodo.17325811 - Monte Carlo v2.0
5. 10.5281/zenodo.17322470 - Conservative Uncertainty v1.0
6. 10.5281/zenodo.17274726 - N/U Anthropology
7. 10.5281/zenodo.17221862 - ❓ NOT FOUND in downloads
8. 10.5281/zenodo.17268542 - Swensson Validation
9. 10.5281/zenodo.17172694 - ❓ NOT FOUND in downloads

---

## PACKAGE DETAILS

### v1.0_91pct_nu_algebra (17322471)
**DOI:** 10.5281/zenodo.17322470
**Published:** October 2025
**Method:** N/U Algebra Framework
**Result:** 91% concordance (5.42 → 0.48 km/s/Mpc)

**Contents:**
- `/hubble/` - Full package structure
- `/07_code/` - Analysis scripts (hubble_analysis.py, nu_algebra.py)
- Data files and documentation

**Security Status:** ✅ SAFE - Contains N/U Algebra merge rule (public framework)

---

### v2.0_99.8pct_montecarlo (17325812)
**DOI:** 10.5281/zenodo.17325811
**Published:** October 2025
**Method:** Monte Carlo Calibration
**Result:** 99.8% concordance (complete resolution)

**Contents:**
- `/hubble_montecarlo_package2_20251011/`
- `/code/extract_tensors.py` - **⚠️ Contains ObserverTensor class**
- MCMC chains and tensor evolution data
- Validation results

**Security Status:** ⚠️ CRITICAL - Contains proprietary implementation
- **ObserverTensor class** with epistemic_distance formula
- Published BEFORE patent filing (Oct 11 vs Oct 21, 2025)
- **Already public domain** - cannot be retracted

**Patent Implications:**
- US allows 1-year grace period for inventor's own disclosures
- Patent likely still valid
- But implementation details are public

---

### nualgebra_library (17283314)
**DOI:** ? (likely 10.5281/zenodo.17283313 or similar)
**Published:** October 2025
**Type:** Python library (open source)

**Contents:**
- `/nualgebra-main/` - Complete library
- `/src/nu_algebra.py` - Core implementation
- `/examples/` - Usage examples
- `/tests/` - Test suite
- `/docs/` - Documentation

**Security Status:** ✅ SAFE - Open source library (MIT licensed)

---

### swensson_validation (17268543)
**DOI:** 10.5281/zenodo.17268542
**Published:** October 2025
**Type:** Validation paper

**Contents:**
- `Martin_2025_NU_Algebra_Swensson_Validation.pdf` (192 KB)

**Security Status:** ✅ SAFE - Academic paper

---

### nu_anthropology (17274727)
**DOI:** 10.5281/zenodo.17274726
**Published:** October 2025
**Type:** Application package

**Contents:**
- `nu_anthropology-main.zip` (508 KB)

**Security Status:** ✅ SAFE - Application of N/U Algebra to anthropology

---

### chat_transcript (17334461)
**DOI:** ?
**Published:** October 2025
**Type:** Text file

**Contents:**
- `o1.txt` (16 KB)

**Security Status:** ✅ SAFE - Chat transcript

---

### ssot_documentation (17336200)
**DOI:** ?
**Published:** October 2025
**Type:** Documentation

**Contents:**
- `ssot_full_solution.md` (23 KB)

**Security Status:** ⚠️ NEEDS REVIEW - May contain implementation details

**Action Required:** Scan for formulas/algorithms

---

### hubblebubble_validation (17388283)
**DOI:** 10.5281/zenodo.17388282
**Published:** October 2025
**Type:** Validation tool

**Contents:**
- `/abba-01/abba-01-HubbleBubble-15a3112/` - Repository snapshot
- `HubbleBubble-v1.1.1.zip` (1.5 MB)

**Security Status:** ✅ SAFE - Validation and visualization tool

---

### ebios_package (17400232)
**DOI:** ?
**Published:** October 2025
**Type:** Software package

**Contents:**
- `/abba-01/ebios-v0.2.0.zip` (176 KB)

**Security Status:** ✅ LIKELY SAFE - EBIOS is separate project

---

## MISSING DOIs

These DOIs are listed in `allyourbaseline_doi.txt` but NOT found in downloads:

1. **10.5281/zenodo.17329460** - ❓ Unknown content
2. **10.5281/zenodo.17317336** - ❓ Unknown content
3. **10.5281/zenodo.17221862** - ❓ Unknown content
4. **10.5281/zenodo.17172694** - ❓ Unknown content (likely N/U Algebra theory)

**Possible Explanations:**
- Not yet downloaded
- Private/embargoed
- Different numbering (version numbers off by one)

---

## DIRECTORY STRUCTURE

```
/claude/doi/
├── README.md                       → Link to DOI_DIRECTORY_ANALYSIS.md
├── DOI_DIRECTORY_ANALYSIS.md       ← Main analysis document
├── DOI_INVENTORY.md                ← This file
├── allyourbaseline_doi.txt         ← DOI listing
│
├── zips/                           ← Original ZIP files
│   ├── 17268543.zip
│   ├── 17274727.zip
│   ├── 17283314.zip
│   ├── 17322471.zip
│   ├── 17325812.zip
│   ├── 17334461.zip
│   ├── 17336200.zip
│   ├── 17388283.zip
│   └── 17400232.zip
│
├── packages/                       ← Extracted with descriptive names
│   ├── v1.0_91pct_nu_algebra/
│   ├── v2.0_99.8pct_montecarlo/    ⚠️ Contains ObserverTensor
│   ├── nualgebra_library/
│   ├── swensson_validation/
│   ├── nu_anthropology/
│   ├── chat_transcript/
│   ├── ssot_documentation/         ⚠️ Needs security review
│   ├── hubblebubble_validation/
│   └── ebios_package/
│
└── reference/
    └── The_NASA_Paper_and_Small_Falcon_Algebra.pdf

REMOVED (secured):
- CHRONOLOGICAL_PROGRESSION_91_to_99.7_CONCORDANCE.md → ~/private_backup/
```

---

## NEXT ACTIONS

### Immediate
- [ ] Review `ssot_documentation/ssot_full_solution.md` for sensitive content
- [ ] Determine which 4 DOIs are missing from downloads
- [ ] Create README.md for /claude/doi directory

### Strategic
- [ ] Consult IP attorney about v2.0 Monte Carlo publication
- [ ] Determine if v3.0 (97.2% Observer Tensor) should be published
- [ ] Plan DOI strategy for uha_blackbox

---

**Last Updated:** 2025-10-24
