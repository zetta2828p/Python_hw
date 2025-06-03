# Нажать на кнопку
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Переходим на указанную страницу
driver.get('http://uitestingplayground.com/ajax')

# Нашли элемент синяя кнопка, делаем клик
ajax_button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton')
ajax_button.click()

# Ждем, пока не появится элемент с текстом
green_text = WebDriverWait(driver, 20).until(
    ec.visibility_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
)

# Получаем текст из зеленой плашки
text = green_text.text

# Выводим текст в консоль
print(text)

# Закрываем браузер
driver.quit()
