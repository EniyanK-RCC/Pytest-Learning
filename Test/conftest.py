import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Environment to run tests against")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--env") == "prod":
        skip_prod = pytest.mark.skip(reason="do not run on prod")
        for item in items:
            if "skip_on_prod" in item.keywords:
                item.add_marker(skip_prod)