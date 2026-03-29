# UHA PATENT AMENDMENTS — NEW MATTER FOR NON-PROVISIONAL
## Continuation-in-Part (CIP) Specification and Claims

**Filing basis**: Provisional US 63/902,536 (filed 2025-10-21)
**Non-provisional deadline**: 2026-10-21
**New matter date**: 2026-03-27
**Author**: Eric D. Martin / All Your Baseline LLC

---

## OVERVIEW OF NEW MATTER

The provisional (Claims 1–40) covers the cosmological-scale UHA encoding using:
- Linear radial normalization: s₁ = r / R_H
- Fixed 21-bit Morton encoding
- Single operational mode (cosmological)

This amendment adds six categories of new matter that extend UHA to local/terrestrial
precision scales (10 cm target) while maintaining backward compatibility with
cosmological-scale operation. These are material new features not disclosed in the
provisional, requiring CIP treatment.

| New Feature | Claims | Operational Impact |
|-------------|--------|-------------------|
| Scale dilation | 41–42 | Precision adapts with cosmic epoch |
| Multi-tier radial bands | 43–45 | K-zone spatial segmentation |
| Logarithmic radial normalization | 46–47 | Span 10cm → Hubble horizon in single index |
| Adaptive bit depth by spatial regime | 48–49 | Bit budget tracks resolution need |
| Stated 10 cm precision target | 50 | Quantified near-field performance floor |
| Local-mode / cosmological-mode switch | 51–52 | Formal mode-select with deterministic rules |

---

## SPECIFICATION ADDITIONS

### Section A: Scale Dilation

The cosmic scale factor a encodes the epoch at which a spatial address is created.
At small a (early universe), the proper distance per comoving unit is compressed;
at a = 1 (present), it is maximized. Scale dilation is the operation of adapting
the quantization grid so that physical resolution is preserved across epochs.

For a Morton index with N bits per coordinate, the physical length represented by
the least-significant bit is:

    δ_phys(a, N) = a · R_H(a) / 2^N

Without scale dilation, δ_phys varies by orders of magnitude as a ranges over
cosmological time. With scale dilation, N is chosen as a function of a such that
δ_phys(a, N(a)) ≤ ε_target for a user-specified precision floor ε_target.

The dilation function is:

    N(a) = ⌈log₂( a · R_H(a) / ε_target )⌉

clamped to [N_min, N_max] = [10, 63].

This ensures that spatial addresses at all epochs carry equivalent physical
precision. The encoded CosmoID already encodes a, so a decoder can recover
N(a) deterministically without side-channel information.

### Section B: Multi-Tier Radial Bands

Cosmological and terrestrial applications require different resolution budgets.
A multi-tier radial band system partitions the radial axis [0, R_H] into K
contiguous bands B_0, B_1, ..., B_{K-1}, each with a dedicated bit allocation
and optional local coordinate origin.

Canonical 4-tier partition:

| Tier | Name | Radial Range | Physical Examples |
|------|------|-------------|-------------------|
| 0 | Local | r < r₀ | Earth surface, LEO, solar system |
| 1 | Stellar | r₀ ≤ r < r₁ | Nearby stars, stellar clusters |
| 2 | Galactic | r₁ ≤ r < r₂ | Milky Way, Local Group |
| 3 | Cosmological | r₂ ≤ r ≤ R_H | Large-scale structure, CMB |

Default thresholds: r₀ = 1 Mpc, r₁ = 100 Mpc, r₂ = 1000 Mpc.

Within each tier, normalized coordinates are computed relative to the tier's
local range [r_{k-1}, r_k], maximizing the dynamic range of the Morton index
within that tier. The tier index k (2 bits for K=4) is prepended to the Morton
index, yielding a composite spatial index:

    σ_composite = (k << 63) | morton_index_within_tier

The TLV field structure (Claim 9) accommodates this via the existing optional
anchor metadata field or a dedicated TIER TLV field (type byte = 0x05).

### Section C: Logarithmic Radial Normalization

Linear radial normalization s₁ = r / R_H distributes quantization levels
uniformly across [0, R_H]. Because astronomical objects of interest span many
orders of magnitude in distance (10 cm to 14 Gpc), linear normalization allocates
most quantization levels to sparsely populated large-scale regions and
under-resolves the dense near-field.

Logarithmic radial normalization uses a reference scale r₀ to map the full
dynamic range into [0, 1] uniformly in log-space:

    s₁_log = log(1 + r / r₀) / log(1 + R_H / r₀)

Properties:
- s₁_log ∈ [0, 1] for all r ∈ [0, R_H]
- At r = r₀: s₁_log ≈ 0.5 · log(2) / log(1 + R_H/r₀)  (adjustable midpoint)
- As r₀ → ∞: s₁_log → r / R_H  (recovers linear normalization)
- Physical resolution at r: δr(r) = r₀ · (1 + r/r₀) · δs₁_log

Default reference scale: r₀ = 1 AU = 1.496 × 10⁻⁷ Mpc.

This single formula spans sub-centimeter terrestrial positions and the Hubble
horizon without switching regimes, while concentrating quantization levels at
the high-density near-field distances where precision is most needed.

The normalization mode (linear vs. logarithmic, and r₀) is encoded in the
CosmoID computation (Claim 6) by including normalization parameters in the
hash input string, ensuring self-decoding addresses carry their normalization
metadata.

### Section D: Adaptive Bit Depth by Spatial Regime

The Morton encoding bit depth N (Claims 2–3) is not required to be uniform across
all spatial positions. Adaptive bit depth selects N as a function of the radial
tier (Section B) or the physical distance r, allocating more bits to near-field
positions where physical precision requirements are highest and fewer bits to
cosmological positions where data volume and transmission bandwidth constrain
the address size.

Adaptive allocation table (example):

| Tier | Bit Depth N | Spatial Resolution | Address Size (bits) |
|------|------------|-------------------|---------------------|
| 0 (Local) | 63 | ~10⁻¹⁸ R_H_local | 189 |
| 1 (Stellar) | 42 | ~10⁻¹² R_H_stellar | 126 |
| 2 (Galactic) | 28 | ~10⁻⁸ R_H_galactic | 84 |
| 3 (Cosmological) | 21 | ~10⁻⁶ R_H | 63 |

The bit depth N is determined by:

    N(r) = max(N_min, min(N_max, N_base - β · ⌊log₁₀(r / r₀)⌋))

where N_base, β, and r₀ are configurable parameters stored in the CosmoID hash
input (ensuring deterministic decoding). N_min = 10 (Claim 3 minimum preserved).

Adaptive bit depth reduces total address size for cosmological batch operations
(Claim 38) while preserving maximum precision for near-field telemetry (Claim 26).

### Section E: 10 cm Precision Target

For Local Tier (Tier 0, r < 1 Mpc) operation with logarithmic normalization and
N = 63-bit Morton encoding, the UHA system achieves a worst-case physical
resolution bound of:

    δ_phys_local ≤ 10 cm

at Earth-surface distances (r ≈ 6.371 × 10⁻⁹ Mpc), verified as follows:

    r₀ = 1 AU = 1.496 × 10⁻⁷ Mpc
    R_H = c/H₀ = 299792.458/67.4 ≈ 4448 Mpc  (Planck 2018)
    δs₁ = 1 / 2^63 ≈ 1.084 × 10⁻¹⁹
    ln(1 + R_H/r₀) = ln(1 + 4448/1.496×10⁻⁷) = ln(2.97×10¹⁰) ≈ 24.12

    δr = r₀ · (1 + r/r₀) · δs₁ · ln(1 + R_H/r₀)
       ≈ 1.496×10⁻⁷ · 1.043 · 1.084×10⁻¹⁹ · 24.12
       ≈ 4.07 × 10⁻²⁵ Mpc
       ≈ 1.26 × 10⁻² m    [1.26 cm]

The 10 cm bound (Claim 50) is intentionally conservative. Actual computed
resolution with the Claim 47 default r₀=1 AU is ~1.26 cm — approximately 8×
better than the stated bound. Claim 50 is valid as a lower-precision floor.

Precision is a function of r₀. The resolution formula is:

    δr(r, r₀, N) = r₀ · (1 + r/r₀) · (1/2^N) · ln(1 + R_H/r₀)

At Earth surface (r = Earth radius = 6.371×10⁻⁹ Mpc), N=63:

    r₀ = 1 AU              → δr ≈ 1.26 cm   (Claim 47/50 canonical)
    r₀ = Earth radius      → δr ≈ 1.16 mm   (optimal for surface ops)
    r₀ = 1 km              → δr ≈ 0.99 mm
    r₀ = 1 m               → δr ≈ 1.14 cm   (degrades for r >> r₀)

NOTE: Resolution is best when r₀ ≈ r (the measurement distance). For r >> r₀,
the (1 + r/r₀) ≈ r/r₀ term dominates and resolution degrades. For ultra-precise
local operation, r₀ should be tuned to the scale of the region being addressed.

For practical deployment:
  - r₀ = 1 AU (Claim 47 default):  1.26 cm at Earth surface, N=63
  - r₀ = Earth radius:              1.16 mm at Earth surface, N=63
  - r₀ = Earth radius, N=42:       ~38 m (GPS-class, lowest bit depth)
  - DESI fiducial (cosmological):   arcsecond-class at Gpc scales

This precision target is relevant to Claim 26 (telemetry) for low-Earth orbit
spacecraft navigation, and to terrestrial sensor networks requiring sub-decimeter
positioning with cryptographically auditable coordinate provenance.

### Section G: Near-Origin Handling

For spatial position vectors with radial distance r approaching zero, spherical
coordinate angular components (θ, φ) become undefined. The UHA system resolves
this singularity via an explicit origin convention:

For r < ε_origin (where ε_origin = 10⁻³⁰ Mpc, below any physically measurable
scale), the angular components θ and φ are set to zero by convention, and the
normalized radial coordinate s₁ = 0 exactly. The CosmoID hash for such a position
includes the flag `origin=true`, marking the address as a zero-vector origin.

For encoders handling sub-epsilon precision (e.g., co-located sensors), the
caller must supply local Cartesian offsets as METADATA TLV fields rather than
relying on spherical coordinates; the spherical address encodes the origin and
the Cartesian metadata carries the sub-origin displacement.

This convention is deterministic and self-decoding: a decoder encountering an
address with s₁ = 0 and `origin=true` in the CosmoID applies zero-vector
convention without ambiguity.

### Section I: Cross-Survey ξ Comparison Without H₀ Alignment

In practice, different observational surveys — for example, a spectroscopic galaxy
redshift survey and a CMB-derived distance measurement catalog — may each report
spatial position measurements using distinct cosmological parameter sets that differ
in the assumed Hubble constant H₀. Under conventional distance measures, comparing
such surveys requires converting one dataset into the other's H₀ frame, a procedure
that introduces systematic frame-mixing artifacts proportional to the H₀ discrepancy
between surveys.

The present invention eliminates this conversion requirement. Because ξ = d_c / R_H(a)
is dimensionless and is normalized by the cosmological horizon radius derived from
each survey's own parameter set, ξ values from the first survey and ξ values from
the second survey may be compared directly — without converting either survey into a
common H₀ frame — provided the CosmoIDs of the two surveys are identical or are
related by a defined Gateway Transform G: S_i × Ω → S_j × Ω′ that maps one
parameter set to the other with bounded transformation error.

Any apparent tension between two surveys attributable solely to differing H₀
assumptions is eliminated by the ξ normalization. The residual after ξ-normalization
is the physically meaningful comparison: it reflects genuine differences in matter
distribution, dark energy evolution, or observational systematics, not coordinate
artifacts introduced by H₀ convention differences.

This comparison method is the primary commercial application of the ξ coordinate
output described in Claim 55 and the comparison method claimed in Claim 57. It is
directly demonstrated in the inventor's published analysis of DESI DR1 and DR2 BAO
data (Zenodo 10.5281/zenodo.19304441), where ξ-normalization removes approximately
90% of the reported Hubble tension as a coordinate artifact.

### Section H: CosmoID Semantics and Comparability

A CosmoID is a cryptographic hash of the complete encoding parameter set:
(H₀, Ω_m, Ω_Λ, Ω_r, Ω_k, a, r₀, R_H, normalization_mode, r_switch,
δ_threshold, N, N_base, β, r_ref, tier_boundaries, origin_flag).

Two spatial addresses are directly comparable — meaning their encoded indices
measure the same physical distance scale and can be differenced, averaged, or
sorted — if and only if their CosmoIDs are identical, or are related by a
defined Gateway Transform G: S_i × Ω → S_j × Ω′ (OMMP Layer 1) that maps one
parameter set to the other with bounded transformation error. Addresses whose
CosmoIDs are neither identical nor gateway-transformable must be re-encoded to
a common parameter set before comparison.

### Section F: Local-Mode / Cosmological-Mode Switch

The UHA system supports two operational modes with formally defined transition
criteria:

**Cosmological Mode** (the mode of Claims 1–40):
- R_H is computed via full Friedmann integral (Claim 5)
- Radial normalization: s₁ = r / R_H (linear) or s₁_log (logarithmic with large r₀)
- Hubble parameter H(a) includes all density components (Ω_r, Ω_m, Ω_k, Ω_Λ)
- Required when r ≥ r_switch or when ΔH/H (expansion correction) ≥ δ_threshold

**Local Mode** (new matter):
- R_H is replaced by a local reference radius R_local (e.g., Earth radius, solar
  system boundary, or user-defined)
- Hubble expansion term is set to zero: H(a) → H_local (constant or flat)
- Computation reduces to Euclidean normalization with CosmoID fingerprinting intact
- Logarithmic normalization (Section C) with small r₀ is the default
- Required when r < r_switch and expansion correction < δ_threshold

**Mode selection rule** (deterministic, implemented in encoder):

    if r < r_switch AND (H₀ · r / c) < δ_threshold:
        mode = LOCAL
        R_ref = R_local
    else:
        mode = COSMOLOGICAL
        R_ref = R_H(a)

Default values: r_switch = 100 Mpc, δ_threshold = 0.01 (1% expansion correction).

The selected mode and r_switch threshold are encoded in the CosmoID hash input,
ensuring that the address is fully self-decoding across both modes. A decoder
recovers the mode deterministically from the CosmoID without external metadata.

The mode switch enables seamless UHA addressing for:
- Terrestrial sensor networks (Local mode, 10 cm precision)
- Spacecraft navigation (Local mode transitioning to Cosmological as r increases)
- Cosmological surveys (Cosmological mode, arcsecond precision at Gpc scales)
- Multi-scale observational pipelines spanning both regimes

---

## NEW CLAIMS (41–52)

The following claims depend on or are independent of Claims 1–40 of the
provisional application US 63/902,536.

---

**41.** The method of claim 1, further comprising:

    h) determining, by the processor, a target physical precision ε_target;

    i) computing an adaptive bit depth N(a) = ⌈log₂(a · R_H(a) / ε_target)⌉,
       clamped to a range from a minimum bit depth N_min to a maximum bit depth
       N_max; and

    j) performing the encoding of step (d) using the adaptive bit depth N(a),
       wherein the adaptive bit depth varies as a function of the cosmic scale
       factor a such that the physical spatial resolution of the spatial address
       is bounded above by ε_target across all cosmic epochs.

---

**42.** The method of claim 41, wherein the adaptive bit depth N(a) and the
target precision ε_target are included in the hash input for computing the
CosmoID, such that a decoder can recover the adaptive bit depth deterministically
from the CosmoID without external metadata.

---

**43.** The method of claim 1, wherein normalizing the three coordinates
further comprises:

    a) partitioning a radial range from zero to the cosmological horizon radius
       into K contiguous radial bands, each band associated with a band index k
       and a radial range [r_{k-1}, r_k];

    b) determining the band index k corresponding to the radial distance r of the
       spatial position vector;

    c) computing a within-band normalized radial coordinate s₁_k = (r - r_{k-1})
       / (r_k - r_{k-1}); and

    d) assembling a composite spatial index comprising the band index k and a
       Morton encoding of (s₁_k, s₂, s₃), wherein the band index is stored as
       a prefix of the composite spatial index.

---

**44.** The method of claim 43, wherein K = 4 and the four radial bands
correspond to local, stellar, galactic, and cosmological spatial regimes,
with default boundaries at r₀ = 1 Mpc, r₁ = 100 Mpc, and r₂ = 1000 Mpc.

---

**45.** The method of claim 43, wherein the bit depth allocated to Morton
encoding within each radial band is individually configurable, and wherein
radial bands corresponding to smaller physical scales are allocated higher bit
depths than radial bands corresponding to larger physical scales.

---

**46.** The method of claim 1, wherein computing the first normalized coordinate
s₁ comprises applying a logarithmic transformation:

    s₁ = log(1 + r / r₀) / log(1 + R_H / r₀)

where r is the radial distance of the spatial position vector, R_H is the
cosmological horizon radius, and r₀ is a positive reference scale parameter,
such that the quantization density of the spatial index is proportional to
1/(r + r₀), concentrating spatial resolution at radial distances near zero
relative to r₀.

---

**47.** The method of claim 46, wherein r₀ is selected from the group
consisting of: 1 Astronomical Unit (AU), 1 parsec, 1 kiloparsec, and
1 megaparsec; and wherein r₀ is included in the hash input for computing
the CosmoID such that a decoder can recover r₀ deterministically from the
CosmoID.

---

**48.** The method of claim 1, wherein encoding the three normalized coordinates
comprises:

    a) determining a spatial regime of the spatial position vector based on
       its radial distance r;

    b) selecting a bit depth N from a predetermined mapping of spatial regime
       to bit depth, wherein spatial regimes corresponding to smaller radial
       distances are mapped to higher bit depths; and

    c) performing Morton Z-order encoding of the three normalized coordinates
       using the selected bit depth N;

    wherein the selected bit depth N and the spatial regime boundaries of the
    predetermined mapping are included in the CosmoID hash input.

---

**49.** The method of claim 48, wherein the bit depth N is selected according
to:

    N(r) = max(N_min, min(N_max, N_base - β · ⌊log₁₀(r / r_ref)⌋))

where N_base, β, r_ref, N_min, and N_max are configurable parameters, and
N_min is at least 10.

---

**50.** The method of claim 46, wherein the reference scale r₀ is 1 AU,
the maximum bit depth N_max is 63, and the spatial position vector is located
within 1 megaparsec of the origin, wherein the physical spatial resolution
of the spatial address satisfies:

    δ_phys ≤ 0.10 meters

at radial distances up to the radius of the Earth, providing centimeter-class
spatial addressing with cryptographically auditable coordinate provenance.

---

**51.** A computer-implemented method for mode-selective encoding of a spatial
position in an expanding spacetime framework, the method comprising:

    a) receiving, by a processor, a spatial position vector having three
       coordinates and a cosmic scale factor a;

    b) computing, by the processor, a radial distance r from the spatial
       position vector;

    c) determining, by the processor, an operational mode from:
       - a LOCAL mode, selected when r is less than a mode-switch threshold
         r_switch and when a Hubble expansion correction H₀ · r / c is less
         than a threshold δ_threshold; and
       - a COSMOLOGICAL mode, selected otherwise;

    d) in LOCAL mode: computing a reference radius R_local, setting the
       Hubble expansion term to zero, and encoding the spatial position using
       the method of claim 46 with R_local as the normalization reference;

    e) in COSMOLOGICAL mode: computing a cosmological horizon radius R_H(a)
       using the method of claim 5, and encoding the spatial position using
       the method of claim 1;

    f) generating a CosmoID by computing a cryptographic hash whose inputs
       include the selected mode, r_switch, δ_threshold, and the cosmological
       or local reference radius; and

    g) assembling a spatial address comprising the cosmic scale factor, the
       spatial index, the CosmoID, and an integrity verification code,
       wherein the spatial address is self-decoding across both modes.

---

**52.** The method of claim 51, wherein r_switch is 100 megaparsecs,
δ_threshold is 0.01, and R_local is selected from the group consisting of:
the radius of the Earth, the radius of the Moon's orbit, the radius of the
solar system, and a user-specified local bounding radius; and wherein a
decoder recovers the selected mode deterministically from the CosmoID without
external configuration.

---

**53.** The method of claim 1, further comprising:

    h) computing a three-dimensional uncertainty ellipsoid for the spatial
       position vector, the uncertainty ellipsoid defined by three semi-axis
       lengths (u₁, u₂, u₃) in spherical coordinates;

    i) normalizing the three semi-axis lengths by the cosmological horizon
       radius to produce three normalized uncertainty coordinates, each in
       a range from zero to one;

    j) encoding the three normalized uncertainty coordinates using a
       space-filling curve to produce a one-dimensional uncertainty index
       σ_unc; and

    k) including the uncertainty index σ_unc in the spatial address as an
       uncertainty vector field, wherein the spatial address encodes both
       the position and its associated measurement uncertainty in a single
       self-decoding structure.

---

**54.** The method of claim 1, further comprising:

    h) receiving a velocity vector having three components representing the
       proper motion or peculiar velocity of an object at the spatial
       position;

    i) normalizing the velocity vector components by a reference velocity
       scale to produce three normalized velocity coordinates, each in a
       range from zero to one;

    j) encoding the three normalized velocity coordinates using a
       space-filling curve to produce a one-dimensional velocity index
       σ_vel; and

    k) including the velocity index σ_vel in the spatial address as a
       velocity vector field, wherein the spatial address encodes position,
       velocity, and cosmological context in a single self-decoding tuple.

---

**55.** The method of claim 11, further comprising:

    h) extracting, by the processor, the CosmoID from the decoded spatial
       address, the CosmoID encoding the cosmological parameter set
       (H₀, Ω_m, Ω_Λ, Ω_r, Ω_k, a) and the normalization reference
       R_H used during encoding;

    i) computing, by the processor, a dimensionless comoving distance
       ratio:

           ξ = d_c / R_H(a)

       where d_c is the comoving distance recovered from the decoded
       spatial index and R_H(a) is the cosmological horizon radius
       recovered from the CosmoID, such that ξ ∈ [0, 1] is unit-free
       and independent of any particular choice of H₀, distance units,
       or reference frame convention;

    j) asserting, by the processor, the frame-invariance property:
       for any two spatial addresses A₁ and A₂ encoding the same physical
       position under different cosmological parameter sets or reference
       frames, ξ(A₁) = ξ(A₂) if and only if their CosmoIDs are identical
       or are related by a defined Gateway Transform G: S_i × Ω → S_j × Ω′;
       addresses for which this condition does not hold must be re-encoded
       to a common CosmoID before ξ values are compared; and

    k) outputting, by the processor, the dimensionless ratio ξ as a
       frame-agnostic, H₀-independent observable suitable for direct
       comparison across cosmological surveys, instruments, and epochs
       without unit conversion or reference frame transformation,
       wherein ξ is the unique self-decoding coordinate output of the
       spatial address that is invariant under the full group of
       CosmoID-preserving reference frame changes.

---

**56.** A system for computing and propagating spatial addresses with
associated measurement uncertainties, the system comprising:

    a) a memory configured to store a plurality of spatial addresses
       encoded according to the method of claim 1, each spatial address
       associated with at least one uncertainty index encoded according
       to the method of claim 53;

    b) a processor configured to:
       - execute an uncertainty propagation module that applies
         conservative interval arithmetic operations to pairs of
         uncertainty indices, producing a composite uncertainty index
         bounding the combined measurement uncertainty; and
       - execute a reconciliation module that identifies spatial addresses
         with overlapping uncertainty ellipsoids and computes a
         bias-reduced consensus position and uncertainty;

    wherein the conservative interval arithmetic operations preserve
    the property that the true spatial position lies within the
    decoded uncertainty ellipsoid with probability at least 1 - ε
    for a user-specified coverage parameter ε.

---

**60.** A computer-implemented method for generating a three-dimensional,
frame-agnostic structural map of the observable universe from observational
survey data, the method comprising:

    a) receiving, by a processor, a plurality of observational records from one
       or more astronomical surveys, each record comprising at least angular
       position information and a redshift-derived or distance-derived spatial
       measurement;

    b) determining, by the processor, for each observational record, a
       horizon-normalized radial coordinate:

           ξ = d_c / R_H(a)

       where d_c is the comoving distance derived from the redshift or distance
       measurement and R_H(a) = c / H(a) is the cosmological horizon radius
       computed from a cosmological parameter set associated with the record,
       such that ξ ∈ [0, 1] is dimensionless and independent of the absolute
       value of H₀;

    c) combining, by the processor, the normalized radial coordinate ξ with
       angular coordinates (θ, φ) for each record to produce a three-dimensional
       shell-coordinate position:

           P_shell = (ξ, θ, φ)

       representing the position of the observed object on a horizon-normalized
       celestial shell;

    d) determining, by the processor, that the cosmological parameter sets
       associated with the observational records are directly comparable by
       verifying that their associated CosmoIDs are identical or are related
       by a defined Gateway Transform with bounded transformation error;

    e) constructing, by the processor, a three-dimensional structural map of
       large-scale cosmological matter distribution by aggregating the
       shell-coordinate positions P_shell of step (c) into a spatial
       representation, wherein the spatial representation is one or more of:
       a point-cloud representation, a voxelized density field, a
       shell-banded matter distribution map, or a redshift-shell tomographic
       representation; and

    f) outputting, by the processor, the three-dimensional structural map for
       display, transmission, storage, or further statistical analysis,
       wherein the map is frame-agnostic in that no conversion to a common
       H₀ value is required as a precondition for comparing observations
       from surveys with differing assumed H₀ values.

---

**61.** The method of claim 60, wherein constructing the three-dimensional
structural map of step (e) further comprises:

    a) partitioning the normalized radial axis into a plurality of shell bands
       at radial intervals Δξ;

    b) counting, for each shell band, the number of observational records
       whose ξ coordinate falls within that band to produce a shell-band
       density profile; and

    c) comparing the shell-band density profile to a theoretical prediction
       derived from a cosmological model to identify residual structure
       not attributable to H₀-dependent coordinate artifacts.

---

**62.** The method of claim 60, wherein the cosmological parameter sets of
step (d) differ in their assumed value of H₀, and wherein the three-dimensional
structural map generated in step (e) is equivalent for both parameter sets
because the normalization of step (b) removes H₀ dependence from the radial
coordinate, such that the map reflects the underlying physical matter
distribution rather than a coordinate convention.

---

**57.** A computer-implemented method for frame-agnostic comparison of cosmological
survey data, the method comprising:

    a) receiving, by a processor, a first plurality of spatial position measurements
       from a first observational survey, each measurement associated with a
       first cosmological parameter set comprising at least a Hubble constant H₀⁽¹⁾,
       a matter density Ω_m⁽¹⁾, and a scale factor a;

    b) receiving, by the processor, a second plurality of spatial position
       measurements from a second observational survey, each measurement
       associated with a second cosmological parameter set comprising at least
       a Hubble constant H₀⁽²⁾ differing from H₀⁽¹⁾;

    c) computing, by the processor, for each measurement in the first plurality,
       a dimensionless comoving distance ratio:

           ξ⁽¹⁾ = d_c / R_H⁽¹⁾(a)

       where d_c is the comoving distance and R_H⁽¹⁾(a) = c / H(a) is the
       cosmological horizon radius computed from the first cosmological
       parameter set;

    d) computing, by the processor, for each measurement in the second plurality,
       a dimensionless comoving distance ratio:

           ξ⁽²⁾ = d_c / R_H⁽²⁾(a)

       computed from the second cosmological parameter set;

    e) generating, by the processor, a CosmoID for the first survey and a
       CosmoID for the second survey, each CosmoID comprising a cryptographic
       hash of the respective cosmological parameter set;

    f) determining, by the processor, that the CosmoID of the first survey and
       the CosmoID of the second survey are either:
       (i) identical, or
       (ii) related by a defined Gateway Transform G: S_i × Ω → S_j × Ω′
            that maps one cosmological parameter set to the other with
            bounded transformation error; and

    g) comparing, by the processor, ξ⁽¹⁾ values from the first survey directly
       to ξ⁽²⁾ values from the second survey without requiring conversion to a
       common H₀ value, wherein the comparison is valid because ξ is
       dimensionless and H₀-independent by construction, and wherein any
       apparent tension between the two surveys attributable to differing H₀
       assumptions is eliminated by the normalization of step (c) and (d).

---

**58.** The method of claim 57, wherein the first observational survey comprises
BAO distance measurements from a spectroscopic galaxy redshift survey and the
second observational survey comprises CMB-derived distance measurements, and
wherein the ξ comparison of step (g) identifies residual physical tension
between the surveys that is not attributable to differing H₀ assumptions.

---

**59.** The method of claim 57, wherein the Gateway Transform of step (f)(ii)
comprises a parameter-space mapping that preserves the comoving distance ratio
ξ to within a specified tolerance, and wherein the transformation error bound
is included in the CosmoID metadata such that a decoder can verify the
validity of the cross-survey comparison without recomputing the full
Friedmann integral.

---

## DEPENDENCY TREE

```
Claims 1-40 (provisional — unchanged)
    │
    ├── 41 (scale dilation — depends on 1)
    │     └── 42 (CosmoID encodes dilation params — depends on 41)
    │
    ├── 43 (multi-tier radial bands — depends on 1)
    │     ├── 44 (4-tier canonical partition — depends on 43)
    │     └── 45 (per-tier bit depth — depends on 43)
    │
    ├── 46 (logarithmic normalization — depends on 1)
    │     └── 47 (r₀ selection + CosmoID encoding — depends on 46)
    │
    ├── 48 (adaptive bit depth — depends on 1)
    │     └── 49 (N(r) formula — depends on 48)
    │
    ├── 50 (10 cm precision — depends on 46)
    │
    ├── 51 (mode switch — independent claim)
    │     └── 52 (default parameters — depends on 51)
    │
    ├── 53 (uncertainty vector σ_unc — depends on 1)
    ├── 54 (velocity vector σ_vel — depends on 1)
    ├── 55 (ξ frame-invariance — depends on Claim 11; TIGHTENED 2026-03-28)
    │     key assertion: ξ(A₁)=ξ(A₂) iff CosmoIDs identical or gateway-transformable
    ├── 56 (UHA + uncertainty propagation system — independent claim)
    │     └── depends on 1 and 53
    │
    ├── 57 (cross-survey ξ comparison — INDEPENDENT CLAIM; added 2026-03-29)
    │     commercial hook: comparing DESI/Planck/Euclid without H₀ alignment
    │     └── 58 (BAO vs CMB specific embodiment — depends on 57)
    │     └── 59 (Gateway Transform tolerance — depends on 57)
    │
    └── 60 (3D shell-geometry map generation — INDEPENDENT CLAIM; added 2026-03-29)
          data pipeline: survey records → ξ-normalized shell → 3D structural map
          └── 61 (shell-band density profile + model comparison — depends on 60)
          └── 62 (H₀-invariance of generated map — depends on 60)
```

Total new claims: 22 (Claims 41–62)
Total claims after amendment: 62

Independent claims added: 51, 56, 57, 60 (plus 41, 43, 46, 48 which depend on 1
but are structurally independent in scope).
Claim 55 depends on Claim 11 (tightened 2026-03-28).
Claim 57 added 2026-03-29: cross-survey comparison method (primary licensing hook).
Claim 60 added 2026-03-29: 3D shell-geometry map generation (data pipeline layer).
Total independent claims: 10 (provisional) + 7 (new) = 17. Within USPTO limit of 20.

---

## PRIOR ART DIFFERENTIATION (new matter)

| Feature | Closest Prior Art | Differentiation |
|---------|------------------|-----------------|
| Scale dilation | N/A (no cosmological coordinate system adapts bit depth with a) | Novel: deterministic N(a) from single formula |
| Multi-tier bands | HEALPix nside parameter | HEALPix is single-tier, angular only; no radial banding |
| Log normalization | World Geodetic System (WGS-84) log depth | WGS-84 is Earth-local, not self-decoding, no CosmoID |
| Adaptive bit depth | Variable-length spatial indexing (R-trees) | R-trees are query-time, not embedded in coordinate address |
| 10 cm precision | GPS (WGS-84, 3.5m without DGPS) | UHA: cryptographically auditable, cosmology-portable, self-decoding |
| Mode switch | None (no system spans cm to Gpc with same address format) | Fully novel: single address format, deterministic mode recovery |
| Uncertainty vector (σ_unc) | FITS WCS error columns (separate metadata) | UHA: uncertainty encoded IN the address, not as side-channel metadata |
| Velocity vector (σ_vel) | Gaia proper motion catalog (external table) | UHA: velocity embedded in self-decoding address tuple |
| ξ coordinate | Comoving distance ratio (textbook) | Novel: ξ as explicit named output of self-decoding address with CosmoID provenance |
| UHA + uncertainty system | N/U Algebra standalone | Novel: combination of coordinate address + conservative interval propagation in one system |

---

## NOTES FOR PATENT ATTORNEY

1. **CIP vs. Continuation**: All new features constitute new matter not
   disclosed in the provisional. A Continuation-in-Part (CIP) is required,
   not a plain Continuation. The CIP claims priority to 63/902,536 for
   Claims 1–40 and its own filing date for Claims 41–56.

2. **35 USC § 112 enablement**:
   - Claims 41–45, 48–49, 53–54: Derivable from existing `uso/L4_UHA_Transport/uha_encoder.py`
   - Claims 46–47, 50: `UHAEncoder.normalize_log()` — IMPLEMENTED 2026-03-28 in
     `uso/L4_UHA_Transport/uha_encoder.py`. Verified: δr = 1.26 cm at Earth surface
     (N=63, r₀=1 AU). `UHAEncoder.log_norm_resolution()` provides the § 112 verification formula.
   - Claims 48–49: `UHAEncoder.adaptive_bit_depth()` — IMPLEMENTED 2026-03-28.
     N varies 63→10 across radial decades; N_min=10 preserved per Claim 3.
   - Claims 51–52: `UHAEncoder.select_mode()` — IMPLEMENTED 2026-03-28. Returns
     UHAMode.LOCAL or UHAMode.COSMOLOGICAL deterministically. `UHAMode` enum exported.
   - Claims 55–56: ξ output exists in `tools/uha_xi_output.py`; uncertainty
     propagation exists in N/U Algebra repo (Zenodo 17172694)

   - Fix 1 — Near-origin singularity: `UHAEncoder.is_origin()` + zero-vector convention
     in `normalize_log()`. Spec: Section G (CosmoID `origin=true` flag). IMPLEMENTED 2026-03-28.
   - Fix 2 — CosmoID semantics: `COSMO_ID_COMPARABLE` constant + full definition in
     class docstring. Spec: Section H. IMPLEMENTED 2026-03-28.

   **§ 112 STATUS: All blocking items resolved. All clarity gaps closed. CIP is fileable.**

3. **Independent claim count**: 16 total independent claims after CIP.
   Within the 20-independent-claim limit without excess claim fees.

4. **Claim 55 (ξ coordinate) — tighten before filing**:
   As drafted, ξ = s₁ is thin (just reading the first coordinate). Strengthen
   by adding the invariance property: ξ is invariant under reference frame
   change and cosmological parameter convention. Make it a dependent claim
   on Claim 11 (decoding) and add: "wherein ξ is equal for any two spatial
   addresses encoding the same physical position regardless of the reference
   frame or cosmological parameter set used during encoding, provided the
   CosmoIDs are reconciled." That's the real novel assertion.

5. **Claim 56 (UHA + N/U Algebra) — prior art risk CLEARED (2026-03-27)**:
   N/U Algebra published on Zenodo (DOI 10.5281/zenodo.17172694) on
   2025-09-21 — 30 days before the UHA provisional filing (2025-10-21).
   This is within the 35 USC §102(b)(1)(A) one-year inventor grace period.
   NOT a double-patenting issue (N/U Algebra was never patented, only
   published open-source). Remaining risk: §103 obviousness argument that
   combining two inventor-published works is obvious. Counter: encoding
   uncertainty INSIDE the address tuple (not as external metadata) is not
   suggested by either publication separately.

6. **FIG. 8 alignment**: The filed provisional (FINAL.txt) describes FIG. 8 as
   "Multi-Vector Extension architecture for encoding uncertainty and velocity
   vectors." Claims 53–54 now match what FIG. 8 depicts — closing the
   spec/claims gap that existed in the provisional.

5. **Figures needed**: Add figures for:
   - FIG. 11: Multi-tier radial band diagram
   - FIG. 12: Log vs. linear normalization comparison
   - FIG. 13: Local-mode / cosmological-mode switch flowchart
   - FIG. 14: Adaptive bit depth allocation table (visual)
   - FIG. 15: ξ coordinate output pipeline
   - FIG. 16: UHA + uncertainty propagation system architecture

6. **Deadline**: Non-provisional due 2026-10-21. CIP can be filed any time
   before provisional expires. File CIP simultaneously with or before the
   non-provisional.

7. **OMMP — EXCLUDED from this CIP (deliberate decision, 2026-03-27)**:
   The OMMP (Observer, Measurement, Method, Probe) observer tensor framework
   [a, P_m, 0_t, 0_a] is NOT included in this CIP. Rationale:
   - OMMP is absent from the filed provisional — it would be entirely new matter
   - OMMP is different subject matter (observer classification vs. coordinate encoding)
   - Separate prosecution reduces cross-contamination risk if §101 is raised for OMMP
   - BROADER_PATENT_FRAMEWORK.md (internal strategy doc) recommends OMMP as Patent 3
   **Action**: File OMMP as a standalone provisional patent (Patent 3 in portfolio).
   Reference this CIP (and the UHA provisional) as related applications in the OMMP filing.
