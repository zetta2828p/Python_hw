from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера для Firefox
driver = webdriver.Firefox()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввод текста "Sky"
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")

# Очистка поля
input_field.clear()

# Ввод текста "Pro"
input_field.send_keys("Pro")

# Закрытие страницы браузера
driver.quit()
