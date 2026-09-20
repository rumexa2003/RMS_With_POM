from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.waiter import WaiterPage
from pages.order import ordering

def test_order_kitchen_take():
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

        # order=ordering(page)
        # order.select_new_order()
        # page.wait_for_timeout(2000)
        # order.select_table()
        # order.select_table_type()

        # order.select_food()
        # page.wait_for_timeout(7000)

        # order.select_add_button()
        # page.wait_for_timeout(2000)

        # order.send_bar()
        # order.select_add_button()
        # page.wait_for_timeout(2000)

        # order.select_kitchen()
        # page.wait_for_timeout(5000)

# incase of takeaway:
        order=ordering(page)
        order.select_new_order()
        page.wait_for_timeout(2000)
        order.select_takeaway()
        page.wait_for_timeout(2000)

        order.select_food()
        page.wait_for_timeout(7000)

        order.select_add_button()
        page.wait_for_timeout(2000)

        order.send_bar()
        order.select_add_button()
        page.wait_for_timeout(2000)

        order.select_kitchen()
        page.wait_for_timeout(5000)    

    

        browser.close()



