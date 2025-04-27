import allure
import requests

from example.utils import allure_attach


def get_main_page(api_url):
    with allure.step('Получаем главную страницу'):
        method = 'GET'
        try:
            with allure.step(f'Отправить {method} для получения главной страницы'):
                response = requests.request(method=method, url=f'{api_url}')

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                allure_attach.response_code(str(response.status_code))

            assert response.status_code == 200, (f'Get main page. '
                                                 f'Response code: {response.status_code} ')

            return None

        except requests.ConnectionError as e:
            with allure.step(f'API connection error: {e}'):
                raise Exception(f'API connection error: {e}')