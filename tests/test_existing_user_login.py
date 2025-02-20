from config import BASE_URL, TEST_USER
from locators.locators import PageLocators
from pages.login_page import LoginPage


def test_user_login(driver):
    """Test login via enter button on main page"""
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.enter_button_front_page()
    login_page.login_existing_user(TEST_USER["email"], TEST_USER["password"])

    # Verify successful login
    assert login_page.is_displayed(PageLocators.USER_ACCOUNT_BUTTON), (
        "User account button not visible after login"
    )


def test_login_with_user_account(driver):
    """Test login via profile login button"""
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.profile_login_button_front_page()
    login_page.login_existing_user(TEST_USER["email"], TEST_USER["password"])

    # Verify successful login
    assert login_page.is_displayed(PageLocators.USER_ACCOUNT_BUTTON), (
        "User account button not visible after login"
    )


def test_user_login_with_forgot_password(driver):
    """Test forgot password functionality"""
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.profile_login_button_front_page()
    login_page.forgot_password_button_login_page(TEST_USER["email"])

    # Verify successful password recovery request
    assert login_page.is_displayed(PageLocators.RECOVER_BUTTON), (
        "Recovery confirmation not visible"
    )


def test_user_login_with_invalid_password(driver):
    """Test login via 'Personal Account' button with invalid password"""
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.enter_button_front_page()
    login_page.login_existing_user(TEST_USER["email"], "123")
    login_page.enter_button_login_page()

    # Verify error message
    error_message = login_page.get_error_message()
    assert error_message == "Некорректный пароль", (
        f"Expected error message 'Некорректный пароль', got '{error_message}'"
    )
