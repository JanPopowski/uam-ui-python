import pytest
from playwright.sync_api import Page, expect

def test_alert_accept(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # 1. Obsłuż JS Alert (accept).
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    
    result = page.locator("#result")
    expect(result).to_have_text("You successfully clicked an alert")

def test_confirm_dismiss(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # 2. Obsłuż JS Confirm (dismiss) i zweryfikuj wynik.
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    
    result = page.locator("#result")
    expect(result).to_have_text("You clicked: Cancel")

def test_prompt_accept(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # 3. Obsłuż JS Prompt (wpisz tekst), zaakceptuj i zweryfikuj wynik.
    def handle_prompt(dialog):
        dialog.accept("Hello Playwright!")
        
    page.on("dialog", handle_prompt)
    page.get_by_role("button", name="Click for JS Prompt").click()
    
    result = page.locator("#result")
    expect(result).to_have_text("You entered: Hello Playwright!")
