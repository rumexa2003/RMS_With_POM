import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.manager import ManagerPage
from pages.admin import adminPage
from pages.cashier import CashierPage
from pages.stock import Stock
from pages.stock import expenses
from pages.stock import income
@pytest.mark.parametrize(
    "role",
    ["admin", "manager","cashier"]
)
@pytest.mark.parametrize(
    "types",
    ["stock","income","expenses"]
)
def test_approve_request(page,role,types):
    login=LoginPage(page)
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()

    
    
    if role=="manager":
        portal=ManagerPage(page)
        portal.select_staff()
        portal.enter_pin("0000")
        portal.start_shift()

    elif role=="cashier":
        portal=CashierPage(page)
        portal.select_staff()
        portal.enter_pin("0000")
        portal.start_shift()
        
    elif role=="admin":
        portal=adminPage(page)
        portal.open()
        portal.enter_rest("GC-01")
        portal.enter_mail("nabinbamthakuri2055@gmail.com")
        portal.enter_wording("gecko01#")
        portal.auth()

    portal.open_stock()
    if types=="stock":
        s=Stock(page)
        s.wait_for_timeout(2000)

        s.click_add()
        s.input_name("Coke")
        s.wait_for_timeout(2000)

        s.select_category()
        s.wait_for_timeout(2000)

        s.select_drop()
        s.wait_for_timeout(2000)

        s.select_drink()
        s.select_m()
        s.wait_for_timeout(2000)

        s.click_stock("10")
        s.wait_for_timeout(2000)

        s.click_cost_price("90")
        s.wait_for_timeout(2000)

        s.click_price("100")
    elif types=="expenses":
        e=expenses(page)
        e.click_cashflow()
        e.wait_for_timeout(2000)
        e.add_expenses("Electricity")
        e.click_dropdown()
        e.click_amount("5000")
        e.wait_for_timeout(2000)
        e.add_date("2026-09-09")
        e.wait_for_timeout(2000)
        e.click_save()


    
    elif types=="income":
        e=expenses(page)
        e.click_cashflow()
        e.wait_for_timeout(2000)
        i=income(page)
        i.click_income()
        i.wait_for_timeout(2000)

        i.select_category("Event Booking")
        i.click_dropdown()
        i.wait_for_timeout(2000)
        i.select_amount("5000")
        i.select_date("2026-09-09")        
        i.wait_for_timeout(2000)
        i.click_save()
        # i.select_date()
