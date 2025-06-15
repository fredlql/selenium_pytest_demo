import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run tests in headless mode"
    )

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    if request.config.getoption("--headless"):
        options.add_argument("--headless")
    options.add_argument("--window-size=1280,1024")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    # TEARDOWN : capture si échec
    if hasattr(request.node, "rep_call") and request.node.rep_call=="failed":
        test_name = request.node.name
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/{test_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"\n📸 Screenshot saved: {screenshot_path}")

    driver.quit()

def pytest_runtest_makereport(item, call):
    if "driver" in item.fixturenames and call.when == "call":
        setattr(item, "rep_call", call)

