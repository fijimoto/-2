from selenium.webdriver.support.wait import WebDriverWait

from config_reader import ConfigReader

config = ConfigReader()


class BasePage:
    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, timeout or config.timeouts["wait_default"])
        self.fast_wait = WebDriverWait(
            driver, config.timeouts["wait_default"], poll_frequency=0.1)
