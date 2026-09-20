from playwright.sync_api import Page
class adminPage:
    def __init__(self,page:Page):
        self.page=page
    #         table_input = page.get_by_placeholder("e.g. KTM-01")
    #         table_input = page.get_by_placeholder("admin@gecko.works")
    #       authenticate = page.get_by_text("AUTHENTICATE", exact=True)

    # authenticate.click()
        


        self.rest=page.get_by_placeholder("e.g. KTM-01")
        self.mail=page.get_by_placeholder("admin@gecko.works")
        self.word=page.get_by_placeholder("••••••••")
        self.menu_icon=page.get_by_text("Menu Engine", exact=True)
        self.category_button=page.get_by_role("button", name="New Category")
        
                        
        self.cate_name=page.category_input = page.get_by_placeholder("e.g. Starters")
            # category_input.fill("Automation Category")
        self.create_button=page.get_by_role("button", name="Create")

        self.auth_button=page.get_by_text("AUTHENTICATE")

        


        self.select_cate= page.get_by_text("admin cate", exact=True)
    
    


        self.adding_dish_button=page.get_by_role("button", name=" Dish")
    
    
    
        self.dish_name = page.get_by_placeholder("Item Name")
    # dish_name_input.fill("Signature Burger")

    

        self.price= page.locator("input[type='number'][placeholder='0']")
    # price_input.fill("350")

    
        self.save=page.get_by_role("button", name="Save Dish")

        self.reports_link = page.get_by_role("link", name="Reports", exact=True)
        


    def open(self):
        self.page.goto(
            "https://rms.geckoworksnepal.com.np/login"  
        )
    def enter_rest(self,code):
        self.rest.fill(code)
    def enter_mail(self,code2):
        self.mail.fill(code2)
    def enter_wording (self,code3):
        self.word.fill(code3)
    def auth(self):
        self.auth_button.click()
    def click_menu(self):
            self.menu_icon.click()
    def click_cate(self):
            self.category_button.click()
    def select_cate_name(self,text):
            self.cate_name.fill(text)
    def click_create(self):
            self.create_button.click()
    # adding dish
    def click_category(self):
         self.select_cate.click()
    def click_dish(self):
         self.adding_dish_button.click()
    def selecting_dish_name(self,dish):
          self.dish_name.fill(dish)
    def select_dish_price(self,price):
         self.price.fill(price)
    def click_save(self):
         self.save.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)
    def open_reports(self):
        self.reports_link.click()
        
        