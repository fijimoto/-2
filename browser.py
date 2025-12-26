from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options

from enums import Language
from config_reader import ConfigReader


class Browser:
    _driver = None
    _lang = None

    @staticmethod
    def get(url: str, lang: Language = Language.RU):
        if Browser._driver is None or Browser._lang != lang:
            Browser._create_driver(lang)
        Browser._driver.get(url)
        return Browser._driver

    @staticmethod
    def _create_driver(lang: Language):
        if Browser._driver:
            try:
                Browser._driver.quit()
            except WebDriverException as e:
                print(f"Ошибка при закрытии браузера: {e}")

        config = ConfigReader()
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": lang.value})

        window_size = config.browser.get("window_size", "1920,1080")
        options.add_argument(f"--window-size={window_size}")

        Browser._driver = webdriver.Chrome(options=options)
        Browser._lang = lang

    @staticmethod
    def quit():
        if Browser._driver:
            Browser._driver.quit()
        Browser._driver = None
        Browser._lang = None
