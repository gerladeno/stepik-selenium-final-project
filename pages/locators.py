from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_PRODUCT = (By.CSS_SELECTOR, "div.alert-success strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
