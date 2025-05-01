import allure

from example.pages.API.get_main_page import get_main_page


@allure.epic('API')
@allure.story('Get main page')
@allure.title('Get main page')
@allure.feature('Get main page')
@allure.label('microservice', 'API')
@allure.label('owner', 'rs')
@allure.tag('regress', 'smoke', 'API')
@allure.severity('Critical')
def test_get_main_page(api_url):
    get_main_page(api_url)