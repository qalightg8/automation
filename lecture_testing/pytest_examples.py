import pytest


@pytest.fixture()
def example_fixture():
    print('Setup is here')
    yield
    print('Tear Down is here')


@pytest.fixture(autouse=True)
def my_custom_fixture_two():
    print('Fixture two working')
    print('second line')
    yield
    print('fixture ends here')


def test_without_fixture():
    print('Test without fixture executed')
    pass


def test_with_fixture(example_fixture):
    print('Test WITH fixture executed')
