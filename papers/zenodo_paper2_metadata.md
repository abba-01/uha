# Zenodo Upload Metadata — Paper 2
## "The Partition of Cosmological Tensions"

---

### TITLE
The Partition of Cosmological Tensions: A Three-Component Decomposition Using Horizon-Normalized Coordinates

### AUTHORS
Martin, Eric D.
  Affiliation: All Your Baseline LLC
  ORCID: (add if you have one)

### UPLOAD TYPE
Publication → Preprint

### PUBLICATION DATE
2026-03-27

### DESCRIPTION (paste into Zenodo description field)

---

**Discovery Context and Temporal Sequence**

This paper is the second in a sequence that emerged from an empirical observation, not from a theoretical framework built in advance.

The starting point was the Hubble tension itself: the well-documented ~5σ discrepancy between the SH0ES distance-ladder measurement of H₀ = 73.04 ± 1.04 km/s/Mpc and the Planck CMB inference of H₀ = 67.4 ± 0.5 km/s/Mpc. While investigating the structure of this discrepancy, it became apparent that the two pipelines express cosmological distances in ways that encode H₀ differently — one geometrically (Cepheid calibration), one through a full CMB likelihood.

The normalized coordinate ξ = dc/dH was introduced as a diagnostic: a dimensionless representation of comoving distance that cancels explicit H₀-scaling for redshift-derived distances. This was not designed to make the tension disappear. It was designed to ask: *what fraction of the apparent discrepancy is a property of the comparison conventions, and what fraction survives as a physical signal?*

**What the analysis found — in the order it was found:**

1. ~93% of the raw H₀ tension statistic dissolves under ξ-normalization, consistent with the two pipelines using incompatible H₀-dependent distance conventions.

2. The residual after normalization (~7%) decomposes into a matter density deficit (Ωm ≈ 0.295 vs Planck's 0.315) and a weak dark energy signal (w₀ ≠ −1 at ~1.81σ under conservative N/U bounds).

3. DESI DR1 BAO subsequently reported Ωm = 0.295 ± 0.015 from a fully independent H₀-free measurement. This was not known when the framework was developed.

**Why additional framework was laid out before submission:**

Reviewers reasonably ask: Is ξ-normalization a tautology? Is the result H₀-frame-dependent? Does it preserve information? Does it add value over standard methods?

To answer these questions rigorously, a supporting validation framework was developed (available in the companion repository `abba-01/hubble-anisotropy`):

- Proof 1: Distance ratios are exactly preserved across all H₀ frames (residual = 0.00e+00, verified against GAIA DR3 parallax)
- Proof 2: ξ is monotone and continuous from stellar (pc) to CMB (Gpc) scales — no discontinuities
- Proof 3: H₀ variation leaves ξ invariant (range 5.5×10⁻¹⁷); Ωm and w₀ variation changes ξ (ξ is a diagnostic, not a tautology)
- Proof 4: Round-trip μ → ξ → μ residual = 0.00e+00; uncertainty tracking matches GAIA DR3 precision exactly
- Proof 5: ξ reduces per-SN H₀ scatter by 38% vs raw local H₀ estimates; z-dependent residuals confirm non-trivial physical content

This framework was not part of the original discovery. It was built afterward to give reviewers the tools to evaluate the claim on its merits without having to take any single step on faith.

**Relation to companion work:**

- Paper 1 (Martin 2026a, DOI: 10.5281/zenodo.19230366): introduces ξ and demonstrates the ~93% frame-artifact finding on the SH0ES/Pantheon+ sample
- N/U Algebra (Martin 2025, DOI: 10.5281/zenodo.17172694): conservative uncertainty propagation framework used for significance bounds
- UHA Patent (US Provisional 63/902,536): encoding infrastructure (Morton encoder, CosmoID, TLV format) — the scientific results do not require the full patent architecture, only ξ

**Euclid DR1 (October 2026) represents the pre-registered decisive test.** Independent measurements of Ωm, S8, and the w₀wa plane from Euclid will either confirm or refute the framework's predictions without any additional free parameters.

---

### KEYWORDS
Hubble tension, cosmological tensions, distance normalization, xi coordinate, matter density, dark energy, BAO, S8 tension, frame artifacts, Omega_m, w0wa, DESI, Euclid, Pantheon+, UHA, N/U algebra

### LICENSE
Creative Commons Attribution 4.0 International (CC BY 4.0)

### RELATED IDENTIFIERS
- Is supplement to: 10.5281/zenodo.19230366  (Paper 1)
- Is supplement to: 10.5281/zenodo.17172694  (N/U Algebra)
- References: 10.5281/zenodo.19232340         (UHA v2.0.0 pre-registration)

### ACCESS
Open Access

---

## NOTES FOR ZENODO UPLOAD

1. Upload file: `hubble_tension_partition.pdf`
2. Optional: also upload `paper2_submission_v3.tar.gz` as supplementary
3. After minting, update this file with the assigned DOI
4. Then run: git add + commit + push to abba-01/uha

**DOI assigned: 10.5281/zenodo.19272498** (minted 2026-03-27)
