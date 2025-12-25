import pytest

from enums import Language
from pages.home_page import HomePage
from pages.search_page import SearchPage


class TestSteamSearch:

    @pytest.mark.parametrize("language", [Language.RU, Language.EN])
    @pytest.mark.parametrize("game_name, count", [
        ("The Witcher", 10),
        ("Fallout", 20),
    ])
    def test_price_sorting_desc(self, browser_instance, game_name, count, language):
        """Проверка сортировки игр по убыванию цены"""
        home_page = HomePage(browser_instance)
        search_page = SearchPage(browser_instance)

        home_page.open()
        assert home_page.is_opened(), "Главная страница не открылась"

        home_page.search_game(game_name)

        assert search_page.is_opened(), "Страница поиска не открылась"

        search_page.sort_by_price_desc()

        prices = search_page.get_prices(count)

        expected = sorted(prices, reverse=True)
        assert prices == expected, f"Actual: {prices}, Expected: {expected}"
