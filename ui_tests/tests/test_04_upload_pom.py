import pytest
from playwright.sync_api import Page
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.upload_page import UploadPage

def test_file_upload_pom(page: Page):
    upload_page = UploadPage(page)
    upload_page.load()
    
    # 1. Wgraj plik (np. example.txt).
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "example.txt")
    
    # 2. Kliknij Upload.
    upload_page.upload_file(file_path)
    
    # 3. Zweryfikuj, że strona pokazuje nazwę pliku.
    upload_page.expect_file_uploaded("example.txt")
