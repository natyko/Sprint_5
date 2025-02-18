from config import BASE_URL, TEST_USER
from locators.locators import PageLocators
from pages.login_page import LoginPage
from pages.registration_page import RegisterPage
from utils.generate_email import generate_random_email


def test_valid_registration(driver):
    """Test registration via registration form"""
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)
    random_email = generate_random_email()

    register_page.open(BASE_URL)
    register_page.register("Test User", random_email, TEST_USER["password"])
    login_page.login(random_email, TEST_USER["password"])

    # Verify successful registration and login
    assert login_page.is_displayed(PageLocators.USER_ACCOUNT_BUTTON), (
        "User account button not visible after registration"
    )
