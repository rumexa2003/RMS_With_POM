import pytest
from playwright.sync_api import expect
from pages.admin import adminPage
from pages.admin import SettingsPage

def test_call_waiter(page):
    portal=adminPage(page)
    portal.open()
    portal.enter_rest("GC-01")
    portal.enter_mail("nabinbamthakuri2055@gmail.com")
    portal.enter_wording("gecko01#")
    portal.auth()
    settings = SettingsPage(page)

    settings.open_settings()

    new_page = settings.open_external_link()

    new_page.get_by_text(
        "Call Waiter",
        exact=True
    ).click()

    new_page.get_by_placeholder(
        "e.g. 5, A2, Outside-1"
    ).fill("Cafe-1")

    new_page.get_by_role(
        "button",
        name="Call now",
    ).click()