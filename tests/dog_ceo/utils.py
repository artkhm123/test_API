import random
import requests

TEST_REQUEST_BODY = {"breed": "newfoundland"}
URL = "https://dog.ceo/"
TEST_REQUEST_BODY = {"breed": "newfoundland"}


def get_breeds_list():
    """Returns a list of all dog breeds from
    https://dog.ceo/api/breeds/list/all"""
    response = requests.get(URL + "api/breeds/list/all")
    breeds = response.json()
    breeds_list = []
    for k, v in breeds['message'].items():
        breeds_list.append(k)
    return breeds_list


def get_breeds_with_sub_breeds():
    """Returns a list of all dogs breed which have sub-breed from
        https://dog.ceo/api/breeds/list/all"""
    response = requests.get(URL + "api/breeds/list/all")
    subbreeds = response.json()
    subbreeds_list = []
    for k, v in subbreeds['message'].items():
        subbreeds_list.append(k)
    return subbreeds_list


ROUTES_LIST = [
    "api/breeds/list/all",
    "api/breeds/image/random",
    f"api/breeds/image/random/{random.randint(1, 50)}",
    f"api/breed/{random.choice(get_breeds_list())}/images",
    f"api/breed/{random.choice(get_breeds_list())}/images/random",
    f"api/breed/{random.choice(get_breeds_list())}/images/random/{random.randint(1, 50)}",
    f"api/breed/{random.choice(get_breeds_with_sub_breeds())}/list",
    f"api/breed/{random.choice(get_breeds_list())}/images"
]

schema_breed_image = {
    "message": {"type": "list", "required": True},
    "status": {"type": "string", "required": True}
}

schema_breed_list = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "message": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                }
            ]
        },
        "status": {
            "type": "string"
        }
    },
    "required": [
        "message",
        "status"
    ]
}
