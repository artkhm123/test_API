import pytest
import requests
from jsonschema import validate

from utils import *


@pytest.mark.smoke
@pytest.mark.parametrize("resource, schema", [
    (RESOURCES_LIST["posts"], schema_posts),
    (RESOURCES_LIST["comments"], schema_comments),
    (RESOURCES_LIST["albums"], schema_albums),
    (RESOURCES_LIST["photos"], schema_photos),
    (RESOURCES_LIST["todos"], schema_todos),
    (RESOURCES_LIST["users"], schema_users)
])
def test_jsonplaceholder_schemas_validate(resource, schema, jsonplaceholder_url):
    """Validate schemas for all resources for https://jsonplaceholder.typicode.com """
    get_response = requests.get(jsonplaceholder_url + resource)
    assert get_response.status_code == 200
    validate(instance=get_response.json(), schema=schema)


@pytest.mark.regress
def test_get_exact_post_positive(jsonplaceholder_url):
    """Get exact post by post id - positive cases : randon int from [1,100]"""
    post_num = random.randint(1, POSTS_AMAUNT)
    get_response = requests.get(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(post_num))
    assert get_response.status_code == 200
    assert get_response.json()["id"] == post_num


@pytest.mark.regress
@pytest.mark.parametrize("post_number", [-1, 0, 101, "str"],
                         ids=["negative = -1",
                              "zero = 0",
                              "over the border = 101",
                              "string = str"])
def test_get_exact_post_negative(post_number, jsonplaceholder_url):
    """Negative cases for getting exact post by number: number beyond the limits or str"""
    get_response = requests.get(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(post_number))
    assert get_response.status_code == 404
    assert get_response.json() == {}


@pytest.mark.smoke
@pytest.mark.parametrize("postId", [1, 2, 3])
def test_deleting_a_resource_positive(jsonplaceholder_url, postId):
    """Delet the resource (post) by id - DELETE method"""
    delete_responce = requests.delete(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(postId))
    assert delete_responce.status_code == 200
    assert delete_responce.json() == {}


@pytest.mark.xfail
@pytest.mark.regress
@pytest.mark.parametrize("postId", [-11, 0, 200, "str"],
                         ids=["negative = -11",
                              "zero = 0",
                              "over the border = 200",
                              "string = str"])
def test_deleting_a_resource_negative(jsonplaceholder_url, postId):
    """Delet the resource (post) by id - DELETE method"""
    delete_responce = requests.delete(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(postId))
    assert delete_responce.status_code == 404
    assert delete_responce.json() == {}


@pytest.mark.smoke
@pytest.mark.parametrize("title", ["APPER CASE TITLE", "lower case title", ""])
@pytest.mark.parametrize("body", ["APPER CASE BODY", "lower case body", ""])
@pytest.mark.parametrize("userId", [123, 1])
def test_creat_a_resource(title, body, userId, jsonplaceholder_url):
    """Creating a resource(post) - POST method on /posts"""
    post_body = {"title": title, "body": body, "userId": userId}
    post_responce = requests.post(jsonplaceholder_url + RESOURCES_LIST["posts"], data=post_body)
    assert post_responce.status_code == 201
    assert post_responce.json()["title"] == title
    assert post_responce.json()["body"] == body
    assert int(post_responce.json()["userId"]) == userId
    assert post_responce.json()["id"] == 101


@pytest.mark.smoke
@pytest.mark.parametrize("title", ["APPER CASE TITLE", "lower case title", ""])
@pytest.mark.parametrize("body", ["APPER CASE BODY", "lower case body", ""])
@pytest.mark.parametrize("userId", [123, 1])
@pytest.mark.parametrize("postId", [1, 2, 3])
def test_update_a_resource(title, body, userId, postId, jsonplaceholder_url):
    """Updating a resource(post) - PUT method on posts/{postId}"""
    put_body = {"id": postId, "title": title, "body": body, "userId": userId}
    put_responce = requests.put(jsonplaceholder_url + RESOURCES_LIST["posts"] + str(postId), data=put_body)
    assert put_responce.status_code == 200
    assert put_responce.json()["title"] == title
    assert put_responce.json()["body"] == body
    assert int(put_responce.json()["userId"]) == userId
    assert put_responce.json()["id"] == postId
