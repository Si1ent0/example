import allure

from allure_commons.types import Severity

from example.application import app


@allure.epic("Main page")
@allure.feature("Main page")
@allure.story("Quick Auth")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "web", "reg")
@allure.severity(Severity.CRITICAL)
@allure.link("https://vkvideo.ru/", name="main page")
@allure.step("Проверка окна быстрой авторизации через логин")
def test_quick_auth_login(browser_config):
    app.main_page.open_main_page()
    app.quick_auth.close_wrapper()
    app.quick_auth.quick_log_button_should_be_click()
    app.quick_auth.block_quick_auth()


@allure.epic("Main page")
@allure.feature("Main page")
@allure.story("Quick Auth")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "web", "reg")
@allure.severity(Severity.CRITICAL)
@allure.link("https://vkvideo.ru/", name="main page")
@allure.step("Проверка окна быстрой авторизации через регистрацию")
def test_quick_auth_reg(browser_config):
    app.main_page.open_main_page()
    app.quick_auth.close_wrapper()
    app.quick_auth.quick_reg_button_should_be_click()
    app.quick_auth.block_quick_auth()


@allure.epic("Main page")
@allure.feature("Main page")
@allure.story("Quick Auth")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "web", "reg")
@allure.severity(Severity.CRITICAL)
@allure.link("https://vkvideo.ru/", name="main page")
@allure.step("Проверка активности кнопки Продолжить")
def test_quick_auth_button(browser_config):
    app.main_page.open_main_page()
    app.quick_auth.close_wrapper()
    app.quick_auth.quick_reg_button_should_be_click()
    app.quick_auth.phone_number_input()
    app.quick_auth.active_button_continue_with_phone_number()