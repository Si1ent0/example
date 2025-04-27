import allure

from allure_commons.types import Severity
from example.application import app


@allure.epic("Main page")
@allure.feature("Main page")
@allure.story("Main page element on display")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "web", "reg")
@allure.severity(Severity.CRITICAL)
@allure.link("https://vkvideo.ru/", name="main page")
@allure.step("Проверка элементов на странице")
def test_element_should_be_display(browser_config):
    # Открытие страницы Main
    app.main_page.open_main_page()
    # Проверка элементов на странице
    app.main_page.top_bar_element_should_be_display()
    app.main_page.left_bar_element_should_be_display()
    app.main_page.quick_log_element_should_be_display()
    app.main_page.tab_slider_element_should_be_display()

