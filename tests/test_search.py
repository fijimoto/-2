import pytest

from config_reader import ConfigReader
from pages.home_page import HomePage
from pages.search_page import SearchPage

config = ConfigReader()


@pytest.mark.parametrize(("game_name", "count"), [("Fallout", 20), ("The Witcher", 10)])
def test_price_sorting_desc(driver, game_name, count):
    home_page = HomePage(driver, timeout=config.timeouts["wait_default"])
    search_page = SearchPage(driver, timeout=config.timeouts["wait_default"])

    assert home_page.is_opened(), "Главная страница не открылась"

    home_page.input_game_name(game_name)
    home_page.search_game()

    assert search_page.is_opened(), "Страница поиска не открылась"

    search_page.click_sort_dropdown()
    search_page.select_price_desc()
    search_page.wait_results_updated()

    prices = search_page.get_prices(count)

    assert prices == sorted(prices, reverse=True), (
        f"Сортировка по убыванию неверна!\n"
        f"Фактические цены: {prices}\n"
        f"Ожидалось: {sorted(prices, reverse=True)}"
    )
