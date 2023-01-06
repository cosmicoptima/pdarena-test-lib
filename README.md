Install this repository as a package and use it like so:

```python
from pdarena_test_lib import Validator

# takes two arguments: n_matchups and n_rounds
validator = Validator(10, 10)

def should_defect(opponent, history):
    # YOUR BOT'S CODE GOES HERE
    pass

validator.validate(should_defect)
```

This will print a message indicating whether your bot is valid. If your bot is valid, the message will contain its overall score against each testcase. If your bot is invalid, the message will contain the reason why.

You can also define your own testcases:

```python
from pdarena_test_lib import Validator

testcases = [
    # YOUR TESTCASES GO HERE
]

validator = Validator(10, 10, testcases)
```

# installation

## ...with pip

Run the following:

`pip install git+https://github.com/cosmicoptima/pdarena-test-lib`

## ...with poetry

Add the following to `pyproject.toml` under `tool.poetry.dependencies`:

```toml
pdarena-test-lib = { git = "https://github.com/cosmicoptima/pdarena-test-lib" }
```
