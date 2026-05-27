from playwright.sync_api import expect
from pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    @property
    def add_button(self):
        return self.page.locator("button", has_text="Add Element")

    @property
    def delete_buttons(self):
        return self.page.locator("button", has_text="Delete")

    def add_elements(self, count: int) -> "AddRemoveElementsPage":
        for _ in range(count):
            self.add_button.click()
        return self

    def delete_by_index(self, index: int) -> "AddRemoveElementsPage":
        self.delete_buttons.nth(index).click()
        return self

    def delete_all(self) -> "AddRemoveElementsPage":
        while self.delete_buttons.count() > 0:
            self.delete_buttons.nth(0).click()
        return self

    def expect_delete_count(self, count: int) -> None:
        expect(self.delete_buttons).to_have_count(count)