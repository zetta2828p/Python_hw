from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Инициализация драйвера для Firefox
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/login")

    # Ввод логина
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    # Ввод пароля
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    # Клик по кнопке Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # Вывести текст с зеленой плашки в консоль
    flash_message = driver.find_element(By.ID, "flash").text
    print("Сообщение системы:", flash_message.split("×")[0].strip())

finally:
    # Закрытие браузера
    driver.quit()
