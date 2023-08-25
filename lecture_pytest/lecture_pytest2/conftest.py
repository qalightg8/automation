import pytest


@pytest.fixture(autouse=True)
def lecture2_pytest_fixture():
    print('lecture2_pytest_fixture setup')
    yield
    print('lecture2_pytest_fixture teardown')

