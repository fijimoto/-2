from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        """Ждем видимость элемента и возвращаем его"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Ждем появления всех элементов и возвращаем список"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Ждем кликабельности и кликаем"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        """Ждем видимость, очищаем и вводим текст"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
