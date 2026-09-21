
from playwright.sync_api import Page,expect

class Add_staff:

    def __init__(self, page: Page):
        self.page = page
        # page.get_by_text("Staff Hub").click()

    # page.wait_for_timeout(1000)  

        self.add_s=page.get_by_role("button", name="New Staff", exact =True)
    # page.wait_for_timeout(1000)  

        self.sname = page.get_by_placeholder("e.g. Nischal Shrestha")
    # category_input.fill("Staff 1")

        self.role = page.locator('select[name="role"]')
        # self.role_dropdown = page.locator('select[name="role"]')
        # self.pin_input = page.get_by_placeholder("0000")

        self.create_button = page.get_by_role(
            "button", name="Create ", exact=True
        )


    # expect(role).to_be_visible()
    # role.select_option("cashier")
    # expect(role).to_have_value("cashier")

        self.pin= page.get_by_placeholder("0000")
    # pin.fill("0000")
   
        self.button = page.get_by_role("button", name="Create ", exact=True)
    # button.scroll_into_view_if_needed()
    # button.click()
    def click_adds(self):
        self.add_s.click()
    def click_staff_name(self,sname):
        self.sname.fill(sname)
    def select_role(self, role):
        expect(self.role).to_be_visible()
        self.role.select_option(role)
        # expect(self.role).to_have_value(role)
    def enter_pin(self,pin):
        self.pin.fill(pin)
    def click_button(self):
        self.button.click()
    def wait_for_timeout(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)
    

