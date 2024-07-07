from pydantic import BaseModel, field_validator, validator, Field
from typing import Tuple, Optional
from conf.conf import KEY, BASE_URL_3_0
import requests
# from conf.conf import




class Validate_Base_Model(BaseModel):
    address_name: Optional[str] = None
    building_name: Optional[str] = None
    full_name: Optional[str] = None
    id: str
    name: str
    purpose_name: Optional[str] = None
    subtype: Optional[str] = None
    type: str



class Validate_items_Base_model(BaseModel):
    address_name: str
    building_name: str
    full_name: str
    id: str
    name: str
    purpose_name: str
    type: str




# class Get_Exercise_Base_Model(BaseModel):
#     bodyPart: str
#     equipment: str
#     gifUrl: str
#     id: str
#     name: str
#     target: str
#     secondaryMuscles: Tuple[str, ...]
#     instructions: Tuple[str, ...]
#
#
#     @field_validator('bodyPart')
#     def check_correct_bodypart(cls, bodyPart):
#         if bodyPart not in BODYPARTS:
#             raise ValueError("Wrong bodypart data")
#
#     @field_validator('equipment')
#     def check_correct_bodypart(cls, equipment):
#         if equipment not in EQUIPMENTTYPE:
#             raise ValueError("Wrong equipmentType data")
#
#     @field_validator('id')
#     def check_correct_bodypart(cls, id: str):
#         if id.isdigit() and int(id) > 0:
#             pass
#         else:
#             raise ValueError("Wrong id")
#
#
#
