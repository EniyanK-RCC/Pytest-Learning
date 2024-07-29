import pytest
from palindrome import isPalindrome

def pytest_addoption(parser):
    parser.addoption("--word", action="store", default="word", help="word to test for palindrome")

@pytest.fixture
def word(request):
    return request.config.getoption("--word")

def test_palindrome(word):
    assert isPalindrome(word)