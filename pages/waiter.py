from playwright.sync_api import Page


class WaiterPage:

    def __init__(self, page: Page):
        self.page = page

        self.staff_button = page.get_by_role(
            "button"
        ).filter(
            has_text="Astha"
        )

        self.start_shift_button = page.get_by_role(
            "button",
            name="Start Shift"
        )
        self.report_button=page.get_by_text("Reports")
        self.apply_button=page.get_by_role("button", name="leave", exact=True)


    def select_staff(self):
        self.staff_button.click()

    def enter_pin(self, pin):

        for digit in pin:
            self.page.get_by_role(
                "button",
                name=digit
            ).click()

    def start_shift(self):
        self.start_shift_button.click()
    def click_report_button(self):
        self.report_button.click()
    def click_leave_button(self):
        self.apply_button.click()