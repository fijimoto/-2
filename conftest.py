import pytest

from config_reader import ConfigReader
from enums import Language
from browser import Browser

config = ConfigReader()


@pytest.fixture(params=[Language.RU, Language.EN], scope="function")
def lang(request):
    return request.param


@pytest.fixture(scope="function")
def driver(lang):
    Browser._driver = None
    drv = Browser(lang)
    drv.get(config.base_urls["steam"])
    yield drv
    Browser.quit()
