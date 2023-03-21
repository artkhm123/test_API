import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com/",
        help="url to execute"
    )


@pytest.fixture
def jsonplaceholder_url(request):
    return request.config.getoption("--url")
