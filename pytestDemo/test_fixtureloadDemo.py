import pytest

from pytestDemo.conftest import test_data


@pytest.mark.usefixtures("test_data")

class Loaddata:
    def test_actualdata(self): #when you return something then we need to pass fixture name though we declare gobally
        print(test_data)
