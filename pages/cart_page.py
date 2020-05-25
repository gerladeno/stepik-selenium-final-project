from .locators import CartPageLocators
from .base_page import BasePage


class CartPage(BasePage):
    def cart_is_empty(self):
        content = self.browser.find_element(*CartPageLocators.CART_EMPTY).text
        assert "Your basket is empty." in content, "Cart is not empty. {}".format(content)

    def no_items_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Cart is not empty!"
