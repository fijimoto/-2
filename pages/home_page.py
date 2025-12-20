from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@name='term']")
    SEARCH_BUTTON = (
        By.XPATH, "//form[@role='search']//button[@type='submit']")

    def open_home(self, url):
        self.open(url)

    def search_game(self, game_name):
        self.send_keys(self.SEARCH_INPUT, game_name)
        self.click(self.SEARCH_BUTTON)
