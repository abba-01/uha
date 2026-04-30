# Universal Horizon Address (UHA) — Formula White Paper
**Author:** Eric D. Martin | ORCID: 0009-0006-5944-1742
**Patent:** US 63/902,536 (non-provisional due 2026-10-21)
**Source repo:** /scratch/repos/uha/ | /scratch/repos/uha-blackbox/ | /scratch/repos/hubble-tensor/

---

## 1. Origin

UHA is a cosmological coordinate system that normalizes any spatial position against the particle horizon, producing a dimensionless invariant ξ ∈ [0,1] whose value is independent of H₀. Because both the comoving distance d_c and the Hubble horizon d_H scale as 1/H₀, their ratio cancels H₀ exactly. This invariance transforms the Hubble tension from a measurement conflict into a coordinate-frame artifact — approximately 93% of the apparent tension dissolves in ξ space; the remaining ~3% is a genuine physical residual (Ω_m discrepancy).

UHA is universal: it mints a structured address for ANY observable with a defined spacetime location, not only cosmological objects.

---

## 2. Physical Constants (Anchors)

```
c       = 299,792.458 km/s   (exact)
f₂₁     = 1,420.405751768 MHz  (21cm hydrogen line, exact)
H₀      = [67.4–73.04] km/s/Mpc  (parameter — encoded in CosmoID)
```

---

## 3. Cosmological Background Formulas

### Scale Factor → Redshift
```
a = 1 / (1 + z)
```

### Hubble Parameter Evolution
```
H(a) = H₀ √[Ω_r · a⁻⁴ + Ω_m · a⁻³ + Ω_Λ]

Ω_r = radiation density parameter
Ω_m = matter density parameter
Ω_Λ = dark energy density parameter
```

### Cosmic Lookback Time
```
T(a) = ∫₀ᵃ da' / (a' · H(a'))
```

### Comoving Particle Horizon (Hubble Horizon)
```
d_H(a) = c · ∫₀ᵃ da' / (a'² · H(a'))

At a=1 (today): d_H ≈ 14,000 Mpc  (R_H)
```

---

## 4. H₀ Invariance — Core Result

```
ξ = d_c / d_H

Both d_c and d_H scale as 1/H₀ → ratio is H₀-independent.
```

This is the foundational identity of UHA. Coordinates expressed in ξ are invariant under the choice of H₀, making cross-survey comparisons exact.

---

## 5. Spatial Normalization (3D → ξ)

### Step 1: Spherical to Comoving
```
Input: (r, θ, φ) in comoving Mpc
```

### Step 2: Dimensionless Unit Cube
```
s₁ = r / d_H(a)
s₂ = (1 − cos θ) / 2
s₃ = φ / (2π)

Result: (s₁, s₂, s₃) ∈ [0,1]³
```

### Step 3: Morton Z-Order Encoding
```
Discretize each sᵢ → N bits
Interleave bits → integer index I
ξ = (I + 1/2) / 2^(3N)

Properties:
  - Preserves 3D spatial locality
  - Hierarchical resolution: Δr = d_H / 2^N
  - Maps 3D space → 1D continuously and invertibly
```

### Resolution Schedule
```
Δr(N) = R_H / 2^N  where R_H = 14,000 Mpc

N=8:  Δr ≈ 55 Mpc    (cosmic void scale)
N=12: Δr ≈ 3.4 Mpc   (galaxy cluster scale)
N=16: Δr ≈ 0.21 Mpc  (galaxy scale)
N=20: Δr ≈ 13 kpc    (stellar group scale)
N=24: Δr ≈ 0.84 kpc  (open cluster scale)
Optimal cosmological range: N = 8–24 bits
```

---

## 6. Time Offset

```
Δt = (d_H / c) · ξ   [units: Gyr]
```

---

## 7. UHA Record Format (Encoded String)

```
Anchor=<T>[Gyr];
Redshift_z=<z>;
Scale_a=<a>;
Horizon=<d_H>[Gly];
Offset_Tedge=<Δt>[Gyr];
Check=<CRC>

Example:
Anchor=1.000000E-02Gyr; Redshift_z=1.385800E+02;
Scale_a=7.164352E-03; Horizon=4.260832E+01Gly;
Offset_Tedge=1.377689E+01Gyr; Check=11170
```

---

## 8. Decode Path

```
1. Read: T (Anchor), d_H (Horizon), Δt (Offset_Tedge)
2. Recover ξ = Δt / (d_H / c)
3. Index I = ⌊ξ · 2^(3N)⌋
4. De-interleave bits → (x_N, y_N, z_N)
5. s₁ = x_N / 2^N, etc.
6. Recover (r, θ, φ) via inverse of Step 2
```

---

## 9. CosmoID Fingerprint

```
CosmoID = sha256(H₀, Ω_m, Ω_r, Ω_Λ)  [64-bit truncated]

Purpose:
  - Labels the cosmological parameter set used for this address
  - Enables coordinate transformation between parameter sets
  - Detects parameter mismatches across datasets
```

---

## 10. UHA Tuple Structure

```
A = (a, ξ, û, CosmoID; anchors)

a       = cosmic scale factor at observation epoch
ξ       = normalized Morton spatial index ∈ [0,1]
û       = unit directional 3-vector
CosmoID = parameter fingerprint (sha256)
anchors = optional reference metadata (redshift, survey name, etc.)
```

---

## 11. OMMP Integration

```
oMMP record: [UHA_observer_location].[observation_tuple]

Observer anchors the record, not the observed event.
The dot separates observer address from measurement tuple.
```

---

## 12. Hubble Tension Resolution Results

| Tension | H₀ artifact removed in ξ | Physical residual | Physical cause |
|---------|--------------------------|-------------------|---------------|
| H₀ (SNe Ia) | ~93% | ~7% | Ω_m discrepancy |
| H₀ (Cepheid geometric) | Survives (expected) | ~3% | Genuine H₀ signal |
| BAO | ~0% | ~100% | Ω_m (DESI vs Planck) |
| S8/σ₈ | ~0–3% | ~97% | Ω_m / σ₈ |
| Age tension | Large (SH0ES) | Dissolves at H₀≈70 | 4/7 GCs exceed SH0ES age |

**Convergent signal:** All late-universe probes → Ω_m ≈ 0.295 vs Planck 0.315 (~6%)

Published: DOI 10.5281/zenodo.19154280
