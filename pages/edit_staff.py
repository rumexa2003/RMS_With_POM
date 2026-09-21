
from playwright.sync_api import Page

class Edit:

    def __init__(self, page: Page):
        self.page = page
        
        self.staff_card = page.locator("div").filter(
        has=page.get_by_role("heading", name="Astha")
        ).last
        
        self.profile=page.get_by_role("button", name="profile")



        self.edit_button=page.get_by_role("button", name="Edit")

        self.phone=page.get_by_placeholder("Phone", exact=True)  
     
    
        self.button = page.get_by_role("button", name="Update", exact=True)
   
    def select_staff(self):
        self.staff_card.click()
    def click_profile(self):
        self.profile.click()
    def click_edit(self):
        self.edit_button.click()
    def fill_phone(self,phone):
        self.phone.fill(phone)
    # def update_button(self):
        # self.button.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)
    