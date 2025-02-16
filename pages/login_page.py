from pages.base_page import BasePage
from locators.locators import PageLocators
import time


class LoginPage(BasePage):
    def login(self, email, password):
        """Perform user login"""
        time.sleep(1)
        self.enter_text(PageLocators.EMAIL_INPUT, email)
        time.sleep(1)
        self.enter_text(PageLocators.PASSWORD_INPUT, password)
        time.sleep(1)
        self.click(PageLocators.LOGIN_ENTER_BUTTON)

    def enter_button_front_page(self):
        """Click the enter button on the front page"""
        time.sleep(1)
        self.click(PageLocators.ENTER_BUTTON)

    def enter_button_login_page(self):
        """Click the enter button on the login page"""
        time.sleep(1)
        self.click(PageLocators.LOGIN_ENTER_BUTTON)

    def logo_button(self):
        time.sleep(1)
        self.click(PageLocators.LOGO)

    def logo_botton_is_displayed(self):
        self.is_displayed(PageLocators.LOGO)

    def logo_botton_is_enabled(self):
        self.is_enabled(PageLocators.LOGO)

    def profile_login_button_front_page(self):
        """Click the enter button on the front page"""
        time.sleep(1)
        self.click(PageLocators.USER_ACCOUNT_BUTTON)

    def forgot_password_button_login_page(self, email):
        """Click the enter button on the front page"""
        time.sleep(1)
        self.click(PageLocators.FORGOT_PASSWORD_BUTTON)
        time.sleep(1)
        self.enter_text(PageLocators.EMAIL_INPUT, email)
        time.sleep(1)
        self.click(PageLocators.RECOVER_BUTTON)

    def login_existing_user(self, email, password):
        """Login with existing user"""
        self.enter_text(PageLocators.EMAIL_INPUT, email)
        time.sleep(1)
        self.enter_text(PageLocators.PASSWORD_INPUT, password)
        time.sleep(1)
        self.click(PageLocators.LOGIN_ENTER_BUTTON)

    def get_error_message(self):
        """Wait and retrieve the login error message"""
        time.sleep(1)  # Wait to ensure the error message appears
        return self.find_element(PageLocators.PASSWORD_ERROR_MESSAGE).text

    def user_login_click_constractor(self):
        """Click on constructor button"""
        time.sleep(1)
        self.click(PageLocators.NAV_CONSTRUCTOR_BUTTON)
