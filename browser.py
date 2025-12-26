from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from enums import Language
from config_reader import ConfigReader


class Browser:
    _driver = None

    def __new__(cls, lang: Language = Language.RU):
        if cls._driver is None:
            cls._create_driver(lang)
        return cls._driver

    @staticmethod
    def _create_driver(lang: Language):
        config = ConfigReader()
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": lang.value})

        window_size = config.browser.get("window_size", "1920,1080")
        options.add_argument(f"--window-size={window_size}")

        Browser._driver = webdriver.Chrome(options=options)

    @staticmethod
    def quit():
        if Browser._driver:
            Browser._driver.quit()
        Browser._driver = None
