import json
import requests
from deepdiff import DeepDiff

from conf.conf import STATUSCODES, query_params
from conf.conf import BASE_URL_3_0, KEY
from BaseModels.Classes_with_base_model import Validate_Base_Model


class Get_query_Responce():
    def __init__(self, *args, **kwargs):
        query_params_str = self.concat_kwargs(**kwargs)
        if 'q' in kwargs and kwargs['q'] is not None:
            self.query = kwargs['q']
        self.url = BASE_URL_3_0 + f'/items?' + query_params_str
        self.response = requests.get(self.url)
        self.response_json = self.response.json()
        self.status_code = self.response.status_code
        if 'result' in self.response_json and 'items' in self.response_json['result']:
            # print(json.dumps(self.response_json, indent=4, ensure_ascii=False))
            self.city_id = str(self.response_json['result']['items'][0]['id'])
            print(self.city_id)
        else:
            self.city_id = None

    @staticmethod
    def concat_kwargs(**kwargs) -> str:
        pairs = [f"{key}={value}" for key, value in kwargs.items()]
        result = "&".join(pairs)
        return result

    def validate_status_code(self, status_code):
        if status_code in STATUSCODES:
            assert self.status_code == status_code, f"Recieved wrong status code\n{self}"
        else:
            assert False, 'Invalid status code'
        return self

    def validate_model(self):
        if self.city_id is not None:
            for item in self.response_json['result']['items']:
                Validate_Base_Model.model_validate_json(json.dumps(item))

    def validate_items_data(self, item_data: dict):
        for key, value in item_data.items():
            if key == ['']:
                diff = DeepDiff(value, self.response_json['result']['items'], ignore_order=True)
                assert not diff, 'diff log:' + str(diff)
        return self


    def __str__(self):
        str = f"\n\nstatus_code: {self.status_code}\n" + \
              f"requested url:{self.url}\n"
        if self.city_id is not None:
            return str + f"meta: {json.dumps(self.response_json['meta'], indent=4, ensure_ascii=False)}\n" + \
                f"body: {json.dumps(self.response_json['result'], indent=4, ensure_ascii=False)}"
        else:
            return str + "No Data"
