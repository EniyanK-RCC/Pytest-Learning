import pytest
from app import Calculator

@pytest.fixture(scope="module")
def calc():
    print("fixture scope is set to function by default")
    return Calculator()
    yield
    print("teardown code")


def pytest_addoption(parser):
    parser.addoption("--num1", action="store", default=1, type=int, help="First number")
    parser.addoption("--num2", action="store", default=1, type=int, help="Second number")

@pytest.fixture
def num1(request):
    return request.config.getoption("--num1")

@pytest.fixture
def num2(request):
    return request.config.getoption("--num2")