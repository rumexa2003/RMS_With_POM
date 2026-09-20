from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.bar import BarPage


def test_bar():
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

            bar=BarPage(page)
            bar.select_staff()
            bar.enter_pin("0000")
            bar.start_shift()
            bar.start_shift()
            browser.close()


      