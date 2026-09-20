import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.waiter import WaiterPage
from pages.cashier import CashierPage
from pages.kitchen import KitchenPage
from pages.bar import BarPage
from pages.manager import ManagerPage
from pages.admin import adminPage
from pages.logout import Logout

@pytest.mark.parametrize(
    "role",
    ["waiter", "chef", "manager","admin","bar","admin"]
)
def test_adding_cate(page,role):
    login=LoginPage(page)
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()

    if role=="bar":
        bar=BarPage(page)
        bar.select_staff()
        bar.enter_pin("0000")
        bar.start_shift()
        bar.start_shift()
        logout=Logout(page)
        logout.logout_button()
        
        bar.wait_for_timeout(2000)

    elif role=="chef":
        chef=KitchenPage(page)
        chef.select_staff()
        chef.enter_pin("0000")
        chef.start_shift()
        chef.start_2()
        logout=Logout(page)
        logout.logout_button()
       
        chef.wait_for_timeout(2000)



    elif role=="manager":
        manager=ManagerPage(page)
        manager.select_staff()
        manager.enter_pin("0000")
        manager.start_shift()
        logout=Logout(page)
        logout.logout_button()


    elif role=="admin":
        admin=adminPage(page)
        admin.open()
        admin.enter_rest("GC-01")
        admin.enter_mail("nabinbamthakuri2055@gmail.com")
        admin.enter_wording("gecko01#")
        admin.auth()
        logout=Logout(page)
        logout.logout_button()
      