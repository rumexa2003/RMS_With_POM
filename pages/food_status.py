from playwright.sync_api import Page

class food_status:

    def __init__(self, page: Page):
        self.page = page

        self.dish = page.get_by_text(
            "Chinese Chop Suey (Indo-Chinese style) (Veg)"
        ).first

        self.drink = page.get_by_text(
            "Apple Iced Tea"
        ).first

        self.prep = page.get_by_role(
            "button",
            name="Start Preparing"
        )

        self.allready = page.get_by_role(
            "button",
            name="All Ready"
        )

    def select_dish(self):
        self.dish.click()

    def select_drink(self):
        self.drink.click()

    def start_preparing(self):
        self.prep.click()

    def all_ready(self):
        self.allready.click()
        
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)