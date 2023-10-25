# Any pytest file should start with test_filename or filename_test
# Pytest method name should start with word test
# Any code should be wrapped in method only
# In Pytest test case name is method name only so as per test scenario, please specify suitable test case/method name
# -k : method name execution with regular expression -s : Logs in output -v : More info metadata
# We can run the specific file by py.test <filename>
# We can mark test with '@pytest.mark.smoke' and then run with -m smoke
# We can skip the test case '@pytest.mark.skip'
# @pytest.mark.xfail
# Fixtures are used as setup and tear down methods for test cases
# conftest file to generalize fixture and to make it available for all test cases
# data driver and parameterization can be done with return statement is tuple format
# when we define fixture scope to class only, it will run once before call is initiated and at the end

import pytest


@pytest.mark.smoke
def test_FirstPytestProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
