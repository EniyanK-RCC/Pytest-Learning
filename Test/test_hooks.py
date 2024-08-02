import pytest

@pytest.mark.skip_on_prod
def test_feature():
    print("dev")
    assert True

@pytest.mark.other
def test_other_feature(env):
    print("dev and prod")
    assert env in ["dev", "prod"]

