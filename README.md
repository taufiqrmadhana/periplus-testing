# Periplus Automated Testing (Python + Playwright)

Automated testing script using **Python**, **Playwright**, and **Dotenv** for the [Periplus](https://www.periplus.com/) website. Tests include login functionality and add-to-cart functionality.

---

## How It Works

The script performs the following tests:

### Login Test
1. Launches a Chromium browser (non-headless for visual debugging)
2. Navigates to the Periplus login page
3. Loads login credentials from the `.env` file
4. Fills in the email and password
5. Clicks the login button
6. Verifies that login is successful by checking the URL

### Cart Test
1. Uses the session from the successful login
2. Navigates to a specified book product page (from `.env` or uses a default)
3. Checks the initial cart count
4. Clicks the "Add to Cart" button
5. Verifies the cart count has increased by 1
6. Reports success or failure

---

## Project Structure

```
periplus-testing/
├── .env                # Secret credentials and configuration (not tracked in Git)
├── main.py             # Main test script using Playwright
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env and other unnecessary files
└── README.md           # This documentation file
```

---

## How to Run the Tests

### 1. Clone the repository & navigate to project

```bash
git clone https://github.com/yourusername/periplus-testing.git
cd periplus-testing
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
BOOKURL=https://www.periplus.com/p/your-preferred-book-url  # Optional - uses default if not provided
```

Make sure the email and password are valid and registered on https://www.periplus.com/

### 5. Run the script

```bash
python main.py
```

You'll see the browser open, perform the login steps, navigate to the product page, add the item to cart, and print results in the console.

---

## Sample Output

A successful test run will output something like:

```
Navigating to login page...
Filling in login credentials...
URL after login: https://www.periplus.com/_index_/index
Successfully Logged In
Navigating to product page...
Initial cart count: 0
Cart count after adding: 1
Product successfully added to cart!
```

---