from playwright.sync_api import Page, expect
from .base_page import BasePage

class AlertsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def __init__(self, page: Page):
        super().__init__(page)
        self.js_alert_button = page.get_by_role("button", name="Click for JS Alert")
        self.js_confirm_button = page.get_by_role("button", name="Click for JS Confirm")
        self.js_prompt_button = page.get_by_role("button", name="Click for JS Prompt")
        self.result_text = page.locator("#result")

    def load(self):
        self.go_to(self.URL)

    def trigger_alert(self):
        self.js_alert_button.click()

    def trigger_confirm(self):
        self.js_confirm_button.click()

    def trigger_prompt(self):
        self.js_prompt_button.click()

    def expect_result_text(self, expected_text: str):
        expect(self.result_text).to_have_text(expected_text)
