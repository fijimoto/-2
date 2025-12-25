from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from config_reader import ConfigReader
from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_PRICE_DESC = (By.ID, "Price_DESC")
    GAME_CARDS = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    PRICE_ELEMENT = (By.XPATH, ".//div[@data-price-final]")
    LOADER = (
        By.XPATH, "//div[@id='search_result_container' and contains(@style, 'opacity: 0.5')]")

    def is_opened(self):
        """Проверка что страница поиска открыта"""
        return self.wait.until(EC.presence_of_element_located(self.GAME_CARDS))

    def sort_by_price_desc(self):
        """Сортировка по убыванию цены"""
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        dropdown.click()

        price_option = self.wait.until(
            EC.element_to_be_clickable(self.SORT_PRICE_DESC)
        )
        price_option.click()

        fast_wait = WebDriverWait(
            self.driver, ConfigReader.get("timeout"), poll_frequency=0.1)

        try:
            fast_wait.until(EC.presence_of_element_located(self.LOADER))
        except TimeoutException:
            pass

        fast_wait.until_not(EC.presence_of_element_located(self.LOADER))

        self.wait.until(
            EC.presence_of_all_elements_located(self.GAME_CARDS)
        )

    def get_prices(self, count):
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
