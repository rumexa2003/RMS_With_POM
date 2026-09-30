import pyautogui
from playwright.sync_api import Page

class Payment:
    def __init__(self,page:Page):
        self.page=page
        self.payment_pending = page.locator("button").filter(has_text="payment_pending" ).nth(0)
        self.qr=page.get_by_role("button", name="FonePay", exact=True)
        self.credit=page.get_by_role("button", name="Credit", exact=True)
        self.customer = page.get_by_placeholder("* Select or Type Customer Name")
        self.confirm_payment = page.get_by_role("button",name="Confirm Payment")
# bill trial
        self.bill = page.get_by_role(
            "button",
            name="Print Bill",
            exact=True
        )

    def print_bill(self):
        self.bill.click()

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
    # def click_print_in_preview(self):
    #     for _ in range(10):
    #         self.page.keyboard.press("Tab")

    #     self.page.keyboard.press("Enter")
    # def click_print_in_preview(self):
    #     for i in range(10):
    #         self.page.keyboard.press("Tab")
    #         print(f"Tab {i + 1}")

    #     print("Print button should now be focused")
    #     self.page.wait_for_timeout(3000)
    #     self.page.keyboard.press("Enter")

    #     print("Enter pressed")
    #     self.page.wait_for_timeout(5000)
    def click_print_in_preview(self):
        for i in range(10):
            self.page.keyboard.press("Tab")
            print(f"Tab {i + 1}")

        print("Print button focused")

        self.page.wait_for_timeout(2000)

        pyautogui.press("enter")

        print("Physical Enter sent")
        self.page.wait_for_timeout(5000)
    def save_printed_bill(self):
        # for i in range(4):
        #         self.page.keyboard.press("Tab")
        #         print(f"Tab {i + 1}")
        pyautogui.write("test_bill.pdf")

        self.page.wait_for_timeout(1000)

        pyautogui.press("enter")

        print("Bill save")

    def cancel_save_dialog(self):
        for i in range(4):
            pyautogui.press("tab")
            print(f"Save dialog Tab {i + 1}")

        print("Cancel button focused")

        pyautogui.press("enter")

        print("Cancel selected")
        self.page.wait_for_timeout(2000)