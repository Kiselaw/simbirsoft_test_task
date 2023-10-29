from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

WAIT_TIME = 5


class BasePage:
    """Определение базовых методов для всех страниц."""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                           message=f"Can't find element by locator {locator}")

    def get_elements(self, locator, wait_time=WAIT_TIME):
        return WebDriverWait(self.driver, wait_time).until(EC.presence_of_all_elements_located((By.XPATH, locator)),
                                                           message=f"Can't find elements by locator {locator}")

    def get_subelements(self, element, locator):
        return element.find_elements(By.XPATH, locator)

    def click(self, element):
        element.click()

    def input(self, element, data):
        element.send_keys(data)

    def get_the_page(self, url):
        return self.driver.get(url)

    def refresh(self):
        self.driver.refresh()
