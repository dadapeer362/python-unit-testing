import unittest
from calculator.calculator_v2 import CalculatorV2


class TestCalculator(unittest.TestCase):
    # It will calls first for every test case before running
    def setUp(self):
        print('setUp Invoked!')
    
    # It will calls last for every test case after running
    def tearDown(self):
        print('tearDown Invoked!')

    '''
    To test addition test cases
    '''
    # To skip the test case
    @unittest.skip
    def test_calculator_add_positive_numbers(self):
        print('Adding two positive numbers')
        result = CalculatorV2(30, 70).calc_add()
        self.assertEqual(result, 100)

    # To skip the test case with reason
    @unittest.skip('not required to test')
    def test_calculator_add_negative_numbers(self):
        print('Adding two negative numbers')
        result = CalculatorV2(-30, -70).calc_add()
        self.assertEqual(result, -100)

    def test_calculator_add_postive_and_negative_numbers(self):
        print('Adding one positive and one negative numbers')
        result = CalculatorV2(30, -70).calc_add()
        self.assertEqual(result, -40)

    '''
    To test substraction test cases
    '''
    def test_calculator_sub_positive_numbers(self):
        print('Substracting two positive numbers')
        result = CalculatorV2(30, 70).calc_sub()
        self.assertEqual(result, -40)

    def test_calculator_sub_negative_numbers(self):
        print('Substracting two negative numbers')
        result = CalculatorV2(-30, -70).calc_sub()
        self.assertEqual(result, 40)

    def test_calculator_sub_postive_and_negative_numbers(self):
        print('Substracting one positive and one negative numbers')
        result = CalculatorV2(30, -70).calc_sub()
        self.assertEqual(result, 101)