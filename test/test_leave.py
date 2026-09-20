# from playwright.sync_api import sync_playwright
# from pages.login_page import LoginPage
# from pages.waiter import WaiterPage
# from pages.leave import leave_section

# def test_leave():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(
#             headless=False,
#             slow_mo=1000
#         )
#         page=browser.new_page()
#         login=LoginPage(page)
#         login.open()
#         login.enter_restaurant_code("GC-01")
#         login.activate_system()

#         waiter=WaiterPage(page)
#         waiter.select_staff()
#         waiter.enter_pin("0000")
#         waiter.start_shift()

#         leave=leave_section(page)
#         leave.click_report_button()
#         leave.click_leave_button()
#         leave.click_apply_button()
#         leave.click_urgent_button()
#         leave.enter_leave_dates("2026-09-28", "2026-10-01")
#         leave.click_reason("I need leave for personal reasons")
#         leave.click_submit()
#         browser.close()


import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.waiter import WaiterPage
from pages.kitchen import KitchenPage
from pages.bar import BarPage
from pages.leave import leave_section


@pytest.mark.parametrize(
    "role",
    ["waiter", "chef", "bar"]
)
def test_leave_request(page, role):

    login = LoginPage(page)

    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()

    # Login according to the selected role
    if role == "waiter":
        waiter = WaiterPage(page)
        waiter.select_staff()
        waiter.enter_pin("0000")
        waiter.start_shift()
        waiter.click_report_button()
        waiter.click_leave_button()

    elif role == "chef":
        chef=KitchenPage(page)
        chef.select_staff()
        chef.enter_pin("0000")
        chef.start_shift()
        chef.start_2()
        chef.click_report_button()
        chef.click_leave_button()


        # Chef login steps

        # pass

    elif role == "bar":
        bar=BarPage(page)
        bar.select_staff()
        bar.enter_pin("0000")
        bar.start_shift()
        bar.start_shift()
        bar.click_report_button()
        bar.click_leave_button()

        # Bar login steps

        # pass

    # Common Leave functionality
    leave = leave_section(page)
    # leave.click_report_button()
    # leave.click_leave_button()
    leave.click_apply_button()
    leave.click_urgent_button()
    leave.enter_leave_dates("2026-09-28", "2026-10-01")
    leave.click_reason("I need leave for personal reasons")
    
    leave.click_submit()
    
    
    page.wait_for_timeout(2000)
    
    print("URL after submit:", page.url)


    # expect(
    #     leave.success_message
    # ).to_be_visible()