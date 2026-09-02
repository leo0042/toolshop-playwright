# Toolshop Playwright UI Automation

A small end-to-end UI automation project built with **Python, Playwright, and pytest** to automate key user flows in the Toolshop web application.

The project focuses on practical UI automation using reliable locators, user-facing actions, and meaningful assertions rather than building an unnecessarily complex automation framework.

## Project Overview

**Application:** Toolshop  
**Automation Type:** UI / End-to-End Testing  
**Language:** Python  
**Framework:** Playwright + pytest  
**Browser:** Chromium

The application used for this project is a practice e-commerce application containing product browsing and shopping-cart functionality.

## Automated Test Scenarios

The project currently contains **4 automated tests** covering the following core scenarios:

| Test | Scenario | Expected Result |
|---|---|---|
| Search by keyword | Search for an existing product keyword | Matching products are displayed |
| Search with no results | Search for a non-existent keyword | Zero products are returned |
| Open product details | Select a product from the catalog | Product details are displayed |
| Add product to cart | Add a product to the cart | Cart quantity is updated |

## Project Structure

```text
toolshop-playwright/
├── tests/
│   ├── test_search.py
│   ├── test_product.py
│   └── test_cart.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Key Playwright Concepts Used

- `page.goto()` for navigation
- Role/text/test-oriented locators
- CSS attribute locators where appropriate
- `click()`
- `fill()`
- `expect()` assertions
- URL and element-state validation
- Dynamic validation of search results
- Playwright's automatic waiting and synchronization

## Locator Investigation

During development, a search test initially failed because the locator targeted:

```text
data-testid="search-query"
```

while the actual application element used:

```text
data-test="search-query"
```

The locator was corrected after inspecting the application's DOM.

This reinforced an important UI automation practice: when a locator fails, first verify that the locator actually matches the application's DOM before introducing waits, sleeps, or retries.

## Running the Tests

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install
```

### 4. Run the test suite

```bash
pytest
```

The repository is configured to run the tests using Chromium by default.

## Test Results

**4 tests passed successfully.**

```text
4 passed
```

## Relationship to Manual QA Project

This automation project uses the same Toolshop application as my manual/API QA project, but has a separate focus.

The manual QA project focuses on:

- Test planning
- Manual functional testing
- Test cases and execution
- Bug reporting
- API testing with Postman
- Browser DevTools investigation

This project focuses specifically on:

- UI automation
- Playwright
- Python
- Automated assertions
- Locator strategy
- End-to-end regression coverage

The projects are therefore complementary rather than being a single duplicated project. 
