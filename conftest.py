import pytest

from browser import Browser
from enums import Language


@pytest.fixture
def browser_instance(request):
    Browser._instance = None
    Browser._driver = None

    language = request.node.callspec.params.get("language", Language.EN)

    browser = Browser(language)
    driver = browser.get_driver()

    yield driver

    browser.quit()
