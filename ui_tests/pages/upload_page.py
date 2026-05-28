from playwright.sync_api import Page, expect
from .base_page import BasePage

class UploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    def __init__(self, page: Page):
        super().__init__(page)
        self.file_input = page.locator("#file-upload")
        self.upload_button = page.get_by_role("button", name="Upload")
        self.uploaded_files_heading = page.get_by_role("heading", name="File Uploaded!")
        self.uploaded_files_list = page.locator("#uploaded-files")

    def load(self):
        self.go_to(self.URL)

    def upload_file(self, file_path: str):
        self.file_input.set_input_files(file_path)
        self.upload_button.click()

    def expect_file_uploaded(self, filename: str):
        expect(self.uploaded_files_heading).to_be_visible()
        expect(self.uploaded_files_list).to_contain_text(filename)
