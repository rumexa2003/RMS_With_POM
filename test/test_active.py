from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.waiter import WaiterPage
from pages.active import ActivePage

def test_active_status():
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
        
        
        waiter=WaiterPage(page)
        waiter.select_staff()
        waiter.enter_pin("0000")
        waiter.start_shift()

        active=ActivePage(page)
        active.click_active_button()
        active.click_pending_button()
        active.click_cooking_button()
        active.click_ready_serve_button()
        active.click_served_button()
        active.click_waste_button()
        browser.close()