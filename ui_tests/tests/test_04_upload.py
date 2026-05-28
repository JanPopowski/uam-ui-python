import pytest
import os
from playwright.sync_api import Page, expect

def test_file_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    
    # 1. Wgraj plik (np. example.txt).
    # Create the file path assuming example.txt is in the same directory or project root
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "example.txt")
    
    page.locator("#file-upload").set_input_files(file_path)
    
    # 2. Kliknij Upload.
    page.get_by_role("button", name="Upload").click()
    
    # 3. Zweryfikuj, że strona pokazuje nazwę pliku.
    expect(page.get_by_role("heading", name="File Uploaded!")).to_be_visible()
    uploaded_file = page.locator("#uploaded-files")
    expect(uploaded_file).to_contain_text("example.txt")
