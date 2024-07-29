import pytest

def pytest_addoption(parser):
    parser.addoption("--num1", action="store", default=1, type=int, help="First number")
    parser.addoption("--num2", action="store", default=1, type=int, help="Second number")

@pytest.fixture
def num1(request):
    return request.config.getoption("--num1")

@pytest.fixture
def num2(request):
    return request.config.getoption("--num2")

@pytest.fixture(autouse=True, scope="function")
def setup_and_teardown():
    print("setup code running")
    yield
    print("teardown code running")