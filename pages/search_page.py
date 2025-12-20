from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_PRICE_DESC = (By.ID, "Price_DESC")
    GAME_CARDS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    PRICE_ELEMENT = (By.XPATH, ".//div[@data-price-final]")
    ACTIVE_SORT_OPTION = (
        By.XPATH, "//a[@id='Price_DESC' and contains(@class, 'active')]")

    def sort_by_price_desc(self):
        """Выбираем сортировку по убыванию цены"""
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        dropdown.click()

        price_option = self.wait.until(
            EC.element_to_be_clickable(self.SORT_PRICE_DESC)
        )
        price_option.click()

        self.wait.until(
            EC.presence_of_element_located(self.ACTIVE_SORT_OPTION)
        )

    def get_prices(self, count: int) -> list[int]:
        """Возвращаем список цен первых N игр"""
        cards = self.wait.until(
            EC.presence_of_all_elements_located(self.GAME_CARDS)
        )[:count]

        prices = []
        for card in cards:
            try:
                price_el = card.find_element(*self.PRICE_ELEMENT)
            except NoSuchElementException:
                continue

            price = int(price_el.get_attribute("data-price-final"))
            prices.append(price)

        return prices
