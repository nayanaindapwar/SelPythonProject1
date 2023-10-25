# Any pytest file should start with test_filename or filename_test
# Pytest method name should start with word test
# Any code should be wrapped in method only
# In Pytest test case name is method name only so as per test scenario, please specify suitable test case/method name
# -k : method name execution with regular expression -s : Logs in output -v : More info metadata
# We can run the specific file by py.test <filename>
# We can mark test with '@pytest.mark.smoke' and then run with -m smoke
# We can skip the test case '@pytest.mark.skip'
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_FirstPytestProgram():
    msg = "Hello"
    assert msg == "hi", "Test failed because string do not match"


def test_SecondCreditCard():
    a=3
    b=6
    assert a+3 == 6, "Addition do not match"


def test_fixtureDemo(setup):
    print("I will execute steps in fixture demo method")





