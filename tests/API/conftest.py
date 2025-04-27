import pytest


@pytest.fixture
def api_url():
    return 'https://vkvideo.ru/'


@pytest.fixture
def headers():
    headers = \
        {
            'accept': '/',
        }
    return headers