import pytest


@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    print('Session fixture setup')
    yield
    print('Session fixture teardown')


@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('Module fixture setup')
    yield
    print('Module fixture teardown')


@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    print('Class fixture setup')
    yield
    print('Class fixture teardown')


@pytest.fixture(scope='function', autouse=True)
def function_fixture():
    print('Function fixture setup')
    yield
    print('Function fixture teardown')


class TestFixtures:

    def test_fixtures_1(self):
        pass

    def test_fixtures_2(self):
        pass
