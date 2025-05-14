import allure

from api.get_main_page import get_main_page, check_response_code


@allure.epic('api')
@allure.story('Get main page')
@allure.title('Get main page')
@allure.feature('Get main page')
@allure.label('microservice', 'api')
@allure.label('owner', 'rs')
@allure.tag('regress', 'smoke', 'api')
@allure.severity('Critical')
def test_get_main_page(api_url):
    response = get_main_page(api_url)
    check_response_code(response)