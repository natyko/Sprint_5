import time

from pages import user_account_page
from pages.login_page import LoginPage


def test_constructor_click(driver):
    """Test navigation from user account to constructor."""
    login_page = LoginPage(driver)

    fixed_email = "naty@yopmail.com"
    fixed_password = "Privet123"

    login_page.open("https://stellarburgers.nomoreparties.site")
    time.sleep(2)
    login_page.profile_login_button_front_page()
    login_page.login_existing_user(fixed_email, fixed_password)
    time.sleep(2)
    login_page.user_login_click_constractor()


def test_logout_button(driver):
    """Test clicking on the logout button."""
    login_page = LoginPage(driver)
    fixed_email = "123@yopmail.com"
    fixed_password = "privet123$"
    login_page.open("https://stellarburgers.nomoreparties.site/login")
    time.sleep(1)
    login_page.login_existing_user(fixed_email, fixed_password)
    login_page.profile_login_button_front_page()
    login_page.profile_login_button_front_page()
    time.sleep(2)
    user_account_page.UserAccount(driver).user_logout()
