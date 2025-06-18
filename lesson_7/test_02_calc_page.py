# Тестовый сценарий
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    page.open()

    page.set_delay("45")

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    screen_locator = page.get_screen_locator()
    wait = WebDriverWait(driver, 46)
    result = wait.until(
        ec.text_to_be_present_in_element(
            screen_locator, "15"
        )
    )

    assert result, "Результат не равен 15"
