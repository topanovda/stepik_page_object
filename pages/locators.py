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


class ProductPageLocators:
    ADD_BASKET_BUTTON = ("xpath", "(//button[@type='submit'])[2]")
    ITEM_ADDED_TO_CART = (
        "css selector",
        ".alert-safe:nth-of-type(1) .alertinner strong",
    )
    PRODUCT_NAME = ("xpath", "//div[@class='col-sm-6 product_main']//h1[1]")
    BASKET_VALUE = ("css selector", ".alert-info .alertinner strong")
    COST_OF_GOOD = ("xpath", "(//p[@class='price_color'])[1]")
    SUCCESS_MESSAGE = ("xpath", "(//*[@id='messages']/div[1]/div/text())[2]")
