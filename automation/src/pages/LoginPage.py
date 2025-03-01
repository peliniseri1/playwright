from automation.src.pages.MainPage import MainPage


class LoginPage:

    def __init__(self, page):
        self.page=page
        self._email = page.locator("input[name='login email']")
        self._password = page.locator("input[name='login-password']")
        self._login_btn = page.locator("button.q-button.submit")
        self._error_msg = page.locator("span.message")

    def enter_mail(self, email):
        self._email.clear()
        self._email.fill(email)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def click_login(self):
        self._login_btn.click()

    def do_login(self, credentials):
        self.enter_mail(credentials['mail'])
        self.enter_password(credentials['password'])
        self.click_login()

        return MainPage(self.page)

    @property
    def err_msg_loc(self):
        return self._error_msg

    @property
    def login_button(self):
        return self._login_btn