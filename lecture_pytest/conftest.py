import pytest


@pytest.fixture(autouse=True)
def global_lecture_pytest_fixture():
    print('global_lecture_pytest_fixture setup')
    yield
    print('global_lecture_pytest_fixture teardown')

