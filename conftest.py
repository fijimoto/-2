import pytest

from browser import Browser
from pages.home_page import HomePage
from pages.search_page import SearchPage


@pytest.fixture(scope="session")
def driver():
    """Singleton браузер на всю сессию тестов"""
    browser = Browser()
    driver = browser.get_driver()
    driver.maximize_window()
    yield driver
    browser.close()


@pytest.fixture
def home_page(driver):
    """Фикстура для главной страницы"""
    return HomePage(driver)


@pytest.fixture
def search_page(driver):
    """Фикстура для страницы результатов"""
    return SearchPage(driver)
