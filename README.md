# Periplus Login Automated Test (Python + Playwright)

Automated login testing script using **Python**, **Playwright**, and **Dotenv** for the [Periplus](https://www.periplus.com/) website.

---

## How It Works

The script does the following steps:
1. Launches a Chromium browser (non-headless for visual debugging).
2. Navigates to the Periplus login page.
3. Loads login credentials from the `.env` file.
4. Fills in the email and password.
5. Clicks the login button.
6. Verifies that login is successful by checking the URL or DOM.
7. Closes the browser.

---

## Project Structure

```
playwright-test/
├── .env                # Secret credentials (not tracked in Git)
├── login_test.py       # Main test script using Playwright
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env and other unnecessary files
└── README.md           # This documentation file
```

---

## How to Run the Test

### 1. Clone the repository & navigate to project

```bash
git clone https://github.com/yourusername/periplus-login-test.git
cd playwright-test
```

### 2. Create and activate virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Setup your `.env` file
Create a `.env` file in the root directory and add:

```env
EMAIL=your_email@example.com
PASSWORD=your_password_here
```

Make sure the email and password are valid and registered in https://www.periplus.com/

### 5. Run the script

```bash
python login_test.py
```

You'll see the browser open, perform the login steps, and print results in the console.

## Coming Soon

 **Next Test Case**: Add-to-Cart Functionality
The next implementation will extend this script to:
* Search for a product
* Add it to the cart
* Verify the cart contains the selected item
