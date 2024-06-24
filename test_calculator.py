# test_calculator.py

import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        result = multiply(3, 5)
        self.assertEqual(result, 15)

    def test_multiply_negative_numbers(self):
        result = multiply(-4, 2)
        self.assertEqual(result, -8)

    def test_multiply_float_numbers(self):
        result = multiply(2.5, 4)
        self.assertAlmostEqual(result, 10.0, places=1)

    def test_multiply_zero(self):
        result = multiply(10, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
