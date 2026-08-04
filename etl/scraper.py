import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

with sync_playwright() as pw:
    pw.selectors.set_test_id_attribute("data-adalo-id")
    browser = pw.chromium.launch(
        headless=False, args=["--disable-blink-features=AutomationControlled"]
    )
    page = browser.new_page()
    page.goto("https://app.adalo.com/en/login?redirect=%2F")
    page.get_by_placeholder("Email Address").fill(os.environ["PW_EMAIL"])
    page.get_by_placeholder("••••••••").fill(os.environ["PW_PASSWORD"])
    page.get_by_role("button", name="Sign In").click()
    page.locator("a.navbar-user-avatar").click()
    page.locator('[data-adalo-id="team-switcher"]').get_by_text(
        "PRP Team"
    ).click()
    page.pause()

# try:
#     browser = pw.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://app.adalo.com/en/login?redirect=%2F")
# finally:
#     context_manager.__exit__()
