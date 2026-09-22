from playwright.sync_api import Page

class ManagerPage:

    def __init__(self,page:Page):
        self.page=page
        self.staff_button=page.get_by_role(
            "button"
        ).filter(
            has_text="Nabin"
        )

        self.start_shift_button=page.get_by_role(
            "button",
            name="Start Shift"
        )
        # adding

        self.menu=page.get_by_text("Menu Mgmt", exact=True)
        self.select_cate=page.locator("button").filter(has_text="Iced Tea")

        self.dish=page.get_by_text("Add Dish")
    
            
        self.add_drink= page.get_by_placeholder("Item Name")
        self.price = page.locator("input[type='number'][placeholder='0']")    
        self.save=page.get_by_role("button", name="Save Dish")
        self.reports_link = page.get_by_role("link", name="Reports", exact=True)
        self.inventory=page.get_by_role("link",name="Inventory", exact=True)
        # specials:Inventory

        self.link = page.get_by_role("link", name="Specials", exact=True)
    # link.click()
    # page.wait_for_timeout(1000)  

        self.dish = page.locator("div.grid.grid-cols-12").filter(
        has_text="American Chopsey"
        )

        self.toggle = self.dish.locator("button")
        self.cashflow=page.get_by_role("button",name="Log Cashflow")

    def select_staff(self):
        self.staff_button.click()

    def enter_pin(self,pin):
        for digit in pin:
            self.page.get_by_role(
                "button",
                name=digit
            ).click()
            
    def start_shift(self):
        self.start_shift_button.click()

    #adding a dish in bar:
    def click_menu(self):
        self.menu.click()
    def click_cate_name(self):
        self.select_cate.click()
    def click_new_dish(self):
        self.dish.click()
    def write_dish_name(self,drink):
        self.add_drink.fill(drink)
    def select_dish_price(self,price):
        self.price.fill(price)
    def scroll_down(self):
        self.page.evaluate("window.scrollBy(0, 500)")
    def save_button(self):
        self.save.click()
    def open_reports(self):
        self.reports_link.click()
    # specials:
    def click_specials(self):
        self.link.click()
    def click_toggle(self):
        self.toggle.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)
    def open_stock(self):
        self.inventory.click()
    def open_log(self):
        self.cashflow.click()


    