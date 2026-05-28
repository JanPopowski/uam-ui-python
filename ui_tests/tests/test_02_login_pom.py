import pytest
from playwright.sync_api import Page
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

def test_login_invalid_pom(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    
    login_page.login("invalid_user", "invalid_password")
    
    # 1. Dla błędnych danych pojawia się błąd.
    login_page.expect_error_message("Your username is invalid!")

def test_login_valid_pom(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    # 2. Dla poprawnych danych pojawia się sukces.
    login_page.expect_success_message("You logged into a secure area!")
    
    # 3. Po wylogowaniu wraca ekran logowania.
    login_page.logout()
    login_page.expect_login_page_visible()
    login_page.expect_success_message("You logged out of the secure area!")
