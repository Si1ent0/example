
import allure

from selene import browser, be, have


class QuickAuth:
    def __init__(self):
        self.wrapper_close = browser.element('.notifier_close_wrap')
        # Блок быстрой авторизации
        self.quick_log_button = browser.element(
            '//div[@class="VideoQuickLogin__actions"]/div[@data-task-click="VideoShowcase/login"]')
        self.quick_reg_button = browser.element(
            '//div[@class="VideoQuickLogin__actions"]/a[@data-task-click="VideoShowcase/registration"]')
        self.block_quick_auth = browser.element(".vkc__AuthRoot__wrapper")
        self.qr_code = browser.element(".vkc__QRCode__image")
        self.title_qr_quick_auth = browser.element('//span[contains(text(),"Быстрый вход по QR-коду")]')
        self.text_qr_quick_auth = browser.element(
            "//span[contains(text(), 'Отсканируйте QR-код сканером  в приложении ВКонтакте  или камерой устройства')]")
        self.title_quick_auth = browser.element('.vkc__DefaultSkin__caption')
        self.phone_input_quick_auth = browser.element('//input[@name="phone"]')
        self.button_continue_active = browser.element('button.vkuiButton__sizeL.vkuistyles__-focus-visible')
        self.button_continue_not_active = browser.element('button.vkuiButton__disabled')

    @allure.step("Закрытие wrapper")
    def close_wrapper(self):
        self.wrapper_close.click()

    @allure.step("Кликабельна кнопка 'логина быстрого входа'")
    def quick_log_button_should_be_click(self):
        self.quick_log_button.should(be.clickable)
        self.quick_log_button.click()

    @allure.step("Кликабельна кнопка 'регистрации быстрого входа'")
    def quick_reg_button_should_be_click(self):
        self.quick_reg_button.should(be.clickable)
        self.quick_reg_button.click()

    @allure.step("Отображается блок 'быстрой авторизации'")
    def block_quick_auth_should_be_visible(self):
        self.block_quick_auth.should(be.visible)

    @allure.step("Проверка qr code")
    def qr_code_should_be_display(self):
        self.qr_code.should(be.visible)

    @allure.step("Проверка текста quick auth")
    def qr_block_should_have_text(self):
        self.title_qr_quick_auth.should(have.text('Быстрый вход по QR-коду'))
        self.text_qr_quick_auth.should(have.text(
            'Отсканируйте QR-код сканером в приложении ВКонтакте или камерой устройства'))
        self.title_quick_auth.should(have.text('Вход в «VK Видео»'))
        self.button_continue_not_active.should(have.text('Продолжить'))

    @allure.step("Ввод телефона в поле ввода")
    def phone_number_input_should_be_active(self):
        self.phone_input_quick_auth.type(' 999 999-99-99')

    @allure.step("Кнопка 'Продолжить' активна")
    def  active_button_continue_with_phone_number(self):
        self.button_continue_active.should(be.visible)

    @allure.step("Кнопка 'Продолжить' не активна")
    def  not_active_button_continue_without_phone_number(self):
        self.button_continue_not_active.should(be.visible)

    @allure.step("Проверка окна быстрой авторизации")
    def element_quick_auth_should_be_visible(self):
        self.block_quick_auth_should_be_visible()
        self.qr_code_should_be_display()
        self.not_active_button_continue_without_phone_number()