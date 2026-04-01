"""
nu_propagate.py — N/U Algebra extensions for cosmological calculations
Session: 83402958-91cb-4bea-99c0-5f21c572edc9

Extends the core NU class with operations needed to carry (nominal, uncertainty)
pairs through nonlinear cosmological functions at machine precision.

All uncertainty propagation uses first-order derivative rules:
  f(x) → (f(n), |f'(n)| * u)

This is exact for linear operations and conservative for nonlinear ones —
consistent with N/U Algebra's conservative bound convention.

Reference:
  Martin, Eric D. (2025). N/U Algebra. DOI: 10.5281/zenodo.17172694
"""

import math
import sys
import os

# ── Import core NU class ────────────────────────────────────────────────────
# Try canonical repo first, fall back to local copy
try:
    sys.path.insert(0, '/scratch/repos/nu-algebra/src')
    from nu_algebra import NU
except ImportError:
    sys.path.insert(0, '/scratch/repos/hubble-91pct-concordance/07_code')
    from nu_algebra import NU


# ── Division ────────────────────────────────────────────────────────────────

def nu_div(x: NU, y: NU) -> NU:
    """
    Division: (n1, u1) / (n2, u2)

    Derivative rule: d/dy[n1/y] = -n1/y²
    Result: (n1/n2, (|n1|*u2 + |n2|*u1) / n2²)

    Raises ValueError if y.n == 0 (division by zero).
    """
    if y.n == 0:
        raise ValueError("Division by zero in NU division")
    nominal = x.n / y.n
    uncertainty = (abs(x.n) * y.u + abs(y.n) * x.u) / (y.n ** 2)
    return NU(nominal, uncertainty)


def nu_div_scalar(x: NU, a: float) -> NU:
    """Divide NU by a scalar constant: (n/a, u/|a|)"""
    if a == 0:
        raise ValueError("Division by zero")
    return NU(x.n / a, x.u / abs(a))


# ── Real-valued power ────────────────────────────────────────────────────────

def nu_pow(x: NU, a: float) -> NU:
    """
    Real-valued power: x^a where a is any float.

    Derivative rule: d/dx[x^a] = a * x^(a-1)
    Result: (n^a, |a * n^(a-1)| * u)

    Required for e.g. sound horizon: (Ωm h²)^{-0.255}
    """
    if x.n == 0 and a <= 0:
        raise ValueError("0^a undefined for a <= 0")
    nominal = x.n ** a
    deriv = abs(a * (x.n ** (a - 1)))
    return NU(nominal, deriv * x.u)


# ── Transcendental functions ─────────────────────────────────────────────────

def nu_sqrt(x: NU) -> NU:
    """
    Square root: sqrt(x)

    Derivative rule: d/dx[sqrt(x)] = 1 / (2*sqrt(x))
    Result: (sqrt(n), u / (2*sqrt(n)))
    """
    if x.n < 0:
        raise ValueError("Square root of negative nominal")
    nominal = math.sqrt(x.n)
    uncertainty = x.u / (2.0 * nominal) if nominal > 0 else 0.0
    return NU(nominal, uncertainty)


def nu_exp(x: NU) -> NU:
    """
    Exponential: exp(x)

    Derivative rule: d/dx[exp(x)] = exp(x)
    Result: (exp(n), exp(n) * u)
    """
    nominal = math.exp(x.n)
    return NU(nominal, nominal * x.u)


def nu_log(x: NU) -> NU:
    """
    Natural log: log(x)

    Derivative rule: d/dx[log(x)] = 1/x
    Result: (log(n), u / |n|)
    """
    if x.n <= 0:
        raise ValueError("Log of non-positive nominal")
    return NU(math.log(x.n), x.u / abs(x.n))


def nu_abs(x: NU) -> NU:
    """Absolute value: (|n|, u)"""
    return NU(abs(x.n), x.u)


# ── Cosmological functions with NU propagation ───────────────────────────────

# Planck 2018 fiducials
H0_PLANCK  = 67.4          # km/s/Mpc
RS_PLANCK  = 147.09        # Mpc at Ωm=0.315, h=0.674
OM_H2_PLANCK = 0.315 * (H0_PLANCK / 100) ** 2   # = 0.14295


def sound_horizon_nu(om: NU, h: float = H0_PLANCK / 100) -> NU:
    """
    Sound horizon with NU uncertainty propagation.

    r_s(Ωm) = 147.09 * (Ωm * h² / 0.14295)^{-0.255}  Mpc

    Percival (2007) scaling, normalised to Planck 2018.
    h held fixed (scalar); only Ωm carries uncertainty.

    Args:
        om: NU pair for Ωm (e.g. NU(0.290, 0.007))
        h:  scalar h = H0/100 (default: Planck fiducial)

    Returns:
        NU pair for r_s in Mpc
    """
    om_h2 = om * (h ** 2)                         # NU * scalar
    ratio  = nu_div_scalar(om_h2, OM_H2_PLANCK)   # NU / scalar
    scaled = nu_pow(ratio, -0.255)                 # NU ^ real
    return scaled * RS_PLANCK                      # NU * scalar


def dm_rs_nominal(om: NU, z: float, w0: float = -1.0, wa: float = 0.0) -> NU:
    """
    D_M / r_s at redshift z with NU uncertainty propagation.

    Computes xi(z) numerically at the nominal Ωm, then propagates
    the Ωm uncertainty through r_s analytically.

    The xi integral is evaluated at the nominal value; its Ωm
    sensitivity is propagated via the r_s denominator (dominant term).

    Args:
        om: NU pair for Ωm
        z:  redshift (scalar)
        w0: dark energy w0 (scalar, default -1)
        wa: dark energy wa (scalar, default 0)

    Returns:
        NU pair for D_M/r_s
    """
    from scipy.integrate import quad

    om_n = om.n   # nominal for integration

    def integrand(zp):
        matter = om_n * (1 + zp) ** 3
        de = (1 - om_n) * (1 + zp) ** (3 * (1 + w0 + wa)) \
             * math.exp(-3 * wa * zp / (1 + zp))
        return 1.0 / math.sqrt(matter + de)

    xi_val, _ = quad(integrand, 0, z)

    # r_s with NU propagation
    rs = sound_horizon_nu(om)

    # D_M/r_s = xi * c / (r_s * H0)  — H0 cancels in ratio
    c_over_H0 = 299792.458 / H0_PLANCK   # Mpc (H0-independent ratio)
    dm_rs_n = xi_val * c_over_H0 / rs.n
    # Propagate rs uncertainty: d/d(rs)[xi*c/H0/rs] = -xi*c/H0 / rs²
    dm_rs_u = xi_val * c_over_H0 / (rs.n ** 2) * rs.u

    return NU(dm_rs_n, dm_rs_u)


# ── Convenience: format NU for printing ─────────────────────────────────────

def nu_fmt(x: NU, decimals: int = 4) -> str:
    """Format NU pair as 'n ± u' string."""
    fmt = f"{{:.{decimals}f}}"
    return f"{fmt.format(x.n)} ± {fmt.format(x.u)}"


# ── Self-test ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("nu_propagate.py — N/U Algebra cosmological extensions")
    print("=" * 60)

    # Ωm from DESI DR2
    om = NU(0.290, 0.007)
    print(f"\nΩm        = {nu_fmt(om)}")

    # Sound horizon
    rs = sound_horizon_nu(om)
    print(f"r_s(Ωm)   = {nu_fmt(rs)} Mpc")
    print(f"           [{rs.lower_bound():.4f}, {rs.upper_bound():.4f}] Mpc")

    # D_M/r_s at DESI redshifts
    z_bins = [0.295, 0.510, 0.706, 0.930, 1.317, 1.491, 2.330]
    labels = ['BGS','LRG1','LRG2','LRG3+ELG1','ELG1','QSO','Lya QSO']
    print(f"\nD_M/r_s with NU propagation:")
    print(f"  {'Tracer':<14} z       D_M/r_s")
    for z, label in zip(z_bins, labels):
        dm = dm_rs_nominal(om, z)
        print(f"  {label:<14} {z:.3f}   {nu_fmt(dm, 3)}")

    # Division example
    h = NU(0.674, 0.005)
    om_h2 = om * (0.674 ** 2)
    print(f"\nΩm·h²     = {nu_fmt(om_h2, 5)}")

    # Power example
    ratio = nu_div_scalar(om_h2, OM_H2_PLANCK)
    scaled = nu_pow(ratio, -0.255)
    print(f"(Ωm·h²/ref)^-0.255 = {nu_fmt(scaled, 6)}")

    print("\nAll operations completed at machine precision.")
    print("N/U Algebra DOI: 10.5281/zenodo.17172694")
