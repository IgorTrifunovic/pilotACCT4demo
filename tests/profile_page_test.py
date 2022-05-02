from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.pp = ProfilePage(self.driver)


    def test_avatar_photo_change(self):
        self.lp.login("avantage2022test@yopmail.com", "!#Test13")
        self.pp.clickProfileIcon()
        self.pp.clickPlayerAccountTab()
        self.pp.clickPlayerProfile()