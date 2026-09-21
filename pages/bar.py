from playwright.sync_api import Page

class BarPage:

    def __init__(self,page:Page):
        self.page=page
        self.staff_button=page.get_by_role(
            "button"
        ).filter(
            has_text="Bar"
        )

        self.start_shift_button=page.get_by_role(
            "button",
            name="Start Shift"
        )

        self.reports_icon = page.locator(
                "svg.lucide-file-chart-column-increasing"
        )
        self.leave_icon=page.get_by_role("button", name="Leave Status")

        self.menu_icon=page.menu_icon = page.locator("svg.lucide-layout-grid")
        
        self.category_button=page.get_by_role("button", name="Category")

                
        self.cate_name=page.category_input = page.get_by_placeholder("e.g. Cocktails, Hookah")
    
        self.create_button=page.get_by_role("button", name="Create")
    
        self.select_cate=page.get_by_text("Bar Cate", exact=True)
        self.bar_drink=page.get_by_text("New Drink")
        self.drink_name=page.get_by_placeholder("e.g. Classic Mojito")
        self.drink_price=page.locator("input[type='number'][placeholder='0']")  
        self.save=page.get_by_role("button", name="Save Drink")

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
    def start_shift1(self):
        self.start_shift_button.click()

    def click_report_button(self):
        self.reports_icon.click()
    def click_leave_button(self):
        self.leave_icon.click()

    def click_menu(self):
        self.menu_icon.click()
    def click_cate(self):
        self.category_button.click()
    def select_cate_name(self,text):
        self.cate_name.fill(text)
    def click_create(self):
        self.create_button.click()

    def click_cate_name(self):
        self.select_cate.click()

    def click_new_drink(self):
        self.bar_drink.click()
    def write_drink_name(self,drink):
        self.drink_name.fill(drink)
    def select_drink_price(self,price):
        self.drink_price.fill(price)
    
    def scroll_down(self):
        self.page.evaluate("window.scrollBy(0, 500)")

    def save_button(self):
        self.save.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)

    # def select_drink(self):
    #     self.drink.click()
  
