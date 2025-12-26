from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_DROPDOWN = (
        By.XPATH, "//button[contains(@class, 'trigger') and contains(@id, 'sort_by_trigger')]")
    SORT_PRICE_DESC = (
        By.XPATH, "//*[contains(@id,'sort_by_droplist')]//a[contains(@id,'Price_DESC')]")
    ALL_PRICES = (By.CSS_SELECTOR,
                  "a.search_result_row div.discount_final_price")
    LOADER = (
        By.XPATH, "//div[@id='search_result_container' and contains(@style, 'opacity: 0.5')]")

    def is_opened(self):
        """Проверка что страница поиска открыта"""
        return self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))

    def click_sort_dropdown(self):
        """Клик по dropdown сортировки"""
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN))
        dropdown.click()

    def select_price_desc(self):
        """Выбор сортировки по убыванию цены"""
        option = self.wait.until(
            EC.element_to_be_clickable(self.SORT_PRICE_DESC))
        option.click()

    def wait_results_updated(self):
        """Ожидание обновления результатов"""
        self.fast_wait.until(EC.visibility_of_element_located(self.LOADER))
        self.fast_wait.until_not(EC.visibility_of_element_located(self.LOADER))

    def get_prices(self, count):
        """Получение списка цен"""
        prices_elements = self.wait.until(
            EC.presence_of_all_elements_located(self.ALL_PRICES))
        all_prices = []

        for p in prices_elements:
            lines = p.text.splitlines()
            text = lines[-1].replace("€", "").replace(",",
                                                      ".").replace("₽", "").strip()
            try:
                price = float(text)
            except ValueError:
                price = 0.0
            all_prices.append(price)

            if len(all_prices) >= count:
                break

        return all_prices
