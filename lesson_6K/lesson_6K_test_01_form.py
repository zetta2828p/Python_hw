import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Фикстура для настройки драйвера браузера
@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    # Открытие страницы
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    fields_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    # Нажатие кнопки
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка подсветки поля Zip code
    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")

    # Проверка подсветки остальных полей
    valid_fields = [
        "first-name", "last-name", "address", "city", "country",
        "e-mail", "phone", "job-position", "company"
    ]

    for field_id in valid_fields:
        element = driver.find_element(By.ID, field_id)
        assert "alert-success" in element.get_attribute("class")
