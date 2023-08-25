import logging


def test_logging_1():
    logging.debug('test_logging_1 executed')


def test_logging_2():
    logging.info('test_logging_2 executed')


def test_logging_3():
    logging.error('test_logging_3 executed')


def foo():
    raise TypeError('raise type error for test')


def test_logging_4():
    try:
        foo()
    except TypeError as e:
        logging.exception(f'{e}, {type(e)}')


def test_logging_5():
    logging.info('just info')
