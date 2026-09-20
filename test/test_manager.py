from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.manager import ManagerPage

def test_manager_login():
    with sync_playwright() as p:
        browser=p.chromium.launch(
            headless=False,
            slow_mo=1000
        )
        page=browser.new_page()

        login=LoginPage(page)
        login.open()
        login.enter_restaurant_code("GC-01")
        login.activate_system()

        manager=ManagerPage(page)
        manager.select_staff()
        manager.enter_pin("0000")
        manager.start_shift()
        page.wait_for_timeout(5200)
        browser.close()