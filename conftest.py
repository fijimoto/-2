import pytest
from faker import Faker

from config_reader import ConfigReader
from enums import Language
from browser import Browser

fake = Faker()
config = ConfigReader()


@pytest.fixture()
def random_email():
    return fake.email()


@pytest.fixture()
def random_password():
    return fake.password(length=8)


@pytest.fixture(params=[Language.RU, Language.EN], scope="function")
def lang(request):
    return request.param


@pytest.fixture(scope="function")
def driver(lang):
    drv = Browser.get(url=config.base_urls["steam"], lang=lang)
    yield drv
    Browser.quit()
