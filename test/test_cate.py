import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.kitchen import KitchenPage
from pages.bar import BarPage
from pages.manager import ManagerPage
from pages.admin import adminPage

@pytest.mark.parametrize(
    "role",
    ["admin", "chef", "bar"]
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
        bar.click_menu()
        bar.click_cate()
        bar.select_cate_name("Bar Cate")
        bar.click_create()
        bar.wait_for_timeout(5000)

        # bar.click_new_drink()
        # bar.write_drink_name.fill()
        # bar.select_drink_price.fill()
        # bar.scroll_down()
        # bar.save_button()
    elif role=="chef":
        chef=KitchenPage(page)
        chef.select_staff()
        chef.enter_pin("0000")
        chef.start_shift()
        chef.start_2()
        chef.click_menu()
        chef.click_cate()
        chef.select_cate_name("kitchen cate")
        chef.click_create()
        chef.wait_for_timeout(5000)

    elif role=="admin":
        admin=adminPage(page)
        admin.open()
        admin.enter_rest("GC-01")
        admin.enter_mail("nabinbamthakuri2055@gmail.com")
        admin.enter_wording("gecko01#")
        admin.auth()
        admin.click_menu()
        admin.click_cate()
        admin.select_cate_name("admin cate")
        admin.click_create()
        admin.wait_for_timeout(5000)


