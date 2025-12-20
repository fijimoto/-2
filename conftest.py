import pytest

from browser import Browser
from enums import Language


@pytest.fixture
def driver(request):
    """Браузер для каждого теста (чистый кеш и куки)"""
    language = getattr(request, "param", Language.EN)

    browser = Browser(language=language.value)
    driver = browser.get_driver()
    driver.maximize_window()

    yield driver

    browser.quit()
