from utils import *
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://dog.ceo/",
        help="url to execute"
    )


@pytest.fixture
def dog_ceo_url(request):
    return request.config.getoption("--url")


@pytest.fixture(params=ROUTES_LIST)
def get_route(request):
    return request.param
