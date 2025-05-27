import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера для Google Chrome
driver = webdriver.Chrome()

try:
    # Переход на нужную страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Поиск и клик по основной (синий) кнопке
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    # Пауза на 5 секунд
    time.sleep(5)

    # Проверка, что кнопка может быть идентифицирована с помощью класса 'btn-primary'
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()
