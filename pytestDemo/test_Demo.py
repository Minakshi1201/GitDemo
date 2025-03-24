#any pytest file start with test_
#always write code inside function
#method name starts with test
#method name is nothing but test case so write carefully
# -k starts with method name
#-v and -s for console log
#you can mark(tag) test cases and run them with -m smoke
#use skip to skip particular test case
# xfail will run test case but in output it will not show it is pass or fail
#datadriven and paramertrization can be done using return statement
#fixture scope written only in class , it will run only once class is initiliazed

import pytest
#@pytest.mark.smoke
#@pytest.mark.skip
def test_funct():
    print("Hello Pytest")

@pytest.mark.xfail
def test_creditcard_function():
    print("Welcome")

def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])