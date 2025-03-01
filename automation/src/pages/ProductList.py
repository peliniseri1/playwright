from automation.src.pages.Product import Product


class ProductList:
    def __init__(self, page):
        self.page = page
        self._searched_product_name = page.locator('div.dscrptn.dscrptn-V2 h1')
        self._product_in_page = page.locator('div.p-card-img-wr').nth(0)

    def click_first_product(self):
        self._product_in_page.click()
        return Product(self.page)

    @property
    def searched_product_name(self):
        return self._searched_product_name