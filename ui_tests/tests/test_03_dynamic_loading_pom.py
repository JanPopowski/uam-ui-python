import pytest
from playwright.sync_api import Page
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.dynamic_loading_page import DynamicLoadingPage

def test_dynamic_loading_pom(page: Page):
    dynamic_loading_page = DynamicLoadingPage(page)
    dynamic_loading_page.load()
    
    # 1. Kliknij Start.
    dynamic_loading_page.start_loading()
    
    # 2. Poczekaj aż pojawi się tekst Hello World! bez sleep.
    # 3. Zweryfikuj widoczność i treść.
    dynamic_loading_page.expect_hello_text_visible_and_correct()
