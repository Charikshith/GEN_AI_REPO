

## 001 What is OOP



## Introduction to Object-Oriented Programming in Python

Now that we've covered a majority of the Python language, it's time to dive into more advanced and popular coding concepts. One of the most significant paradigms in programming is **Object-Oriented Programming (OOP)**. Over the next few lessons, we'll explore how to use OOP in Python, and how it can make your code more reusable, organized, and effective in various scenarios.

### What is Object-Oriented Programming?

Object-Oriented Programming is a programming paradigm that revolves around the concept of **classes** and **objects**. It's a way of designing and organizing code that simulates real-world objects and systems. While OOP is a fundamental concept in many programming languages like Java, C++, and C#, it is also present in Python, though not as heavily emphasized.

### Why Learn OOP in Python?

Although Python is not as strictly OOP-focused as some other languages, understanding and using OOP concepts can greatly enhance your coding skills. Here are a few reasons why OOP is important to learn:

1. **Code Reusability**: OOP allows you to create reusable code. Once you define a class, you can create multiple objects from it, reducing redundancy in your code.

2. **Modularity**: OOP helps in breaking down a complex program into smaller, manageable modules (classes), making it easier to maintain and modify.

3. **Real-World Modeling**: OOP makes it easier to model real-world objects and systems. For example, you can create a `Car` class with attributes like color, model, and methods like `start_engine()` or `accelerate()`.

### What You'll Learn in Upcoming Lessons

In the next few lessons, we'll dive deeper into the world of OOP in Python. Here’s a sneak peek at what we’ll cover:

- **Classes and Objects**: Learn how to define classes and create objects from them.
- **Attributes and Methods**: Understand how to define and use attributes (data) and methods (functions) within a class.
- **Inheritance**: Discover how to create new classes based on existing ones, inheriting their properties and behaviors.
- **Polymorphism**: Explore how objects of different classes can be treated as objects of a common superclass.
- **Encapsulation and Abstraction**: Learn how to hide complex implementation details and expose only the necessary information.

By the end of this series, you’ll be comfortable working with OOP concepts in Python, making your code more organized, reusable, and efficient.

### Tips and Tricks

- **Start Small**: Don’t try to implement OOP in every part of your code right away. Start with small projects to get a feel for how classes and objects work.
- **Keep it Simple**: Avoid overcomplicating your classes. A class should represent a single responsibility or concept.
- **Use Inheritance Wisely**: Inheritance is a powerful tool, but it can lead to tight coupling between classes. Consider using composition instead when appropriate.
- **Practice, Practice, Practice**: Like any new concept, OOP requires practice. Try to apply what you learn in real-world scenarios or personal projects.

### What's Next?

In the next lesson, we’ll start by creating our first class in Python. You’ll learn how to define a class, create objects, and work with attributes and methods. Stay tuned for more exciting content as we explore the world of Object-Oriented Programming in Python!

---

If you have any questions or need clarification on any of the concepts covered, feel free to ask in the comments below. Happy coding!

---


## 002 Classes & Objects



## Understanding Classes in Python: A Step-by-Step Guide

Classes are a fundamental concept in object-oriented programming (OOP), and Python makes it easy to work with them. In this blog post, we’ll explore how to create a class, understand its components, and use it to create objects. Let’s dive in!

### What is a Class?

A class is like a blueprint or a template that defines the properties and behaviors of an object. Think of it as a design pattern or a template that can be used to create multiple objects. For example, if you want to create a lamp, you can define a `Lamp` class that includes all the functionalities a lamp should have, such as turning on, turning off, and describing its properties.

### Creating a Class

Let’s create a simple `Lamp` class to illustrate the concept. Here’s how you can define it:

```python
class Lamp:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def turn_on(self):
        print(f"{self.model} is turned on.")

    def turn_off(self):
        print(f"{self.model} is turned off.")

    def describe(self):
        print(f"This lamp is model {self.model} and color {self.color}.")
```

#### Breaking Down the Class

1. **`__init__` Method (Constructor):**
   - The `__init__` method is a special method that gets called when you create a new object from the class. It initializes the attributes of the class.
   - In this case, we’re initializing `model` and `color` attributes.

2. **Methods:**
   - `turn_on()`: Simulates turning on the lamp.
   - `turn_off()`: Simulates turning off the lamp.
   - `describe()`: Prints out the model and color of the lamp.

### Creating Objects from the Class

Once you’ve defined the class, you can create as many objects as you want. Each object will have its own set of attributes and will be able to call the methods defined in the class.

```python
# Creating a red lamp
red_lamp = Lamp("RRX55", "red")
red_lamp.turn_on()  # Output: RRX55 is turned on.
red_lamp.describe()  # Output: This lamp is model RRX55 and color red.

# Creating a blue lamp
blue_lamp = Lamp("RRX56", "blue")
blue_lamp.turn_off()  # Output: RRX56 is turned off.
blue_lamp.describe()  # Output: This lamp is model RRX56 and color blue.
```

### Modifying Object Attributes

One of the powerful features of OOP is the ability to modify object attributes after creation. For example, if you repaint the lamp, you can update its color:

```python
red_lamp.color = "blue"
red_lamp.describe()  # Output: This lamp is model RRX55 and color blue.
```

### Benefits of Object-Oriented Programming

- **Reusability:** You can create multiple objects from the same class, reducing code duplication.
- **Modularity:** Each object is independent and can be manipulated without affecting other objects.
- **Easier Maintenance:** If you need to update the functionality of the lamp, you only need to modify the class, and all objects created from it will inherit the changes.

### Tips and Tricks

1. **Use Meaningful Names:**
   - Always use descriptive names for your classes, methods, and attributes. This makes your code easier to understand and maintain.

2. **Type Hinting:**
   - Use type hints to specify the expected types of parameters and return values. This improves code readability and helps catch errors early.

3. **Keep Methods Short:**
   - Each method should perform a single, well-defined task. This makes your code easier to test and debug.

4. **Debugging:**
   - Use print statements or a debugger to understand how your objects are behaving. This is especially useful when you’re learning OOP.

5. **Practice:**
   - The best way to get comfortable with classes is to create them! Try modeling different real-world objects, like cars, books, or even animals.

### Conclusion

Classes are a powerful tool in Python that allow you to create reusable, modular code. By defining a class, you’re creating a blueprint that can be used to generate multiple objects, each with its own unique characteristics. Whether you’re building a simple lamp or a complex system, classes will help you organize your code and make it easier to maintain.

Remember, practice is key. Start by creating simple classes and gradually move on to more complex ones. Happy coding!

---


## 003 What is self



## Understanding the `self` Keyword in Python Classes

Now that we've created our `Lamp` class, it's time to dive into one of the most essential concepts in Python classes: the `self` keyword. You've probably noticed that `self` appears in almost every function and variable declaration within a class, but what does it really do? Let's break it down and explore why it's so crucial in object-oriented programming.

---

### What is the `self` Keyword?

The `self` keyword is a reference to the current instance of a class. It's used to distinguish instance-specific attributes and methods from class-level attributes and methods. In other words, `self` allows us to ensure that changes made to variables or attributes only affect the specific instance of the class (e.g., `red_lamp`) and not the class itself or other instances (e.g., `blue_lamp`).

---

### Why Do We Use `self`?

When you create multiple instances of a class (like `red_lamp` and `blue_lamp`), each instance has its own set of attributes. The `self` keyword helps Python understand which instance's attributes or methods you're referring to.

For example:
```python
class Lamp:
    def __init__(self, model):
        self.model = model

red_lamp = Lamp("Red Lamp")
blue_lamp = Lamp("Blue Lamp")
```

- Here, `self.model` inside the `__init__` method refers to the instance being created (`red_lamp` or `blue_lamp`).
- When you create `red_lamp`, `self` points to the `red_lamp` instance, and `self.model` is set to "Red Lamp".
- Similarly, when you create `blue_lamp`, `self` points to the `blue_lamp` instance, and `self.model` is set to "Blue Lamp".

This ensures that changes to one instance don't affect the other.

---

### Is `self` Mandatory?

Yes, `self` is required as the first parameter in instance methods. It's a convention that tells Python you're working with instance-specific attributes or methods. If you try to access or modify an attribute without `self`, you'll get an error because Python won't know which instance you're referring to.

For example:
```python
def __init__(model):  # This will cause an error
    model = model
```

Instead, you must include `self`:
```python
def __init__(self, model):  # Correct way
    self.model = model
```

---

### Can We Rename `self`?

Technically, yes! While `self` is the standard convention, you can use any other name, like `this` or `apple`. However, sticking to `self` is highly recommended because it makes your code more readable and aligns with Python's conventions.

```python
class Lamp:
    def __init__(this, model):  # Works, but not recommended
        this.model = model
```

---

### Tips and Tricks

1. **Use `self` Consistently**: Always include `self` as the first parameter in instance methods and when defining instance attributes. This ensures your code works as expected.
2. **Avoid Confusion with Class Attributes**: Remember that `self` refers to the instance, not the class. If you want to create class-level attributes, define them outside of instance methods.
3. **Keep It Descriptive**: Use `self` to make your code clear. For example, `self.model` is much more descriptive than `model`.
4. **Experiment with Examples**: The best way to understand `self` is by creating multiple instances of a class and observing how changes affect each instance independently.

---

### Final Thoughts

The `self` keyword might seem confusing at first, but it becomes second nature as you work more with object-oriented programming in Python. It's the key to ensuring that each instance of your class behaves independently, making your code more predictable and maintainable. So, embrace `self` and let it help you write cleaner, more organized Python code!

---


## 004 Class Variables & Instance Variables



## Understanding Class Variables and Instance Variables in Python

### Introduction

In object-oriented programming (OOP) with Python, understanding the distinction between class variables and instance variables is crucial. These concepts determine how data is stored and accessed within classes and their instances. This guide will clarify the differences and provide a practical example to illustrate their usage and potential pitfalls.

### Instance Variables

Instance variables are data members that are unique to each instance of a class. They are defined within the class methods, typically in the `__init__` method, and are associated with the `self` parameter. Each instance of the class has its own copy of these variables, allowing for individual customization.

**Example of Instance Variables:**

```python
class Animal:
    def __init__(self, name):
        self.name = name  # Instance variable

dog = Animal("Buddy")
cat = Animal("Whiskers")
```

In this example, `name` is an instance variable. Each instance (`dog` and `cat`) has its own `name`.

### Class Variables

Class variables are shared among all instances of a class. They are defined outside of any method, directly within the class definition. Changes to a class variable affect all instances since they share the same memory space.

**Example of Class Variables:**

```python
class Animal:
    tricks = []  # Class variable

dog = Animal()
cat = Animal()
```

Here, `tricks` is a class variable. Both `dog` and `cat` instances refer to the same list.

### A Practical Example

Let's create an `Animal` class to demonstrate the use of both instance and class variables.

```python
class Animal:
    tricks = []  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

    def teach_trick(self, trick_type):
        self.tricks.append(trick_type)
```

### The Problem with Modifying Class Variables

When modifying class variables through instance methods, unexpected behavior can occur because all instances share the same variable.

```python
dog = Animal("Buddy")
cat = Animal("Whiskers")

dog.teach_trick("make dinner")
dog.teach_trick("go work at a job")

print(dog.tricks)  # Output: ['make dinner', 'go work at a job']
print(cat.tricks)  # Output: ['make dinner', 'go work at a job']
```

Both `dog` and `cat` instances display the same tricks, demonstrating that modifying a class variable through one instance affects all instances.

### Best Practices and Tips

- **Instance Variables for Unique Data:** Use instance variables for data that should be unique to each instance, such as `name` or `age`.
- **Class Variables for Shared Data:** Reserve class variables for data that should be shared by all instances, like a common setting or constant.
- **Avoid Mutable Class Variables:** Mutable types like lists and dictionaries as class variables can lead to unintended side effects. Instead, use instance variables for such data.
- **Use `@classmethod` for Class-Level Operations:** When modifying class variables, consider using class methods to maintain clarity and avoid confusion.

### Conclusion

Understanding the difference between class and instance variables is essential for effective OOP in Python. By following best practices and being mindful of how variables are defined and accessed, you can write more predictable and maintainable code.

### Tips and Tricks

- **Use `self` Explicitly:** Always use `self` when referring to instance variables to avoid confusion with local variables.
- **Immutable Defaults:** Avoid using mutable objects as default arguments for instance variables to prevent unexpected behavior across function calls.
- **Testing with Multiple Instances:** When working with class variables, test your code with multiple instances to ensure the behavior matches your expectations.

By adhering to these guidelines, you can leverage the power of OOP in Python effectively, ensuring your code is both efficient and easy to understand.

---


## 005 Getters & Setters



```markdown
## Mastering Getters and Setters in Python: A Comprehensive Guide

Getters and setters are fundamental concepts in object-oriented programming (OOP) that help encapsulate data and control access to class attributes. In Python, while you can directly access and modify class attributes, using getters and setters provides a more structured and maintainable approach. This guide will walk you through the why and how of using getters and setters in Python.

### What Are Getters and Setters?

Getters and setters are methods that allow you to access and modify class attributes indirectly. A getter retrieves the value of a private attribute, while a setter modifies it. This abstraction layer is useful for:

- **Validation:** Ensure that only valid values are set.
- **Logging:** Track when an attribute is accessed or modified.
- **Encapsulation:** Hide internal implementation details.
- **Flexibility:** Add additional logic when getting or setting a value.

### Why Use Getters and Setters?

Before diving into the implementation, let’s understand the motivation behind using getters and setters.

#### Direct Access vs. Controlled Access

Without getters and setters, you can directly access and modify attributes:

```python
class Fruit:
    def __init__(self, name):
        self.name = name

fruit = Fruit("Apple")
fruit.name = "Banana"
```

However, this approach lacks control and transparency. By using getters and setters, you can enforce specific behaviors when accessing or modifying attributes.

### Implementing Getters and Setters in Python

Python provides a convenient way to create getters and setters using the `@property` decorator.

#### Step 1: Define a Private Attribute

In Python, private attributes are denoted by a leading underscore (`_`). While not enforced, this convention signals that the attribute should be accessed through methods.

```python
class Fruit:
    def __init__(self, name):
        self._name = name
```

#### Step 2: Create a Getter

A getter is created using the `@property` decorator. This allows you to access the attribute like a property.

```python
class Fruit:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Accessing the name attribute...")
        return self._name
```

#### Step 3: Create a Setter

A setter is created using the `@x.setter` decorator, where `x` is the name of the property.

```python
class Fruit:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Accessing the name attribute...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting the name attribute...")
        self._name = value
```

### Benefits of Using Getters and Setters

- **Validation:** You can add checks to ensure only valid values are set.
- **Logging:** You can log when an attribute is accessed or modified.
- **Encapsulation:** You can change the internal implementation without affecting external code.
- **Flexibility:** You can add additional logic when getting or setting a value.

### Practical Example

Let’s create a `Fruit` class with a `name` attribute and demonstrate how getters and setters work.

```python
class Fruit:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting the name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting the name to", value)
        self._name = value

# Create an instance
apple = Fruit("Apple")

# Access the name
print("Fruit name:", apple.name)

# Change the name
apple.name = "Banana"

# Access the updated name
print("Updated fruit name:", apple.name)
```

**Output:**

```
Getting the name...
Fruit name: Apple
Setting the name to Banana
Getting the name...
Updated fruit name: Banana
```

### Creating Additional Properties

You can create additional properties for other attributes, such as `calories`:

```python
class Fruit:
    def __init__(self, name, calories):
        self._name = name
        self._calories = calories

    @property
    def calories(self):
        print("Getting the calories...")
        return self._calories

    @calories.setter
    def calories(self, value):
        if value < 0:
            raise ValueError("Calories cannot be negative.")
        print("Setting the calories to", value)
        self._calories = value

# Example usage
fruit = Fruit("Apple", 95)
print("Calories:", fruit.calories)
fruit.calories = 100
```

### Tips and Tricks

1. **Use Type Hints:**
   Add type hints for better code readability and to help with static type checking.

   ```python
   def name(self) -> str:
       ...
   ```

2. **Keep Getters Simple:**
   Avoid complex logic in getters to prevent unexpected side effects.

3. **Add Validation in Setters:**
   Ensure that only valid values are accepted by adding checks in setters.

4. **Use Logging:**
   Add print statements or logging to track when attributes are accessed or modified.

5. **Avoid Overuse:**
   Use getters and setters only when necessary. Direct access is acceptable for simple cases.

By following these guidelines, you can effectively use getters and setters in Python to write more maintainable and robust code.
```

---


## 006 __init__()



## Understanding Initializers in Python

### Introduction to Initializers

Initializers in Python are special methods that set up the initial state of an object when it is created. The most common initializer is the `__init__` method, which is a dunder method (short for "double underscore"). This method is automatically called when an object of the class is instantiated.

### The `__init__` Method

The `__init__` method is defined within a class and is used to initialize the attributes of the class. Here’s an example of a `Car` class that uses an initializer:

```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        print(f"The car model is {self.model} and the color is {self.color}.")
```

- **Parameters**: The `__init__` method can take parameters, which are used to set up the initial state of the object.
- **Instance Variables**: Inside the `__init__` method, instance variables are created using `self.variable_name`. These variables are associated with each instance of the class.

### Example Usage

When you create an object of the `Car` class, the `__init__` method is called automatically:

```python
car1 = Car("BMW", "Blue")
car2 = Car("Ferrari", "Red")
```

- **Output**:
  ```
  The car model is BMW and the color is Blue.
  The car model is Ferrari and the color is Red.
  ```

### Adding Logic to the Initializer

You can add any logic inside the `__init__` method, such as calculations, validations, or even calling other methods.

```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.mileage = 0
        print(f"A new car of model {self.model} and color {self.color} has been created.")
        
    def drive(self):
        self.mileage += 10
        print(f"The {self.color} {self.model} has driven 10 miles. Current mileage: {self.mileage} miles.")
```

### Key Points

1. **Purpose**: The `__init__` method is used to initialize the attributes of the class and perform any necessary setup tasks.
2. **Execution**: The `__init__` method is called automatically when an object is created.
3. **Flexibility**: You can add any logic inside the `__init__` method, such as setting default values, performing validations, or running other methods.
4. **Variable Naming**: The instance variables do not have to have the same name as the parameters passed to the `__init__` method. However, it’s a good practice to keep them consistent for readability.

### Tips and Tricks

- **Meaningful Variable Names**: Always use meaningful and descriptive names for your variables to improve code readability.
- **Avoid Heavy Computations**: Keep the `__init__` method concise and avoid heavy computations. If you need to perform complex tasks, consider doing them in separate methods that can be called after the object is initialized.
- **Use of `self`**: Always refer to instance variables using `self` to avoid confusion and ensure that the variables are correctly associated with the instance.
- **Error Handling**: Use the `__init__` method to validate inputs and handle potential errors to ensure that objects are created in a consistent and valid state.

By following these guidelines and best practices, you can effectively use initializers to create robust and well-structured classes in Python.

---


## 007 Constructors



Constructors in Python: A Comprehensive Guide

Constructors play a pivotal role in object-oriented programming, serving as the foundation for initializing objects. In Python, the constructor is defined by the `__init__` method within a class. This method is automatically called upon the creation of an instance, ensuring that the object is properly set up with the necessary attributes and initial state.

### The Role of the Constructor

The primary function of a constructor is to initialize an object when it is instantiated. This includes setting default values for attributes or accepting parameters to customize the object's state. For instance, consider a `Car` class where the constructor might accept `make` and `model` as parameters, ensuring each `Car` object has these attributes defined.

### Customizing the Constructor

Constructors can be tailored to meet specific needs. They can accept parameters, allowing for the customization of each object. For example, a `Fruit` class might have a constructor that accepts a `name` parameter, setting the fruit's name upon instantiation. Additionally, constructors can execute any necessary code, such as calculating derived attributes or logging initialization events.

### Default Values in Constructors

To enhance flexibility, constructors can be designed with default parameter values. This allows objects to be created without explicitly passing all arguments, providing a default initialization. For example, a `Fruit` object could default to 'fruit' if no name is provided, ensuring that an object always has a valid state even when parameters are omitted.

### Example Usage

Here's an example of a `Car` class with a constructor that accepts `make` and `model`:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating an instance
my_car = Car('Toyota', 'Corolla')
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla
```

### Key Takeaways

- **Initialization**: Constructors ensure that objects are created in a consistent and predictable state.
- **Customization**: Parameters allow for tailored object creation, meeting specific requirements.
- **Flexibility**: Default values provide a fallback, making object creation versatile.
- **Functionality**: Beyond attribute assignment, constructors can execute any necessary setup code.

### Conclusion

Constructors are fundamental in Python, enabling developers to create robust, customizable objects. By understanding and effectively utilizing constructors, you can craft classes that produce objects ready for use, enhancing both code clarity and maintainability.

---


## 008 __str__() & __repr__()



## Customizing Object Representation in Python: __str__ and __repr__ Dunder Methods

In Python, when you print an object, you often get a default representation that looks something like `<__main__.Car object at 0x...>`. This isn’t very helpful for understanding what the object actually represents. To make your objects more readable and user-friendly, Python provides two special Dunder methods: `__str__` and `__repr__`. These methods allow you to define custom string representations for your objects.

### What is the `__str__` Dunder Method?

The `__str__` method is used to return a string representation of an object that is meant to be human-readable. This is the method that gets called when you use the `str()` function or when you print an object.

#### Example Implementation

```python
class Car:
    def __init__(self, model, caller):
        self.model = model
        self.caller = caller

    def __str__(self):
        return f"{self.model} {self.caller}"
```

In this example, when you create a `Car` object and print it, you’ll get a readable string like `BMW blue` instead of the default memory address.

### What is the `__repr__` Dunder Method?

The `__repr__` method is similar to `__str__`, but its purpose is different. It should return a string that represents the object in a way that is useful for developers. Ideally, it should be a string that could be used to recreate the object.

#### Example Implementation

```python
class Car:
    def __init__(self, model, caller):
        self.model = model
        self.caller = caller

    def __repr__(self):
        return f"Car(model='{self.model}', caller='{self.caller}')"
```

When you call `repr(car)` or use the `%r` format specifier, you’ll get a string like `Car(model='BMW', caller='blue')`, which is useful for debugging and logging.

### Key Differences Between `__str__` and `__repr__`

- **Purpose**:
  - `__str__`: Human-readable string.
  - `__repr__`: Unambiguous representation for developers.

- **Usage**:
  - `__str__`: Called by `str()` and `print()`.
  - `__repr__`: Called by `repr()` and is the fallback for `str()` if `__str__` is not defined.

- **Output**:
  - `__str__`: Should return a string that makes sense to end-users.
  - `__repr__`: Should return a string that is useful for developers and could be used to recreate the object.

### When to Use Each

- Use `__str__` for:
  - Providing a user-friendly representation of your object.
  - Returning a string that is meant to be displayed to end-users.

- Use `__repr__` for:
  - Providing a detailed, developer-friendly representation of your object.
  - Returning a string that could be used to recreate the object.

### Tips and Tricks

- **Consistency**: Always implement both `__str__` and `__repr__` for your custom classes. This ensures that your objects have meaningful representations in different contexts.

- **Readability**: Keep `__str__` simple and focused on readability. Avoid including too much technical detail in this method.

- **Reproducibility**: Make sure that the string returned by `__repr__` is unambiguous and, if possible, could be used to recreate the object.

- **Best Practices**: Follow Python’s official guidelines for special methods to ensure consistency across your codebase.

By implementing these Dunder methods, you can make your objects more informative and easier to work with, both for yourself and other developers who use your code.

---


## 009 __eq__



## Custom Class Comparison in Python: A Deep Dive

### Introduction

When working with classes in Python, comparing instances can sometimes yield unexpected results. By default, Python's `==` operator does not compare the attributes of objects but instead checks if both variables refer to the same object in memory. This can lead to confusion, especially when you want to determine if two instances of a class are "equal" based on their attribute values. In this post, we'll explore how to customize the comparison logic for class instances using Python's dunder (special) methods.

### The Problem with Default Class Comparison

Let's consider an example to illustrate the issue. Suppose we have a `Fruit` class with attributes `name` and `calories`:

```python
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

apple = Fruit("Apple", 10)
apple2 = Fruit("Apple", 10)
print(apple == apple2)  # Output: False
```

As you can see, even though `apple` and `apple2` have the same attributes with the same values, the comparison returns `False`. This is because Python's default `==` operator checks for identity, not equality of attributes.

### Customizing the Equality Check

To achieve the desired comparison behavior, we need to define a custom equality check using the `__eq__` dunder method. This method allows us to specify how instances of our class should be compared.

Here's how we can modify the `Fruit` class to include a custom `__eq__` method:

```python
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
```

In this implementation, the `__eq__` method compares the `__dict__` attribute of the instances. The `__dict__` attribute is a dictionary that contains all the instance's attributes and their values. By comparing these dictionaries, we ensure that all attributes are checked for equality.

Now, let's test the comparison again:

```python
apple = Fruit("Apple", 10)
apple2 = Fruit("Apple", 10)
print(apple == apple2)  # Output: True

apple3 = Fruit("Apple", 20)
print(apple == apple3)  # Output: False
```

As expected, `apple == apple2` returns `True` because their attributes are identical, while `apple == apple3` returns `False` because their `calories` differ.

### Customizing the Comparison Logic

The beauty of the `__eq__` method lies in its flexibility. You can customize the comparison logic to suit your needs. For example, if you want to compare only specific attributes, you can modify the method accordingly:

```python
def __eq__(self, other):
    return self.name == other.name
```

This implementation compares only the `name` attribute, ignoring other attributes like `calories`.

### Important Considerations

1. **Type Checking**: When implementing `__eq__`, ensure that the `other` object is an instance of the same class. If `other` does not have the expected attributes, it may raise an `AttributeError`.

2. **Symmetry**: The `__eq__` method should be symmetric. That is, `a == b` should return the same result as `b == a`.

3. **Consistency**: The comparison logic should be consistent across all instances of the class.

### Tips and Tricks

- **Use `__dict__` for Simplicity**: Comparing `__dict__` is a concise way to check all attributes. However, ensure that this approach aligns with your use case.

- **Handle `None` and Different Types**: Always check if `other` is an instance of your class before accessing its attributes to avoid `AttributeError` or unexpected behavior.

- **Override `__hash__` if Needed**: If you plan to use your objects in hashable collections (like `set` or as dictionary keys), consider overriding the `__hash__` method as well.

- **Test Thoroughly**: Always test your custom comparison logic with various scenarios to ensure it behaves as expected.

By implementing the `__eq__` method, you can define how instances of your class should be compared, enabling more intuitive and meaningful equality checks. This is especially useful in scenarios where you need to compare objects based on their attribute values rather than their identity in memory.

---

### Summary

- Default comparison in Python checks for identity, not equality of attributes.
- Use the `__eq__` dunder method to customize the comparison logic.
- Comparing `__dict__` is a simple way to check all attributes.
- Always consider edge cases and ensure your comparison logic is robust.

With this approach, you can create classes that behave intuitively when compared, making your code more readable and maintainable.

---


## 010 Methods VS Functions



```markdown
## Understanding the Difference Between Functions and Methods in Python

When working with Python, it's easy to get confused between the terms "function" and "method." While they may seem similar, understanding their differences is crucial for writing clean and effective code. In this post, we'll break down the key distinctions between functions and methods in Python, providing you with a clear understanding of when and how to use each.

### What is a Function?

A function in Python is a standalone block of code that can be called multiple times from different parts of your program. Functions are independent and don't belong to any class or object. They are defined using the `def` keyword and can take arguments and return values.

Here's an example of a simple function:

```python
def hello():
    print("Hello")

# Calling the function
hello()  # Outputs: Hello
```

As you can see, functions are straightforward. They are defined once and can be called anywhere in your code without needing to be tied to a class or object.

### What is a Method?

A method, on the other hand, is a function that is associated with a class. Methods are used to perform actions on instances of a class. They are defined inside the class and are typically used to modify or interact with the data (attributes) of the class.

Here's an example of a class with a method:

```python
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def eat(self):
        print(f"{self.name} has been eaten.")

# Creating an instance of Fruit
banana = Fruit("Banana", 10)

# Calling the method
banana.eat()  # Outputs: Banana has been eaten.
```

In this example, `eat` is a method of the `Fruit` class. To call the method, we need to create an instance of the class (in this case, `banana`) and then use the dot notation to access the method.

### Key Differences Between Functions and Methods

1. **Ownership**:
   - Functions are standalone and do not belong to any class or object.
   - Methods are part of a class and are called on instances of that class.

2. **Usage**:
   - Functions can be called directly by their name.
   - Methods require an instance of the class to be called.

3. **Purpose**:
   - Functions are general-purpose and can be used in various contexts.
   - Methods are specific to the class and are used to perform operations related to the class's data.

4. **Syntax**:
   - Functions are defined outside of any class.
   - Methods are defined inside a class and typically include the `self` parameter.

### Tips and Tricks

- **Use the Correct Terminology**: While it's common to use "function" and "method" interchangeably in casual conversation, it's important to use the correct terms when writing code or explaining concepts to others. This helps maintain clarity and avoids confusion.

- **Understand the Role of `self`**: In methods, the first parameter is usually `self`, which refers to the instance of the class. This allows the method to access and modify the attributes of the class.

- **Keep It Organized**: Functions are great for organizing code that doesn't depend on a class. Use functions for utility code that doesn't need to be tied to a specific object.

- **Practice Makes Perfect**: The more you write code, the more natural the distinction between functions and methods will become. Practice by creating classes with methods and standalone functions.

By understanding the difference between functions and methods, you'll be able to write more organized and maintainable code. Remember, functions are standalone blocks of code, while methods are tied to classes and are used to interact with class data. Happy coding!
```

---


## 011 Private & Protected



## Understanding Private and Protected Attributes and Methods in Python

Python is a versatile and dynamic programming language that supports object-oriented programming (OOP) concepts. One of the key aspects of OOP is encapsulation, which involves hiding internal details of an object from the outside world and only exposing necessary information. In Python, we achieve this using private and protected attributes and methods. Let’s dive into how these work and how to use them effectively.

### Public vs. Private Attributes

In Python, by default, all attributes (variables) and methods (functions) are public. This means they can be accessed and modified from anywhere in the program. However, there are scenarios where we want to restrict access to certain attributes or methods to ensure data integrity and encapsulation.

Let’s consider an example:

```python
class Lamp:
    def __init__(self, name, model):
        self.name = name  # Public attribute
        self.__model = model  # Private attribute

# Creating an instance of Lamp
my_lamp = Lamp("Table Lamp", 101)

# Accessing public attribute
print(my_lamp.name)  # Outputs: Table Lamp

# Trying to access private attribute directly
print(my_lamp.__model)  # Raises AttributeError
```

In the above code:
- `self.name` is a public attribute and can be accessed directly using `my_lamp.name`.
- `self.__model` is a private attribute, and trying to access it directly using `my_lamp.__model` will raise an `AttributeError`.

### Name Mangling in Private Attributes

Python performs a process called name mangling when you use double underscores. This means that the attribute name is internally changed to make it difficult to access it accidentally. For example, `self.__model` is internally converted to `self._Lamp__model`. 

Here’s how you can access a private attribute using name mangling:

```python
print(my_lamp._Lamp__model)  # Outputs: 101
```

However, this is not recommended because it defeats the purpose of making the attribute private in the first place.

### Private Methods

Just like attributes, methods can also be made private. Private methods are intended to be used internally within the class and should not be called from outside the class.

Here’s an example of a private method:

```python
class Lamp:
    def __init__(self, name, model):
        self.name = name
        self.__model = model

    def description(self):
        print(f"This is a {self.name} with model {self.__model}")

    def __self_maintenance(self):
        print("The lamp is performing self-maintenance.")

# Creating an instance of Lamp
my_lamp = Lamp("Table Lamp", 101)

# Calling public method
my_lamp.description()  # Outputs: This is a Table Lamp with model 101

# Trying to call private method directly
my_lamp.__self_maintenance()  # Raises AttributeError
```

In the above code:
- `description()` is a public method and can be called using `my_lamp.description()`.
- `__self_maintenance()` is a private method and cannot be called directly from outside the class.

If you try to call the private method directly, you’ll get an `AttributeError`. However, just like with private attributes, you can access private methods using name mangling:

```python
my_lamp._Lamp__self_maintenance()  # Outputs: The lamp is performing self-maintenance.
```

Again, this is not recommended as it bypasses the encapsulation.

### Protected Attributes and Methods

Python also supports protected attributes and methods, which are denoted by a single underscore. These are not enforced by Python but are rather a naming convention to indicate that the attribute or method should be treated as protected.

Here’s an example:

```python
class Lamp:
    def __init__(self, name, model, version):
        self.name = name
        self._model = model  # Protected attribute
        self.__version = version  # Private attribute

    def description(self):
        print(f"This is a {self.name} with model {self._model}")

    def _update_version(self):  # Protected method
        self.__version += 1

# Creating an instance of Lamp
my_lamp = Lamp("Table Lamp", 101, 123456)

# Accessing protected attribute
print(my_lamp._model)  # Outputs: 101

# Calling protected method
my_lamp._update_version()
print(my_lamp._Lamp__version)  # Outputs: 123457
```

In the above code:
- `_model` is a protected attribute and can be accessed directly using `my_lamp._model`.
- `_update_version()` is a protected method and can be called using `my_lamp._update_version()`.

Protected attributes and methods are typically used when you want to allow subclasses to access them but keep them internal to the class hierarchy.

### Inheritance and Protected Members

One of the key differences between private and protected members is their behavior in inheritance. Protected members can be accessed in subclasses, while private members cannot (without name mangling).

Here’s an example:

```python
class ElectricLamp(Lamp):
    def __init__(self, name, model, version):
        super().__init__(name, model, version)

    def do_something(self):
        print(f"The {self.name} is doing something.")
        print(f"Current version: {self._model}")
        self._update_version()

# Creating an instance of ElectricLamp
my_electric_lamp = ElectricLamp("Electric Lamp", 202, 789123)

# Calling methods
my_electric_lamp.do_something()
```

In the above code:
- The `ElectricLamp` class inherits from `Lamp` and can access the protected attribute `_model` and the protected method `_update_version()`.

### Best Practices and Tips

1. **Use Private Members for Encapsulation**: Use double underscores for attributes and methods that should be private to ensure they are not accessed directly from outside the class.

2. **Use Protected Members for Inheritance**: Use single underscores for attributes and methods that should be accessible in subclasses but are intended to be internal to the class hierarchy.

3. **Avoid Name Mangling**: While Python allows you to access private members using name mangling, it’s generally not recommended as it breaks encapsulation.

4. **Consistency is Key**: Be consistent in your use of private and protected members. This makes your code easier to understand and maintain.

5. **Document Your Code**: Use docstrings to document your classes, methods, and attributes. This helps other developers understand your code better.

### Final Thoughts

Understanding and using private and protected attributes and methods is crucial for writing clean, maintainable, and encapsulated code in Python. By following the conventions outlined in this post, you can ensure that your code is robust, secure, and adheres to OOP principles.

Remember, encapsulation is not about making things impossible to access but about making it clear what should and shouldn’t be accessed directly. This helps prevent accidental modifications and ensures that your code behaves as expected.

---

### Tips and Tricks

- **Use Private Members Sparingly**: While private members are useful for encapsulation, overusing them can make your code harder to debug and test.

- **Prefer Protected Members for Internal Use**: If you need to allow subclasses to access certain attributes or methods, use protected members instead of private ones.

- **Leverage Name Mangling with Caution**: While name mangling provides a way to access private members, it should be used judiciously and only when absolutely necessary.

- **Follow PEP 8 Guidelines**: Adhere to Python’s official style guide, PEP 8, for naming conventions and best practices.

- **Test Your Code Thoroughly**: Ensure that your use of private and protected members does not introduce unintended side effects or bugs.

By following these tips and understanding the concepts of private and protected members, you can write more organized and maintainable Python code. Happy coding!

---


## 012 Inheritance



## Understanding Inheritance in Python

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows us to create a new class based on an existing class. The existing class is called the *base class* or *parent class*, while the new class is called the *subclass* or *child class*. Inheritance helps in code reusability by allowing the subclass to inherit all the attributes and methods of the base class and adding new features or overriding existing ones as needed.

### Creating the Base Class

Let's start by creating a base class called `Animal`. This class will have common attributes and methods that all animals share.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
```

In this `Animal` class:
- The `__init__` method initializes each animal with a `name`.
- The `eat` method prints a message indicating that the animal is eating.
- The `sleep` method prints a message indicating that the animal is sleeping.

### Creating Subclasses

Now, let's create subclasses `Cat` and `Dog` that inherit from the `Animal` class. These subclasses will have their own specific attributes and methods in addition to the inherited ones.

#### Creating the Cat Subclass

```python
class Cat(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
    
    def meow(self):
        print(f"{self.name} says meow.")
```

In the `Cat` class:
- The `__init__` method calls the parent class's `__init__` using `super().__init__(name)` to initialize the `name` attribute.
- It also initializes a `weight` attribute specific to cats.
- The `meow` method is unique to the `Cat` class and prints a message indicating that the cat meows.

#### Creating the Dog Subclass

```python
class Dog(Animal):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job
    
    def work_at_job(self):
        print(f"{self.name} is working as a {self.job}.")
```

In the `Dog` class:
- The `__init__` method calls the parent class's `__init__` using `super().__init__(name)` to initialize the `name` attribute.
- It also initializes a `job` attribute specific to dogs.
- The `work_at_job` method is unique to the `Dog` class and prints a message indicating the dog's job.

### Instantiating Objects

Now, let's create instances of the `Cat` and `Dog` classes and demonstrate how they inherit and use the methods from the `Animal` class.

```python
# Creating a Cat instance
cat = Cat("Apple", 100)
cat.meow()        # Output: Apple says meow.
cat.sleep()      # Output: Apple is sleeping.

# Creating a Dog instance
dog = Dog("Waffles", "Chef")
dog.work_at_job()  # Output: Waffles is working as a Chef.
dog.sleep()       # Output: Waffles is sleeping.
```

### Benefits of Inheritance

The power of inheritance becomes clear when you see that both `Cat` and `Dog` classes inherit the `eat` and `sleep` methods from the `Animal` class without having to redefine them. This reduces code duplication and makes the code easier to maintain.

### Tips and Tricks

1. **Keep Base Classes Simple**: Ensure your base class contains only the most common attributes and methods that all subclasses will need. This makes your code more modular and easier to extend.

2. **Use the `super()` Function**: Always use `super()` to call the parent class's methods, especially in the `__init__` method. This ensures that the parent class's initialization is properly handled.

3. **Add Unique Functionality in Subclasses**: Subclasses should add methods or attributes that are specific to the subclass, making each subclass unique while still inheriting general functionality from the parent class.

4. **Avoid Redundant Code**: Inheritance helps reduce redundancy by allowing you to reuse code from the parent class. Avoid duplicating code in subclasses unless absolutely necessary.

5. **Experiment with Multiple Levels of Inheritance**: You can create a hierarchy of classes where a subclass can itself be a parent to another subclass. This allows for even more specialized classes.

By following these principles, you can leverage the power of inheritance to create robust, modular, and maintainable object-oriented programs in Python.

---


## 013 super()



## Understanding the Power of `super()` in Python Inheritance

Inheritance is one of the most powerful features of object-oriented programming (OOP) in Python. It allows us to create a new class based on an existing class, inheriting its attributes and methods. However, when working with inheritance, you might have encountered the `super()` keyword. In this blog post, we’ll explore what `super()` is, how it works, and why it’s so useful when dealing with class inheritance.

### What is `super()`?

The `super()` keyword in Python is used to access methods and properties of a parent class (also called a superclass) from a child class (also called a subclass). It returns a temporary object of the parent class, allowing you to call methods of the parent class from the child class.

### Why Do We Need `super()`?

When you create a subclass, you might want to add new functionality or override existing methods of the parent class. However, you might still need to use some of the parent class’s methods. This is where `super()` comes into play. It helps you:

1. Avoid rewriting code.
2. Access parent class methods and attributes.
3. Maintain a clean and organized code structure.

### Example: Using `super()` in Inheritance

Let’s consider an example to understand how `super()` works in practice.

#### Parent Class: `Lamp`
```python
class Lamp:
    def __init__(self, name):
        self.name = name
    
    def turn_on(self):
        print(f"The lamp {self.name} is turning on.")
    
    def turn_off(self):
        print(f"The lamp {self.name} is turning off.")
```

#### Child Class: `ElectricLamp`
```python
class ElectricLamp(Lamp):
    def __init__(self, name):
        super().__init__(name)
        
    def turn_on(self):
        print("Using electricity to turn on the lamp.")
        super().turn_on()
```

In this example:

1. The `ElectricLamp` class inherits from the `Lamp` class.
2. In the `__init__` method of `ElectricLamp`, we use `super().__init__(name)` to call the constructor of the parent class (`Lamp`). This ensures that the `name` attribute is properly initialized in the parent class.
3. The `turn_on` method in `ElectricLamp` overrides the `turn_on` method of `Lamp`. However, we still want to use the parent class’s implementation. Here, we use `super().turn_on()` to call the parent class’s method.

### How `super()` Helps

By using `super()`, we achieve the following:

1. **Code Reusability**: We don’t have to rewrite the code that already exists in the parent class. Instead, we reuse it.
2. **Cleaner Code**: Our code becomes cleaner and more maintainable because we avoid duplicating functionality.
3. **Easier Maintenance**: If the parent class’s method changes in the future, the child class will automatically inherit those changes without requiring any modifications.

### Running the Example

Let’s create an instance of `ElectricLamp` and see how it works:

```python
lamp = ElectricLamp("Bob")
lamp.turn_on()
```

Output:
```
Using electricity to turn on the lamp.
The lamp Bob is turning on.
```

As you can see, `super()` allows us to combine our own implementation with the parent class’s implementation seamlessly.

### Tips and Tricks

1. **Use `super()` with Arguments in Python 3**: In Python 3, you can use `super()` without any arguments. However, if you’re working with multiple inheritance, it’s a good practice to pass the class and instance explicitly: `super(ClassName, self).method()`.

2. **Method Resolution Order (MRO)**: Understand how Python resolves method calls in the presence of multiple inheritance. The MRO determines the order in which `super()` will search for methods in parent classes.

3. **Avoid Hardcoding Parent Class Names**: Using `super()` makes your code more flexible because it dynamically refers to the parent class, rather than hardcoding the parent class name.

4. **Be Cautious in Multiple Inheritance**: While `super()` is incredibly useful, it can lead to unexpected behavior in complex multiple inheritance scenarios. Always test your code thoroughly.

5. **Override Methods Judiciously**: Only override methods when necessary. If you don’t need to modify a method, let it inherit the parent class’s implementation.

By mastering the use of `super()`, you’ll be able to write more efficient, maintainable, and scalable code when working with inheritance in Python. Whether you’re building simple classes or complex hierarchies, `super()` will be your go-to tool for accessing and extending parent class functionality.

---


## 014 @classmethod & @staticmethod



## Understanding Static Methods and Class Methods in Python

### Introduction

In Python, methods within a class can be categorized into instance methods, static methods, and class methods. Each serves a distinct purpose, and understanding their differences is crucial for effective programming. This post delves into static methods and class methods, explaining their use cases and providing examples for clarity.

### Static Methods

**Definition:**  
A static method is a function that belongs to a class rather than an instance of the class. It doesn't require the `self` parameter and can be called without creating an instance of the class.

**Example:**  
```python
class Calculator:
    @staticmethod
    def add_numbers(a: float, b: float) -> float:
        return a + b

# Usage without instance
result = Calculator.add_numbers(10, 20)
print(result)  # Outputs: 30
```

**Use Cases:**  
- **Utility Functions:** Static methods are ideal for utility functions that don't depend on class or instance variables.
- **Code Organization:** They help keep related functions organized within a class, making code easier to find and maintain.

### Class Methods

**Definition:**  
A class method is bound to the class and not an instance. It uses the `cls` parameter to refer to the class itself.

**Example:**  
```python
class Calculator:
    variable = 10  # Class variable

    def __init__(self, name: str, version: int):
        self.name = name
        self.version = version

    @classmethod
    def create_with_version(cls, name: str, version: int):
        return cls(name, version)

# Usage
calculator = Calculator.create_with_version("Bob", 100)
print(calculator.name)  # Outputs: Bob
print(calculator.version)  # Outputs: 100
```

**Use Cases:**  
- **Alternative Constructors:** They provide alternative ways to create instances of a class, such as factories.
- **Class-Level Operations:** They are useful for operations involving class variables or when modifying the class itself.

### Comparison of Methods

| Method Type      | Parameter | Instance Required | Use Case Example                          |
|------------------|-----------|-------------------|------------------------------------------|
| Instance Method  | `self`    | Yes               | Instance-specific operations              |
| Static Method   | None      | No                | Utility functions, organization           |
| Class Method     | `cls`     | No                | Alternative constructors, class operations|

### Tips and Tricks

- **Static vs. Class Methods:** Use static methods for utility functions and class methods when you need to access or modify class variables.
- **Readability:** Prefer static methods over class methods when the function doesn't depend on the class to improve readability.
- **PEP Compliance:** Ensure static methods have the `@staticmethod` decorator to avoid PEP 8 warnings.
- **Testing:** Use class methods for setting up test fixtures or creating test instances.

By understanding and appropriately using static and class methods, you can write more organized, maintainable, and efficient Python code.

---


## 015 @abstractmethod



## Understanding Abstract Methods in Python

Abstract methods in Python are a powerful tool for ensuring consistency and proper implementation across classes. They act as blueprints that define the structure of a class, making sure that certain methods are implemented by any subclass. In this blog post, we'll explore how to create and use abstract methods effectively.

### What Are Abstract Methods?

Abstract methods are methods declared in a class with no implementation. They are defined using the `@abstractmethod` decorator from the `abc` (Abstract Base Classes) module. These methods serve as a blueprint, forcing subclasses to implement them. This ensures that any class derived from the abstract base class adheres to the defined structure.

### Step-by-Step Guide to Using Abstract Methods

1. **Import the Required Modules**

   To work with abstract methods, you need to import `ABC` and `abstractmethod` from the `abc` module.

   ```python
   from abc import ABC, abstractmethod
   ```

2. **Create an Abstract Base Class**

   Define a class that inherits from `ABC`. This class will contain your abstract methods.

   ```python
   class Phone(ABC):
       def __init__(self, model: str):
           self.model = model
           self._power = 50  # Default battery level

       @abstractmethod
       def call(self, target: str):
           pass

       @property
       @abstractmethod
       def power(self):
           pass
   ```

   - **Initialization**: The `__init__` method sets up the initial state of the object.
   - **Abstract Methods**: `call` and `power` are abstract methods that must be implemented by any subclass.

3. **Implementing Subclasses**

   Create a subclass that inherits from the abstract base class and implements all abstract methods.

   ```python
   class iBanana(Phone):
       def __init__(self, model: str):
           super().__init__(model)

       def call(self, target: str):
           return f"Calling {target} on {self.model}"

       @property
       def power(self):
           return f"Battery level: {self._power}%"
   ```

   - **Initialization**: The subclass initializes the parent class using `super().__init__`.
   - **Method Implementation**: Both `call` and `power` methods are implemented to provide specific functionality.

4. **Instantiating the Subclass**

   Once all abstract methods are implemented, you can create instances of the subclass.

   ```python
   phone = iBanana("iBanana X")
   print(phone.call("John Doe"))  # Output: Calling John Doe on iBanana X
   print(phone.power)  # Output: Battery level: 50%
   ```

5. **Handling Missing Implementations**

   If a subclass does not implement all abstract methods, attempting to instantiate it will raise a `TypeError`.

   ```python
   class IncompletePhone(Phone):
       def __init__(self, model: str):
           super().__init__(model)
   ```

   Trying to create an instance of `IncompletePhone` will result in:

   ```
   TypeError: Can't instantiate abstract class IncompletePhone with abstract methods call, power
   ```

### Tips and Tricks

- **Use `pass` or `NotImplementedError`**: In abstract methods, use `pass` or raise `NotImplementedError` to indicate that the method must be implemented in subclasses.
  
  ```python
  @abstractmethod
  def some_method(self):
      raise NotImplementedError("Subclass must implement this method")
  ```

- **Organize Code**: Keep abstract base classes in separate modules or files to maintain clean code structure.

- **Avoid Instantiating Abstract Classes**: Remember that abstract base classes cannot be instantiated directly. Always create instances of subclasses that implement all abstract methods.

- **Use Property Decorators with Abstract Methods**: Abstract methods can be combined with property decorators to enforce the implementation of getters, setters, or other property-related methods.

- **Document Your Abstract Methods**: Use docstrings to provide clear documentation about what each abstract method should do. This helps developers understand the expected behavior when implementing subclasses.

### Conclusion

Abstract methods are a valuable feature in Python that helps enforce consistency and structure in your code. By defining abstract base classes, you can ensure that all subclasses implement the necessary methods, leading to more robust and maintainable code. Remember to always implement all abstract methods in your subclasses and avoid instantiating abstract classes directly.

By following the guidelines and best practices outlined in this post, you can effectively utilize abstract methods to create well-structured and consistent class hierarchies in your Python projects.

---


## 016 Protocols



## Understanding Protocols in Python: A Flexible Approach to Type Checking

### Introduction to Protocols

Protocols in Python offer a subtle yet powerful way to enforce certain structures or behaviors in classes without the need for traditional inheritance. They act as blueprints or contracts that classes can adhere to, ensuring that they possess specific methods or attributes. This approach is particularly useful for promoting loose coupling and flexibility in your code.

### Defining a Protocol

To create a protocol, you import `Protocol` from the `typing` module and define a class that inherits from it. This class outlines the required methods and attributes that any conforming class must have.

```python
from typing import Protocol

class Printable(Protocol):
    pages: int
    
    def print(self) -> None:
        pass
    
    def recycle(self) -> None:
        pass
```

### Implementing the Protocol

Classes can conform to the protocol by implementing all the required methods and attributes. They do not need to explicitly inherit from the protocol, relying instead on duck typing.

```python
class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
        
    def print(self) -> None:
        print(f"Printing book: {self.title}")
        
    def recycle(self) -> None:
        print(f"Recycling book: {self.title}")
```

### Using the Protocol for Type Checking

Functions can be annotated to accept only objects that conform to the protocol, ensuring type safety.

```python
def print_item(printable: Printable) -> None:
    printable.print()
```

### Example Usage

When passing instances of classes that conform to the protocol, everything works as expected.

```python
book = Book("Python Programming", 300)
print_item(book)  # Output: Printing book: Python Programming
```

However, if a class does not implement all required methods, the type checker will flag it, even if the code runs.

```python
class Magazine:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
        
    def print(self) -> None:
        print(f"Printing magazine: {self.title}")
```

### Extending Functionality

Classes can have additional methods beyond the protocol's requirements without causing issues.

```python
class Book:
    # ... existing methods ...
    
    def burn(self) -> None:
        print(f"Burning book: {self.title}")
```

### Advantages Over Traditional Inheritance

Protocols offer several advantages:

1. **Flexibility**: Classes can implement the protocol without inheritance, allowing for diverse implementations.
2. **Duck Typing**: Conformance is based on the presence of required methods and attributes, not inheritance.
3. **Explicit Interfaces**: Clearly define the required methods and attributes for better code clarity.

### Real-World Applications

Protocols are ideal for scenarios where multiple classes need to adhere to a common interface without sharing a base class. For example, defining a `Vehicle` protocol with methods like `start_engine` and `accelerate` allows different vehicle types to implement these methods in their own way.

### Conclusion

Protocols enhance Python's type system by enabling flexible and loose coupling of classes. They provide a way to define interfaces without strict inheritance, leveraging duck typing for conformance. This approach makes your code more adaptable and maintainable, aligning with Python's philosophy of "we are all consenting adults."

### Tips and Tricks

- **Use Protocols for Interfaces**: Define protocols to specify required methods and attributes for classes without enforcing inheritance.
- **Leverage Duck Typing**: Rely on the presence of required methods rather than strict type checks for more flexibility.
- **Combine with Other Type Hints**: Use protocols with unions or optional types for complex type annotations.
- **Enhance Code Readability**: Protocols make your code's expected structures and behaviors explicit, improving readability and maintainability.

By incorporating protocols into your Python code, you can write more flexible, maintainable, and type-safe programs.

---


## 017 __init__ vs __new__



## Understanding the `__new__` Dunder Method in Python

The `__new__` dunder method is one of Python's lesser-known but powerful tools. It allows developers to control the creation of new instances of a class. This method is particularly useful for implementing design patterns like the Singleton pattern or for creating class factories. In this post, we'll explore how to use the `__new__` method through practical examples.

---

### What is the `__new__` Method?

The `__new__` method is a static method that gets called before the `__init__` method. It is responsible for creating the new instance of the class. While `__init__` initializes the instance, `__new__` actually creates it. This method returns an instance of the class, and it's the first method to be called when an object is instantiated.

The signature of the `__new__` method is as follows:

```python
def __new__(cls, *args, **kwargs):
```

- `cls`: The class itself.
- `*args` and `**kwargs`: Any arguments passed to the class constructor.

---

### Implementing the Singleton Pattern

One of the most common use cases for the `__new__` method is implementing the Singleton pattern. The Singleton pattern ensures that only one instance of a class is created, no matter how many times the class is instantiated.

Here's an example of a Singleton class:

```python
class Connection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Connecting for the first time.")
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            print("Warning: A connection already exists.")
            return cls._instance

    def __init__(self):
        print("Connected to the internet.")
```

In this example:

1. The `_instance` class variable keeps track of the single instance.
2. The `__new__` method checks if an instance already exists.
   - If not, it creates a new instance and assigns it to `_instance`.
   - If an instance already exists, it returns the existing instance.
3. The `__init__` method is called every time a new instance is created or an existing one is returned.

When you run this code:

```python
conn1 = Connection()
conn2 = Connection()
print(conn1 is conn2)  # Output: True
```

Both `conn1` and `conn2` will reference the same instance.

---

### Using `__new__` as a Class Factory

Another interesting use case for the `__new__` method is to create a class factory. This allows you to return different classes based on the arguments passed to the constructor.

Here's an example of a `Vehicle` class that returns different subclasses based on the number of wheels:

```python
class Vehicle:
    def __new__(cls, wheels):
        if wheels == 2:
            return Motorbike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)

    def __init__(self, wheels):
        self.wheels = wheels
        print(f"Initializing vehicle with {wheels} wheels.")

class Motorbike:
    def __init__(self):
        print("Initializing motorbike.")

class Car:
    def __init__(self):
        print("Initializing car.")
```

In this example:

1. The `Vehicle` class's `__new__` method checks the number of wheels.
2. If the number of wheels is 2, it returns a `Motorbike` instance.
3. If the number of wheels is 4, it returns a `Car` instance.
4. For any other number of wheels, it creates a default `Vehicle` instance.

When you run this code:

```python
mb = Vehicle(2)    # Output: Initializing motorbike.
car = Vehicle(4)   # Output: Initializing car.
truck = Vehicle(6) # Output: Initializing vehicle with 6 wheels.
```

---

### Key Differences Between `__new__` and `__init__`

- `__new__` is called before `__init__`.
- `__new__` is responsible for creating the instance, while `__init__` initializes it.
- `__new__` can return an instance of a different class, while `__init__` cannot.

---

### Tips and Tricks

- **Use Cases**: The `__new__` method is particularly useful for implementing singletons, class factories, or caching mechanisms.
- **Return Value**: Always ensure that `__new__` returns an instance of the class or a subclass. If it doesn't, the `__init__` method will not be called.
- **Design Patterns**: Familiarize yourself with design patterns like Singleton, Factory, and Builder. These patterns often rely heavily on the `__new__` method.
- **Debugging**: When working with `__new__`, use the `id()` function to check if multiple instances are being created.
- **Inheritance**: Be cautious when overriding `__new__` in subclasses. Ensure that the parent class's `__new__` method is properly handled.

---

### Conclusion

The `__new__` dunder method is a powerful tool in Python that allows developers to control object creation at a low level. While it's not commonly used in everyday programming, it's essential for implementing certain design patterns and complex class behaviors. By understanding how to use `__new__`, you can write more robust and flexible classes.

---
