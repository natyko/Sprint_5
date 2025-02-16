import time

from pages.login_page import LoginPage


def test_user_login(driver):
    """Тест вход по кнопке «Войти в аккаунт» на главной"""
    driver.maximize_window()
    login_page = LoginPage(driver)

    fixed_email = "naty@yopmail.com"
    fixed_password = "Privet123"

    login_page.open("https://stellarburgers.nomoreparties.site")
    time.sleep(1)
    login_page.enter_button_front_page()
    login_page.login_existing_user(fixed_email, fixed_password)


def test_login_with_user_account(driver):
    """Тест вход через кнопку «Личный кабинет»"""
    driver.maximize_window()
    login_page = LoginPage(driver)

    fixed_email = "naty@yopmail.com"
    fixed_password = "Privet123"

    login_page.open("https://stellarburgers.nomoreparties.site")
    time.sleep(1)
    login_page.profile_login_button_front_page()
    login_page.login_existing_user(fixed_email, fixed_password)


def test_user_login_with_forgot_password(driver):
    """Тест вход через кнопку «Забыли пароль?»"""
    driver.maximize_window()
    login_page = LoginPage(driver)
    fixed_email = "naty@yopmail.com"
    login_page.open("https://stellarburgers.nomoreparties.site")

    login_page.profile_login_button_front_page()
    login_page.forgot_password_button_login_page(fixed_email)


def test_user_login_with_invalid_password(driver):
    """Тест вход через кнопку «Личный кабинет» с неверным паролем"""
    driver.maximize_window()
    login_page = LoginPage(driver)
    fixed_email = "naty@yopmail.com"
    fixed_password = "123"
    login_page.open("https://stellarburgers.nomoreparties.site")

    login_page.enter_button_front_page()
    login_page.login_existing_user(fixed_email, fixed_password)
    login_page.enter_button_login_page()
    assert login_page.get_error_message() == "Некорректный пароль", (
        "Error message is not displayed or incorrect"
    )
