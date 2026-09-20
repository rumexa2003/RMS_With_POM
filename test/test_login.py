
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.waiter import WaiterPage

def test_waiter_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000
        )

        page = browser.new_page()

        login = LoginPage(page)

        login.open()
        login.enter_restaurant_code("GC-01")
        login.activate_system()
      
        browser.close()

# import pytest
# from pages.login_page import LoginPage


# @pytest.mark.parametrize("role", ["waiter", "chef", "bar"])
# def test_login(page, role):

#     login = LoginPage(page)

#     login.open()
#     login.enter_restaurant_code("GC-01")
#     login.activate_system()
#     login.login_as_role(role)