import pytest
import os


def test_one():
    assert True


def test_two():
    l1 = [1, 2, 3]
    l2 = [3, 4, 5]
    assert l1 == l2


@pytest.mark.skip('just don`t want to run this test')
def test_three():
    assert True


@pytest.mark.smoke
def test_1():
    pass


@pytest.mark.smoke
@pytest.mark.regression
def test_2():
    pass


@pytest.mark.regression
def test_3():
    pass


@pytest.mark.xfail
def test_4():
    pass


@pytest.mark.skipif(os.name not in ['nt'], reason='only unix systems')
def test_5():
    print(os.name)
    pass


