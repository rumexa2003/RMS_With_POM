from playwright.sync_api import Page

class Logout:

    def __init__(self, page: Page):
        self.page = page
        
        self.logout=page.get_by_role("button", name="Sign Out")
    def logout_button(self):
        self.logout.click()