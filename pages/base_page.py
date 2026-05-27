from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str) -> "BasePage":
        self.page.goto(url)
        return self

    def expect_url(self, url: str) -> None:
        expect(self.page).to_have_url(url)

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)