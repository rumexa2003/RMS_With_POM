from playwright.sync_api import Page
class ActivePage:
    def __init__(self,page:Page):
        self.page=page


        self.active_button=page.get_by_text("Active Order")
    

        self.pending_button=page.get_by_role("button", name="Pending")
  

        self.cooking_button=page.get_by_role("button", name="Cooking")

        self.ready_serve=page.get_by_role("button", name="Ready to Serve")


        self.serve_button=page.get_by_role("button", name="Served")

        self.waste_button=page.get_by_role("button", name="Waste")
    def click_active_button(self):
        self.active_button.click()

    def click_pending_button(self):
        self.pending_button.click()

    def click_cooking_button(self):
        self.cooking_button.click()
    def click_ready_serve_button(self):
        self.ready_serve.click()
    def click_served_button(self):
        self.serve_button.click()
    def click_waste_button(self):
        self.waste_button.click()
