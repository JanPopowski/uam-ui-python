import pytest
from datetime import datetime
from pathlib import Path
from playwright.sync_api import Page

ARTIFACTS_DIR = Path("artifacts")


def pytest_configure(config):
    ARTIFACTS_DIR.mkdir(exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page: Page | None = item.funcargs.get("page")
        if page:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"{item.name}_{timestamp}.png".replace("/", "_")
            path = ARTIFACTS_DIR / name
            page.screenshot(path=str(path), full_page=True)


@pytest.fixture(scope="session")
def settings():
    return {
        "add_remove_url": "https://the-internet.herokuapp.com/add_remove_elements/",
        "login_url": "https://the-internet.herokuapp.com/login",
        "dynamic_loading_1_url": "https://the-internet.herokuapp.com/dynamic_loading/1",
        "upload_url": "https://the-internet.herokuapp.com/upload",
        "alerts_url": "https://the-internet.herokuapp.com/javascript_alerts",
        "valid_user": "tomsmith",
        "valid_pass": "SuperSecretPassword!",
    }


@pytest.fixture
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 768},
        "locale": "pl-PL",
        "timezone_id": "Europe/Warsaw",
    }