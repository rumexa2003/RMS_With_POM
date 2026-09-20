from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.cashier import CashierPage

def test_cashier_login():
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

        cashier=CashierPage(page)
        cashier.select_staff()
        cashier.enter_pin("0000")
        cashier.start_shift()
        page.wait_for_timeout(5000)
        browser.close()