from playwright.sync_api import Page

class KitchenPage:

    def __init__(self,page:Page):
        self.page=page
        self.staff_button=page.get_by_role(
            "button"
        ).filter(
            has_text="Anish"
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
        
                        
        self.cate_name=page.category_input = page.get_by_placeholder("e.g. Starters, Main Course")
            # category_input.fill("Automation Category")
        self.create_button=page.get_by_role("button", name="Create")

        self.select_cate=page.get_by_text("kitchen cate", exact=True)

        self.new_dish=page.get_by_text("New Dish")
    
    
        self.dish_name = page.get_by_placeholder("e.g. Signature Burger")
    # dish_name_input.fill("Signature Burger")

    
        self.price = page.locator("input[type='number'][placeholder='0']")
    # price_input.fill("350")

    
  
    
        self.save=page.get_by_role("button", name="Save Dish")
    

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

    def start_2(self):
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
    
    def click_new_dish(self):
        self.new_dish.click()
    def write_dish_name(self,dish):
        self.dish_name.fill(dish)
    def select_dish_price(self,price):
        self.price.fill(price)
        
    def scroll_down(self):
        self.page.evaluate("window.scrollBy(0, 500)")
    def save_button(self):
        self.save.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)

