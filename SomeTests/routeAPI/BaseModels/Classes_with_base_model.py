from pydantic import BaseModel, field_validator, validator, Field


class validate_result(BaseModel):
    duration: int
    length: int