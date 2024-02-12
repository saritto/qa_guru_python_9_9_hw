from selene import browser, be, by


def test_github():
    browser.open("https://github.com")
    browser.element('div.search-input-container').click()
    browser.element('#query-builder-test').type("eroshenkoam/allure-example").press_enter()

    browser.element('a[href="/eroshenkoam/allure-example"]').click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)
