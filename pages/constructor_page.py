from locators.locators import PageLocators
import time

from pages.login_page import LoginPage


class Constractor(LoginPage):
    def constructor_buttons(self):
        """Click on log out button"""
        time.sleep(1)
        self.click(PageLocators.SAUCES_BUTTON)
        time.sleep(1)
        self.click(PageLocators.INGREDIENTS_BUTTON)
        time.sleep(1)
        self.click(PageLocators.BUNS_BUTTON)

    def navigate_to_constructor(self):
        """Navigate to the constructor page"""
        time.sleep(1)
        self.click(PageLocators.NAV_CONSTRUCTOR_BUTTON)
        time.sleep(1)
