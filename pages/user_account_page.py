from pages.base_page import BasePage
from locators.locators import PageLocators
import time


class UserAccount(BasePage):
    def user_logout(self):
        """Click on log out button"""
        time.sleep(1)
        self.click(PageLocators.LOGOUT_BUTTON)
