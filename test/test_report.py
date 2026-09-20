import pytest
from pages.login_page import LoginPage
from pages.cashier import CashierPage
from pages.report_section import Report
from pages.manager import ManagerPage
from pages.admin import adminPage

# @pytest.mark.parametrize(
#         "role",
#         ["credit_ledger","transactions"]
# )

@pytest.mark.parametrize(
    "role",
    ["admin", "cashier", "manager"]
)
@pytest.mark.parametrize(
    "report_type",
    ["credit_ledger", "transactions"]
)
def test_reports(page, role, report_type):

    login = LoginPage(page)
        
    login.open()
    login.enter_restaurant_code("GC-01")
    login.activate_system()
   
    if role == "admin":
        portal = adminPage(page)
        portal.open()
        portal.enter_rest("GC-01")
        portal.enter_mail("nabinbamthakuri2055@gmail.com")
        portal.enter_wording("gecko01#")
        portal.auth()

    elif role == "cashier":
        portal = CashierPage(page)
        portal.select_staff()
        portal.enter_pin("0000")
        portal.start_shift()

    elif role == "manager":
        portal = ManagerPage(page)
        portal.select_staff()
        portal.enter_pin("0000")
        portal.start_shift()

    # 3. Login / enter that portal
    

    # 4. Open Reports
    portal.open_reports()

    # 5. Create shared Reports page
    reports = Report(page)

    if report_type=="credit_ledger":
        report=Report(page)
        # report.click_report()
        report.wait_for_timeout(5000)
# manually! if needed
        # report.click_credit()
        # report.wait_for_timeout(5000)
        # report.click_credit_acc()
        # report.click_clear()
       


# paying the credits on the first come first served:
        report.click_credit()
        report.wait_for_timeout(2000)
        if not reports.has_customers():
            print("Credit Ledger is empty. Nothing to clear.")
        return

        customer_name = report.get_first_customer_name()

        print("Customer selected:", customer_name)

        report.select_customer(customer_name)

        report.wait_for_timeout(1000)

        report.click_clear()

        report.wait_for_timeout(2000)
        report.click_confirm()
        report.click_clear()


        # assert not report.customer_is_visible(customer_name)


        report.click_close()
        report.wait_for_timeout(5000)

    
    elif report_type=="transactions":
     
            t=Report(page)
            # t.click_report()
            t.wait_for_timeout(5000)
            t.select_date()
            t.wait_for_timeout(5000)

            t.select_month()
            t.wait_for_timeout(5000)


