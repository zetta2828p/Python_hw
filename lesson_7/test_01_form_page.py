# Тестовый сценарий
import pytest
from selenium import webdriver
from form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    page = FormPage(driver)
    page.open()

    data = {
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

    for field, value in data.items():
        page.fill_field(field, value)

    page.submit()

    # Проверка подсветки zip-code (ожидаем alert-danger)
    zip_class = page.get_field_class("zip-code")
    assert "alert-danger" in zip_class.split(), (
        "Поле Zip code не подсвечено красным"
    )

    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field in valid_fields:
        field_class = page.get_field_class(field)
        assert "alert-success" in field_class.split(), (
            f"Поле {field} не подсвечено зеленым"
        )
