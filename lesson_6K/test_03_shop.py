import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Фикстура для настройки драйвера браузера
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop_operations(driver):
    # Открытие сайта магазина
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Добавление товаров в корзину
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for item_id in items_to_add:
        add_to_cart_button = driver.find_element(By.ID, item_id)
        add_to_cart_button.click()

    # Переход в корзину
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    # Нажатие кнопки Checkout
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Заполнение формы данными
    first_name_field = driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("Natalya")

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Martynenko")

    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("353451")

    # Нажатие кнопки Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Проверка итоговой стоимости
    total_label = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    assert "Total: $58.29" in total_label.text, "Итоговая сумма не $58.29"
