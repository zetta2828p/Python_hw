from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера для Firefox
driver = webdriver.Firefox()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/login")

# Ввод значения в поле username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

# Ввод значения в поле password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

# Нажатие кнопки Login
button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

# Вывод текста с зеленой плашки в консоль
success_message = driver.find_element(By.ID, "flash").text
print(driver.find_element(By.ID, "flash").text)

# Завершение работы драйвера
driver.quit()
