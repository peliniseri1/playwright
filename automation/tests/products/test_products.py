
from playwright.sync_api import Page, expect

from automation.src.pages.MainPage import MainPage
from automation.src.pages.ProductList import ProductList
from automation.src.pages.Product import Product

def xtest_search_item(login_fixture) -> None:
    page = login_fixture
    main_page= MainPage(page)
    main_page.search_product("Avene")

    productList= ProductList(page)
    expect(productList.searched_product_name).to_contain_text("Avene")


def test_go_to_product_itself(login_fixture)-> None:
    page = login_fixture
    main_page = MainPage(page)
    main_page.search_product("Avene")

    productList = ProductList(page)

    expect(productList.searched_product_name).to_contain_text("Avene")

    productList.click_first_product()

    product=Product(page)
    page.on('dialog', lambda dialog: dialog.accept())
    page.wait_for_selector('button.add-to-basket:has-text("Sepete Ekle")', state='visible')

    expect(product.add_to_basket_button_visibility).to_contain_text("Sepete Ekle")

