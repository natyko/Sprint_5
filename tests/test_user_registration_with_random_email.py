from pages.registration_page import RegisterPage
from pages.login_page import LoginPage
from utils.generate_email import generate_random_email


def test_valid_registration(driver):
    """Тест вход через кнопку в форме регистрации,"""
    driver.maximize_window()
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)

    random_email = generate_random_email()
    print(f"Generated email: {random_email}")

    register_page.open("https://stellarburgers.nomoreparties.site")
    register_page.register("Test User", random_email, "validPass123")
    login_page.login(random_email, "validPass123")
