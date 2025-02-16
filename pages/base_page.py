from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        """Initialize with WebDriver"""
        self.driver = driver

    def open(self, url):
        """Open a website"""
        self.driver.get(url)

    def find_element(self, locator):
        """Find an element"""
        return self.driver.find_element(By.XPATH, locator)

    def click(self, locator):
        """Click an element"""
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        """Enter text into an input field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        """Check if an element is displayed"""
        return self.find_element(locator).is_displayed()

    def is_enabled(self, locator):
        """Check if an element is enabled"""
        return self.find_element(locator).is_enabled()
