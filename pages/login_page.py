import time
import utilities.custom_logger as cl
from pages.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = '//*[@id="root"]/div/div[1]/div/header[1]/div/div[3]/div/div/p/span[1]'
    _login_with_email = '/html/body/div[2]/div[3]/div/div/div[2]/div/div[2]/button/span'
    _email_field = '//*[@id="logInForm"]/div/div[2]/div/div/div/input'
    _password_field = '//*[@id="logInForm"]/div/div[3]/div[2]/div/div/div/input'
    _login_button = '//*[@id="logInForm"]/button/span'
    _playerprofile_icon = '//*[@id="root"]/div/div[1]/div/header[1]/div/div[3]/div/div/button/span[1]/span/div'
    _playerenotification_tab = '//*[@id="simple-menu"]/div[3]/div/div[1]/div/div[1]/div'
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._login_with_email, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")
        time.sleep(1)

    def login(self, email="", password=""):
        self.nav.navigate_confirmAge()       # slucajno bio obrisan nav page
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.elementClick(self._playerprofile_icon, locatorType="xpath")
        result = self.isElementPresent(self._playerenotification_tab,
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[@class='dynamic-text help-block']",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.nav.navigateToSettings()
        self.elementClick(locator="//a[@href='/logout']", locatorType='xpath')
