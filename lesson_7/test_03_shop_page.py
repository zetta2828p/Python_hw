# Тестовый сценарий
import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from checkout_overview_page import CheckoutOverviewPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop_operations(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]

    for product in products:
        main_page.add_product(product)

    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Natalya", "Martynenko", "353451")

    overview_page = CheckoutOverviewPage(driver)
    overview_page.wait_for_total()

    total = overview_page.get_total()
    assert total == "Total: $58.29", (
        "Итоговая сумма не $58.29"
    )
