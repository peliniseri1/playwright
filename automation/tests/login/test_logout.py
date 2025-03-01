from playwright.sync_api import Page, expect

from automation.src.pages.LoginPage import LoginPage


def test_logout(set_up_tear_down) -> None:
    page=set_up_tear_down
    credentials = {'mail': 'pelinsibel2000@gmail.com', 'password': '555K1818p..p'}
    login_page = LoginPage(page)
    main_page = login_page.do_login(credentials)

    login_successful = main_page.logged_in_mainpage
    expect(login_successful).to_have_text("Hesabım")


    if login_successful.is_visible():
        main_page.do_logout()


    expect(main_page._myaccount).to_have_text("Giriş Yap")

