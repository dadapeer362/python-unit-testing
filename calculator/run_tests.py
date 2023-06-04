# importing unittest and required modules
import unittest
from calculator import test_calculator_v1, test_calculator_v2

# creating an instance of the TestLoader
loader = unittest.TestLoader()

# creating an instance of the TestSuite
suite = unittest.TestSuite()

# add test cases to the TestSuite instance
suite.addTests(loader.loadTestsFromModule(test_calculator_v1))
suite.addTests(loader.loadTestsFromTestCase(test_calculator_v2.TestCalculator))

# create and instance of TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)

# run the TextTestRunner
test_results = runner.run(suite)

total_ran = test_results.testsRun
total_skipped = len(test_results.skipped)
total_errors = len(test_results.failures)
total_failures = len(test_results.errors)

print(f'Total Ran     : {total_ran}')
print(f'Total Skipped : {total_skipped}')
print(f'Total Errors  : {total_errors}')
print(f'Total Failures: {total_failures}')