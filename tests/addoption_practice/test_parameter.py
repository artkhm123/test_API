import requests


def test_status_code(base_url_ya, expected_status_code):
    resp = requests.get(base_url_ya)
    assert resp.status_code == int(expected_status_code)
