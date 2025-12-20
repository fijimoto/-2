from selenium import webdriver


class Browser:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = webdriver.Chrome()
        return cls._instance

    def get_driver(self):
        return self.driver

    def close(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
            Browser._instance = None
