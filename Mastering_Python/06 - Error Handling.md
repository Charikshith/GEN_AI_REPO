

# 6.1 User Input



## Handling Errors in Python: Managing User Input

Handling errors is a crucial part of programming, and one of the most common places you'll encounter errors is through user input. Users can enter unexpected data, such as emojis, letters, or invalid characters, which can cause your program to crash. In this post, we'll explore how to handle such errors gracefully and make your program more robust.

### Understanding User Input in Python

In Python, you can take user input using the built-in `input()` function. This function always returns a string, regardless of what the user enters. For example:

```python
user_input = input("Please enter something: ")
print(user_input)
print(type(user_input))
```

If the user enters `100`, the type will still be `str`, not `int`. This is important because if you try to perform operations that expect a different data type (like addition), it will throw an error.

### The Problem with User Input

Let's consider a simple calculator example where we ask the user to input two numbers:

```python
a = input("Enter number A: ")
b = input("Enter number B: ")
print(f"The sum of {a} and {b} is {a + b}")
```

If the user enters `10` and `15`, the program will try to add the strings `"10"` and `"15"`, resulting in `"1015"`, which is not the desired result. If the user enters non-numeric values like `hello` or an emoji, the program will throw an error.

### Handling Errors Gracefully

To prevent your program from crashing and to provide a better user experience, you need to handle errors. This is where exception handling comes into play. We'll cover this in detail in the next lesson, but the key idea is to anticipate potential errors and handle them gracefully.

### Tips and Tricks

1. **Use Try-Except Blocks**: Always use try-except blocks when dealing with user input to catch and handle exceptions.
   
2. **Validate Inputs**: Before processing user input, validate it to ensure it meets your expectations (e.g., checking if it's a number).

3. **Keep It Clean**: Use functions to handle repetitive tasks, like getting and validating user input.

4. **Use Specific Exceptions**: Instead of catching the general `Exception`, use specific exceptions like `ValueError` or `TypeError` to handle different error cases.

5. **Inform the User**: Always provide clear feedback to the user when an error occurs, so they know what went wrong and how to fix it.

6. **Test Thoroughly**: Test your program with different types of inputs to ensure it handles all edge cases.

By following these best practices, you can write more robust programs that handle errors gracefully and provide a better user experience.

---

### Additional Information

- **Loop Until Valid Input**: Use loops to continuously prompt the user for input until they provide valid data.
- **Handle Multiple Exceptions**: Use multiple `except` blocks to handle different types of errors differently.
- **Log Errors**: Consider logging errors for debugging purposes, even if you're handling them gracefully.

Stay tuned for the next lesson, where we'll dive deeper into exception handling and explore how to implement these strategies in your code!

---


# 6.2 Try...Except



## Handling Errors and Exceptions in Python: A Comprehensive Guide

### Introduction

When working with user inputs or performing operations that can potentially fail, it's essential to handle errors gracefully. In Python, this is achieved using `try` and `except` blocks. In this guide, we'll explore how to handle errors effectively, starting from basic error handling to more advanced techniques.

---

### Handling User Input Errors

One of the most common scenarios where errors occur is when dealing with user inputs. When a user enters a value, it is always returned as a string. Attempting to convert this string to a numeric type (like `int` or `float`) can raise exceptions if the input is not valid.

#### Basic Error Handling with `try` and `except`

Here’s a simple example of handling user input errors:

```python
try:
    number = float(input("Enter a number: "))
    print(f"You entered: {number}")
except:
    print("Something went wrong!")
```

This code tries to convert the user's input to a `float`. If it fails, it catches the exception and prints a generic error message. However, this approach is not ideal because it doesn’t provide specific information about the error.

---

### Catching Specific Exceptions

To improve error handling, it's better to catch specific exceptions rather than using a generic `except` block. Python raises different exceptions for different errors, and we can handle them individually.

#### Example: Handling `ValueError`

When converting a string to a number, Python raises a `ValueError` if the conversion fails. Let's modify the code to catch this specific exception:

```python
try:
    number = float(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Please enter a valid number!")
```

Now, the code provides a more meaningful error message when the input cannot be converted to a number.

#### Example: Handling `ZeroDivisionError`

Another common exception is `ZeroDivisionError`, which occurs when attempting to divide by zero. Here’s how to handle it:

```python
try:
    number = float(input("Enter a number: "))
    result = number / 0  # This will raise ZeroDivisionError
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Please do not divide by zero!")
```

This code handles both `ValueError` and `ZeroDivisionError` separately, providing specific error messages for each case.

---

### Combining Multiple Exception Handlers

You can combine multiple `except` blocks to handle different types of exceptions. Additionally, you can use the generic `except` block to catch any unexpected errors:

```python
try:
    number = float(input("Enter a number: "))
    result = number / 0
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Please do not divide by zero!")
except:
    print("Something unexpected went wrong!")
```

This approach ensures that your program handles both expected and unexpected errors gracefully.

---

### Using Recursion for Retry Logic

If you want to give users another chance to enter valid input, you can use recursion. Here’s how to modify the code to retry:

```python
def do_math():
    try:
        number = float(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError:
        print("Please enter a valid number!")
        do_math()  # Recursive call to retry

do_math()
```

This code will keep asking the user for input until a valid number is entered.

---

### Tips and Tricks

1. **Be Specific with Exceptions**: Always try to catch specific exceptions (`ValueError`, `ZeroDivisionError`, etc.) instead of using a generic `except` block. This makes your code more robust and easier to debug.

2. **Provide Meaningful Error Messages**: Instead of printing generic messages like "Something went wrong!", provide context-specific messages like "Please enter a valid number!".

3. **Log Exceptions for Debugging**: Use the `as` keyword to access the exception object and log it for debugging purposes:

   ```python
   try:
       number = float(input("Enter a number: "))
   except ValueError as e:
       print(f"Error: {e}")
   ```

4. **Combine Error Handling with Recursion**: Use recursion to allow users to retry their input, improving the user experience.

5. **Keep Error Handling Local**: Avoid using a single `try-except` block to handle all errors in your program. Instead, handle errors locally where they are most likely to occur.

6. **Test Your Error Handling**: Always test your code with different types of inputs to ensure your error handling works as expected.

---

By following these best practices, you can write more robust and user-friendly Python programs. Remember, error handling is not just about preventing crashes—it’s about providing a better experience for your users.

---


# 6.3 Else...Finally



## Using Else and Finally Blocks with Try-Except in Python

In this blog post, we’ll explore how to use the `else` and `finally` blocks with `try-except` statements in Python. Building on the concepts of `else` blocks with `for` and `while` loops, we’ll see how these blocks can add functionality to error handling in your code.

---

### Using the Else Block with Try-Except

The `else` block in Python is not just limited to `for` and `while` loops. You can also use it with `try-except` blocks to execute code when no exceptions occur.

#### Example Code:

```python
try:
    number = float(input("Enter a number: "))
    print(number)
except ValueError as e:
    print(f"Exception: {e}")
else:
    print("Successfully executed code.")
```

- The `else` block will only execute if the code in the `try` block runs without raising an exception.
- If the user enters a valid number (e.g., `10`), the `try` block will succeed, and the `else` block will print "Successfully executed code."
- If the user enters an invalid input (e.g., `o`), the `except` block will catch the exception, and the `else` block will not execute.

---

### Using the Finally Block with Try-Except

The `finally` block is used to execute code regardless of whether an exception occurred or not. It is typically used for cleanup actions, such as closing files or releasing resources.

#### Example Code:

```python
try:
    number = float(input("Enter a number: "))
    print(number)
except ValueError as e:
    print(f"Exception: {e}")
finally:
    print("This will always run.")
```

- The `finally` block will execute regardless of whether the `try` block succeeds or raises an exception.
- If the user enters a valid number (e.g., `9`), the `try` block will succeed, the `else` block will execute, and then the `finally` block will run.
- If the user enters an invalid input (e.g., `ABC`), the `except` block will catch the exception, and the `finally` block will still execute.

---

### Handling Multiple Points of Failure

Errors can occur in any part of your program, including the `finally` block. For example:

```python
try:
    number = float(input("Enter a number: "))
    print(number)
    result = 1 / 0  # This will raise a ZeroDivisionError
except ValueError as e:
    print(f"Exception: {e}")
finally:
    print("This will always run.")
```

- In this example, the `try` block will first convert the input to a float. If successful, it will attempt to divide by zero, which raises a `ZeroDivisionError`.
- Since the `except` block only catches `ValueError`, the `ZeroDivisionError` will not be caught, and the program will crash after the `finally` block executes.

To handle multiple points of failure, you can nest `try-except` blocks:

```python
try:
    number = float(input("Enter a number: "))
    print(number)
    try:
        result = 1 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
except ValueError as e:
    print(f"Exception: {e}")
finally:
    print("This will always run.")
```

- This way, you can handle specific exceptions in different parts of your code.

---

### Key Differences Between Else and Finally

- **Else Block**: Executes only if the `try` block runs without raising an exception.
- **Finally Block**: Executes regardless of whether an exception was raised or caught.

---

### Tips and Tricks

1. **Use `finally` for Cleanup**: The `finally` block is ideal for releasing resources, closing files, or resetting variables.
2. **Avoid Resource Leaks**: Always use `finally` to ensure that resources like file handles or network connections are properly closed.
3. **Keep it Simple**: Avoid complex logic in the `else` block. Use it for simple success notifications or logging.
4. **Nesting Try-Except Blocks**: While nesting is possible, it’s often unnecessary. Structure your code to minimize nested `try-except` blocks for better readability.

By incorporating `else` and `finally` blocks into your `try-except` statements, you can write more robust and reliable Python code.

---


# 6.4 Raise


## Manually Raising Errors in Python

Error handling is a crucial part of writing robust and reliable code in Python. While Python automatically raises errors for certain conditions, there are times when you might want to manually raise an error. This can be useful for controlling the flow of your program based on specific conditions or for creating custom error messages.

### Raising Custom Errors

In Python, you can manually raise an error using the `raise` keyword. This allows you to create custom error messages tailored to your specific needs. Here’s an example of how you can do this:

```python
user_input = input("Enter a value: ")
if user_input == "zero":
    raise Exception("Please never use zero!")
```

In this example, if the user enters "zero," the program will raise an exception with the message "Please never use zero!".

### A Practical Example: Checking Internet Connection

A more practical example might involve checking whether an internet connection is available. You can use a boolean variable to represent the connection status and raise an error if the connection is not available.

```python
is_connected = False  # Replace this with your actual connection check logic

if not is_connected:
    raise Exception("No internet connection available.")
else:
    print("Connected to the internet.")
```

This code will raise an exception with the message "No internet connection available" if the internet connection is not available.

### Combining with Try-Except Blocks

To make your code more robust, you can combine manual error raising with try-except blocks. This allows you to handle exceptions gracefully and provide meaningful feedback to the user.

```python
def connect_to_internet():
    is_connected = False  # Replace this with your actual connection check logic
    if not is_connected:
        raise Exception("No internet connection available.")
    else:
        print("Connected to the internet.")

try:
    connect_to_internet()
except Exception as e:
    print(f"An error occurred: {e}")
```

In this example, if the `connect_to_internet()` function raises an exception, the except block will catch it and print a user-friendly message.

### Best Practices for Raising Custom Errors

While manually raising errors can be very useful, it’s important to use this feature judiciously. Here are some best practices to keep in mind:

1. **Be Specific with Exceptions**: Instead of raising a generic `Exception`, consider using more specific exception types like `ConnectionError` or `ValueError`. This makes it easier to handle different types of errors in your code.

    ```python
    if not is_connected:
        raise ConnectionError("No internet connection available.")
    ```

2. **Avoid Overuse**: Raising too many custom exceptions can make your code harder to maintain and debug. Use this feature only when it adds clear value to your program.

3. **Provide Meaningful Error Messages**: Always include a clear and descriptive message with your exceptions. This will help anyone reading your code (including yourself) understand why the error was raised.

### Tips and Tricks

- **Use Built-in Exceptions**: Python has a wide range of built-in exceptions that you can use for common scenarios. For example, `ValueError` for invalid values, `TypeError` for incorrect types, and `FileNotFoundError` for missing files.

- **Custom Exception Classes**: If you find yourself raising the same type of error repeatedly, consider creating a custom exception class. This can make your code more organized and easier to maintain.

    ```python
    class CustomConnectionError(ConnectionError):
        pass

    if not is_connected:
        raise CustomConnectionError("No internet connection available.")
    ```

- **Debugging**: When debugging, it’s often helpful to include additional information in your error messages, such as variable values or the state of the program at the time the error was raised.

By following these guidelines and using manual error raising judiciously, you can write more robust and user-friendly code. Remember, error handling is not just about preventing crashes—it’s also about making your program more informative and easier to use.


---


# 6.5 Fixing Unknown Errors


## Mastering Error Handling in Python: A Beginner's Guide

As you start your journey with Python, understanding how to handle errors and exceptions is a crucial skill. Errors can seem daunting at first, but with practice and the right approach, you can debug your code like a pro. In this post, we'll explore how to interpret error messages, use online resources effectively, and improve your coding skills through research.

### Understanding Error Messages

Python error messages are designed to be helpful. Let's take a look at a common example:

```python
print("Hello)
```

When you run this code, you'll get a `SyntaxError: unterminated string literal`. The error message tells you exactly what's wrong—the string is missing a closing quote. The red underline in your editor is another clue. Hovering over it might even tell you, "Missing the closing quote."

These hints are there to help you fix the issue quickly. The key is to read the error message carefully and act on the clues provided.

### Debugging Runtime Errors

Not all errors are syntax-related. Runtime errors occur when your code runs but encounters an issue during execution. Let's consider an example:

```python
def say_hello(people: list[str]):
    for person in people:
        print(person)

say_hello(100)
```

Running this code will result in a `TypeError: 'int' object is not iterable`. Let's break down the error message:

1. **Traceback**: The error trace shows where the error occurred. In this case, it happened in the `say_hello` function at line 2.
2. **Error Message**: The bottom line of the traceback gives the specific error: `int object is not iterable`. This tells you that you tried to loop over a non-iterable object (in this case, an integer).

### Researching Errors

When you're stuck, Google is your best friend. Copy the error message and search for it along with the keyword "Python." For example:

```
TypeError: int object is not iterable Python
```

#### Using Stack Overflow

Stack Overflow is a goldmine for developers. When you search for the error, you'll likely find multiple answers. Here's how to make the most of it:

1. **Read the Question**: Ensure the problem described matches your issue.
2. **Check the Answers**: The highest-rated answer is often the best, but don't ignore other responses—sometimes simpler explanations can be found lower down.
3. **Learn from Solutions**: Use the solutions to fix your code, but also take the time to understand why the error occurred.

#### Exploring Other Resources

If Stack Overflow doesn't have the answer, don't worry. Websites like [freeCodeCamp](https://www.freecodecamp.org/) and official Python documentation can provide additional insights.

### Fixing the Error

Let's fix our earlier example:

```python
def say_hello(people: list[str]):
    for person in people:
        print(person)

# Fix the argument to be an iterable
say_hello(["Mario", "Luigi"])
```

### Common Errors and Solutions

1. **NameError**

   ```python
   print(a_hello)
   ```

   - **Error Message**: `NameError: name 'a_hello' is not defined`
   - **Solution**: Check if the variable or function is defined. In this case, the correct function is `say_hello`.

2. **TypeError**

   ```python
   say_hello(100)
   ```

   - **Error Message**: `TypeError: 'int' object is not iterable`
   - **Solution**: Ensure the argument is iterable. For numbers, consider using `range()`.

### Tips and Tricks

1. **Read Error Messages Carefully**: Python error messages are descriptive. Take your time to understand what they're telling you.
2. **Use Type Hints**: Type hints can help catch errors early and make your code more readable.
3. **Leverage Online Resources**: Don't be afraid to search for your error online. Someone else has likely encountered the same issue.
4. **Practice, Practice, Practice**: The more you code, the more familiar you'll become with common errors and their solutions.
5. **Experiment and Learn**: Don't be afraid to try new things and make mistakes. Debugging is a natural part of the learning process.

### Final Thoughts

Every error is an opportunity to learn and improve. With practice, you'll become faster at identifying and fixing issues. Remember, the Python community is vast, and resources are just a search away. Keep coding, and soon you'll be handling errors like a pro!



---
