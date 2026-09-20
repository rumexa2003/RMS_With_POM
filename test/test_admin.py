from playwright.sync_api import sync_playwright
from pages.admin import adminPage

def test_admin_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000
        )
        page=browser.new_page()
        admin=adminPage(page)
        admin.open()
        admin.enter_rest("GC-01")
        admin.enter_mail("nabinbamthakuri2055@gmail.com")
        admin.enter_wording("gecko01#")
        admin.auth()
        browser.close()
