from playwright.sync_api import Page, expect
from .base_page import BasePage

class DynamicLoadingPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    def __init__(self, page: Page):
        super().__init__(page)
        self.start_button = page.get_by_role("button", name="Start")
        self.hello_text = page.locator("#finish h4")

    def load(self):
        self.go_to(self.URL)

    def start_loading(self):
        self.start_button.click()

    def expect_hello_text_visible_and_correct(self):
        expect(self.hello_text).to_be_visible(timeout=10000)
        expect(self.hello_text).to_have_text("Hello World!")
