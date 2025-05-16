import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def test_login():
    if not EMAIL or not PASSWORD:
        raise ValueError("EMAIL or PASSWORD is missing in .env file")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            print("Navigating to login page...")
            page.goto("https://www.periplus.com/account/Login")

            print("Filling in login credentials...")
            page.fill('input[name="email"]', EMAIL)
            page.fill('input[name="password"]', PASSWORD)
            page.click('#button-login')

            page.wait_for_timeout(3000)

            current_url = page.url
            print(f"URL after login: {current_url}")
            print("Succesfully Logged In")
        except Exception as e:
            print(f"Test Failed: {e}")
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    test_login()