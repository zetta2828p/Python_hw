# Сверка итоговой суммы заказа
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def get_total(self):
        return self.driver.find_element(*self.total_label).text

    def wait_for_total(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            ec.presence_of_element_located(self.total_label)
        )
