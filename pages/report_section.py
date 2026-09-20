from playwright.sync_api import Page
class Report:
    def __init__(self,page:Page):
        self.page=page
        # self.reports_link = page.get_by_role("link", name="Reports", exact=True)
        # self.report=page.get_by_role("button", name="Reports")


    
 
        self.credit_button=page.get_by_role("button", name="Credit Ledger")
        self.customer = page.get_by_role("button",name="customer",exact=False)
        self.clear_dues_button=page.get_by_role("button",name="Clear Dues", exact=True ).nth(0)

        self.close_button = page.get_by_role("button").filter( has=page.locator("svg.lucide-x"))


        self.date_dropdown = page.locator("button").filter(has=page.locator("svg.lucide-calendar"))
        self.confirm_button = page.get_by_role( "button",name="Confirm",exact=True)


    # date_dropdown.click()
    # page.wait_for_timeout(5000) 
    # page.wait_for_timeout(1000)

        self.days_30 = page.get_by_role("button",name="30 Days",exact=True)
    # days_30.click()
    # # page.wait_for_timeout(5000)
    def click_credit(self):
        self.credit_button.click()
    def click_report(self):
        self.report.click()
    def click_close(self):
        self.close_button.click()
    def click_clear(self):
        self.clear_dues_button.click()
    def click_credit_acc(self):
        self.customer.click()

        # expense:
    def select_date(self):
        self.date_dropdown.click()
    def select_month(self):
        self.days_30.click()

    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)

        
    def get_first_customer(self):
        return self.page.get_by_role(
            "button",
            name="Due:",
            exact=False
        ).first


    def get_first_customer_name(self):
        customer = self.get_first_customer()

        return customer.locator("p").first.inner_text()


    def select_customer(self, customer_name):
        customer = self.page.get_by_role(
            "button",
            name=customer_name,
            exact=False
        )


        customer.click()
    
    def click_confirm(self):
        self.confirm_button.click()
    def customer_is_visible(self, customer_name):
        customer = self.page.get_by_role(
            "button",
            name=customer_name,
            exact=False
        )

        return customer.is_visible()




    def get_first_customer_name(self):
        customer = self.get_first_customer()

        return customer.locator("p").first.inner_text()

    def select_customer(self, customer_name):
        self.page.get_by_role(
            "button",
            name=customer_name,
            exact=False
        ).click()
    def has_customers(self):
        customer = self.page.get_by_role(
            "button",
            name="Due:",
            exact=False
        )

        return customer.count() > 0