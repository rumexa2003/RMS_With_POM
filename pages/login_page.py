from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.restaurant_code = page.get_by_placeholder("GECKO-01")

        self.activate_button = page.get_by_role(
            "button",
            name="Activate System"
        )

    def open(self):
        self.page.goto(
            "https://rms.geckoworksnepal.com.np/staff/login"
        )

    def enter_restaurant_code(self, code):
        self.restaurant_code.fill(code)

    def activate_system(self):
        self.activate_button.click()

# from playwright.sync_api import Page


# class LoginPage:

#     def __init__(self, page: Page):
#         self.page = page

#         self.restaurant_code = page.get_by_placeholder("GECKO-01")

#         self.activate_button = page.get_by_role(
#             "button",
#             name="Activate System"
#         )

#         self.waiter_button = page.get_by_role(
#             "button"
#         ).filter(has_text="Astha")

#         self.chef_button=page.get_by_role(
#             "button"
#         ).filter(has_text="Anish")

#         self.bar_button=page.get_by_role(
#             "button"
#         ).filter(has_text="Bar")

#     def open(self):
#         self.page.goto(
#             "https://rms.geckoworksnepal.com.np/staff/login"
#         )

#     def enter_restaurant_code(self, code):
#         self.restaurant_code.fill(code)

#     def activate_system(self):
#         self.activate_button.click()

#     def login_as_role(self, role):

#         if role == "waiter":
#             self.waiter_button.click()

#             # your remaining waiter login steps
#             # keypad clicks
#             # Start Shift
#             # etc.

#         elif role == "chef":
#             # Chef-specific login steps
#             self.chef_button.click()

#         elif role == "bar":
#             # Bar-specific login steps
#             self.bar_button.click()

#         else:
#             raise ValueError(f"Unknown role: {role}")