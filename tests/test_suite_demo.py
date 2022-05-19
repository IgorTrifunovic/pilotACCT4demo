import unittest
from tests.login_tests import LoginTests
from tests.register_test import RegisterTests


# Get all tests from the test clases
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterTests)


# Create a test suite combination all test clases
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
