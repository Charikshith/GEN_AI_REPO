

## 001 Intro



## Unit Testing in Python: A Comprehensive Guide

Unit testing is a crucial part of software development that helps ensure your code is reliable, stable, and functions as expected. In this guide, we'll explore the basics of unit testing in Python, the models to follow, and how to implement tests using the pytest framework.

### Introduction to Unit Testing

Unit testing involves testing individual components (units) of your code to verify they work correctly. It's a practice that helps catch bugs early, making your code more robust and reducing the likelihood of errors in production.

### The Arrange-Act-Assert Model

The Arrange-Act-Assert (AAA) model is a common testing pattern:

1. **Arrange**: Set up the necessary conditions and inputs for the test.
2. **Act**: Execute the function or method being tested.
3. **Assert**: Verify that the results match your expectations.

This model provides a clear structure for writing tests.

### Introduction to pytest

Python's `unittest` module is built-in, but `pytest` offers a more user-friendly experience. Install it using pip:

```bash
pip install pytest
```

### Setting Up pytest

1. **Installation**: Install pytest if not already installed.
2. **Test Naming**: Name test files starting with `test_` and functions with `test_`.
3. **Running Tests**: Use the pytest command in your terminal to execute tests.

### Importance of Unit Testing

- **Catches Bugs Early**: Identifies issues before they reach production.
- **Ensures Robustness**: Tests handle unexpected inputs and edge cases.
- **Facilitates Refactoring**: Gives confidence that changes won't break existing code.
- **Improves Code Quality**: Encourages better design and modular code.

### Writing Unit Tests

Let's create tests for a simple addition function.

#### Example Function: `add_numbers`

```python
def add_numbers(a: float, b: float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return 0
    return a + b
```

#### Test Cases

1. **Test Valid Addition**

```python
def test_add_two_positive_numbers():
    a = 5
    b = 3
    expected = 8
    actual = add_numbers(a, b)
    assert actual == expected
```

2. **Test with Zero**

```python
def test_add_zero():
    a = 0
    b = 5
    expected = 5
    actual = add_numbers(a, b)
    assert actual == expected
```

3. **Test Invalid Input**

```python
def test_add_invalid_input():
    a = "five"
    b = 3
    expected = 0
    actual = add_numbers(a, b)
    assert actual == expected
```

### Tips and Tricks

1. **Descriptive Names**: Use clear test names like `test_add_positive_numbers`.
2. **Test Edge Cases**: Include tests for extreme values and invalid inputs.
3. **Use Test Groups**: Organize related tests into groups for better management.
4. **Type Hints**: Utilize type hints for clarity and better code maintenance.
5. **Test-Driven Development (TDD)**: Write tests before coding to ensure functionality.

By following these guidelines and practicing regularly, you'll enhance your code's reliability and your testing skills.

---


## 002 Fixtures



## Fixtures in PyTest: A Comprehensive Guide

Fixtures are a powerful feature in PyTest that help simplify your test code by providing a fixed baseline so that tests run reliably and consistently. Fixtures can be used to setup and teardown resources needed for tests, such as data, connections, or any other dependencies. In this guide, we'll explore how to use fixtures in PyTest to make your unit testing more efficient and maintainable.

### Project Structure

Before diving into fixtures, let's quickly look at the project structure. We'll create a `tests` folder where we'll store our test files. Inside this folder, we'll have a file called `test_sample_module.py` where we'll write our tests for the `sample_module.py` functions.

### Sample Module

Let's start by creating a simple `sample_module.py` with two functions we want to test:

```python
def sort_numbers(numbers: list[int]) -> list[int]:
    return sorted(numbers)

def reverse_numbers(numbers: list[int]) -> list[int]:
    return list(reversed(numbers))
```

### Writing Tests Without Fixtures

Before we introduce fixtures, let's see how we would write tests without them. In `test_sample_module.py`, we'll import PyTest and the functions we want to test:

```python
import pytest
from sample_module import sort_numbers, reverse_numbers
```

Now, let's write a test for the `sort_numbers` function:

```python
def test_sort_numbers():
    numbers = [9, 5, -1, -10, 10]
    expected = [-10, -1, 5, 9, 10]
    actual = sort_numbers(numbers)
    assert actual == expected
```

Similarly, we can write a test for the `reverse_numbers` function:

```python
def test_reverse_numbers():
    numbers = [9, 5, -1, -10, 10]
    expected = [10, -10, -1, 5, 9]
    actual = reverse_numbers(numbers)
    assert actual == expected
```

### The Problem with Redundant Data

You might have noticed that both tests use the same list of numbers. If we have multiple tests that require the same data, repeating this setup in each test becomes redundant and can lead to maintenance issues. This is where fixtures come into play.

### Introducing Fixtures

A fixture is a function that provides a fixed baseline so that tests execute reliably and consistently. Fixtures can be reused across multiple tests. Let's create a fixture for our sample numbers:

```python
@pytest.fixture
def sample_numbers_unsorted() -> list[int]:
    return [9, 5, -1, -10, 10]
```

### Using Fixtures in Tests

Now, let's modify our tests to use the fixture:

```python
def test_sort_numbers(sample_numbers_unsorted: list[int], expected_sorted: list[int]) -> None:
    actual = sort_numbers(sample_numbers_unsorted)
    assert actual == expected_sorted

def test_reverse_numbers(sample_numbers_unsorted: list[int], expected_reversed: list[int]) -> None:
    actual = reverse_numbers(sample_numbers_unsorted)
    assert actual == expected_reversed
```

### Tips and Tricks

1. **Parameterization**: Fixtures can be parameterized to provide different sets of data for tests. This is useful when you need to test multiple scenarios.

2. **Teardown**: Fixtures can also handle cleanup actions after tests are executed. This is particularly useful for resources like database connections or file handles.

3. **Scope**: Fixtures can be scoped to run once for all tests in a module, session, or package. This is useful for expensive setup operations.

4. **Reusing Fixtures**: Fixtures can be reused across multiple test files by placing them in a `conftest.py` file.

5. **Complex Setup**: For complex setup operations, fixtures can encapsulate the setup and teardown logic, making your tests cleaner and more readable.

6. **Debugging**: If you need to debug your fixtures, you can add print statements or use a debugger to see what's happening during setup and teardown.

### Conclusion

Fixtures are a powerful tool in PyTest that can help simplify your test code by reducing redundancy and improving consistency. By using fixtures, you can make your tests more maintainable and easier to understand. Whether you're dealing with simple data or complex resources, fixtures provide a flexible way to manage your test setup and teardown.

By following the tips and tricks outlined in this guide, you can get the most out of fixtures in your PyTest-driven projects. Happy testing!

---


## 003 conftest.py



## Leveraging `conftest.py` in Pytest for Efficient Testing

Pytest is a powerful testing framework that offers numerous features to streamline your testing workflow. One such feature is the `conftest.py` file, which allows you to share common functionality across multiple test files. In this blog post, we'll explore how to utilize `conftest.py` to create fixtures and mock external calls, making your tests more efficient and maintainable.

### Introduction to `conftest.py`

The `conftest.py` file is a special file in Pytest that enables sharing of fixtures, test data, and other helper functions across multiple test files. When Pytest runs, it automatically searches for this file in your project directory and uses the fixtures defined within it. This eliminates the need to duplicate code across multiple test files.

### Creating Fixtures in `conftest.py`

Fixtures are functions that provide a fixed baseline so that tests execute reliably and consistently. They can setup resources needed for tests and teardown them after. Let's create a simple fixture that provides unsorted numbers:

```python
# conftest.py
import pytest

@pytest.fixture
def sample_numbers_unsorted() -> list[int]:
    return [-1, 3, 2, 1, 0]
```

This fixture can be used in any test file to get a list of unsorted integers.

### Monkey Patching with Fixtures

One common use case for fixtures is mocking external calls, such as API requests. Mocking prevents your tests from making real network calls, which can be slow and expensive. Let's create a fixture that mocks an API call:

```python
# conftest.py
@pytest.fixture(autouse=True)
def disable_api_data(monkeypatch):
    def mock_get_api_data() -> str:
        return "modified_data"
    
    monkeypatch.setattr("sample_module.get_api_data", mock_get_api_data)
```

The `autouse=True` parameter ensures this fixture is applied to all tests automatically. It uses `monkeypatch` to replace the `get_api_data` function with a mock that returns predefined data.

### Testing with Shared Fixtures

Now, let's use these fixtures in our test files. Here's an example of testing the `reverse_text` function:

```python
# test_sample_module.py
def test_reverse_text(sample_text: str) -> None:
    actual = sample_module.reverse_text(sample_text)
    expected = "ananab"
    assert actual == expected
```

And here's how to test the mocked API call:

```python
# test_sample_module.py
def test_api_returns_data() -> None:
    actual = sample_module.get_api_data()
    expected = "modified_data"
    assert actual == expected
```

### Tips and Tricks

- **Organize Your Fixtures**: Use `conftest.py` to keep your fixtures organized and reusable across multiple test files.
- **Use `autouse` Wisely**: The `autouse` parameter can be useful for applying fixtures to all tests, but use it sparingly to avoid unintended side effects.
- **Scope Your Fixtures**: Fixtures can have different scopes (e.g., `function`, `class`, `module`, `package`). Choose the appropriate scope based on your needs.
- **Keep Tests Independent**: Ensure that each test remains independent and doesn’t rely on side effects from other tests.
- **Mock External Calls**: Always mock external calls like APIs or database queries to keep your tests fast and reliable.

By leveraging `conftest.py` and fixtures, you can write more efficient and maintainable tests. This approach not only reduces code duplication but also makes your test suite faster and more reliable.

---


## 004 Marks



## Mastering PyTest: Using Marks to Organize Your Tests

PyTest is a powerful testing framework for Python that offers a wide range of tools to make your testing experience more efficient and organized. One such tool is the *mark* decorator, which allows you to categorize and control the execution of your tests. In this blog post, we'll explore how to use the `@pytest.mark` decorator to skip, fail, or conditionally run specific tests.

### Introduction to PyTest Marks

Marks are a way to label your tests, enabling PyTest to treat them differently during execution. They are particularly useful for organizing tests into groups or specifying particular behaviors for certain tests. In this lesson, we'll focus on three specific marks: `xfail`, `skip`, and `skipif`.

### 1. Using `@pytest.mark.xfail` for Expected Failures

The `@pytest.mark.xfail` mark is used to indicate that a test is expected to fail. This is particularly useful for tests that are known to be broken but should not block the rest of the test suite from running.

#### Example Code:

```python
import pytest

@pytest.mark.xfail
def test_will_always_fail():
    assert False

def test_always_succeeds():
    assert True
```

#### Explanation:

- The `test_will_always_fail` function is marked with `@pytest.mark.xfail`, indicating that this test is expected to fail.
- When you run your tests, PyTest will report this test as "xfail" instead of "fail," meaning it was expected to fail and is not treated as an error.
- The `test_always_succeeds` function is a normal test that will pass as expected.

### 2. Using `@pytest.mark.skip` for Unconditional Skips

The `@pytest.mark.skip` mark is used to skip a test unconditionally. This means that the test will not be executed at all, regardless of any conditions.

#### Example Code:

```python
import pytest

def test_sort_numbers(sample_numbers):
    actual = sample_module.sort_numbers(sample_numbers)
    expected = sorted(sample_numbers)
    assert actual == expected

@pytest.mark.skip
def test_reverse_numbers(sample_numbers):
    actual = sample_module.reverse_numbers(sample_numbers)
    expected = sorted(sample_numbers, reverse=True)
    assert actual == expected
```

#### Explanation:

- The `test_reverse_numbers` function is marked with `@pytest.mark.skip`, so it will be skipped during test execution.
- When you run your tests, PyTest will ignore this test entirely, and it will not appear in the test results as either a pass or fail.

### 3. Using `@pytest.mark.skipif` for Conditional Skips

The `@pytest.mark.skipif` mark is similar to `@pytest.mark.skip`, but it allows you to specify a condition under which the test should be skipped. This is useful when you want to skip a test only under certain circumstances.

#### Example Code:

```python
import pytest

def test_sort_numbers(sample_numbers):
    actual = sample_module.sort_numbers(sample_numbers)
    expected = sorted(sample_numbers)
    assert actual == expected

@pytest.mark.skipif(True, reason="Expression evaluated to True")
def test_reverse_numbers(sample_numbers):
    actual = sample_module.reverse_numbers(sample_numbers)
    expected = sorted(sample_numbers, reverse=True)
    assert actual == expected
```

#### Explanation:

- The `test_reverse_numbers` function is marked with `@pytest.mark.skipif`, with the condition `True` and a reason for skipping.
- When you run your tests, PyTest will skip this test and provide the reason for skipping it.
- You can replace `True` with any boolean expression to conditionally skip the test.

### Running the Tests

When you run your tests, PyTest will handle the marked tests according to their annotations:

1. The `test_will_always_fail` test will be marked as "xfail" because it is expected to fail.
2. The `test_reverse_numbers` test will be skipped unconditionally.
3. The `test_always_succeeds` and `test_sort_numbers` tests will run normally.

### Tips and Tricks

- **Use `@pytest.mark.xfail` for Known Issues**: If you have a test that is known to fail due to a bug or incomplete implementation, mark it with `@pytest.mark.xfail` to prevent it from blocking your test suite.
- **Skip Tests with Care**: Use `@pytest.mark.skip` and `@pytest.mark.skipif` judiciously. Skipping too many tests can lead to a false sense of security, as important tests may be ignored.
- **Provide Clear Reasons for Skipping**: When using `@pytest.mark.skipif`, always provide a clear reason for skipping the test. This helps other developers understand why the test was skipped.
- **Use Environmental Conditions**: The `@pytest.mark.skipif` mark can be used with environmental conditions, such as checking the operating system or the presence of certain dependencies.
- **Experiment with Marks**: PyTest allows you to create custom marks. Experiment with creating your own marks to categorize your tests further.

By using these marks effectively, you can make your test suite more organized, efficient, and easier to maintain. In the next lesson, we'll explore even more advanced features of PyTest to further enhance your testing workflow.

---


## 005 Parametrize



## Using PyTest's Parameterize Mark to Streamline Your Tests

PyTest is a powerful testing framework for Python that offers a wide range of features to make your testing process more efficient and effective. In this post, we'll explore one of PyTest's most useful features: the `@pytest.mark.parametrize` decorator. This tool allows you to run the same test function with multiple sets of inputs, saving you time and reducing code duplication.

### The Problem: Test Code Duplication

Imagine you have a function that needs to be tested with multiple input scenarios. For example, consider a simple function that reverses text. Without parameterization, you might write multiple test functions, each with a different input:

```python
def test_reverse_text_simple():
    actual = sample_module.reverse_text("ABC")
    expected = "CBA"
    assert actual == expected

def test_reverse_text_empty():
    actual = sample_module.reverse_text("")
    expected = ""
    assert actual == expected
```

This approach leads to duplicated code, which can become hard to maintain as the number of test cases grows.

### The Solution: PyTest's Parameterize Mark

The `@pytest.mark.parametrize` decorator solves this problem by allowing you to run the same test function with multiple sets of inputs. Here's how you can use it:

```python
@pytest.mark.parametrize(
    "text_to_reverse,expected_result",
    [
        ("ABC", "CBA"),
        ("Apple", "elppA"),
        ("", ""),
    ],
)
def test_reverse_text_parameterized(text_to_reverse, expected_result):
    actual = sample_module.reverse_text(text_to_reverse)
    assert actual == expected_result
```

In this example:
- The `@pytest.mark.parametrize` decorator is applied to the test function.
- The first argument to `parametrize` is a string specifying the parameter names.
- The second argument is a list of tuples, where each tuple contains the input parameters for a test case.
- The test function receives these parameters and uses them to perform the test.

### How It Works

When you run the test, PyTest will automatically generate separate test cases for each tuple in the list. This means that:
- If you have three tuples in the list, PyTest will run three separate tests.
- Each test will use the corresponding input parameters.
- If any of the tests fail, PyTest will report which specific input caused the failure.

### Example with Different Data Types

The `parametrize` mark is not limited to string inputs. You can use it with any data type, including numbers and mixed types. Here's an example:

```python
@pytest.mark.parametrize(
    "sample_text",
    [
        "Apple",
        "Banana",
        100,
        "Orange",
    ],
)
def test_text_is_string(sample_text):
    assert isinstance(sample_text, str)
```

In this case:
- The test will run four times, once for each item in the list.
- The test will pass for the string inputs ("Apple", "Banana", "Orange") but fail for the integer input (100).

### Benefits of Using Parameterize

- **Reduces Code Duplication**: You don't need to write multiple test functions for similar test cases.
- **Improves Readability**: Your test code becomes cleaner and easier to understand.
- **Saves Time**: Writing and maintaining tests becomes more efficient.
- **Flexibility**: You can easily add or remove test cases by modifying the list of tuples.

### Tips and Tricks

- **Use Meaningful Parameter Names**: Choose parameter names that clearly describe what each value represents.
- **Keep Test Cases Simple**: Avoid complex logic within the test cases. Keep the focus on testing the functionality.
- **Use Type Hints**: Include type hints in your test functions to make the code more readable and maintainable.
- **Test Edge Cases**: Use parameterization to test edge cases, such as empty strings, zero values, or extreme inputs.
- **Combine with Other Marks**: You can combine `@pytest.mark.parametrize` with other PyTest marks (e.g., `@pytest.mark.skip`, `@pytest.mark.xfail`) for more complex testing scenarios.

By incorporating `@pytest.mark.parametrize` into your testing workflow, you can write more efficient and maintainable tests. This feature is especially useful when you need to test a function with multiple input scenarios, ensuring your code is robust and reliable.

---


## 006 Testing Errors



## Testing for Exceptions in Python Functions with PyTest

Testing is an essential part of software development, and ensuring that our functions behave as expected, especially when it comes to raising errors or exceptions, is crucial. In this blog post, we will explore how to test for exceptions in Python functions using PyTest. Specifically, we will focus on testing for `TypeError` exceptions and other generic exceptions.

### Why Test for Exceptions?

Before diving into the implementation, let's briefly discuss why testing for exceptions is important. Exceptions are a way for our functions to signal that something unexpected has happened. For example, a function might expect a certain type of input, and if it receives a different type, it should raise a `TypeError`. By testing these scenarios, we ensure that our functions behave correctly under various conditions.

### Testing for TypeErrors

Let's start with a simple example. Suppose we have a function that raises a `TypeError` under certain conditions. We want to write a test to ensure that this behavior is correct.

#### Example Function

Consider the following function:

```python
def function(var: str) -> str:
    if not isinstance(var, str):
        raise TypeError("Input must be a string.")
    return var
```

This function takes a variable `var` as input, checks if it's a string, and raises a `TypeError` if it's not. Otherwise, it returns the input string.

#### Writing the Test

To test this function, we want to ensure that it raises a `TypeError` when given a non-string input. We can use PyTest's `raises` context manager for this purpose.

```python
def test_function_raises_type_error():
    with pytest.raises(TypeError):
        function(9)
```

In this test, we use the `pytest.raises()` context manager to assert that calling `function(9)` (where `9` is an integer) raises a `TypeError`. If the function behaves as expected, the test will pass.

### Handling Multiple Error Types

In some cases, a function might raise different types of errors depending on the input. For example, it might raise a `TypeError` for invalid types and a generic `Exception` for other unexpected behavior.

#### Example Function with Multiple Errors

Let's modify our function to include multiple error conditions:

```python
def function(var: str) -> str:
    if not isinstance(var, str):
        raise TypeError("Input must be a string.")
    if var == "":
        raise Exception("Input string cannot be empty.")
    return var
```

This function now raises a `TypeError` if the input is not a string and a generic `Exception` if the input is an empty string.

#### Testing for Multiple Errors

We can write separate tests for each error condition:

```python
def test_function_raises_type_error():
    with pytest.raises(TypeError):
        function(9)

def test_function_raises_exception():
    with pytest.raises(Exception):
        function("")
```

In these tests, we use the `raises` context manager to check for both `TypeError` and generic `Exception`.

### Running the Tests

When you run these tests, PyTest will execute each test case and report whether it passed or failed. For example:

- If the function correctly raises a `TypeError` when passed a non-string input, the first test will pass.
- If the function raises a `TypeError` instead of an `Exception` when passed an empty string, the second test will fail, and you'll see an error message indicating that a `TypeError` was raised instead of the expected `Exception`.

### Tips and Tricks

1. **Be Specific with Error Types**: Always specify the exact type of error you expect. This makes your tests more precise and easier to debug.

2. **Test Each Error Condition Separately**: Write separate test cases for each type of error your function can raise. This helps in isolating issues and makes your test suite more maintainable.

3. **Include Error Messages**: If your function raises errors with specific messages, you can include these messages in your tests for even more precise validation.

4. **Use Descriptive Test Names**: Name your test functions descriptively so that it's clear what each test is checking for.

5. **Test for Expected Behavior**: In addition to testing for errors, also test the normal behavior of your function to ensure it works as expected under valid conditions.

### Conclusion

Testing for exceptions is a critical part of ensuring the reliability and robustness of your Python code. By using PyTest's `raises` context manager, you can easily write tests that verify whether your functions raise the expected errors under various conditions. Remember to be specific with error types, test each error condition separately, and include descriptive test names for clarity. Happy testing!

---
