import pytest

from browser import Browser


@pytest.fixture
def browser_instance(request):
    Browser._instance = None
    Browser._driver = None

    language = request.node.callspec.params.get("language", "en")
    lang_value = language.value if hasattr(language, "value") else language

    browser = Browser(lang_value)
    driver = browser.get_driver()
    driver.maximize_window()

    yield driver

    browser.quit()
