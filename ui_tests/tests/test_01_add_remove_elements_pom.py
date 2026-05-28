import pytest
from playwright.sync_api import Page
import sys
import os

# Add the project root to sys.path to import pages
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.add_remove_elements_page import AddRemoveElementsPage

def test_add_remove_elements_pom(page: Page):
    add_remove_page = AddRemoveElementsPage(page)
    add_remove_page.load()
    
    # 1. Kliknij Add Element 3 razy.
    add_remove_page.add_element(times=3)
    
    # 2. Zweryfikuj, że są 3 przyciski Delete.
    add_remove_page.expect_delete_button_count(3)
    
    # 3. Usuń 1 element i sprawdź, że zostały 2.
    add_remove_page.remove_element()
    add_remove_page.expect_delete_button_count(2)
    
    # 4. Usuń pozostałe i potwierdź, że nie ma żadnych Delete.
    add_remove_page.remove_element()
    add_remove_page.remove_element()
    add_remove_page.expect_delete_button_count(0)
