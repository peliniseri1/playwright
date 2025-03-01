class MainPage:
    def __init__(self, page):
        self._myaccount= page.locator(".link.account-user p.link-text")
        self._logout_btn= page.locator('text=Çıkış Yap')
        self._searchproduct= page.locator('input[placeholder="Aradığınız ürün, kategori veya markayı yazınız"]')
        self._searchicon= page.locator('[data-testid="search-icon"]')

    def hover_myaccount(self):
        self._myaccount.hover()

    def click_logout(self):
        self._logout_btn.click()

    def do_logout(self):
        self._myaccount.hover()
        self._logout_btn.click()

    def search_product(self, product_name):
        self._searchproduct.fill(product_name)
        self._searchicon.click()


    @property
    def logged_in_mainpage(self):
        return self._myaccount

    @property
    def logout_btn(self):
        return self._logout_btn
