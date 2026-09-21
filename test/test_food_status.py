import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.kitchen import KitchenPage
from pages.bar import BarPage
from pages.food_status import food_status

@pytest.mark.parametrize(
    "role",
    ["bar","chef"]
)
def test_status(page,role):
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
        bar.start_shift()

        # bar.select_drink()
        food=food_status(page)
        food.select_drink()
        food.start_preparing()
        food.wait_for_timeout(2000)

        food.all_ready()
        food.wait_for_timeout(2000)


    elif role=="chef":
        chef=KitchenPage(page)
        chef.select_staff()
        chef.enter_pin("0000")
        chef.start_shift()
        chef.start_2()
        food=food_status(page)
        food.select_dish()
        food.wait_for_timeout(2000)

        food.start_preparing()
        food.all_ready()
        food.wait_for_timeout(2000)

        

