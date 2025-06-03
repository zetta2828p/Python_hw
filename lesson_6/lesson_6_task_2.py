# Переименовать кнопку
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()

# Переход на указанную страницу
driver.get('http://uitestingplayground.com/textinput')

# Ввод текста в поле ввода
input_field = driver.find_element(By.ID, 'newButtonName')
input_field.send_keys('SkyPro')

# Нажатие на синюю кнопку
button = driver.find_element(By.ID, 'updatingButton')
button.click()

# Получение текста кнопки
button_text = button.text

# Вывод текста кнопки в консоль
print(button_text)

# Закрытие браузера
driver.quit()
