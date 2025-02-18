class PageLocators:
    # Main Page Locators
    ENTER_BUTTON = "//button[text() = 'Войти в аккаунт']"
    LOGO = "//title[text() = 'Stellar Burgers']"
    ORDERS_BUTTON = "//p[text() = 'Лента Заказов']"  # orders button

    # Register Page Locators
    REGISTER_BUTTON = "//a[text()='Зарегистрироваться']"
    NAME_INPUT_REGISTER = "//fieldset[1]//input"  # username at register
    EMAIL_INPUT_REGISTER = "//fieldset[2]//input"  # user email at register
    PASSWORD_INPUT_REGISTER = "//fieldset[3]//input"  # user password ar register
    SUBMIT_BUTTON = "//button[text() = 'Зарегистрироваться']"  # register button

    # Login Page Locators
    EMAIL_INPUT = "//fieldset[1]//input"  # user email at login
    PASSWORD_INPUT = "//fieldset[2]//input"  # user password at login
    LOGIN_ENTER_BUTTON = "//button[contains(text(), 'Войти')]"  # login button
    PASSWORD_ERROR_MESSAGE = (
        "//p[text() = 'Некорректный пароль']"  # error message for incorrect password
    )
    FORGOT_PASSWORD_BUTTON = (
        "//a[text() = 'Восстановить пароль']"  # forgot password button
    )
    RECOVER_BUTTON = "//button[text() = 'Восстановить']"
    # User Account Page Locators
    USER_ACCOUNT_BUTTON = "//p[text() = 'Личный Кабинет']"  # user account button
    LOGOUT_BUTTON = "//button[text() = 'Выход']"  # logout button
    NAV_CONSTRUCTOR_BUTTON = "//p[text() = 'Конструктор']"  # navigation button
    BURGER_CREATE_BUTTON = "//h1[text() = 'Соберите бургер']"  # create burger button
    # Constructor Page Locators
    BUNS_BUTTON = "//span[text()='Булки']"  # buns button
    SAUCES_BUTTON = "//span[text()='Соусы']"  # sauces button
    INGREDIENTS_BUTTON = "//span[text()='Начинки']"  # fillings button
