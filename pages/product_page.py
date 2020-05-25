from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET), "Button add to basket is not acessible by {}".format(
            *ProductPageLocators.ADD_TO_BASKET)

    def is_correct_product(self, product):
        element = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text
        assert product == element, 'Product name is not equal to {}, it is {} instead.'.format(product, element)

    def is_correct_price(self, price):
        element = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert price == element, 'Product price is not equal to {}, it is {} instead.'.format(price, element)

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

    def get_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT)
