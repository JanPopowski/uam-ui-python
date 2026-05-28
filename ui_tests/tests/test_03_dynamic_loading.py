import pytest
from playwright.sync_api import Page, expect

def test_dynamic_loading(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    # 1. Kliknij Start.
    page.get_by_role("button", name="Start").click()
    
    # 2. Poczekaj aż pojawi się tekst Hello World! bez sleep.
    # Playwright's auto-waiting handles this.
    hello_text = page.locator("#finish h4")
    
    # 3. Zweryfikuj widoczność i treść.
    expect(hello_text).to_be_visible(timeout=10000)
    expect(hello_text).to_have_text("Hello World!")
