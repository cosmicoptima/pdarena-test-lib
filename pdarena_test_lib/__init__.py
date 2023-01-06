from dataclasses import dataclass
from enum import Enum
from rich.console import Console
from time import time
from traceback import format_tb
from typing import Callable, List, Union

console = Console()

# should_defect function
Bot = Callable[['Bot', List[bool]], bool]


class Result(Enum):
    VALID = 0
    TIMEOUT = 1
    EXCEPTION = 2


@dataclass
class ResultDetails:
    result: Result
    scores: Union[List[float], None]
    exception: Union[Exception, None]


def tit_for_tat(opponent: Bot, history: List[bool]) -> bool:
    if len(history) == 0:
        return False
    return history[-1]


cooperate = lambda opponent, history: False
defect = lambda opponent, history: True


class Validator:
    def __init__(self, n_matchups: int, n_rounds: int, testcases: List[Bot] = [tit_for_tat, cooperate, defect]):
        self.testcases = testcases
        self.n_matchups = n_matchups
        self.n_rounds = n_rounds

    def _validate(self, bot: Bot) -> ResultDetails:
        scores = []

        for testcase in self.testcases:
            scores_by_round = []

            for _ in range(self.n_matchups):
                history = []
                for _ in range(self.n_rounds):
                    start = time()

                    try:
                        defected = bot(testcase, history)
                    except Exception as e:
                        return ResultDetails(Result.EXCEPTION, None, e)

                    end = time()
                    if end - start > 1:
                        return ResultDetails(Result.TIMEOUT, None, None)

                    history.append(defected)

                    opponent_defected = testcase(bot, history)
                    table = {
                        (True, True): 5,
                        (True, False): 10,
                        (False, True): 0,
                        (False, False): 8,
                    }
                    scores_by_round.append(table[(defected, opponent_defected)])

            scores.append(sum(scores_by_round) / len(scores_by_round))

        return ResultDetails(Result.VALID, scores, None)

    def validate(self, bot: Bot) -> ResultDetails:
        result = self._validate(bot)

        if result.result == Result.VALID:
            console.print(f"[green]VALID[/green], scores: {', '.join(map(str, result.scores))}")
        elif result.result == Result.TIMEOUT:
            console.print(f"[red]INVALID due to timeout[/red]")
        elif result.result == Result.EXCEPTION:
            console.print(f"[red]INVALID due to exception:[/red]")
            console.print("".join(format_tb(result.exception.__traceback__)))

        return result
