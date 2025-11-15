# dispersion.py
from typing import Iterable, List, Union
import math

Number = Union[int, float]


def _to_list(values: Iterable[Number]) -> List[float]:
    vals = list(values)
    if not vals:
        raise ValueError("sequence is empty")
    return [float(x) for x in vals]


def data_range(values: Iterable[Number]) -> float:
    """Return range = max - min."""
    vals = _to_list(values)
    return max(vals) - min(vals)


def variance(values: Iterable[Number], sample: bool = True) -> float:
    """
    Return variance. By default sample=True uses sample variance (n-1).
    Use sample=False for population variance (n).
    """
    vals = _to_list(values)
    n = len(vals)
    if sample and n < 2:
        raise ValueError("sample variance requires at least two data points")
    mean_val = sum(vals) / n
    ssd = sum((x - mean_val) ** 2 for x in vals)
    denom = n - 1 if sample else n
    return round(ssd / denom, 2)


def stdev(values: Iterable[Number], sample: bool = True) -> float:
    """Return standard deviation (sqrt of variance)."""
    final_val = math.sqrt(variance(values, sample=sample))
    return round(final_val, 2)


def iqr(values: Iterable[Number]) -> float:
    """
    Return interquartile range (Q3 - Q1).
    Uses simple median-of-halves method (consistent with many textbooks).
    """
    vals = sorted(_to_list(values))
    n = len(vals)
    mid = n // 2

    if n % 2 == 0:
        lower = vals[:mid]
        upper = vals[mid:]
    else:
        lower = vals[:mid]      # excludes median
        upper = vals[mid + 1:]  # excludes median

    def _median(arr: List[float]) -> float:
        m = len(arr)
        if m == 0:
            return 0.0
        mid_i = m // 2
        return arr[mid_i] if m % 2 == 1 else (arr[mid_i - 1] + arr[mid_i]) / 2.0

    q1 = _median(lower)
    q3 = _median(upper)
    return q3 - q1


# ---------- Quick usage ----------
if __name__ == "__main__":
    sample = [1, 2, 2, 3, 4, 7, 9]
    print("range:", data_range(sample))
    print("sample variance:", variance(sample, sample=True))
    print("population variance:", variance(sample, sample=False))
    print("sample stdev:", stdev(sample, sample=True))
    print("IQR:", iqr(sample))
