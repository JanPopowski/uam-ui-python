import pytest
from playwright.sync_api import Page
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.alerts_page import AlertsPage

def test_alert_accept_pom(page: Page):
    alerts_page = AlertsPage(page)
    alerts_page.load()
    
    # 1. Obsłuż JS Alert (accept).
    page.on("dialog", lambda dialog: dialog.accept())
    alerts_page.trigger_alert()
    
    alerts_page.expect_result_text("You successfully clicked an alert")

def test_confirm_dismiss_pom(page: Page):
    alerts_page = AlertsPage(page)
    alerts_page.load()
    
    # 2. Obsłuż JS Confirm (dismiss) i zweryfikuj wynik.
    page.on("dialog", lambda dialog: dialog.dismiss())
    alerts_page.trigger_confirm()
    
    alerts_page.expect_result_text("You clicked: Cancel")

def test_prompt_accept_pom(page: Page):
    alerts_page = AlertsPage(page)
    alerts_page.load()
    
    # 3. Obsłuż JS Prompt (wpisz tekst), zaakceptuj i zweryfikuj wynik.
    def handle_prompt(dialog):
        dialog.accept("Hello Playwright!")
        
    page.on("dialog", handle_prompt)
    alerts_page.trigger_prompt()
    
    alerts_page.expect_result_text("You entered: Hello Playwright!")
