import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Фикстура для настройки дайвера браузера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # Установка задержки
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажатие кнопок
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(
        By.XPATH, "//span[contains(@class, 'operator') and text()='+']"
    ).click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата
    result_element = WebDriverWait(driver, 46).until(
        ec.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    assert result_element, "Результат не равен 15"
