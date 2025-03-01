from playwright.sync_api import Page, expect

from automation.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'mail': 'pelinsibel2000@gmail.com', 'password': '555K1818p..p'}
    login_page=LoginPage(page)
    main_page=login_page.do_login(credentials)

    expect(main_page.logged_in_mainpage).to_have_text("Hesabım")
    expect(login_page._login_btn).not_to_be_visible()



def test_login_with_invalid_user(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'mail': 'invalidxuser@gmail.com', 'password': 'xxx'}
    login_page = LoginPage(page)
    main_page = login_page.do_login(credentials)

    error_message= "E-posta adresiniz ve/veya şifreniz hatalı."
    expect(login_page._error_msg).to_contain_text(error_message)
    expect(login_page._login_btn).to_be_visible()



def test_login_with_invalid_password(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'mail': 'pelinsibel2000@gmail.com', 'password': 'xxx'}
    login_page = LoginPage(page)
    main_page = login_page.do_login(credentials)

    error_message = "E-posta adresiniz ve/veya şifreniz hatalı."
    expect(login_page._error_msg).to_contain_text(error_message)
    expect(login_page._login_btn).to_be_visible()


def test_login_with_no_mail(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'mail': ' ', 'password': 'xxx'}
    login_page = LoginPage(page)
    main_page = login_page.do_login(credentials)

    error_message = "Lütfen geçerli bir e-posta adresi giriniz."
    expect(login_page._error_msg).to_contain_text(error_message)
    expect(login_page._login_btn).to_be_visible()

def test_login_with_no_password(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'mail': 'pelinsibel2000@gmail.com', 'password': ''}
    login_page = LoginPage(page)
    main_page = login_page.do_login(credentials)

    error_message = "Lütfen şifrenizi giriniz."
    expect(login_page._error_msg).to_contain_text(error_message)
    expect(login_page._login_btn).to_be_visible()