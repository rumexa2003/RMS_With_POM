import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.manager import ManagerPage
from pages.admin import adminPage
from pages.resleave import StaffPage
from pages.add_new_staff import Add_staff
@pytest.mark.parametrize(
    "role",
    ["admin", "manager"]
)
def test_approve_request(page,role):
    login=LoginPage(page)
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()

    
    
    if role=="manager":
        manager=ManagerPage(page)
        manager.select_staff()
        manager.enter_pin("0000")
        manager.start_shift()
        staff=StaffPage(page)

        staff.wait_for_timeout(5000)
        staff.open_staff_hub()

        a=Add_staff(page)
        a.click_adds()
        a.click_staff_name("Staff")
        a.wait_for_timeout(2000)

        a.select_role("Cashier")
        a.wait_for_timeout(2000)

        a.enter_pin("0000")
        a.wait_for_timeout(2000)
        a.click_button()
        a.wait_for_timeout(5000)

        
      
    elif role=="admin":
        admin=adminPage(page)
        admin.open()
        admin.enter_rest("GC-01")
        admin.enter_mail("nabinbamthakuri2055@gmail.com")
        admin.enter_wording("gecko01#")
        admin.auth()
        staff=StaffPage(page)
        staff.admin_staff()
        a=Add_staff(page)
        a.click_adds()
        a.click_staff_name("Staff A")
        a.wait_for_timeout(2000)
    
        a.select_role("Waiter")
        a.wait_for_timeout(2000)
    
        a.enter_pin("0000")
        a.wait_for_timeout(2000)
        a.click_button()
        a.wait_for_timeout(5000)

    