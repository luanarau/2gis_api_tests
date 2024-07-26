import pytest

BASE_URL = 'http://routing.api.2gis.com/routing/7.0.0/global'

KEY = 'e7f5231f-6951-449a-8ba4-bbefe834b54a'

STATUSCODES = [200, 400, 403, 404, 408, 500]


POINTS_IN_NOVOSIBIRSK = [
    {"lon": 82.9204, "lat": 55.0302, "type": "stop"},
    {"lon": 82.9390, "lat": 55.0084, "type": "stop"}
]

POINTS_IN_MOSCOW = [
    {"lon": 37.618423, "lat": 55.751244, "type": "stop"},
    {"lon": 37.564323, "lat": 55.774532, "type": "stop"}
]

POINTS_IN_SAHALIN = 

POINTS_IN_OMAN = [
    {"lon": 58.5453, "lat": 23.6108, "type": "stop"},
    {"lon": 58.3914, "lat": 23.5859, "type": "stop"}
]

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








