from playwright.sync_api import Page

class Stock:

    def __init__(self,page:Page):
        self.page=page
        self.inventory=page.get_by_text("Inventory",exact=True)
        self.add=page.get_by_role("button",name="Add Stock")
        self.name = page.get_by_placeholder("e.g. Jack Daniels")    
        self.selected_category = page.get_by_text(
        "packaged",
        exact=True
         ).locator("xpath=..")

    #form
        self.category_dropdown_text = page.locator("form").get_by_text(
        "drinks",
        exact=True)    
        self.drink_option = page.locator("span.capitalize").filter(
        has_text="drinks"
        )    
    # drink_option.click()
        self.manual=page.get_by_text("Manual (Not Linked)", exact=True)    
        self.coke=page.get_by_text("Coke", exact=True)    
        self.stock = page.locator('input[name="stock"]')
        self.cost_price = page.locator('input[name="cost_price"]')
        self.price = page.locator('input[name="price"]')
        self.save=page.get_by_role("button", name="Save to Vault")
    def click_invenory(self):
        self.inventory.click()
    def click_add(self):
        self.add.click()
    def input_name(self,name):
        self.name.fill(name)
    def select_category(self):
        self.selected_category.click()
    def select_drop(self):
        self.category_dropdown_text.click()
    def select_drink(self):
        self.drink_option.click()
    def select_m(self):
        self.manual.click()
        self.coke.click()
    def click_stock(self,stock):
        self.stock.fill(stock)
    def click_cost_price(self,cp):
        self.cost_price.fill(cp)
    def click_price(self,p):
        self.price.fill(p)
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)
    def save_button(self):
        self.save.click()

class expenses:
    def __init__(self,page:Page):
        self.page=page
        self.cashflow=page.get_by_role("button",name="Log Cashflow")
        self.t=page.get_by_placeholder("e.g. Plumber Fixing Sink")
        self.l=page.locator("svg.lucide-chevron-down")
        self.amount = page.locator('input[name="amount"]')
        self.date_input = page.locator('input[name="date"]')
        self.save=page.get_by_role("button", name="Save Expense")
    def click_cashflow(self):
        self.cashflow.click()
    def add_expenses(self,amount):
        self.t.fill(amount)
    def click_dropdown(self):
        self.l.click()
    def click_amount(self,a):
        self.amount.fill(a)
    def add_date(self,date):
        self.date_input.fill(date)
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)
    def click_save(self):
        self.save.click()
class income:
    def __init__(self,page:Page):
        self.page=page
        self.income=page.get_by_role("button",name=" Income", exact=True)
        self.category=page.get_by_placeholder("e.g. Wedding Party Catering")
        self.dropdown=page.locator("svg.lucide-chevron-down")
        self.amount = page.locator('input[name="amount"]')
        self.date_input = page.locator('input[name="date"]')
        self.save=page.get_by_role("button", name="Save Income")
    def click_income(self):
        self.income.click()
    def select_category(self,name):
        self.category.fill(name)
    def click_dropdown(self):
        self.dropdown.click()
    def select_amount(self,amt):
        self.amount.fill(amt)
    def select_date(self,date):
        self.date_input.fill(date)
    def click_save(self):
        self.save.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)




    
  

    
    

