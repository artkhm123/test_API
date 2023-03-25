import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://api.openbrewerydb.org/",
        help="url to execute"
    )


@pytest.fixture
def openbrewerydb_url(request):
    return request.config.getoption("--url")
