from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (By.XPATH, "//*[@id='sort_by_trigger']")
    SORT_PRICE_DESC = (By.XPATH, "//*[@id='Price_DESC']")
    ALL_PRICES = (
        By.XPATH, "//a[contains(@class, 'search_result_row')]//div[contains(@class, 'discount_final_price')]")
    LOADER = (
        By.XPATH, "//*[@id='search_result_container' and contains(@style, 'opacity: 0.5')]")

    def wait_for_open(self):
        self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))

    def click_sort_dropdown(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN))
        dropdown.click()

    def select_price_desc(self):
        option = self.wait.until(
            EC.element_to_be_clickable(self.SORT_PRICE_DESC))
        option.click()

    def wait_results_updated(self):
        self.fast_wait.until(EC.visibility_of_element_located(self.LOADER))
        self.fast_wait.until_not(EC.visibility_of_element_located(self.LOADER))

    def get_prices(self, count):
        prices_elements = self.wait.until(
            EC.presence_of_all_elements_located(self.ALL_PRICES))
        prices = []

        for element in prices_elements[:count]:
            text = element.text.splitlines()[-1]
            text = text.replace("€", "").replace(
                "₽", "").replace(",", ".").strip()
            try:
                price = float(text)
            except ValueError:
                price = 0.0
            prices.append(price)

        return prices
