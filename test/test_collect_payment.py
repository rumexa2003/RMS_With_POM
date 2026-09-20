import pytest
from pages.login_page import LoginPage
from pages.cashier import CashierPage
from pages.collect_paymentC import Payment

@pytest.mark.parametrize(
    "role",
    ["cash","QR","Credit"]
)
def test_payment(page,role):
    login = LoginPage(page)
    
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()
    cashier=CashierPage(page)
    cashier.select_staff()
    cashier.enter_pin("0000")
    cashier.start_shift()
    # serving.wait_for_timeout(2000)
    if role=="cash":
        cash=Payment(page)
        cash.click_avaliable_pay()
        cash.click_comfirm_pay()
        cash.wait_for_timeout(2000)
    elif role=="Credit":
        C=Payment(page)
        C.click_avaliable_pay()
        C.click_credit()
        C.c_name("John")
        C.click_comfirm_pay()
        C.wait_for_timeout(2000)
    elif role=="QR":
        q=Payment(page)
        q.click_avaliable_pay()
        q.click_qr()
        q.click_comfirm_pay()
        q.wait_for_timeout(2000)
        