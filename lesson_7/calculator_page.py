# Класс страницы
from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(seconds)

    def click_button(self, button_text):
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    def get_screen_text(self):
        return self.driver.find_element(*self.screen).text

    def get_screen_locator(self):
        return self.screen
