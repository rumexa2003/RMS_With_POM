from playwright.sync_api import Page

class CashierPage:
    def __init__(self,page:Page):
        self.page=page
        self.staff_button=page.get_by_role(
            "button"
        ).filter(
            has_text="Ramala"
        )

        self.start_shift_button=page.get_by_role(
            "button",
            name="Start Shift"
        )
        self.report=page.get_by_role("button", name="Reports")
        self.close=page.get_by_role("button", name="Close Day")
        self.stock=page.get_by_role("button",name="Vault & Ledger")
        


    def select_staff(self):
        self.staff_button.click()

    def enter_pin(self,pin):
        for digit in  pin:
            self.page.get_by_role(
                "button",
                name=digit
            ).click()

    def start_shift(self):
        self.start_shift_button.click()
    def open_reports(self):
        self.report.click()
    def close_day(self):
        self.close.click()
    
    def open_stock(self):
        self.stock.click()