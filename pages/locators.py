class MainPageLocators:
    LOGIN_LINK = ("css selector", "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = ("css selector", "#id_login-username")
    LOGIN_PASSWORD = ("css selector", "#id_login-password")
    LOGIN_SUBMIT = ("xpath", "(//button[@type='submit'])[2]")
    REGISTER_EMAIL = ("css selector", "#id_registration-email")
    REGISTER_PASSWORD = ("css selector", "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = ("xpath", "//input[@id='id_registration-password2']")
    REGISTER_SUBMIT = ("xpath", "(//button[@type='submit'])[3]")
