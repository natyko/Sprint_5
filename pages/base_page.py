"""Base Page"""

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).pause(0.5).click().perform()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator))
            ).is_displayed()
        except TimeoutException:
            return False

    def is_enabled(self, locator):
        try:
            return self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator))
            ).is_enabled()
        except TimeoutException:
            return False

    def is_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        except TimeoutException:
            return False

    def get_text(self, locator):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, locator))).text
