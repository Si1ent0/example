import allure
import requests

from example.utils import allure_attach


def get_main_page(api_url):
    with allure.step('Получаем главную страницу'):
        method = 'GET'
        try:
            with allure.step(f'Отправить {method} для получения главной страницы'):
                response = requests.request(method=method, url=f'{api_url}')
            return response

        except requests.ConnectionError as e:
            with allure.step(f'api connection error: {e}'):
                raise Exception(f'api connection error: {e}')

def check_response_code(response):
    with allure.step('Проверяем, что api возвращает 200 код ответа'):
        allure_attach.response_code(str(response.status_code))
    assert response.status_code == 200, (f'Get main page. '
                                         f'Response code: {response.status_code} ')