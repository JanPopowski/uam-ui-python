import pytest
from playwright.sync_api import Page, expect

def test_login_invalid(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.get_by_label("Username").fill("invalid_user")
    page.get_by_label("Password").fill("invalid_password")
    page.get_by_role("button", name="Login").click()
    
    # 1. Dla błędnych danych pojawia się błąd.
    error_flash = page.locator("#flash")
    expect(error_flash).to_be_visible()
    expect(error_flash).to_contain_text("Your username is invalid!")

def test_login_valid(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    
    # 2. Dla poprawnych danych pojawia się sukces.
    success_flash = page.locator("#flash")
    expect(success_flash).to_be_visible()
    expect(success_flash).to_contain_text("You logged into a secure area!")
    
    # 3. Po wylogowaniu wraca ekran logowania.
    page.get_by_role("link", name="Logout").click()
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()
    
    logout_flash = page.locator("#flash")
    expect(logout_flash).to_be_visible()
    expect(logout_flash).to_contain_text("You logged out of the secure area!")
