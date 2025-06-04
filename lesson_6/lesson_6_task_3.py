# Дождаться картинки
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на указанную страницу
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
    )

# Ожидание загрузки всех изображений
WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.TAG_NAME, 'img')) == 5
    )


# Получение значения атрибута src у третьей картинки
images = driver.find_elements(By.TAG_NAME, 'img')
src_value = images[3].get_attribute('src')

# Вывод значения в консоль
print(src_value)

# Закрытие браузера
driver.quit()
