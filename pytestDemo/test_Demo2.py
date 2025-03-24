
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_funct():
    msg = "Hello"
    assert msg == "Hii","Test failed"

def test_creditcard_function():
    a = 4
    assert a +2 == 6 ,"test Passed"