from dataclasses import dataclass
from enum import Enum
from time import time
from typing import Callable, List, Union

# should_defect function
Bot = Callable[['Bot', List[bool]], bool]


class Result(Enum):
    VALID = 0
    TIMEOUT = 1
    EXCEPTION = 2


@dataclass
class ResultDetails:
    result: Result
    exception: Union[Exception, None]


def tit_for_tat(self, opponent: Bot, history: List[bool]) -> bool:
    if len(history) == 0:
        return False
    return history[-1]


class Validator:
    def __init__(self, n_matchups: int, n_rounds: int, testcases: List[Bot] = [tit_for_tat]):
        self.testcases = testcases
        self.n_matchups = n_matchups
        self.n_rounds = n_rounds

    def validate(self, bot: Bot) -> ResultDetails:
        for testcase in self.testcases:
            for _ in range(self.n_matchups):
                history = []
                for _ in range(self.n_rounds):
                    start = time()

                    try:
                        history.append(bot(testcase, history))
                    except Exception as e:
                        return ResultDetails(Result.EXCEPTION, e)

                    end = time()

                    if end - start > 1:
                        return ResultDetails(Result.TIMEOUT, None)

        return ResultDetails(Result.VALID, None)
