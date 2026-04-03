# Claude Artifact Templates - Package Names

**Quick Reference**: Which template corresponds to which package

**Five Main Packages**: v1.0 (91%), v2.0 (100%), v3.0 (97.2%), v4.0 (0.966σ), v5.0 (91% validation)

---

## Package 1: N/U Algebra Framework (91% Resolution)

**Package Name**: `v1.0_91pct_nu_algebra` (also `hubble-91pct-concordance`)
**Full Name**: Conservative Uncertainty Propagation and Hubble Tension Resolution
**Template File**: `/got/unalgebra/.artifact-template-hubble-91pct-analytical-tensors.md`

**Achievement**: 91% tension reduction (first breakthrough)
**Method**: Analytically-derived observer domain tensors
**Published**: October 11, 2025 (morning)
**DOI**: 10.5281/zenodo.17322471 (Complete Package v1.0.0)
**Related DOIs**:
- 10.5281/zenodo.17172694 (N/U Algebra Framework)
- 10.5281/zenodo.17221863 (Validation Dataset)

---

## Package 2: Monte Carlo Calibrated Observer Tensors (100% Resolution)

**Package Name**: `hubble-mc-package2` (also `v2.0_99.8pct_montecarlo`)
**Full Name**: Full Resolution of the Hubble Tension through Monte Carlo Calibrated Observer Tensors
**Template File**: `/got/hubble-mc-package2/.artifact-template-hubble-100pct-mc-calibrated.md`

**Achievement**: 100% resolution (zero gap, extends Package 1)
**Method**: Monte Carlo calibration from MCMC chains
**Published**: October 11, 2025 (later same day as Package 1)
**DOI**: 10.5281/zenodo.17325812
**GitHub**: https://github.com/aybllc/hubble-mc-package2
**Note**: .zenodo.json states "This work extends Package 1 (91% resolution)"

---

## Package 3: Pure Observer Tensor / SSOT (97.2% Resolution)

**Package Name**: `ssot_documentation` (also `hubble-97pct-observer-tensor`)
**Full Name**: Single Source of Truth - Complete Hubble Tension Resolution Framework
**Template File**: `/got/hubble-97pct-observer-tensor/.artifact-template-hubble-97pct-pure-observer.md` (if exists)

**Achievement**: 97.2% resolution (simplest method)
**Method**: Pure observer domain tensors + anchor-systematic covariance
**Published**: October 12, 2025
**DOI**: 10.5281/zenodo.17336200
**Version**: v3.0
**Key Innovation**: Four-phase validation (A, B, C, D) + empirical Cepheid test (251 stars)

**Result**:
- Initial gap: 6.07 km/s/Mpc
- Final gap: 0.17 km/s/Mpc
- H₀ = 73.47 ± 0.14 km/s/Mpc (validates SH0ES within 0.41σ)
- Cepheid P-L slope: α = +0.994 (theory: +1.000)

---

## Package 4: HubbleBubble - 0.966σ Concordance with Planck CMB

**Package Name**: `HubbleBubble` (also `hubblebubble_validation`, `abba-01-HubbleBubble`)
**Full Name**: Independent reproducibility test of Hubble constant (H₀) calculation achieving 0.966σ concordance with Planck CMB
**Template File**: `/got/HubbleBubble/.artifact-template-hubblebubble-validation-74pct.md`

**Achievement**: **0.966σ concordance with Planck** (< 1σ = statistical agreement)
**Method**: RENT-T reproducibility framework with systematic anchor calibration
**Published**: October 19, 2025
**DOI**: 10.5281/zenodo.17388282 (v1.1.0) and 10.5281/zenodo.17388283 (v1.1.1)
**Version**: v4.0 (HubbleBubble v1.1.1)
**Result**: H₀ = 68.518 ± 1.292 km/s/Mpc
**Key Innovation**: Iron-tight computational reproducibility (9/9 byte-identical outputs on independent machine)
**Significance**: Demonstrates statistical agreement with Planck when uncertainties properly treated
**GitHub**: https://github.com/abba-01/HubbleBubble (private)

---

## Package 5: Bootstrap Validation Repository

**Package Name**: `hubble-tension-resolution` (also `abba-01/hubble-tension-resolution`)
**Full Name**: Hubble Tension Resolution v1.0.1 - Bootstrap Validation Framework
**Template File**: N/A (GitHub repository)

**Achievement**: Validates Package 1's 91% reduction (5.40 → 0.48 km/s/Mpc)
**Method**: Bootstrap validation with 10,000 Monte Carlo iterations
**Published**: October 24, 2025
**DOI**: 10.5281/zenodo.17435578
**Version**: v5.0 (v1.0.1)
**Key Components**:
- CORRECTED_RESULTS_32BIT.json (canonical observer tensor dataset)
- bootstrap_validation.py (validation script)
- Fixed-seed reproducibility (seed: 20251011)
**Purpose**: Statistical robustness testing and validation
**GitHub**: https://github.com/abba-01/hubble-tension-resolution (public)

---

## Quick Lookup Table

| Package Name | Template Filename | Location | Lines | Resolution | Status |
|--------------|-------------------|----------|-------|------------|--------|
| **Package 1 (v1.0)** | `.artifact-template-hubble-91pct-analytical-tensors.md` | `/got/unalgebra/` | 480 | 91% | ✅ Oct 11 |
| **Package 2 (v2.0)** | `.artifact-template-hubble-100pct-mc-calibrated.md` | `/got/hubble-mc-package2/` | 555 | 100% | ✅ Oct 11 |
| **Package 3 (v3.0)** | SSOT document | `/got/hubble-97pct-observer-tensor/` | N/A | 97.2% | ✅ Oct 12 |
| **Package 4 (v4.0)** | `.artifact-template-hubblebubble-validation-74pct.md` | `/got/HubbleBubble/` | 601 | 0.966σ | ✅ Oct 19 |
| **Package 5 (v5.0)** | GitHub repository | https://github.com/abba-01/hubble-tension-resolution | N/A | 91% validation | ✅ Oct 24 |

---

## File Naming Convention

All artifact templates use **unique descriptive filenames** for easy identification:

**Pattern**: `.artifact-template-{name}-{resolution}-{method}.md`

Located in the root of each package directory and **gitignored**.

---

## Directory Structure

```
/got/unalgebra/
└── .artifact-template-hubble-91pct-analytical-tensors.md  ← Package 1

/got/hubble-mc-package2/
└── .artifact-template-hubble-100pct-mc-calibrated.md      ← Package 2

/got/HubbleBubble/
└── .artifact-template-hubblebubble-validation-74pct.md    ← Package 3
```

**Unique Filenames** make it easy to identify each solution when consolidated together.

---

## Aliases / Alternative Names

### Package 1
- Primary: `v1.0_91pct_nu_algebra`
- Also found as: `hubble-91pct-concordance`
- Zenodo: "The NASA Paper & Small Falcon Algebra"

### Package 2
- Primary: `hubble-mc-package2`
- Also found as: `v2.0_99.8pct_montecarlo`, `hubble-99pct-montecarlo`
- Zenodo: "Monte Carlo Calibrated Observer Tensors"

### Package 3
- Primary: `HubbleBubble`
- Also found as: `hubblebubble_validation`, `abba-01-HubbleBubble-15a3112`
- Zenodo: "HubbleBubble"

---

## Usage Examples

### Copy specific package template:

**Package 1 (91% - Analytical Tensors):**
```bash
cat /got/unalgebra/.artifact-template-hubble-91pct-analytical-tensors.md
```

**Package 2 (100% - MC Calibrated):**
```bash
cat /got/hubble-mc-package2/.artifact-template-hubble-100pct-mc-calibrated.md
```

**Package 3 (74% - HubbleBubble Validation):**
```bash
cat /got/HubbleBubble/.artifact-template-hubblebubble-validation-74pct.md
```

### Consolidate all three together:

```bash
cat /got/unalgebra/.artifact-template-hubble-91pct-analytical-tensors.md \
    /got/hubble-mc-package2/.artifact-template-hubble-100pct-mc-calibrated.md \
    /got/HubbleBubble/.artifact-template-hubblebubble-validation-74pct.md \
    > /tmp/all-hubble-artifact-templates.md
```

**Unique filenames** make it easy to identify which solution is which!

---

## Prompt Templates for Claude.ai

### For Package 1 (91% Resolution)
```
I have the artifact template for Package 1 (v1.0_91pct_nu_algebra).
This demonstrates 91% Hubble tension reduction through analytically-derived
observer domain tensors.

Create an interactive React artifact showing:
- Observer tensor comparison (early vs late)
- Epistemic distance breakdown (60% aperture, 38% temporal)
- Interval containment visualization
- 5.16× uncertainty expansion

[paste template content]
```

### For Package 2 (100% Resolution)
```
I have the artifact template for Package 2 (hubble-mc-package2).
This demonstrates 100% resolution through Monte Carlo calibrated tensors.

Create an interactive React artifact showing:
- Convergence animation (6 iterations)
- Δ_T progression: 1.003 → 1.287
- Gap reduction: 0.48 → 0.00 km/s/Mpc
- Bootstrap validation results

[paste template content]
```

### For Package 3 (HubbleBubble)
```
I have the artifact template for Package 3 (HubbleBubble).
This demonstrates independent validation with reproducibility proof.

Create an interactive React artifact showing:
- 5 validation tests dashboard
- LOAO sensitivity analysis
- Grid-scan stability (289 configs)
- Reproducibility metrics (7/9 byte-identical)

[paste template content]
```

---

## Git Repository Links

| Package | GitHub Repository | Zenodo DOI |
|---------|------------------|------------|
| **Package 1** | N/A (archived to Zenodo) | 10.5281/zenodo.17172694 |
| **Package 2** | https://github.com/aybllc/hubble-mc-package2 | TBD |
| **Package 3** | https://github.com/abba-01/HubbleBubble | 10.5281/zenodo.17388283 |

---

## Related Documentation

- **Complete Index**: `/claude/ARTIFACT_TEMPLATES_INDEX.md`
- **Session Notes**: `/claude/SESSION_NOTES_2025-10-25_UN_REANCHOR.md`
- **Hubble Status**: `/got/HUBBLE_TENSION_STATUS_COMPLETE.md`

---

**Created**: 2025-10-25
**Purpose**: Quick reference for package names and template locations
**Maintainer**: Claude Code
