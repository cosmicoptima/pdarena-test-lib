Install this repository as a package and use it like so:

```python
from pdarena_test_lib import Validator

# takes two arguments: n_matchups and n_rounds
validator = Validator(10, 10)

def should_defect(opponent, history):
    # YOUR CODE GOES HERE
    pass

validator.validate(should_defect)
```

You can also define your own testcases:

```python
from pdarena_test_lib import Validator

testcases = [
    # YOUR TESTCASES GO HERE
]

validator = Validator(10, 10, testcases)
```
