import pytest


@pytest.fixture()
def example_fixture():
    print('Setup is here')
    yield
    print('Tear Down is here')


def test_without_fixture():
    print('Test without fixture executed')


def test_with_fixture(example_fixture):
    print('Test WITH fixture executed')
