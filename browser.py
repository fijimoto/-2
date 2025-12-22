from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:
    _instance = None
    _driver = None

    def __new__(cls, language="en"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._driver = cls._create_driver(language)
        return cls._instance

    @staticmethod
    def _create_driver(language):
        options = Options()
        options.add_argument(f"--lang={language}")
        return webdriver.Chrome(options=options)

    @staticmethod
    def get_driver():
        return Browser._driver

    def quit(self):
        if Browser._driver is not None:
            Browser._driver.quit()
            Browser._driver = None
            Browser._instance = None
