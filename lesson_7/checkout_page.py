# Класс для работы со страницей оформления заказа
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(
            *self.postal_code_field).send_keys(postal_code)

    def continue_to_overview(self):
        self.driver.find_element(*self.continue_button).click()

    def fill_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.continue_to_overview()
