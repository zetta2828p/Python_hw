from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера для Google Chrome
driver = webdriver.Chrome()

# Открытие страницы
driver.get("http://uitestingplayground.com/dynamicid")

# Клик по синей кнопке
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
sleep(5)

# Закрытие браузера
driver.quit()
