import json
import requests
from deepdiff import DeepDiff

from routeAPI.conf.conf import BASE_URL, KEY


# from BaseModels.Classes_with_base_model import Validate_Base_Model


class POST_query_Responce():

    def __init__(self, input_data: dict):
        self.input_data = input_data
        self.url = BASE_URL + '?key=' + KEY

        self.answer = requests.post(self.url, json.dumps(input_data))
        self.json_answer = self.answer.json()
        self.status_code = self.answer.status_code
        self.status = self.json_answer['status']

        self.answer_query = self.json_answer['query'] if 'query' in self.json_answer else None
        self.answer_body = self.json_answer['result'] if 'result' in self.json_answer else None

        print(json.dumps(self.json_answer, indent=4))

    def validate_answer_query(self):
        if self.answer_query is not None:
            diff = DeepDiff(self.answer_query, self.input_data)
            assert not diff, f'\nWrong returned query, deepdiff log:\n {diff}'
        return self

    def validate_result_status(self, result_status: str):
        assert self.status == result_status, f'\nWrong rstatusesult answer, expected {result_status}, got {self.status}'
        return self




    # def __str__(self):
    #     pass
