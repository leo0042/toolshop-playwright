 
from playwright.sync_api import Page, expect


def test_add_product_to_cart(page: Page):
    page.goto("https://with-bugs.practicesoftwaretesting.com/#/")

    page.locator('[data-test="product-1"]').click()

    page.locator('[data-test="add-to-cart"]').click()

    expect(
        page.locator('[data-test="cart-quantity"]')
    ).to_have_text("1")