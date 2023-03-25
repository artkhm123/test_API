import numbers
import cerberus
from utils import *
from jsonschema import validate
import pytest


@pytest.mark.smoke
def test_status_for_get_method(get_route, dog_ceo_url):
    """Test that all routes are available with GET method"""
    response_get = requests.get(dog_ceo_url + get_route)
    assert response_get.status_code == 200
    assert response_get.json()["status"] == "success"


@pytest.mark.smoke
def test_status_for_other_methods(get_route, dog_ceo_url):
    """Test that POST, PUT, DELETE methods are not available for all routs"""
    response_delete = requests.delete(dog_ceo_url + get_route)
    response_put = requests.put(dog_ceo_url + get_route, data=TEST_REQUEST_BODY)
    response_post = requests.post(dog_ceo_url + get_route, data=TEST_REQUEST_BODY)
    assert response_delete.status_code == 405
    assert response_delete.json()["status"] == "error"
    assert response_put.status_code == 405
    assert response_delete.json()["status"] == "error"
    assert response_post.status_code == 405
    assert response_delete.json()["status"] == "error"


@pytest.mark.regress
@pytest.mark.parametrize("random_number", [-1, 0, 1, 25, 50, 100, "two"],
                         ids=[
                             "negative = -1",
                             "zero = 0",
                             "lower border = 1",
                             "positive = 25",
                             "higher border = 50",
                             "over the limits = 100500",
                             "letter = two"
                         ])
def test_random_logic_count_all_breeds(random_number, dog_ceo_url):
    """Test that number of pictures returned by https://dog.ceo/api/breeds/image/random/{n}
    equals {n}
    -50 is max amount of returned pictures
    -if {n} is not a number - endpoint returns one random picture
    e.g.
    api/breeds/image/random/3 returns 3 random pictures
    api/breeds/image/random/100500 returns 50 random pictures
    api/breeds/image/random/abc returns 1 random picture
    """

    response = requests.get(dog_ceo_url + f"api/breeds/image/random/{random_number}")
    if isinstance(random_number, numbers.Number):
        if random_number < 1:
            count = 1
        elif random_number > 50:
            count = 50
        else:
            count = random_number
    else:
        count = 1
    assert response.status_code == 200
    assert len(response.json()['message']) == count


breed_generator = (i for i in requests.get(URL + "api/breeds/list/all").json()['message'])


@pytest.mark.regress
@pytest.mark.parametrize("breed", breed_generator)
def test_breed_schema(breed, dog_ceo_url):
    """Validate schema of https://dog.ceo/api/breed/hound/list"""
    response = requests.get(dog_ceo_url + "api/breed/" + str(breed) + "/list")
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema_breed_list)


breed_generator = (i for i in requests.get(URL + "api/breeds/list/all").json()['message'])


@pytest.mark.regress
@pytest.mark.parametrize("breed", breed_generator)
def test_breed_image_schema(dog_ceo_url, breed):
    """Validate schema of https://dog.ceo/api/breeds/{breed}/images"""
    response = requests.get(dog_ceo_url + "api/breed/" + str(breed) + "/images")
    v = cerberus.Validator()
    assert response.status_code == 200
    assert v.validate(response.json(), schema_breed_image)
