from playwright.sync_api import Page


class StaffPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.staff_hub = page.get_by_text("Staff Hub")
        self.review_request = page.get_by_text(
            "Review Request",
            exact=True
        ).nth(0)
        self.approve_button = page.get_by_role(
            "button",
            name="Approve"
        )
        self.staff_admin=page.get_by_text("Staff",exact=True)

    def open_staff_hub(self):
        self.staff_hub.click()

    def admin_staff(self):
        self.staff_admin.click()

    # def select_review_request(self):
    #     # print("Review Request:", self.review_request.count())

    #     staff_card = self.review_request.locator("xpath=..")
    #     staff_card.click()

    # def approve_request(self):
    #     self.approve_button.click()
    
    



    def has_review_request(self):
        return self.review_request.count() > 0

    def select_review_request(self):
        if not self.has_review_request():
            print("No leave review request found.")
            return False

        print(
            f"Review requests found: "
            f"{self.review_request.count()}"
        )

        review_request = self.review_request.first

    
        staff_card = review_request.locator("xpath=..")

        staff_card.click()

        return True



    def approve_request(self):
        self.approve_button.click()

    def approve_leave_request(self):

        if not self.select_review_request():
            print("No leave request to approve.")
            return

        print("Leave request found.")
        print("Approving leave request...")

        self.approve_request()

        print("Leave request approved.")

    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)