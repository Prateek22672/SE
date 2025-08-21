"""
Core quadratic weather model utilities.

Model:
    T(x) = a*x^2 + b*x + c
"""

from dataclasses import dataclass


@dataclass
class QuadraticParams:
    a: float
    b: float
    c: float


def predict_temperature(params: QuadraticParams, x: float) -> float:
    """
    Compute T(x) = a*x^2 + b*x + c.

    Raises:
        TypeError: if non-numeric arguments are passed.
    """
    # Basic type checks for friendly errors
    for name, val in (("a", params.a), ("b", params.b), ("c", params.c), ("x", x)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Parameter {name} must be numeric, got {type(val).__name__}")
    return params.a * (x ** 2) + params.b * x + params.c


def parse_float(value: str, field: str) -> float:
    try:
        return float(value)
    except Exception as e:
        raise ValueError(f"Could not parse '{field}' as float (got '{value}').") from e
