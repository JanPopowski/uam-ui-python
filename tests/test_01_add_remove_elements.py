from playwright.sync_api import Page, expect


def test_add_remove_elements(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    add_btn = page.locator("button", has_text="Add Element")
    delete_buttons = page.locator("button", has_text="Delete")

    for _ in range(3):
        add_btn.click()

    expect(delete_buttons).to_have_count(3)

    delete_buttons.nth(0).click()
    expect(delete_buttons).to_have_count(2)

    delete_buttons.nth(0).click()
    delete_buttons.nth(0).click()
    expect(delete_buttons).to_have_count(0)

def test_add_remove_elements_failing(page: Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    add_btn = page.locator("button", has_text="Add Element")
    delete_buttons = page.locator("button", has_text="Delete")

    for _ in range(3):
        add_btn.click()

    expect(delete_buttons).to_have_count(3)

    delete_buttons.nth(0).click()
    expect(delete_buttons).to_have_count(2)

    delete_buttons.nth(0).click()
    delete_buttons.nth(0).click()
    expect(delete_buttons).to_have_count(1)