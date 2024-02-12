import allure
from selene import browser, be, by
from allure_commons.types import Severity


# decorator labels
@allure.tag("web")
@allure.description("Проверка названия Issue в репозитории. Используются Лямбда шаги через with allure.step")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "saritto")
@allure.link("https://github.com", name="Testing link")
@allure.title("Лямбда шаги через with allure.step")
def test_with_allure_step():
    with allure.step("Открываем главную страницу:"):
        browser.open("https://github.com")

    with allure.step("В поиске ищем репозитории:"):
        browser.element('div.search-input-container').click()
        browser.element('#query-builder-test').type("eroshenkoam/allure-example").press_enter()

    with allure.step("Переходим по найденной ссылке:"):
        browser.element('a[href="/eroshenkoam/allure-example"]').click()

    with allure.step("Переходим в раздел Issues:"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76:"):
        browser.element(by.partial_text("#76")).should(be.visible)
