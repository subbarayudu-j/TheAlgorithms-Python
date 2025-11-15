# frequency_stats.py
from typing import Iterable, Dict, List, Tuple, Union
from collections import Counter

Number = Union[int, float]


def frequency_table(values: Iterable[Number]) -> Dict[Number, int]:
    """Return a frequency table (value -> count)."""
    vals = list(values)
    if not vals:
        return {}
    return dict(Counter(vals))


def relative_frequency(values: Iterable[Number]) -> Dict[Number, float]:
    """Return relative frequencies (value -> proportion)."""
    vals = list(values)
    n = len(vals)
    if n == 0:
        return {}
    cnt = Counter(vals)
    return {k: v / n for k, v in cnt.items()}


def cumulative_frequency(values: Iterable[Number]) -> List[Tuple[Number, int]]:
    """
    Return a sorted list of (value, cumulative_count).
    Example: [1,1,2,3] -> [(1,2),(2,3),(3,4)]
    """
    vals = sorted(list(values))
    if not vals:
        return []
    cnt = Counter(vals)
    items = sorted(cnt.items())
    cum = []
    running = 0
    for val, count in items:
        running += count
        cum.append((val, running))
    return cum


def top_k_modes(values: Iterable[Number], k: int = 1) -> List[Number]:
    """
    Return top-k most frequent values (ties allowed). If k=1 returns list of top mode(s).
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    vals = list(values)
    if not vals:
        return []
    cnt = Counter(vals)
    most_common = cnt.most_common()
    # Determine cutoff frequency for top-k positions
    if k >= len(most_common):
        return [val for val, _ in most_common]
    cutoff = most_common[k - 1][1]
    return [val for val, c in most_common if c >= cutoff]


# ---------- Quick usage ----------
if __name__ == "__main__":
    data = [1, 2, 2, 3, 3, 3, 4]
    print("freq table:", frequency_table(data))
    print("relative freq:", relative_frequency(data))
    print("cumulative freq:", cumulative_frequency(data))
    print("top 2 modes:", top_k_modes(data, k=2))
