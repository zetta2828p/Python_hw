from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Инициализация драйвера для Google Chrome
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/dynamicid")

    # Поиск и клик по синей кнопке
    button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    button.click()

finally:
    # Завершение работы драйвера
    driver.quit()
