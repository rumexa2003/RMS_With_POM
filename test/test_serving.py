import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.waiter import WaiterPage
from pages.cashier import CashierPage
from pages.serve import serve
from pages.kitchen import KitchenPage
from pages.bar import BarPage
from pages.leave import leave_section

@pytest.mark.parametrize(
    "role",
    ["waiter", "cashier"]
)
def test_status(page,role):
    login = LoginPage(page)
    
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()

    if role == "waiter":
        waiter = WaiterPage(page)
        waiter.select_staff()
        waiter.enter_pin("0000")
        waiter.start_shift()
        serving=serve(page)
        serving.click_Wserve()
        serving.wait_for_timeout(2000)

    elif role=="cashier":
        cashier=CashierPage(page)
        cashier.select_staff()
        cashier.enter_pin("0000")
        cashier.start_shift()
        serving=serve(page)
        serving.click_kitchen()
        serving.click_Cserve()
        serving.wait_for_timeout(2000)
