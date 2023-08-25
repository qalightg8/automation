import pytest


def test_four():
    assert True


def test_five_1():
    pass


def test_five_2():
    pass


@pytest.mark.parametrize('param', [1, 2, 3, 'text'])
def test_with_multiple_parameters(param):
    assert type(param) is int


class TestExampleFile2:

    def test_one_in_class(self):
        pass

    def test_two_in_class(self):
        pass

    def test_five_3(self):
        pass
