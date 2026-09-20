from playwright.sync_api import Page
class serve:
    def __init__(self,page:Page):
        self.page=page
        # cashier
        self.kitchen_status=page.get_by_role("button", name="Kitchen Status")
        self.serve_button=page.get_by_role("button", name="Serve Ready Items").nth(0)

        # waiter

        # self.overpage.get_by_text("Overview").click()
        
        self.wserve=page.get_by_role("button", name="Pick Up & Serve").nth(0)
    def click_kitchen(self):
        self.kitchen_status.click()
    def click_Cserve(self):
        self.serve_button.click()
    def click_Wserve(self):
        self.wserve.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)