import csv
import os
import tempfile
import unittest

from expense_calc import calculator as c


def sample():
    ex = []
    c.add_expense(ex, "lunch", 10.0, "food")
    c.add_expense(ex, "bus", 20.0, "transport")
    c.add_expense(ex, "movie", 30.0, "entertainment")
    c.add_expense(ex, "book", 40.0, "other")
    return ex


class TestCalculator(unittest.TestCase):
    def test_total(self):
        self.assertEqual(c.calculate_total(sample()), 100.0)

    def test_total_empty(self):
        self.assertEqual(c.calculate_total([]), 0)

    def test_total_with_tax(self):
        self.assertAlmostEqual(c.total_with_tax(sample()), 10.5 + 22 + 36 + 40)

    def test_total_with_discount(self):
        self.assertAlmostEqual(c.total_with_discount(sample()), 9.5 + 18 + 24 + 40)

    def test_by_category(self):
        self.assertEqual(
            c.totals_by_category(sample()),
            {"food": 10.0, "transport": 20.0, "entertainment": 30.0, "other": 40.0},
        )

    def test_export_csv(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "out.csv")
            c.export_csv(sample(), p)
            with open(p) as f:
                rows = list(csv.reader(f))
        self.assertEqual(rows[0], ["name", "amount", "category"])
        self.assertEqual(len(rows), 5)


if __name__ == "__main__":
    unittest.main()
