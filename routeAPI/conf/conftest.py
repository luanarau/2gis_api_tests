import pytest
import requests
import time
from conf.conf import BASE_URL_3_0, KEY



@pytest.fixture
def get_city_id(city: str):
    url = BASE_URL_3_0 + f'/items?q={city}&key=' + KEY
    json_response = requests.get(url).json()
    if 'result' in json_response and 'items' in json_response['result']:
        return str(json_response['result']['items'][0]['id'])
    else:
        return None


def get_test_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f" test time is: {end}")
        return result
    return wrapper








