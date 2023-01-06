class Validator:
    def __init__(self, testcases, n_matchups=10, n_rounds=10):
        self.testcases = testcases
        self.n_matchups = n_matchups
        self.n_rounds = n_rounds

    def validate(self, bot):
        raise NotImplementedError
