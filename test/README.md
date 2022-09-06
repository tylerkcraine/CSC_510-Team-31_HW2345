# My Tiny Testing Framework

## Introduction:

I made this in response to the fact that we couldn’t use pytest for our unit testing. Keep in mind this testing framework is a bit more limited than pytest.

## General Setup:

You can import things from the code_folder ( renamed because of some clashing namespaces ) as you normally would. Ignore the auto completion complaining its taken care of in the test_runner file. 

### General Test Anatomy:

test_example.py (always name “test_something” or the function won’t pick it up)

```python
# all your imports (ignore errors)
import test_type

class TestExample(test_type.TestType): # make sure it's TestSomething formatting is important
	def test_exampleone:
		# passing test
		assert True # make sure to use assert statement because it works off the AssertionError
	def test_exampletwo
		#falling test
		assert False
```

## Running Testing:

To run tests just run the test_runner.py file in the test folder