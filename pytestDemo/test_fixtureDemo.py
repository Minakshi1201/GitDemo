#conftest file to generailze test cases
import pytest
@pytest.mark.usefixtures("setup")


class TestExample:
    def test_fixturedemo(self):
        print("I will be execute after some time")

    def test_fixturedemo2(self):
        print("I will be execute after some time")
    def test_fixturedemo3(self):
       print("I will be execute after some time")

    def test_fixturedemo4(self):
      print("I will be execute after some time")

def test_fixturedemo5(setup):
    print("I will be execute after some time")

def test_fixturedemo6(setup):
    print("I will be execute after some time")
