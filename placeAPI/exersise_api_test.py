from routeAPI.conf.conf import test_city_valid_data, test_city_invalid_data, test_city_valid_json_responce
from routeAPI.conf.conf import test_valid_query
from classMethods.Get import Get_query_Responce
from routeAPI.conf.conftest import get_test_time





@get_test_time
def test_search_place_valid_city_param_q():
    for city in test_city_valid_data:
        test1 = (Get_query_Responce(q=city).validate_status_code(200).validate_items_data(test_city_valid_json_responce)
                 .validate_model())
@get_test_time
def test_search_place_invalid_city_param_q():
    for city in test_city_invalid_data:
        test1 = (Get_query_Responce(q=city).validate_status_code(200).validate_model())


@get_test_time
def test_search_place_valid_param_q():
    for query in test_valid_query:
        test1 = (Get_query_Responce(q=query).validate_status_code(200).validate_model())





# 4504222397630173
