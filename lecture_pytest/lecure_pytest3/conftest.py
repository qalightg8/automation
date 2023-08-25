import pytest


@pytest.fixture(autouse=True)
def lecture3_pytest_fixture():
    print('lecture3_pytest_fixture setup')
    yield
    print('lecture3_pytest_fixture teardown')

