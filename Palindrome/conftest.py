import pytest
from palindrome import isPalindrome

def pytest_addoption(parser):
    parser.addoption("--word", action="store", default=1, type=str)

@pytest.fixture(scope="module")
def word(request):
    return request.config.getoption("--word")