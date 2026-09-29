import unittest
from goldwalk import (
    N5_START1_PARITY,
    N5_START1_TOTALS,
    closed_totals,
    kappa,
    period_constant_itinerary,
    returns,
    walk,
)


class TestN5Oracle(unittest.TestCase):
    def test_totals_start1(self):
        self.assertEqual(
            closed_totals(5, 1, [2, 3, 4, 5, 6]),
            [N5_START1_TOTALS[L] for L in (2, 3, 4, 5, 6)],
        )

    def test_parity_start1(self):
        for L, (even, odd) in N5_START1_PARITY.items():
            r = returns(5, 1, L, sheet_modulus=2)
            self.assertEqual(r["even"], even)
            self.assertEqual(r["odd"], odd)

    def test_doors(self):
        self.assertEqual(walk(5, 1, (1, 4))[1], 1)
        self.assertEqual(walk(5, 1, (4, 1))[1], 0)
        self.assertEqual(walk(5, 1, (1, 1, 1, 1, 1))[1], 1)

    def test_period(self):
        self.assertEqual(period_constant_itinerary(5, 1, 2), 10)
        self.assertEqual(period_constant_itinerary(8, 2, 4), 16)


class TestKappa(unittest.TestCase):
    def test_unit(self):
        self.assertEqual(kappa(0, 1), 0)
        self.assertEqual(kappa(1, 1), 1)


if __name__ == "__main__":
    unittest.main()