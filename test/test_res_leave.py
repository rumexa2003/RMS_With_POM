import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.manager import ManagerPage
from pages.admin import adminPage
from pages.resleave import StaffPage

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
        if staff.select_review_request():

             staff.wait_for_timeout(2000)
             staff.approve_request()

        else:

            print("Nothing to approve.")
      
    elif role=="admin":
        admin=adminPage(page)
        admin.open()
        admin.enter_rest("GC-01")
        admin.enter_mail("nabinbamthakuri2055@gmail.com")
        admin.enter_wording("gecko01#")
        admin.auth()
        staff=StaffPage(page)
        staff.admin_staff()
        staff.wait_for_timeout(5000)
        if staff.select_review_request():
        
            staff.wait_for_timeout(2000)
            staff.approve_request()
        
        else:
        
            print("Nothing to approve.")
        
        # staff.select_review_request()
        # staff.wait_for_timeout(5000)
        # staff.wait_for_timeout(5000)
        staff.wait_for_timeout(5000)



