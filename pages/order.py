from playwright.sync_api import Page

class ordering:
    def __init__(self,page:Page):
        self.page=page
        self.new_order_button=page.get_by_role("button", name="New Order")
        self.food=page.get_by_text("Indo-Chinese style")
        self.add_button=page.get_by_role("button",name="Add to Order")
        self.send_button=page.get_by_role("button", name="Send to Kitchen")
        self.drink=page.get_by_text("Apple Iced Tea")

        # self.insiderest_button=page.get_by_role("button").filter(has_text="Select Table")
        # self.table_no=page.locator("svg.lucide-arrow-right").nth(0)
        
    # def select_new_order(self):
    #     self.new_order_button.click()
   
    # def select_table(self):
    #     self.insiderest_button.click()
    # def select_table_type(self):
    #     self.table_no.click()
    # def select_food(self):
    #     self.food.click()
    
    # def select_add_button(self):
    #     self.add_button.click()
    # def select_kitchen(self):
    #     self.send_button.click()
    # def send_bar(self):
    #     self.drink.click()


# incase of takeaway:
        self.takeaway_button=page.get_by_role("button").filter(has_text="Open POS")
    def select_new_order(self):
        self.new_order_button.click()

    def select_takeaway(self):
        self.takeaway_button.click()
      
    def select_food(self):
        self.food.click()
        
    def select_add_button(self):
        self.add_button.click()
    def select_kitchen(self):
        self.send_button.click()
    def send_bar(self):
        self.drink.click()



# page.get_by_text("Reports").click()

#     page.wait_for_timeout(2000)

#     page.get_by_role("button", name="leave", exact=True).click()
#     page.get_by_role("button", name="Apply Now", exact=True).click()
#     page.get_by_role("button", name="Urgent", exact=True).click()

#     page.wait_for_timeout(2000)

#     date_inputs = page.locator('input[type="date"]')

#     date_inputs.nth(0).fill("2026-08-31")  # FROM
#     date_inputs.nth(1).fill("2026-09-02")  # TO
#     page.wait_for_timeout(2000)

#     page.get_by_placeholder("Why do you need leave?").fill("I need leave for personal reasons")
#     page.wait_for_timeout(2000)

#     page.get_by_role("button", name="Submit Request").click()
    
#     page.wait_for_timeout(2000)
    
    # Check for "request sent" notification
    # expect(page.get_by_text("Request sent", exact=False)).to_be_visible()