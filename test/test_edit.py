import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.manager import ManagerPage
from pages.admin import adminPage
from pages.resleave import StaffPage
from pages.edit_staff import Edit
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

        e=Edit(page)
        e.select_staff()
        e.click_profile()
        e.wait_for_timeout(1000)
        
        e.click_edit()
        e.wait_for_timeout(2000)

        e.fill_phone("9876543210")
        e.wait_for_timeout(2000)
        e.update_button()
        e.wait_for_timeout(2000)

        
      
    elif role=="admin":
        admin=adminPage(page)
        admin.open()
        admin.enter_rest("GC-01")
        admin.enter_mail("nabinbamthakuri2055@gmail.com")
        admin.enter_wording("gecko01#")
        admin.auth()
        staff=StaffPage(page)
        staff.admin_staff()
        e=Edit(page)
        e.select_staff()
        e.click_profile()
        e.wait_for_timeout(1000)
        
        e.click_edit()
        e.wait_for_timeout(2000)

        e.fill_phone("9876543210")
        e.wait_for_timeout(2000)
        e.update_button()
        e.wait_for_timeout(2000)
    