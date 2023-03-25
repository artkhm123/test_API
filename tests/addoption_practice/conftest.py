import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="url to execute"
    )
    parser.addoption(
        "--status_code",
        default="200",
        help="expected status code"
    )


@pytest.fixture
def base_url_ya(request):
    return request.config.getoption("--url")


@pytest.fixture
def expected_status_code(request):
    return request.config.getoption("--status_code")
