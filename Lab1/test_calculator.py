import unittest
from Lab1 import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertAlmostEqual(calculator.add(2.5, 0.75), 3.25)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(-1, -4), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(0, 1000000), 0)
        self.assertAlmostEqual(calculator.multiply(1.5, 2), 3.0)

    def test_divide(self):
        self.assertAlmostEqual(calculator.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
