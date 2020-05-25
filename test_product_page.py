from pages.product_page import ProductPage


def test_add_product_to_basket_button_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    product = page.get_product().text
    price = page.get_price().text

    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.is_correct_product(product)
    page.is_correct_price(price)
