from playwright.sync_api import sync_playwright, Playwright, Browser, Page
from behave.runner import Context
import json

# Define a custom context class to add type hints

class CustomContext(Context):
    playwright: Playwright
    browser: Browser
    page: Page

def before_all(context: CustomContext):
    # This function is called before all all tests start
    print("Starting playwright...")

    # Load environment variable from env.json
    with open('config/env.json', 'r') as file:
        env_vars = json.load(file)

    # Accessing variables from env.joson
    browser_type = env_vars.get("browser", "chromium")
    headless_mode = env_vars.get("headless", False)

    context.playwright = sync_playwright().start()
    context.browser = context.playwright[browser_type].launch(headless=headless_mode, args=["--start-maximized"])

def before_scenario(context: CustomContext, scenario):
    # This function is called before each scenario starts
    print(f"Starting scenario: {scenario.name}")
    context.page = context.browser.new_page(no_viewport=True)

    
