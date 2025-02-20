"""Registration Page"""

from pages.base_page import BasePage
from locators.locators import PageLocators


class RegisterPage(BasePage):
    def register(self, name, email, password):
        self.click(PageLocators.ENTER_BUTTON)
        self.click(PageLocators.REGISTER_BUTTON)
        self.enter_text(PageLocators.NAME_INPUT_REGISTER, name)
        self.enter_text(PageLocators.EMAIL_INPUT_REGISTER, email)
        self.enter_text(PageLocators.PASSWORD_INPUT_REGISTER, password)
        self.click(PageLocators.SUBMIT_BUTTON)

    def register_using_profile_login_button(self, name, email, password):
        self.click(PageLocators.USER_ACCOUNT_BUTTON)
        self.register(name, email, password)
