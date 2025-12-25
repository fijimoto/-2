from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from enums import Language


class Browser:
    _instance = None
    _driver = None

    def __new__(cls, language=Language.EN):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._driver = cls._create_driver(language)
        return cls._instance

    @staticmethod
    def _create_driver(language):
        options = Options()
        lang_value = language.value if hasattr(language, "value") else language
        options.add_argument(f"--lang={lang_value}")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        return webdriver.Chrome(options=options)

    @staticmethod
    def get_driver():
        return Browser._driver

    @staticmethod
    def quit():
        if Browser._driver is not None:
            Browser._driver.quit()
            Browser._driver = None
            Browser._instance = None
