import pytest


@pytest.fixture(autouse=True)
def lecture1_pytest_fixture():
    print('lecture1_pytest_fixture setup')
    yield
    print('lecture1_pytest_fixture teardown')

