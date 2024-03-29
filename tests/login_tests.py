
from pages.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("avantage2022test@yopmail.com", "!#Test13")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result1, "Login Verification")

    # @pytest.mark.run(order=1)
    # def test_invalidLogin(self):
    #     self.lp.logout()
    #     self.lp.login("test@email.com", "abcabcabc")
    #     result = self.lp.verifyLoginFailed()
    #     assert result == True