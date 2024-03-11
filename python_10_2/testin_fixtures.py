import pytest


@pytest.fixture(scope="session")
def browser():
    print("Browser")
    yield
    print('Closing')


@pytest.fixture()
def login_page(browser):
    print('Login')
    pass


@pytest.fixture()
def user():
    return "username", "password"


def login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


login(login_page, user)

