from routeAPI.classMethods.Post import POST_query_Responce


dict_test = {

    "points": [
        {"lon": 82.8967, "lat": 54.9832, "type": "stop"},
        {"lon": 82.9018, "lat": 54.9862, "type": "stop"}
    ],
    "transport": "car",
    "route_mode": "fastest",
    "traffic_mode": "jam",
    "output": "summary"

}

def test_1():
    post = POST_query_Responce(dict_test).validate_answer_query()
    a = [i for i in range(10)]
    b = [i for i in a if i < 5]
    print(b)

