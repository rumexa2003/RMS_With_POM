
from playwright.sync_api import Page

class Delete_staff:

    def __init__(self, page: Page):
        self.page = page
        
        self.staff_card = page.locator("div").filter(
        has=page.get_by_role("heading", name="Staff")
        ).last

        self.delete_button = page.locator("svg.lucide-trash-2")
        
   
    def select_staff(self):
        self.staff_card.click()
  
    def delete_staff(self):
        self.delete_button.click()
   
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)
    