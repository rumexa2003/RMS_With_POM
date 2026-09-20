from playwright.sync_api import Page
class Payment:
    def __init__(self,page:Page):
        self.page=page
        self.payment_pending = page.locator("button").filter(has_text="payment_pending" ).nth(0)
        self.qr=page.get_by_role("button", name="FonePay", exact=True)
        self.credit=page.get_by_role("button", name="Credit", exact=True)
        self.customer = page.get_by_placeholder("* Select or Type Customer Name")
        self.confirm_payment = page.get_by_role("button",name="Confirm Payment")

    def click_avaliable_pay(self):
        self.payment_pending.click()
    def click_comfirm_pay(self):
        self.confirm_payment.click()
    def click_qr(self):
        self.qr.click()
    def click_credit(self):
        self.credit.click()
    def c_name(self,n):
        self.customer.fill(n)
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)