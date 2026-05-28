from playwright.sync_api import Page, expect
from .base_page import BasePage

class AddRemoveElementsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_element_button = page.get_by_role("button", name="Add Element")
        self.delete_buttons = page.get_by_role("button", name="Delete")

    def load(self):
        self.go_to(self.URL)

    def add_element(self, times: int = 1):
        for _ in range(times):
            self.add_element_button.click()

    def remove_element(self):
        self.delete_buttons.first.click()

    def expect_delete_button_count(self, count: int):
        expect(self.delete_buttons).to_have_count(count)
