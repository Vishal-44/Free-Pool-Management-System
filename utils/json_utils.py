import json

from exceptions import InvalidRequestException

def convert_to_json(json_string):
    try:
        json_data = json.loads(json_string)
        return json_data
    except json.JSONDecodeError as e:
        print("here")
        raise InvalidRequestException()
