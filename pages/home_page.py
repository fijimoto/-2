from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (
        By.XPATH, "//input[contains(@type, 'text') and contains(@role, 'combobox')]")
    SEARCH_BUTTON = (
        By.XPATH, "//form[contains(@role, 'search')]//button[contains(@type, 'submit')]")

    def is_opened(self):
        return self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))

    def input_game_name(self, game_name):
        element = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT))
        element.send_keys(game_name)

    def search_game(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON))
        button.click()
