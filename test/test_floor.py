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
        admin.wait_for_timeout(2000)
        admin.click_floor()
        admin.wait_for_timeout(2000)

        admin.click_edit()
        admin.wait_for_timeout(2000)

        admin.select_cafe()
        admin.wait_for_timeout(2000)

        admin.select_circle()
        admin.wait_for_timeout(2000)
        # admin.click_save()
        admin.wait_for_timeout(2000)

        browser.close()
