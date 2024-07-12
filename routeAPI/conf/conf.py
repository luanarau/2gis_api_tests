BASE_URL = 'http://routing.api.2gis.com/routing/7.0.0/global'

KEY = 'e7f5231f-6951-449a-8ba4-bbefe834b54a'

STATUSCODES = [200, 400, 403, 404, 408, 500]

def make_header(body: dict) -> str:
    return 'Content-Type: application/json' + f'--data {body}'




