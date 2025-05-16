import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
BOOKURL = os.getenv("BOOKURL")

def test_login(playwright):
    """Test login functionality and return browser, context and page"""
    if not EMAIL or not PASSWORD:
        raise ValueError("EMAIL or PASSWORD is missing in .env file")

    browser = playwright.chromium.launch(headless=False)
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
        print("Successfully Logged In")

        return browser, context, page

    except Exception as e:
        print(f"Login Failed: {e}")
        context.close()
        browser.close()
        return None, None, None

def test_cart(page):
    """Test adding a product to cart"""
    book_url = BOOKURL or "https://www.periplus.com/p/9781847740434/daily-wisdom-islamic-prayers-and-supplications"
    try:
        print("Navigating to product page...")
        page.goto(book_url)
        page.wait_for_timeout(2000)

        initial_cart = page.locator('#cart_total_mobile').inner_text()
        initial_count = int(initial_cart.strip() or "0")
        print(f"Initial cart count: {initial_count}")

        add_button = page.locator('button.btn-add-to-cart')
        if add_button.count() == 0:
            raise Exception("Add to Cart button not found.")
        add_button.first.click()

        page.wait_for_timeout(3000)

        final_cart = page.locator('#cart_total_mobile').inner_text()
        final_count = int(final_cart.strip() or "0")
        print(f"Cart count after adding: {final_count}")

        if final_count == initial_count + 1:
            print("Product successfully added to cart!")
        else:
            raise AssertionError("Cart count did not increase after adding product.")
    except Exception as e:
        print(f"Cart Test Failed: {e}")

if __name__ == "__main__":
    with sync_playwright() as playwright:
        browser, context, page = test_login(playwright)
        if page:
            test_cart(page)
            context.close()
            browser.close()
        else:
            print("Login failed, skipping cart test.")