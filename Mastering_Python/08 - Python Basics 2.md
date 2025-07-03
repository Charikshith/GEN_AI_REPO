

## 001 The With Keyword



## Reading Files in Python: Best Practices and Examples

As you progress in your Python journey, you'll inevitably need to work with files, whether it's reading text files, JSON files, or data streams. Python offers several ways to read files, and in this post, we'll explore both the outdated and modern methods, focusing on why the newer approach is superior.

### Understanding the Importance of File Handling

Reading files is a fundamental skill in programming. It allows you to access and manipulate data stored outside your program, making your applications more dynamic and versatile. Whether you're working with text files, configuration files, or data streams, understanding how to read files effectively is crucial.

### The Outdated Way: Using `open()` and `close()`

Let's start by looking at the traditional method of reading files in Python. This approach involves using the `open()` function to open a file and then manually closing it with the `close()` method.

#### Example: Reading a Text File

Suppose we have a file named `sample.txt` containing the text "Avocado is not a vegetable." Here's how you might read it using the outdated method:

```python
file = open("sample.txt")
text = file.read()
print(text)
file.close()
```

#### Why This Method Is Problematic

While this method works, it has significant drawbacks:

1. **Forgetting to Close the File**: One of the most common mistakes is forgetting to call `file.close()`. Leaving a file open can consume system resources and lead to potential errors in your program.

2. **Verbose Syntax**: The syntax is clunky and requires multiple lines of code just to read a simple file.

3. **Error-Prone**: If an error occurs while reading the file, the `close()` method might never be called, leading to resource leaks.

### The Modern Approach: Using the `with` Keyword

Fortunately, Python provides a more elegant and safer way to handle file operations using the `with` keyword. This approach is not only cleaner but also more robust.

#### Example: Reading a Text File with `with`

Here's how you can read the same `sample.txt` file using the modern method:

```python
with open("sample.txt") as file:
    text = file.read()
    print(text)
```

#### Why `with` is Superior

The `with` statement offers several advantages:

1. **Automatic File Closing**: The file is automatically closed after the block of code under the `with` statement is executed, even if an error occurs. This eliminates the risk of forgetting to close the file.

2. **Cleaner Syntax**: The syntax is more readable and concise, reducing the amount of boilerplate code.

3. **Better Resource Management**: The `with` statement ensures that resources, like file handles, are properly managed, making your code safer and more efficient.

### Tips and Tricks

- **Use the `with` Keyword**: Always prefer the `with` statement for file operations. It's the recommended best practice in Python.

- **Handle Exceptions**: When working with files, wrap your code in a `try-except` block to handle potential errors, such as file-not-found exceptions.

- **Specify Read Modes**: When opening files, specify the mode (e.g., `'r'` for reading, `'w'` for writing). This makes your code more explicit and avoids unexpected behavior.

- **Context Managers**: The `with` statement works with context managers. This concept isn't limited to files; it can be used with other resources like network connections.

### Conclusion

Reading files is a fundamental operation in programming, and Python makes it straightforward with the `with` keyword. By adopting the modern approach, you'll write cleaner, safer, and more efficient code. Always remember to use the `with` statement for file operations to ensure your programs are robust and resource-efficient.

### Additional Information

- **File Modes**: Common modes include:
  - `'r'`: Open for reading (default).
  - `'w'`: Open for writing, truncating the file first.
  - `'a'`: Open for writing, appending to the end of the file.
  - `'x'`: Open for exclusive creation, failing if the file exists.
  - `'b'`: Binary mode.
  - `'t'`: Text mode (default).
  - `'+'`: Open for updating (reading and writing).

- **Reading Line by Line**: Instead of reading the entire file at once with `file.read()`, you can read line by line using `file.readlines()` or a `for` loop.

- **Best Practices for File Paths**: Use absolute paths or construct file paths dynamically using the `os` module to ensure compatibility across different operating systems.

By following these guidelines and using the `with` statement, you'll be well on your way to handling files like a pro in Python!

---


## 002 Refactoring



## Refactoring in Python: Save Time and Reduce Errors

Refactoring is a powerful technique in programming that helps you save time and reduce errors by modifying your code in a more efficient way. Instead of manually changing variable names or function names across multiple files, refactoring allows you to make these changes in one place, which are then reflected throughout your entire project. This approach is especially useful when working on large and complex projects where manual changes can lead to mistakes and hours of debugging.

### What is Refactoring?

Refactoring is the process of renaming variables, functions, or other user-defined elements in your code. It ensures that any changes you make to a name are automatically applied wherever that name is used in your project. This eliminates the need to manually search for and update each occurrence, which can be time-consuming and error-prone.

### Refactoring Functions

Let's consider a simple example to understand how refactoring works. Suppose we have a function called `hello` that prints a greeting message:

```python
def hello():
    print("Hello!")

hello()  # Outputs: Hello!
hello()  # Outputs: Hello!
```

Now, if we want to change the name of this function to `greet`, we could manually update each occurrence. However, this approach is risky, especially in large projects where the function might be used in multiple files. Instead, we can use refactoring tools to make this change safely.

Here's how you can refactor the function name:

1. **Highlight the function name** you want to rename.
2. **Right-click** on the function name and navigate to the refactor option (or use the keyboard shortcut, which is often `Shift + F6` or similar depending on your IDE).
3. **Enter the new name** for the function (e.g., `greet`).
4. **Select the scope** where you want to apply the changes (e.g., the entire project).
5. **Apply the changes**.

After refactoring, your code will look like this:

```python
def greet():
    print("Hello!")

greet()  # Outputs: Hello!
greet()  # Outputs: Hello!
```

The function name has been updated everywhere it was used, without any manual intervention.

### Refactoring Modules and Imports

Refactoring isn't limited to functions. You can also refactor module names and their imports. Suppose you have a module called `sample` with a function `do_something`:

```python
# sample.py
def do_something():
    print("Doing something...")
```

In your main script, you might import and use this function like this:

```python
import sample

sample.do_something()  # Outputs: Doing something...
```

If you decide to rename the function `do_something` to something more descriptive, like `perform_task`, you can use refactoring to update all references to this function, including the import statements. Here's how it would look after refactoring:

```python
# sample.py
def perform_task():
    print("Performing task...")
```

```python
import sample

sample.perform_task()  # Outputs: Performing task...
```

### Refactoring Variables

Refactoring works just as well for variables. Suppose you have a variable named `data` that you want to rename to `user_data` for clarity. You can use the refactor tool to update all instances of `data` to `user_data` in your project.

### Tips and Tricks

1. **Avoid Manual Changes**: Never manually change function or variable names across multiple files. This is error-prone and can lead to broken code.
2. **Use Refactoring Tools**: Familiarize yourself with your IDE's refactoring tools. Most modern IDEs like PyCharm, VS Code, and others have built-in refactoring features.
3. **Test After Refactoring**: Always test your code after refactoring to ensure that the changes didn't introduce any bugs.
4. **Refactor Early and Often**: Don't wait until your code is too complex to refactor. Make small, incremental changes as you go.
5. **Consider Third-Party Code**: Be cautious when refactoring code that is part of third-party libraries or frameworks. These should typically be left as-is unless you are modifying the library itself.

By incorporating refactoring into your workflow, you'll write cleaner, more maintainable code and save yourself a lot of time and frustration in the long run.

---


## 003 Truthy & Falsy



## Understanding Truthy and Falsy Values in Python

### Introduction to Truthy and Falsy Values

In Python, every object or value can be evaluated as either `True` or `False` in a boolean context. This fundamental concept is crucial for controlling the flow of your programs, especially when working with conditional statements. Let’s dive into the world of truthy and falsy values and explore how they work.

### What Are Falsy Values?

Falsy values are those that evaluate to `False` when converted to a boolean. Let’s examine some common examples:

#### 1. Empty Collections
- **Empty String**: `""`
- **Empty List**: `[]`
- **Empty Tuple**: `()`
- **Empty Set**: `set()`
- **Empty Dictionary**: `{}`

All empty collections are considered falsy because they contain no elements.

#### 2. Numeric Types
- **Zero**: `0`, `0.0`, `0j`
- **None**: `None`

Any numeric type with a value of zero is falsy, and `None` is inherently falsy.

### What Are Truthy Values?

A value is considered truthy if it does not fall into any of the falsy categories. Here are some examples:

- Non-empty strings: `"hello"`
- Non-empty collections: `["item1", "item2"]`
- Non-zero numeric values: `5`, `-3`, `3.14`
- Boolean `True`

### Testing Truthy and Falsy Values

You can test the truthiness of a value using the `bool()` function or in an `if` statement.

```python
print(bool(""))        # False
print(bool("hello"))   # True
print(bool(0))        # False
print(bool(1))         # True
print(bool([]))        # False
print(bool([1,2,3]))  # True
```

### Practical Implications

Understanding truthy and falsy values is essential for writing clean and efficient code. Consider the following example:

```python
variable = ""
if variable:
    print("Variable is truthy")
else:
    print("Variable is falsy")
# Output: Variable is falsy
```

If `variable` is an empty string, the condition evaluates to `False`, and the else clause is executed.

### Tips and Tricks

1. **Test Values in Interactive Shell**: Use the Python interactive shell to quickly test the truthiness of different values.
2. **Use `bool()` for Explicit Checks**: When you need to explicitly check the boolean value of a variable, use the `bool()` function.
3. **Avoid Using `== False` for Checks**: Instead of using `if my_var == False`, use `if not my_var` to account for all falsy values.
4. **Be Mindful of Empty Collections**: Always consider whether an empty collection should be treated as falsy in your logic.

By mastering truthy and falsy values, you can write more robust and readable Python code. Remember, if it’s empty or zero, it’s falsy; otherwise, it’s truthy!

---


## 004 What Are Enums



## Working with Enums in Python

Enums, short for Enumerations, are a powerful feature in Python that allows developers to define a set of named constants. These constants are immutable and can be used to make your code more readable, maintainable, and less error-prone. In this blog post, we'll explore how to work with enums in Python, their benefits, and how to use them effectively.

### Why Use Enums?

Enums are particularly useful when you need to define a fixed set of distinct values. For example, consider a lamp that can be either "ON" or "OFF". Without enums, you might use strings or integers to represent these states, but this approach can lead to errors due to typos or invalid values.

Using enums ensures that only predefined values are used, reducing the chance of errors and improving code clarity.

### Creating Enums

To create an enum in Python, you need to import the `Enum` class from the `enum` module. Here's how you can define an enum for the lamp example:

```python
from enum import Enum

class State(Enum):
    ON = 0
    OFF = 1
```

In this example, `State` is an enum with two constants: `ON` and `OFF`, assigned the values `0` and `1`, respectively.

### Using Enums in Your Code

Once you've defined an enum, you can use its values in your code. Here's an example of how to check the current state of the lamp:

```python
state = State.ON

if state == State.ON:
    print("The lamp is turned on.")
elif state == State.OFF:
    print("The lamp is turned off.")
```

When you run this code, it will print "The lamp is turned on." because `state` is set to `State.ON`.

### Accessing Enum Values and Names

Enums provide two useful properties: `value` and `name`. The `value` property returns the underlying value of the enum member, while the `name` property returns the name of the member.

```python
print(state.value)  # Outputs: 0
print(state.name)   # Outputs: ON
```

### Another Example: Using Enums for Colors

Let's consider another example where we define an enum for colors:

```python
class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
```

You can use this enum in your code like this:

```python
color = Color.RED

if color == Color.RED:
    print("The color is red.")
elif color == Color.BLUE:
    print("The color is blue.")
elif color == Color.GREEN:
    print("The color is green.")
```

When you run this code, it will print "The color is red." because `color` is set to `Color.RED`.

### Using Enums in Functions

Enums can also be used as parameters in functions. Here's an example:

```python
def check_color(color: Color):
    print(f"The color is {color.name}.")

# Usage
check_color(Color.BLUE)  # Outputs: The color is blue.
```

In this example, the function `check_color` takes a `Color` enum as an argument and prints the name of the color.

### Benefits of Using Enums

1. **Improved Readability**: Enums make your code more readable by providing meaningful names for constants.
2. **Reduced Errors**: By limiting values to a predefined set, enums reduce the chance of errors due to invalid or misspelled values.
3. **Type Safety**: Enums can be used as type hints, ensuring that only valid values are passed to functions or methods.

### Tips and Tricks

- **Use Enums for Constants**: Enums are ideal for defining constants that have a specific set of allowed values.
- **Be Consistent with Names**: Use uppercase letters for enum names to follow Python conventions.
- **Use Type Hints**: Take advantage of type hints to ensure that only enum values are used where expected.
- **Add Methods to Enums**: Enums can have methods, allowing you to add functionality to your constants.
- **Use `enum.auto()`**: For simple enums where you don't need specific values, you can use `enum.auto()` to automatically assign values.

By following these guidelines and examples, you can effectively use enums in your Python code to make it more robust, readable, and maintainable.

---


## 005 Comparing Floats



```markdown
## The Trickiness of Comparing Floats in Python

When working with floating-point numbers in Python, you might encounter some unexpected behavior, especially when comparing them. In this post, we'll explore why comparing floats can be tricky and how to handle such comparisons effectively.

### The Problem: Comparing Floats Directly

Let's start with a simple example that might surprise you:

```python
a = 0.3
b = 0.1 + 0.2

print(a == b)  # Outputs: False
```

Both `a` and `b` appear to be `0.3`, but the comparison returns `False`. To understand why, let's print both values:

```python
print(a)  # Outputs: 0.3
print(b)  # Outputs: 0.30000000000000004
```

### Why Does This Happen?

The root cause lies in how computers store floating-point numbers. Computers use binary to represent numbers, and many decimal fractions cannot be represented exactly in binary. This leads to small rounding errors. For example:

- `0.1` in binary is a repeating fraction, similar to how `1/3` is `0.333...` in decimal.
- When you add `0.1 + 0.2`, the result isn't exactly `0.3` due to these rounding errors.

### How to Compare Floats Accurately

To accurately compare floats, we should consider a small tolerance level. This approach checks if the absolute difference between the two numbers is below a certain threshold. Here's a function that implements this:

```python
def compare_floats(a: float, b: float, tolerance: float = 1e-10) -> bool:
    difference = abs(a - b)
    print(f"a - b = {a - b}")
    return difference < tolerance
```

#### How It Works

1. **Absolute Difference**: The function calculates the absolute difference between `a` and `b`.
2. **Tolerance Check**: It then checks if this difference is smaller than the specified `tolerance` level.
3. **Return Result**: Returns `True` if the difference is within the tolerance, indicating the numbers are effectively equal.

#### Example Usage

Let's test this function with an example:

```python
# Example 1
a = 0.8
b = 0.1 + 0.7
tolerance = 1e-10

print(compare_floats(a, b, tolerance))  # Outputs: True

# Example 2
a = 0.70001
b = 0.7
tolerance = 1e-4

print(compare_floats(a, b, tolerance))  # Outputs: True

# Example 3
a = 0.7
b = 0.71
tolerance = 1e-4

print(compare_floats(a, b, tolerance))  # Outputs: False
```

### Tips and Tricks

- **Use Tolerance Wisely**: Choose your tolerance based on the precision you need. A smaller tolerance (e.g., `1e-10`) is more precise but may not account for very small differences due to rounding errors.
- **Avoid Direct Comparison**: Never directly compare floats using `==` unless you're certain they were not derived from calculations that introduce rounding errors.
- **Be Mindful of Precision**: Floating-point arithmetic can introduce tiny errors, so always consider using a tolerance when comparing the results of calculations.
- **Consider Using Decimal Module**: For financial or high-precision calculations, Python's `decimal` module can provide more precise control over decimal arithmetic.

### Conclusion

Comparing floats directly can lead to unexpected results due to the way computers handle binary representations of decimal numbers. By using a tolerance-based comparison, you can ensure more accurate and reliable results in your Python applications.

Remember, understanding how floating-point numbers work is crucial for avoiding bugs and ensuring the accuracy of your programs.
```

---


## 006 if __name__ ==  __main__



## The Power of `if __name__ == "__main__":` in Python

### Introduction to the `if __name__ == "__main__":` Check

Every Python programmer, whether seasoned or just starting out, should be familiar with a powerful feature that enhances code organization and testing: the `if __name__ == "__main__":` check. This simple yet essential construct is a cornerstone of Python programming and can save you from a world of confusion and unintended behavior in your code.

### What Does `if __name__ == "__main__":` Do?

The `if __name__ == "__main__":` check is a conditional statement that determines whether the code under it is being run directly (as the main program) or being imported as a module in another script. This distinction is crucial because it allows you to write code that behaves differently depending on how it's being executed.

### Why Do We Need This Check?

Imagine you have a module called `sample.py` with some functions and code that you want to test. Without the `if __name__ == "__main__":` check, any code in the module will execute as soon as you import it into another script. This can lead to unexpected behavior, especially if the module contains executable code that should only run when the module itself is executed directly.

For example, consider the following scenario:

```python
# sample.py
def do_something():
    print("Doing something!")

do_something()
```

When you import `sample.py` into another script, the `do_something()` function will execute immediately, even if you didn't explicitly call it. This can clutter your output and cause unintended side effects.

### How to Use the `if __name__ == "__main__":` Check

The solution is to wrap the executable code in your module with the `if __name__ == "__main__":` check. Here's how you can modify the previous example:

```python
# sample.py
def do_something():
    print("Doing something!")

if __name__ == "__main__":
    do_something()
```

Now, `do_something()` will only execute when `sample.py` is run directly (e.g., `python sample.py`). When `sample.py` is imported as a module in another script, the code under the `if __name__ == "__main__":` block will not execute.

### Understanding the Magic Behind `__name__`

The `__name__` variable is a built-in Python variable that holds the name of the module. When you run a script directly, Python sets `__name__` to `"__main__"`. However, when you import a module, `__name__` is set to the name of the module.

For example, if you have two files:

```python
# main.py
print(__name__)
import sample

# sample.py
print(__name__)
```

Running `main.py` will output:

```
__main__
sample
```

This demonstrates that `__name__` is `"__main__"` only in the script being run directly.

### Practical Example: Testing Modules

One of the most common use cases for the `if __name__ == "__main__":` check is testing modules. Suppose you have a module with several functions, and you want to test them. You can include test code under the `if __name__ == "__main__":` block:

```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Testing add function:")
    print(add(5, 3))  # Should output 8
    print("Testing subtract function:")
    print(subtract(10, 4))  # Should output 6
```

When you run `math_utils.py` directly, it will execute the test code. But when you import `math_utils` in another script, only the functions `add` and `subtract` will be available, and the test code will not run.

### Avoiding Common Mistakes

The `if __name__ == "__main__":` check also helps avoid a common pitfall: running the wrong script. When working on multiple files, it's easy to accidentally run a module that isn't the one you're currently editing. By including the `if __name__ == "__main__":` check, you ensure that the code under it only executes when the file is run directly, making it easier to test and debug.

### Tips and Tricks

- **Use it for Testing**: Always include test code under the `if __name__ == "__main__":` block when writing modules. This makes it easy to test functions without running the entire application.
- **Avoid Wildcard Imports**: When importing modules, avoid using `from module import *` as it can lead to namespace pollution and unexpected behavior.
- **Include it in Every Script**: Make it a habit to include the `if __name__ == "__main__":` check in every script you write. It will save you from a lot of confusion and unexpected behavior.
- **Leverage it for Scripting**: If you're writing a script that can be both run directly and imported as a module, use the `if __name__ == "__main__":` block to handle the direct execution logic.
- **Keep it Clean**: Keep the code under the `if __name__ == "__main__":` block minimal and focused on testing or running the script. Avoid putting large amounts of code there.

### Conclusion

The `if __name__ == "__main__":` check is a simple yet powerful feature in Python that every developer should use. It helps prevent unintended code execution when modules are imported, makes testing easier, and clarifies which script is being run. By incorporating this check into your coding habits, you'll write cleaner, more maintainable code and avoid many common pitfalls. So, the next time you write a Python script, make sure to include the `if __name__ == "__main__":` check—it will be worth it!

---


## 007 Scopes



## Understanding Variable Scopes in Python

Variable scopes are a fundamental concept in Python that determine the accessibility and visibility of variables within different parts of your code. Understanding scopes is crucial because it dictates where a variable can be accessed and how it can be used. In this blog post, we’ll explore the concept of scopes in Python, with a focus on global and local variables, and provide some best practices for using them effectively.

---

### What Are Scopes in Python?

A scope in Python refers to the region of the code where a variable is defined and can be accessed. Scopes help organize code by controlling variable visibility and reducing the risk of naming conflicts. In Python, there are two primary types of scopes:

1. **Global Scope**: Variables defined at the top level of a script (not inside any function or class) are in the global scope. These variables can be accessed from anywhere in the script.
   
2. **Local Scope**: Variables defined inside a function or a class are in the local scope. These variables can only be accessed within the function or class where they are defined.

---

### Global Scope in Python

Let’s start with an example of a global variable:

```python
variable = 10  # This is a global variable

def do_something():
    print(variable)  # This will print 10

do_something()
```

In this example, `variable` is defined in the global scope. It can be accessed from anywhere in the script, including inside the `do_something()` function. When you run this code, it will output `10`.

---

### Local Scope in Python

Now, let’s look at an example of a local variable:

```python
def do_something():
    variable2 = 20  # This is a local variable
    print(variable2)  # This will print 20

do_something()
```

Here, `variable2` is defined inside the `do_something()` function. It is only accessible within this function. If you try to access `variable2` outside the function, you’ll get an error because it is not defined in the global scope.

---

### Nested Scopes in Python

Python also allows you to define functions inside functions, creating nested scopes. Let’s see an example:

```python
def hello():
    variable3 = 30  # This is a local variable in the outer function

    def hello2():
        print(variable3)  # This can access variable3 from the outer scope

    hello2()

hello()
```

In this example, `variable3` is defined in the outer function `hello()`. The inner function `hello2()` can access `variable3` because it is defined in the outer scope. However, `variable3` is not accessible outside the `hello()` function.

---

### Best Practices for Using Scopes

Here are some best practices to keep in mind when working with scopes in Python:

1. **Avoid Global Variables**: Global variables should be used sparingly. They can lead to naming conflicts and make your code harder to debug. It’s better to encapsulate variables within functions or classes.

2. **Use Local Variables**: Local variables are safer and more efficient. They are only accessible within their scope, reducing the risk of unintended side effects.

3. **Understand Nested Scopes**: If you define functions inside functions, make sure you understand how variable scoping works. Inner functions can access variables from outer scopes, but variables defined in inner functions are not accessible outside those functions.

4. **Performance Considerations**: Accessing global variables is slightly slower than accessing local variables because Python has to search the global scope. For performance-critical code, prefer local variables.

---

### Tips and Tricks

- **Scope Lookup**: Python follows the LEGB rule for variable lookup (Local, Enclosing, Global, Built-in). This means Python first looks for a variable in the local scope, then in the enclosing scope, then in the global scope, and finally in the built-in scope.

- **Avoid Using the `global` Keyword**: The `global` keyword allows you to modify global variables inside a function. However, using it excessively can lead to the same issues as having too many global variables.

- **Use Encapsulation**: Encapsulate your code in functions or classes to keep variables organized and reduce the risk of naming conflicts.

- **Test Your Code**: Always test your code to ensure variables are behaving as expected. If a variable isn’t accessible where you expect it to be, check its scope.

---

### Conclusion

Understanding variable scopes is essential for writing clean, efficient, and maintainable Python code. By limiting the use of global variables and keeping variables localized to functions or classes, you can avoid naming conflicts and improve the performance of your code. Remember to always test your code to ensure variables are behaving as expected, and use encapsulation to keep your code organized. Happy coding!

---


## 008 Nonlocal & Global



## Understanding Global and Non-Local Keywords in Python

Now that we've covered the basics of variable scoping in Python, it's time to dive deeper into two important keywords: `global` and `non-local`. These keywords help you manage variable scopes within your functions, allowing you to modify variables outside the local scope. Let's explore how they work with practical examples.

---

### Introduction to Global Variables

In Python, a variable defined outside any function or class is considered a global variable. For example:

```python
x = 10  # Global variable

def outer():
    x = 20  # Local variable
    print("Inner:", x)
    
print("Outer:", x)
outer()
```

When you run this code, the output will be:

```
Outer: 10
Inner: 20
```

Here, `x` inside the `outer()` function is a local variable, and the global `x` remains unchanged.

---

### Modifying Global Variables Inside a Function

If you want to modify the global variable inside a function, you need to use the `global` keyword. Here's how it works:

```python
x = 10  # Global variable

def outer():
    global x  # Declare x as global
    x = 20    # Now, this modifies the global variable
    print("Inner:", x)
    
print("Outer:", x)
outer()
```

The output will now be:

```
Outer: 20
Inner: 20
```

By using `global x`, you're telling Python that you want to modify the global variable `x` inside the function.

---

### Creating Global Variables Inside a Function

You can also create a global variable from within a function using the `global` keyword. For example:

```python
def outer():
    global x  # Declare x as global
    x = 20    # This creates a global variable
    
outer()
print("Outer:", x)
```

When you run this code, it will output:

```
Outer: 20
```

This demonstrates that you can create and modify global variables even if they don't exist in the global scope initially.

---

### Understanding the Non-Local Keyword

The `non-local` keyword is used to access variables from an outer scope (but not the global scope). It's particularly useful when working with nested functions. Let's consider an example:

```python
x = 10  # Global variable

def outer():
    x = 20  # Local variable in outer function
    
    def inner():
        x = 30  # Local variable in inner function
        print("Inner:", x)
    
    inner()
    print("Outer:", x)

outer()
print("Global:", x)
```

The output will be:

```
Inner: 30
Outer: 20
Global: 10
```

Here, the `inner()` function creates its own local variable `x`, which shadows the `x` in the outer function.

---

### Modifying Variables in the Outer Scope

To modify the `x` in the outer function from the inner function, use the `non-local` keyword:

```python
x = 10  # Global variable

def outer():
    x = 20  # Local variable in outer function
    
    def inner():
        nonlocal x  # Access the x from the outer function
        x = 30     # Now, this modifies the x in the outer function
        print("Inner:", x)
    
    inner()
    print("Outer:", x)

outer()
print("Global:", x)
```

The output will now be:

```
Inner: 30
Outer: 30
Global: 10
```

By using `nonlocal x`, the inner function modifies the `x` in the outer function, not the global `x`.

---

### Key Differences Between Global and Non-Local

| **Feature**          | **Global**                        | **Non-Local**                     |
|----------------------|-----------------------------------|------------------------------------|
| **Scope**            | Modifies the global variable       | Modifies the variable in the nearest outer scope |
| **Usage**            | Used to access global variables   | Used to access variables in enclosing scopes   |
| **Application**      | Affects the global scope          | Affects only the enclosing function scope |

---

### Tips and Tricks

1. **Use Global and Non-Local Sparingly**: While these keywords are powerful, they can make your code harder to debug. Use them only when necessary.
2. **Avoid Variable Shadowing**: Be cautious when using the same variable name in different scopes, as it can lead to unexpected behavior.
3. **Understand Scope Hierarchy**: Always remember that `global` refers to the top-level global scope, while `non-local` refers to the nearest enclosing scope.
4. **Test Your Code**: Run your code frequently to ensure that variable modifications behave as expected.

By mastering the `global` and `non-local` keywords, you'll have better control over variable scoping in Python, making your code more flexible and easier to maintain.

---
