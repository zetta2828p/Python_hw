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
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Поиск поля ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Ввод текста "Sky"
    input_field.send_keys("Sky")

    # Очистка поля
    input_field.clear()

    # Ввод текста "Pro"
    input_field.send_keys("Pro")

finally:
    # Закрытие браузера
    driver.quit()