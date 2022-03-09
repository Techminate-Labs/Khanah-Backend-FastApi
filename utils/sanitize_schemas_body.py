# This function receives a schema object,
# converts it to a dictionary
# and then returns it with the None values
from pydantic import BaseModel


def sanitize(body: BaseModel) -> dict:
    body = body.dict()
    filtered_body = {}

    for key, value in body.items():
        if value:
            filtered_body[key] = value

    return filtered_body
