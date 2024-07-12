import pytest

BASE_URL = 'http://routing.api.2gis.com/routing/7.0.0/global'

KEY = 'e7f5231f-6951-449a-8ba4-bbefe834b54a'

STATUSCODES = [200, 400, 403, 404, 408, 500]

easy_route = {

    "points": [
        {"lon": 82.8967, "lat": 54.9832, "type": "stop"},
        {"lon": 82.9018, "lat": 54.9862, "type": "stop"}
    ],
    "transport": "car",
    "route_mode": "fastest",
    "traffic_mode": "jam",
    "output": "summary"

}






