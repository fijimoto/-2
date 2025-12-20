import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config_reader import ConfigReader
from enums import Language
from pages.home_page import HomePage
from pages.search_page import SearchPage


class TestSteamSearch:

    @pytest.mark.parametrize("language", [Language.RU, Language.EN])
    @pytest.mark.parametrize("game_name, count", [
        ("The Witcher", 10),
        ("Fallout", 20),
    ])
    def test_price_sorting_desc(self, driver, game_name, count, language):
        """Проверка сортировки игр по убыванию цены"""
        driver.get(ConfigReader.get("base_url"))
        WebDriverWait(driver, ConfigReader.get("timeout")).until(
            EC.presence_of_element_located(HomePage.SEARCH_INPUT)
        )

        home_page = HomePage(driver)
        search_page = SearchPage(driver)

        home_page.search_game(game_name)

        search_page.sort_by_price_desc()

        prices = search_page.get_prices(count)

        expected = sorted(prices, reverse=True)
        assert prices == expected, \
            f"Actual: {prices}, Expected: {expected}"
