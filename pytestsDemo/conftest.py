# ConfTest File
import pytest


@pytest.fixture(scope="class")
def setup():
    print("I am executing test setup fixture")
    yield
    print("I'll execute it last")


@pytest.fixture(scope="class")
def dataLoad():
    print("Creating the user profile")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "rahul", "shetty"), ("firefox", "abc"), ("edge", "pqr")])
def crossBrowser(request):
    return request.param
