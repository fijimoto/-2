from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_PRICE_DESC = (By.ID, "Price_DESC")
    GAME_CARDS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    PRICE_ELEMENT = (By.XPATH, ".//div[@data-price-final]")

    def sort_by_price_desc(self):
        """Выбирает сортировку по убыванию цены"""
        first_card = self.find(self.GAME_CARDS)

        self.click(self.SORT_DROPDOWN)
        self.click(self.SORT_PRICE_DESC)

        self.wait.until(EC.staleness_of(first_card))

        self.wait.until(EC.presence_of_all_elements_located(self.GAME_CARDS))

    def get_prices(self, count):
        """Возвращает список цен первых N игр"""
        cards = self.find_all(self.GAME_CARDS)[:count]
        prices = []

        for card in cards:
            try:
                price_el = card.find_element(*self.PRICE_ELEMENT)
                price = int(price_el.get_attribute("data-price-final"))
                prices.append(price)
            except:
                pass

        return prices
