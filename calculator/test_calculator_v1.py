import unittest
from calculator.calculator_v1 import CalculatorV1


class TestCalculator(unittest.TestCase):
    @unittest.skip('just for testing')
    def test_calculator_add_positive_numbers(self):
        result = CalculatorV1(30, 70).calc_add()
        self.assertEqual(result, 100)

    def test_calculator_add_negative_numbers(self):
        result = CalculatorV1(-30, -70).calc_add()
        self.assertEqual(result, -100)

    def test_calculator_add_postive_and_negative_numbers(self):
        result = CalculatorV1(30, -70).calc_add()
        self.assertEqual(result, -40)