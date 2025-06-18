# Главная страница
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self, product_id):
        add_button = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*add_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
