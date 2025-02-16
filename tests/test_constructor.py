import time

from pages.constructor_page import Constractor


def test_constructor_click(driver):
    """Test navigation constructor"""
    constructor_page = Constractor(driver)
    fixed_email = "123@yopmail.com"
    fixed_password = "privet123$"
    constructor_page.open("https://stellarburgers.nomoreparties.site/login")
    time.sleep(1)
    constructor_page.login_existing_user(fixed_email, fixed_password)
    time.sleep(1)
    constructor_page.constructor_buttons()
