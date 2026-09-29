"""GOLDWALK — marked returns on Cayley graphs of cyclic groups."""
from __future__ import annotations

from collections import Counter
from itertools import product
from typing import Dict, Iterable, List, Sequence, Tuple
import math

Word = Tuple[int, ...]


def kappa(fold: int, letter: int) -> int:
    return 1 if (letter != 0 and fold == letter) else 0


def walk(n: int, start: int, word: Sequence[int]) -> Tuple[List[int], int]:
    i = start % n
    folds = [i]
    c = 0
    for j in word:
        if not (1 <= j <= n - 1):
            raise ValueError(f"letter {j} not in 1..{n-1}")
        c += kappa(i, j)
        i = (i + j) % n
        folds.append(i)
    return folds, c


def letters(n: int) -> range:
    return range(1, n)


def closed_words(n: int, start: int, length: int) -> Iterable[Tuple[Word, int]]:
    start %= n
    for w in product(letters(n), repeat=length):
        folds, c = walk(n, start, w)
        if folds[-1] == start:
            yield w, c


def returns(
    n: int,
    start: int,
    length: int,
    sheet_modulus: int | None = None,
    sheets: int | None = None,
) -> Dict[str, object]:
    if sheet_modulus is None:
        sheet_modulus = sheets
    shards: Counter[int] = Counter()
    for w, c in closed_words(n, start, length):
        shards[c] += 1
    total = sum(shards.values())
    out: Dict[str, object] = {
        "n": n,
        "start": start % n,
        "length": length,
        "closed": total,
        "shards": dict(sorted(shards.items())),
    }
    if sheet_modulus == 2:
        out["even"] = sum(v for k, v in shards.items() if k % 2 == 0)
        out["odd"] = sum(v for k, v in shards.items() if k % 2 == 1)
    elif sheet_modulus is not None:
        buckets: Counter[int] = Counter()
        for k, v in shards.items():
            buckets[k % sheet_modulus] += v
        out["sheets"] = dict(sorted(buckets.items()))
    return out


def closed_totals(n: int, start: int, lengths: Sequence[int]) -> List[int]:
    return [int(returns(n, start, L)["closed"]) for L in lengths]


def period_constant_itinerary(n: int, a: int, sheet_modulus: int) -> int:
    if a % n == 0:
        raise ValueError("letter a must be nonzero in Z_n")
    return sheet_modulus * (n // math.gcd(a % n, n))


N5_START1_TOTALS = {2: 4, 3: 12, 4: 52, 5: 204, 6: 820}
N5_START1_PARITY = {2: (2, 2), 3: (10, 2), 4: (28, 24), 5: (100, 104)}