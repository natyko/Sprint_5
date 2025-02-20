from config import BASE_URL, LOGIN_URL, TEST_USER
from locators.locators import PageLocators
from pages.user_account_page import UserAccount
from pages.login_page import LoginPage


def test_constructor_click(driver):
    """Test navigation from user account to constructor."""
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.profile_login_button_front_page()
    login_page.login_existing_user(TEST_USER["email"], TEST_USER["password"])
    login_page.orders_button()
    login_page.user_login_click_constructor()

    # Verify the current URL is the constructor page
    assert driver.current_url == f"{BASE_URL}/", (
        "Failed to navigate to constructor page"
    )


def test_logout_button(driver):
    """Test clicking on the logout button."""
    login_page = UserAccount(driver)
    login_page.open(LOGIN_URL)
    login_page.login_existing_user(TEST_USER["email"], TEST_USER["password"])
    login_page.profile_login_button_front_page()
    login_page.user_logout()

    # Verify successful logout
    assert login_page.is_displayed(PageLocators.ENTER_BUTTON), (
        "Login button not visible after logout"
    )
