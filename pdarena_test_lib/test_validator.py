from . import Validator, Result
from time import sleep

validator = Validator(10, 10)


def test_valid():
    def valid(opponent, history):
        return False

    assert validator.validate(valid).result == Result.VALID


def test_timeout():
    def timeout(opponent, history):
        sleep(1.1)

    assert validator.validate(timeout).result == Result.TIMEOUT


def test_exception():
    def exception(opponent, history):
        raise Exception

    assert validator.validate(exception).result == Result.EXCEPTION
