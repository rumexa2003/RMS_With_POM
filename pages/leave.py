from playwright.sync_api import Page
class leave_section:
    def __init__(self,page:Page):
        self.page=page
        # self.report_button=page.get_by_text("Reports")
        self.leave_button=page.get_by_role("button", name="leave",exact="True")
        self.apply_button=page.get_by_role("button", name="Apply Now", exact=True)
        self.urgent_button=page.get_by_role("button", name="Urgent", exact=True)

        self.date_inputs = page.locator('input[type="date"]')
        self.reason_box=page.get_by_placeholder("Why do you need leave?")
        self.submit_box=page.get_by_role("button",name="Submit Request")
        # self.success_message = page.get_by_text("Request sent",exact=False)

    # def click_report_button(self):
    #     self.report_button.click()

    # def click_leave_button(self):
    #     self.leave_button.click()

    def click_apply_button(self):
        self.apply_button.click()
    def click_urgent_button(self):
        self.urgent_button.click()

    def enter_leave_dates(self, from_date, to_date):
        self.date_inputs.nth(0).fill(from_date)
        self.date_inputs.nth(1).fill(to_date)
    def click_reason(self,reason):
        self.reason_box.fill(reason)
    def click_submit(self):
        self.submit_box.click()

