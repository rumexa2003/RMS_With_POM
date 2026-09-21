import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.manager import ManagerPage

def test_specials(page):
    login=LoginPage(page)
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()

    
    

    manager=ManagerPage(page)
    manager.select_staff()
    manager.enter_pin("0000")
    manager.start_shift()
    manager.click_specials()
    manager.click_toggle()
    manager.wait_for_timeout(2000)
       