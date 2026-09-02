from playwright.sync_api import Page, expect


def test_search_products_by_keyword(page: Page):
    page.goto("https://with-bugs.practicesoftwaretesting.com/#/")


    keyword = "drill"

    page.locator('[data-test="search-query"]').fill(keyword)
    page.locator('[data-test="search-submit"]').click()

    page.locator('[data-test="search_completed"]').wait_for()

    search_term = page.locator('[data-test="search-term"]')
    expect(search_term).to_have_text(keyword)

    products = page.locator('[data-test="product-name"]')

    for i in range(products.count()):
        expect(products.nth(i)).to_contain_text(
            keyword, ignore_case=True
        )



def test_search_with_no_results(page: Page):
    page.goto("https://with-bugs.practicesoftwaretesting.com/#/")

    search_input = page.locator('[data-test="search-query"]')
    search_button = page.locator('[data-test="search-submit"]')

    keyword = "zzzzz"

    search_input.fill(keyword)
    search_button.click()

    expect(page.locator('[data-test="search-term"]')).to_have_text(keyword)

    expect(
        page.locator('[data-test="search-result-count"]')
    ).to_contain_text("0 products found")

    expect(
        page.locator('[data-test="product-name"]')
    ).to_have_count(0)