import pytest



@pytest.fixture()
def set_up_tear_down(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.trendyol.com/giris?cb=%2F")
    yield page


@pytest.fixture()
def login_fixture(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.trendyol.com/giris?cb=%2F")
    page.locator("input[name='login email']")
    page.fill('input[name="login email"]', 'pelinsibel2000@gmail.com')
    page.fill('input[name="login-password"]', '555K1818p..p')
    page.click('button.q-button.submit')

    page.wait_for_selector('text=Hesabım')

    yield page