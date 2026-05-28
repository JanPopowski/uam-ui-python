import pytest
from playwright.sync_api import Page, expect

def test_add_remove_elements(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # 1. Kliknij Add Element 3 razy.
    add_button = page.get_by_role("button", name="Add Element")
    for _ in range(3):
        add_button.click()

    # 2. Zweryfikuj, że są 3 przyciski Delete.
    delete_buttons = page.get_by_role("button", name="Delete")
    expect(delete_buttons).to_have_count(3)

    # 3. Usuń 1 element i sprawdź, że zostały 2.
    delete_buttons.first.click()
    expect(delete_buttons).to_have_count(2)

    # 4. Usuń pozostałe i potwierdź, że nie ma żadnych Delete.
    delete_buttons.first.click()
    delete_buttons.first.click()
    expect(delete_buttons).to_have_count(0)
