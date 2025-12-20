import pytest

from constants import TEST_DATA


class TestSteamSearch:
    @pytest.mark.parametrize("game_name, count, language, base_url", TEST_DATA)
    def test_price_sorting_desc(self, home_page, search_page, game_name, count, language, base_url):
        """Проверка сортировки игр по убыванию цены"""
        home_page.open_home(base_url)

        home_page.search_game(game_name)

        search_page.sort_by_price_desc()

        prices = search_page.get_prices(count)

        assert prices == sorted(prices, reverse=True), \
            f"[{language}] Цены не отсортированы по убыванию: {prices}"
