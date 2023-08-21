import unittest


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Class Setup here')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Class CleanUp here')


class HumanTest(BaseTest):

    def setUp(self) -> None:
        print('Human tests setup')

    def tearDown(self) -> None:
        print('Human tests teardown')


class Human(HumanTest):

    def test_something1(self):
        print('Test of human OK')

    def test_something2(self):
        print('Test of human OK')
