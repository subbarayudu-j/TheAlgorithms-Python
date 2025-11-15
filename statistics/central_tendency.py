# central_tendency.py
from typing import Iterable, List, Union

Number = Union[int, float]


def mean(values: Iterable[Number]) -> float:
    """Return arithmetic mean of values. Raises ValueError if empty."""
    vals = list(values)
    if not vals:
        raise ValueError("mean() arg is an empty sequence")
    return round(sum(vals) / len(vals), 2)


def median(values: Iterable[Number]) -> float:
    """Return median. For even length returns the average of two middle values."""
    vals = sorted(values)
    if not vals:
        raise ValueError("median() arg is an empty sequence")
    n = len(vals)
    mid = n // 2
    if n % 2 == 1:
        return float(vals[mid])
    return (vals[mid - 1] + vals[mid]) / 2.0


def mode(values: Iterable[Number]) -> Union[Number, List[Number]]:
    """
    Return the mode value if unique, otherwise return a list of modes.
    Example: [1,2,2,3] -> 2 ; [1,1,2,2] -> [1,2]
    """
    vals = list(values)
    if not vals:
        raise ValueError("mode() arg is an empty sequence")
    freq = {}
    for v in vals:
        freq[v] = freq.get(v, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, count in freq.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes


# ---------- Quick usage ----------
if __name__ == "__main__":
    sample = [2, 5, 1, 2, 3, 5, 2]
    print("mean:", mean(sample))
    print("median:", median(sample))
    print("mode:", mode(sample))
