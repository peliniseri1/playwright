class Product:
    def __init__(self, page):
        self.page = page
        self._addto_basket=  page.locator('.add-to-basket-button-text')

    @property
    def add_to_basket_button_visibility(self):
        return self._addto_basket

    def click_add_to_basket(self):
        self._addto_basket.click()

