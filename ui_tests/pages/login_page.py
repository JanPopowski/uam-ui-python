from playwright.sync_api import Page, expect
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.heading = page.get_by_role("heading", name="Login Page")

    def load(self):
        self.go_to(self.URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()

    def expect_error_message(self, message: str):
        expect(self.flash_message).to_be_visible()
        expect(self.flash_message).to_contain_text(message)

    def expect_success_message(self, message: str):
        expect(self.flash_message).to_be_visible()
        expect(self.flash_message).to_contain_text(message)

    def expect_login_page_visible(self):
        expect(self.heading).to_be_visible()
