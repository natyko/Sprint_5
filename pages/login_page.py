"""Login Page"""

from pages.base_page import BasePage
from locators.locators import PageLocators


class LoginPage(BasePage):
    def login(self, email, password):
        self.enter_text(PageLocators.EMAIL_INPUT, email)
        self.enter_text(PageLocators.PASSWORD_INPUT, password)
        self.click(PageLocators.LOGIN_ENTER_BUTTON)

    def enter_button_front_page(self):
        self.click(PageLocators.ENTER_BUTTON)

    def enter_button_login_page(self):
        self.click(PageLocators.LOGIN_ENTER_BUTTON)

    def logo_button(self):
        self.click(PageLocators.LOGO)

    def logo_button_is_displayed(self):
        return self.is_displayed(PageLocators.LOGO)

    def logo_button_is_enabled(self):
        return self.is_enabled(PageLocators.LOGO)

    def profile_login_button_front_page(self):
        self.click(PageLocators.USER_ACCOUNT_BUTTON)

    def orders_button(self):
        self.click(PageLocators.ORDERS_BUTTON)

    def forgot_password_button_login_page(self, email):
        self.click(PageLocators.FORGOT_PASSWORD_BUTTON)
        self.enter_text(PageLocators.EMAIL_INPUT, email)
        self.click(PageLocators.RECOVER_BUTTON)

    def login_existing_user(self, email, password):
        self.enter_text(PageLocators.EMAIL_INPUT, email)
        self.enter_text(PageLocators.PASSWORD_INPUT, password)
        self.click(PageLocators.LOGIN_ENTER_BUTTON)

    def get_error_message(self):
        return self.get_text(PageLocators.PASSWORD_ERROR_MESSAGE)

    def user_login_click_constructor(self):
        self.click(PageLocators.NAV_CONSTRUCTOR_BUTTON)

    def constructor_buttons(self):
        self.click(PageLocators.SAUCES_BUTTON)
        self.click(PageLocators.INGREDIENTS_BUTTON)
        self.click(PageLocators.BUNS_BUTTON)

    def navigate_to_constructor(self):
        self.click(PageLocators.NAV_CONSTRUCTOR_BUTTON)
