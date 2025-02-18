from config import TEST_USER, BASE_URL, ACCOUNT_URL
from pages.login_page import LoginPage


def test_constructor_click(driver):
    """Test navigation constructor"""
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.enter_button_front_page()
    login_page.login_existing_user(TEST_USER["email"], TEST_USER["password"])
    login_page.constructor_buttons()

    # Verify navigation to constructor page
    assert driver.current_url == f"{ACCOUNT_URL}/", (
        "Failed to navigate to constructor page"
    )
