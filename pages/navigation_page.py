import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _player_account_icon = '//*[@id="root"]/div/div[1]/div/header[1]/div/div[3]/div/div/button/span[1]/span/div'
    _user_logout_btn = '//*[@id="simple-menu"]/div[3]/div/div[2]/div[2]/p'  #avantage logout locator
    _confirm_age_btn = "/html/body/div[2]/div[3]/div/div/div[2]/div/div[2]/button/span"

    def navigate_confirmAge(self):
        self.elementClick(self._confirm_age_btn, locatorType="xpath")
