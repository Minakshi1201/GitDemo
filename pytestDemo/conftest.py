import pytest
@pytest.fixture()
def setup():
    print("I will excceucte")
    yield
    print("I will be last")

@pytest.fixture()
def test_data():
    print("Data will be dispalyed")

@pytest.fixture(params=[("Chrome","Minakshi"),("Firefox","Khamkar"),("IE","OK")])
def crossbrowser(request):
    return request.param


