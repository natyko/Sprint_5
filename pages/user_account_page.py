"""User Account Page"""

from locators.locators import PageLocators
from pages.login_page import LoginPage


class UserAccount(LoginPage):
    def user_logout(self):
        self.click(PageLocators.LOGOUT_BUTTON)
