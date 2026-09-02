from playwright.sync_api import Page, expect


def test_open_product_details(page: Page):
    page.goto("https://with-bugs.practicesoftwaretesting.com/#/")

    page.locator('[data-test="product-1"]').click()

    expect(
        page.locator('[data-test="product-name"]')
    ).to_be_visible()

    expect(
        page.locator('[data-test="product-description"]')
    ).to_be_visible()
