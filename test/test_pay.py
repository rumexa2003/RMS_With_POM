# from playwright.sync_api import sync_playwright
import pytest
from pages.login_page import LoginPage
from pages.waiter import WaiterPage
from pages.kitchen import KitchenPage
from pages.bar import BarPage 
from pages.pay import PayrollPage

@pytest.mark.parametrize(
    "role",
    ["waiter", "chef", "bar"]
)

def test_payroll(page,role):
    login=LoginPage(page)
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()
    if role=="waiter":
        waiter=WaiterPage(page)
        waiter.select_staff()
        waiter.enter_pin("0000")
        waiter.start_shift()
        waiter.click_report_button()
        
    elif role=="chef":
        chef=KitchenPage(page)
        chef.select_staff()
        chef.enter_pin("0000")
        chef.start_shift()
        chef.start_2()
        chef.click_report_button()
    elif role=="bar":
        bar=BarPage(page)
        bar.select_staff()
        bar.enter_pin("0000")
        bar.start_shift()
        bar.start_shift()
        bar.click_report_button()
    

    payroll=PayrollPage(page)
    # payroll.select_report()
    payroll.select_payroll()
    page.wait_for_timeout(2000)

