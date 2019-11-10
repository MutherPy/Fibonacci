import unittest
import test_fib

fibTestSuite = unittest.TestSuite()
fibTestSuite.addTest(unittest.makeSuite(test_fib.FibonTest))

runner = unittest.TextTestRunner(verbosity=2)
testResults = runner.run(fibTestSuite)

print("Errors")
print(len(testResults.errors))
print("Failures")
print(len(testResults.failures))
print("Skipped")
print(len(testResults.skipped))
