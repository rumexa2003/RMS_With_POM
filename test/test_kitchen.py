from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.kitchen import KitchenPage

def test_waiter_login():
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

        kitchen=KitchenPage(page)
        kitchen.select_staff()
        kitchen.enter_pin("0000")
        kitchen.start_shift()
        kitchen.start_2()
        page.wait_for_timeout(5000)
        browser.close()
