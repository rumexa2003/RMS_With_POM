from playwright.sync_api import Page
class adminPage:
    def __init__(self,page:Page):
        self.page=page
        self.rest=page.get_by_placeholder("e.g. KTM-01")
        self.mail=page.get_by_placeholder("admin@gecko.works")
        self.word=page.get_by_placeholder("••••••••")
        self.menu_icon=page.get_by_text("Menu Engine", exact=True)
        self.category_button=page.get_by_role("button", name="New Category")             
        self.cate_name=page.category_input = page.get_by_placeholder("e.g. Starters")
        self.create_button=page.get_by_role("button", name="Create")
        self.auth_button=page.get_by_text("AUTHENTICATE")
        self.inventory=page.get_by_text("Inventory",exact=True)
        self.select_cate= page.get_by_text("admin cate", exact=True)
        self.adding_dish_button=page.get_by_role("button", name=" Dish")
        self.dish_name = page.get_by_placeholder("Item Name")
        self.price= page.locator("input[type='number'][placeholder='0']")
        self.save=page.get_by_role("button", name="Save Dish")
        self.reports_link = page.get_by_role("link", name="Reports", exact=True)
        self.floor = page.locator("svg.lucide-layout-grid")
        self.f_edit=page.get_by_role("button",name="Edit Layout")
        self.f_cafe=page.get_by_role("button",name="top floor")
        self.f_circle_button = page.get_by_role("button").filter( has=page.locator("svg.lucide-circle"))
        self.f_save=page.get_by_role("button", name="Save")
        # self.c_settings=page.get_by_text("Settings", exact=True)

    # page.wait_for_timeout(5000)  

    #     self.c_external_link = page.get_by_role("link").filter(has=page.locator("svg.lucide-external-link"))
    # def external_page(self):
    #     with self.page.expect_popup() as popup_info:
    #           self.c_external_link.click()
    #     new_page = popup_info.value
    #     new_page.wait_for_load_state()
    #     return new_page
    
        

    
    #  page.wait_for_timeout(5000)



    # new_page.wait_for_timeout(5000)

    # call_waiter = new_page.get_by_text("Call Waiter", exact=True)

    # call_waiter.click()

    # table_input = new_page.get_by_placeholder("e.g. 5, A2, Outside-1")
    # table_input.fill("Cafe-1")
    # new_page.get_by_role("button", name="Call now").click()

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
        self.inventory.click()

    # floor
    def click_floor(self):
        self.floor.click()
    def click_edit(self):
        self.f_edit.click()
    def select_cafe(self):
        self.f_cafe.click()
    def select_circle(self):
        self.f_circle_button.click()
    def click_save(self):
        self.f_save.click()

class SettingsPage:
    def __init__(self, page: Page):
        self.page = page

        self.settings = page.get_by_text(
            "Settings",
            exact=True
        )

        self.external_link = page.get_by_role("link").filter(
            has=page.locator("svg.lucide-external-link")
        )

    def open_settings(self):
        self.settings.click()

    def open_external_link(self):
        with self.page.expect_popup() as popup_info:
            self.external_link.click()

        new_page = popup_info.value
        new_page.wait_for_load_state()

        return new_page
    