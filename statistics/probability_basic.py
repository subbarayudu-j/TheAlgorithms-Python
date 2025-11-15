# probability_basic.py
from typing import Iterable
import math
from collections import Counter

def factorial(n: int) -> int:
    """Return n! for non-negative integer n."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    return math.prod(range(1, n + 1)) if n > 0 else 1


def permutations(n: int, r: int) -> int:
    """Return P(n, r) = n! / (n-r)!"""
    if not (0 <= r <= n):
        raise ValueError("require 0 <= r <= n")
    return factorial(n) // factorial(n - r)


def combinations(n: int, r: int) -> int:
    """Return C(n, r) = n! / (r! (n-r)!)"""
    if not (0 <= r <= n):
        raise ValueError("require 0 <= r <= n")
    return factorial(n) // (factorial(r) * factorial(n - r))


def binomial_pmf(k: int, n: int, p: float) -> float:
    """
    Return binomial probability P(X = k) for X ~ Binomial(n, p)
    """
    if not (0 <= k <= n):
        raise ValueError("k must be between 0 and n")
    if not (0.0 <= p <= 1.0):
        raise ValueError("p must be between 0 and 1")
    return combinations(n, k) * (p ** k) * ((1 - p) ** (n - k))


def empirical_probability(event_values: Iterable, sample_space_values: Iterable) -> float:
    """
    Compute empirical probability of event_values within sample_space_values.
    event_values may be a subset of sample_space_values (both iterable of outcomes).
    Example: empirical_probability([1,1],[1,1,2,3]) -> 0.5
    """
    s = list(sample_space_values)
    if not s:
        raise ValueError("sample space cannot be empty")
    event_count = sum(1 for x in s if x in set(event_values))
    return event_count / len(s)


# ---------- Quick usage ----------
if __name__ == "__main__":
    print("5! =", factorial(5))
    print("P(5,2) =", permutations(5, 2))
    print("C(5,2) =", combinations(5, 2))
    print("Binomial P(X=2; n=5, p=0.3) =", binomial_pmf(2, 5, 0.3))
    print("Empirical prob of [1] in [1,1,2,3] =", empirical_probability([1], [1,1,2,3]))
