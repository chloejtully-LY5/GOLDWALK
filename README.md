# GOLDWALK

Marked returns on Cayley graphs of cyclic groups.

Cite: https://doi.org/10.5281/zenodo.23021217  
Code: https://github.com/chloejtully-LY5/GOLDWALK

Public oracle, n=5, start 1, lengths 2 through 6:

    4, 12, 52, 204, 820

## Tests

    python3 -m unittest test_goldwalk.py -v

## Smoke

    >>> from goldwalk import returns, walk, period_constant_itinerary
    >>> returns(5, 1, 5, sheet_modulus=2)
    closed: 204
    shards: {0: 66, 1: 80, 2: 34, 3: 24}
    even: 100
    odd: 104
    >>> walk(5, 1, (1, 4))
    ([1, 2, 1], 1)
    >>> walk(5, 1, (4, 1))
    ([1, 0, 1], 0)
    >>> period_constant_itinerary(5, 1, 2)
    10

Period of a^inf based at (a, 0) is m * (n / gcd(a, n)), not lcm.

Theorem card: there is no associative diagonal-only twist of C[Z_n].
Phi is a walk weight, not a product.
