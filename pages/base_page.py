from selenium.webdriver.support.ui import WebDriverWait

from config_reader import ConfigReader


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ConfigReader.get("timeout"))
