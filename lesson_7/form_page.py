# класс страницы
from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get(self.url)

    def fill_field(self, name, value):
        field = self.driver.find_element(By.NAME, name)
        field.clear()
        field.send_keys(value)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_field_class(self, field_id):
        element = self.driver.find_element(By.ID, field_id)
        return element.get_attribute("class")
