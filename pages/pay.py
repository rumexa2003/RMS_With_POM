from playwright.sync_api import Page
class PayrollPage:
    def __init__(self,page:Page):
        self.page=page
        # self.report_button=page.get_by_text("Reports")
        self.payroll_button=page.get_by_role("button",name="payroll")

    # def select_report(self):
    #     self.report_button.click()

    def select_payroll(self):
        self.payroll_button.click()