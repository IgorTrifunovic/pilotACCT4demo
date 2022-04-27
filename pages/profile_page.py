import time
import utilities.custom_logger as cl
from pages.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class ProfilePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _player_profile_menu = '//*[@id="simple-menu"]/div[3]/div/div[2]/a[1]/div[1]/p'
    _playerprofile_icon = '//*[@id="root"]/div/div[1]/div/header[1]/div/div[3]/div/div/button/span[1]/span'
    _player_account_tab = '.account-MuiBadge-root.account-jss110'




    def clickPlayerAccountTab(self):
        self.elementClick(self._player_account_tab, locatorType="xpath")

    def clickProfileIcon(self):
        time.sleep(1)
        self.elementClick(self._playerprofile_icon,locatorType="css")

    def clickPlayerProfile(self):
        self.elementClick(self._player_profile_menu, locatorType="xpath")



