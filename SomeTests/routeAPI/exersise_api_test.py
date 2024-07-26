import json

from routeAPI.classMethods.Post import POST_query_Responce
from routeAPI.conf.conf import easy_route
from routeAPI.BaseModels.Enums import type_of_transport
from routeAPI.conf.conf import BASE_URL, KEY
import requests


def test_1():
    post = POST_query_Responce(easy_route).validate_answer_query().validate_result_status('OK')

def test_valid_transport():
    route = easy_route
    for transport in type_of_transport:
        if transport.name == 'emergency':
            continue
        else:
            request_data = route.copy()
            request_data["transport"] = transport.value
            post = POST_query_Responce(request_data).validate_answer_query().validate_result_status('OK')


def test_transport_emergency():

    easy_route1 = {

        "points": [
            {"lon": 58.5453, "lat": 23.6108, "type": "stop"},
            {"lon": 58.3914, "lat": 23.5859, "type": "stop"}
        ],
        "transport": 'emergency',
        "route_mode": "fastest",
        "traffic_mode": "jam",
        "output": "summary"

    }

    easy_route = {

        "points": [
            {"lon": 82.8967, "lat": 54.9832, "type": "stop"},
            {"lon": 82.9018, "lat": 54.9862, "type": "stop"}
        ],
        "transport": 'emergency',
        "route_mode": "fastest",
        "traffic_mode": "jam",
        "output": "summary"

    }

    post = requests.post(BASE_URL + '?key=' + KEY, json.dumps(easy_route1))
    print(post.json(), post.status_code)

    # post = POST_query_Responce(route).validate_status_code(400)


# def test_3():
#     route = easy_route
#     post = POST_query_Responce(route).validate_answer_query().validate_result_status('OK')
#     length = post.answer_body[0]['length']
#     for i in range(10):
#         easy_route["points"][0]["lon"] = round(easy_route["points"][0]["lon"] - 0.01, 4)
#         easy_route["points"][0]["lat"] = round(easy_route["points"][0]["lat"] - 0.01, 4)
#
#         easy_route["points"][1]["lon"] = round(easy_route["points"][1]["lon"] + 0.01, 4)
#         easy_route["points"][1]["lat"] = round(easy_route["points"][1]["lat"] + 0.01, 4)
#
#         next_post = POST_query_Responce(easy_route).validate_answer_query().validate_result_status('OK')
#         next_length = next_post.answer_body[0]['length']
#         assert length < next_length, 'Wrong calculated responce lenght :('
#         length = next_length
#
#
# def test_3():
#     route = easy_route
#     post = POST_query_Responce(route).validate_answer_query().validate_result_status('OK')
#     length = post.answer_body[0]['length']
#     for i in range(10):
#         easy_route["points"][0]["lon"] = round(easy_route["points"][0]["lon"] + 0.0001, 4)
#         easy_route["points"][0]["lat"] = round(easy_route["points"][0]["lat"] + 0.0001, 4)
#
#         easy_route["points"][1]["lon"] = round(easy_route["points"][1]["lon"] - 0.0001, 4)
#         easy_route["points"][1]["lat"] = round(easy_route["points"][1]["lat"] - 0.0001, 4)
#
#         next_post = POST_query_Responce(easy_route).validate_answer_query().validate_result_status('OK')
#         next_length = next_post.answer_body[0]['length']
#         assert length > next_length, 'Wrong calculated responce lenght :('
#         length = next_length
