import unittest

from real_estate import rental_yield
from roi_calculator import calculate_profit, calculate_roi
from startup_valuation import startup_value


class TestRoiCalculator(unittest.TestCase):
    def test_calculate_profit(self):
        self.assertEqual(calculate_profit(1000, 1250), 250)

    def test_calculate_roi(self):
        self.assertEqual(calculate_roi(1000, 1250), 25)

    def test_calculate_roi_rejects_zero_initial_investment(self):
        with self.assertRaises(ValueError):
            calculate_roi(0, 1250)


class TestRealEstateCalculator(unittest.TestCase):
    def test_rental_yield(self):
        income, yield_percent = rental_yield(200000, 14400, 3400)

        self.assertEqual(income, 11000)
        self.assertEqual(yield_percent, 5.5)

    def test_rental_yield_rejects_negative_costs(self):
        with self.assertRaises(ValueError):
            rental_yield(200000, 14400, -1)


class TestStartupValuation(unittest.TestCase):
    def test_startup_value(self):
        self.assertEqual(startup_value(500000, 0.2), 3500000)

    def test_startup_value_rejects_negative_revenue(self):
        with self.assertRaises(ValueError):
            startup_value(-1, 0.2)


if __name__ == "__main__":
    unittest.main()
