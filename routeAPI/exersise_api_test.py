from routeAPI.classMethods.Post import POST_query_Responce
from routeAPI.conf.conf import easy_route


def test_1():
    post = POST_query_Responce(easy_route).validate_answer_query().validate_result_status('OK')


def test_2():
    route = easy_route
    post = POST_query_Responce(route).validate_answer_query().validate_result_status('OK')
    length = post.answer_body[0]['length']
    for i in range(10):
        easy_route["points"][0]["lon"] = round(easy_route["points"][0]["lon"] - 0.01, 4)
        easy_route["points"][0]["lat"] = round(easy_route["points"][0]["lat"] - 0.01, 4)

        easy_route["points"][1]["lon"] = round(easy_route["points"][1]["lon"] + 0.01, 4)
        easy_route["points"][1]["lat"] = round(easy_route["points"][1]["lat"] + 0.01, 4)

        next_post = POST_query_Responce(easy_route).validate_answer_query().validate_result_status('OK')
        next_length = next_post.answer_body[0]['length']
        assert length < next_length, 'Wrong calculated responce lenght :('
        length = next_length


def test_3():
    route = easy_route
    post = POST_query_Responce(route).validate_answer_query().validate_result_status('OK')
    length = post.answer_body[0]['length']
    for i in range(10):
        easy_route["points"][0]["lon"] = round(easy_route["points"][0]["lon"] + 0.0001, 4)
        easy_route["points"][0]["lat"] = round(easy_route["points"][0]["lat"] + 0.0001, 4)

        easy_route["points"][1]["lon"] = round(easy_route["points"][1]["lon"] - 0.0001, 4)
        easy_route["points"][1]["lat"] = round(easy_route["points"][1]["lat"] - 0.0001, 4)

        next_post = POST_query_Responce(easy_route).validate_answer_query().validate_result_status('OK')
        next_length = next_post.answer_body[0]['length']
        assert length > next_length, 'Wrong calculated responce lenght :('
        length = next_length
