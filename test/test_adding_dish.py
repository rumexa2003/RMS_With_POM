import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.kitchen import KitchenPage
from pages.bar import BarPage
from pages.manager import ManagerPage
from pages.admin import adminPage

@pytest.mark.parametrize(
    "role",
    ["admin", "chef", "bar", "manager"]
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
        bar.click_cate_name()
        bar.click_new_drink()
        bar.write_drink_name("Mango Juice")
        bar.select_drink_price("350")
        bar.scroll_down()
        bar.save_button()
        bar.wait_for_timeout(2000)

    elif role=="chef":
        chef=KitchenPage(page)
        chef.select_staff()
        chef.enter_pin("0000")
        chef.start_shift()
        chef.start_2()
        chef.click_menu()
        chef.click_cate_name()
        chef.click_new_dish()
        chef.write_dish_name("Mango Juice")
        chef.select_dish_price("350")
        chef.scroll_down()
        chef.save_button()
        chef.wait_for_timeout(2000)



    elif role=="manager":
        manager=ManagerPage(page)
        manager.select_staff()
        manager.enter_pin("0000")
        manager.start_shift()
        # manager.start_2()
        manager.click_menu()
        manager.click_cate_name()
        manager.click_new_dish()
        manager.write_dish_name("Mango Juice")
        manager.select_dish_price("350")
        manager.scroll_down()
        manager .save_button()

    elif role=="admin":
        admin=adminPage(page)
        admin.open()
        admin.enter_rest("GC-01")
        admin.enter_mail("nabinbamthakuri2055@gmail.com")
        admin.enter_wording("gecko01#")
        admin.auth()
        admin.click_menu()
        admin.click_category()
        admin.click_dish()
        admin.selecting_dish_name("dish-naem")
        admin.select_dish_price("350")
        admin.click_save()
        admin.wait_for_timeout(5000)

       
    

