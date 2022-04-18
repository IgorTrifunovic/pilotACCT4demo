"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://qc-gmpcl-mix-b2c.sbox.worldsbc.net/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(10)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        # driver.add_cookie({"name": "OptanonConsent", "value": "isIABGlobal=false&datestamp=Thu+Apr+14+2022+10%3A29%3A47+GMT%2B0200+(Central+European+Summer+Time)&version=6.32.0&consentId=606d25b8-9faa-4caf-920a-3e1945001bc8&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1&hosts=&genVendors="})
        driver.add_cookie({"name":"worldsportsbookcompetition.com", "value": "CCE68224-28D3-491F-B7EA-03634769DECA"})
        driver.add_cookie({"name":"OptanonAlertBoxClosed","value":"2022-04-14T09:28:16.485Z"})
        return driver