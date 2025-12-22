from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@name='term']")
    SEARCH_BUTTON = (
        By.XPATH, "//form[@role='search']//button[@type='submit']")

    def search_game(self, game_name):
        """Поиск игры по названию"""
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(game_name)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_button.click()
