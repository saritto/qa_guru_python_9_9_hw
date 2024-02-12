import allure
from selene import browser, be, by
from allure_commons.types import Severity


def test_decorator_allure_step():
    open_main_page()
    search_for_repo("eroshenkoam/allure-example")
    go_to_repo()
    open_issue()
    check_issue("#76")
    # dynamic labels
    allure.dynamic.tag("web")
    allure.dynamic.description("Проверка названия Issue в репозитории. Используются Шаги с декоратором @allure.step")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing link")
    allure.dynamic.title("Шаги с декоратором @allure.step")


@allure.step("Открываем главную страницу:")
def open_main_page():
    browser.open("https://github.com")


@allure.step("В поиске ищем репозитории:")
def search_for_repo(repo):
    browser.element('div.search-input-container').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step("Переходим по найденной ссылке:")
def go_to_repo():
    browser.element('a[href="/eroshenkoam/allure-example"]').click()


@allure.step("Переходим в раздел Issues:")
def open_issue():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером 76:")
def check_issue(num):
    browser.element(by.partial_text(num)).should(be.visible)
