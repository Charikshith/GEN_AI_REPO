

# 001 File Handling



## Mastering File Handling in Python

### Introduction to File Handling

File handling is a fundamental skill in Python programming, allowing you to interact with various file types such as text files, JSON files, and images. This guide will walk you through the essentials of file handling, ensuring you can confidently work with files in your Python projects.

### Understanding File Paths

When working with files, understanding paths is crucial. You can use either relative or absolute paths:

- **Relative Path**: This path is relative to your current working directory. For example, if your script is in the same directory as your file, you can simply use the filename.
  
- **Absolute Path**: This path specifies the exact location of the file on your system. It’s useful if the file isn’t in the same directory as your script.

**Example:**
```python
# Using a relative path
file = open("sample.txt", "r")

# Using an absolute path (Windows)
file = open("C:\\Users\\Username\\Documents\\sample.txt", "r")
```

### Opening Files in Python

Python’s `open()` function is used to open files. It requires two arguments: the file path and the mode in which to open the file.

#### Modes of File Operations

The mode determines what operations you can perform on the file:

- **'r'**: Open for reading (default mode).
- **'w'**: Open for writing, truncating the file if it already exists.
- **'a'**: Open for appending, writing to the end of the file if it exists.
- **'x'**: Create a new file for writing. If the file exists, it will throw an error.

#### Text vs. Binary Mode

Files can be opened in text or binary mode, specified by adding 't' or 'b' to the mode:

- **Text Mode ('t')**: Default mode, used for reading and writing text.
- **Binary Mode ('b')**: Used for files like images and audio, handling data in bytes.

**Example:**
```python
# Opening a text file for reading
file = open("sample.txt", "rt")

# Opening an image in binary mode
image = open("image.jpg", "rb")
```

### Tips and Tricks

- **Use Absolute Paths**: If you encounter issues with relative paths, switch to absolute paths for reliability.
- **Handle Exceptions**: Always use try-except blocks when working with files to handle potential errors gracefully.
- **Close Files Properly**: Use the `close()` method or a `with` statement to ensure files are closed after operations.
- **Best Practices**: 
  - Use `'with'` statements for automatic file handling.
  - Test file operations thoroughly to avoid data loss.
  - Consider using libraries like `pathlib` for advanced path manipulations.

By following these guidelines, you'll be well-equipped to handle various file operations in Python, enhancing your programming skills and project capabilities.

---


# 002 Reading Files



## Working with Files in Python: A Comprehensive Guide

### Introduction

Working with files is an essential part of programming, and Python provides straightforward methods to handle file operations. In this post, we’ll explore how to open, read, and manipulate files using Python. We’ll focus on using the `with` keyword, which simplifies file handling and ensures proper cleanup.

### Using the `with` Keyword

The `with` keyword is the recommended way to open files in Python. It automatically handles closing the file once you’re done, making your code cleaner and less error-prone.

```python
with open("sample.txt", "r") as text:
    # Your file operations go here
```

- **Why `with`?**  
  The `with` statement ensures that the file is properly closed after its suite finishes, even if an exception is raised within it. This is known as a context manager.

### Reading File Content

Once the file is opened, you can read its content using several methods:

#### 1. Reading the Entire File

To read the entire content of the file at once, use the `read()` method.

```python
with open("sample.txt", "r") as text:
    content = text.read()
    print(content)
```

- **Type Hint:**  
  The `read()` method returns a string. You can verify this by checking the type:

  ```python
  t: str = text.read()
  print(type(t))  # Output: <class 'str'>
  ```

#### 2. Reading a Specific Number of Characters

If you want to read a specific number of characters, you can pass an integer to the `read()` method.

```python
with open("sample.txt", "r") as text:
    first_10_chars = text.read(10)
    print(first_10_chars)
```

- **Note:**  
  If you request more characters than are available in the file, `read()` will return all available characters.

#### 3. Reading One Line at a Time

To read the file line by line, use the `readline()` method.

```python
with open("sample.txt", "r") as text:
    first_line = text.readline()
    print(first_line)
```

- **Looping Through Lines:**  
  You can call `readline()` repeatedly to read each line one by one.

  ```python
  with open("sample.txt", "r") as text:
      line1 = text.readline()
      line2 = text.readline()
      line3 = text.readline()
      print(line1)
      print(line2)
      print(line3)
  ```

#### 4. Reading All Lines into a List

To read all lines of the file into a list, use the `readlines()` method.

```python
with open("sample.txt", "r") as text:
    lines = text.readlines()
    print(lines)
```

- **Note:**  
  Each line in the list will include the newline character (`\n`) at the end.

### File Object Attributes

The file object itself contains useful information. For example, you can access the name of the file and its mode.

```python
with open("sample.txt", "r") as text:
    print(text.name)        # Output: sample.txt
    print(text.mode)        # Output: 'r'
    print(text.encoding)   # Output: 'utf-8' (default encoding)
```

### Closing the File Automatically

One of the biggest advantages of using the `with` keyword is that it automatically closes the file for you. This means you don’t need to call `text.close()` manually.

```python
# Manual file handling (not recommended)
file = open("sample.txt", "r")
content = file.read()
file.close()  # You must remember to close the file

# Recommended way using `with`
with open("sample.txt", "r") as text:
    content = text.read()
# The file is automatically closed here
```

### Tips and Tricks

1. **Use Absolute Paths:**  
   If your file is located in a different directory, use the absolute path to ensure Python can find the file.

   ```python
   with open("/path/to/your/file/sample.txt", "r") as text:
       content = text.read()
   ```

2. **Handle Errors Gracefully:**  
   Always wrap file operations in a `try-except` block to handle potential errors like `FileNotFoundError`.

   ```python
   try:
       with open("sample.txt", "r") as text:
           content = text.read()
   except FileNotFoundError:
       print("The file does not exist.")
   ```

3. **Explore File Modes:**  
   Python supports multiple file modes:
   - `r`: Open for reading (default).
   - `w`: Open for writing (truncates the file if it already exists).
   - `a`: Open for appending.
   - `x`: Open for exclusive creation.
   - `b`: Open in binary mode.
   - `t`: Open in text mode (default).
   - `+`: Open for updating (reading and writing).

   ```python
   with open("sample.txt", "rb") as text:
       content = text.read()  # Returns bytes instead of a string
   ```

4. **Be Mindful of File Sizes:**  
   Reading large files with `read()` or `readlines()` can consume a lot of memory. For large files, it’s better to process the file line by line.

5. **Use Context Managers for Other Resources:**  
   The `with` keyword isn’t limited to files. It can be used with other resources like network connections or database transactions.

By following these guidelines and best practices, you can write robust and efficient file-handling code in Python. Happy coding!

---


# 003 Writing & Creating Files



## Editing Text Files in Python: Append, Write, and Read Operations

In the previous tutorial, we explored how to read from a text file in Python. Now, let's dive into how to edit a text file by appending text or replacing it entirely. We'll also cover some advanced modes and operations to make your file handling more efficient.

### Append Mode: Adding Text to a File

When you want to add text to an existing file without overwriting its contents, you can use the **append mode** (`'a'`). However, to make it more versatile, we'll use the **read and append mode** (`'a+'`). This mode allows both reading and writing operations.

```python
with open("sample.txt", "a+") as text:
    text.write("New text added to the end of the file\n")
    text.seek(0)  # Move the cursor to the beginning of the file
    content = text.read()
    print(content)
```

- The `write()` method appends the specified text to the end of the file.
- Use `seek(0)` to move the cursor to the beginning of the file if you want to read the updated content immediately after writing.
- The `read()` method will then return the entire content of the file.

### Write Mode: Replacing Text in a File

If you want to completely replace the content of a file, you can use the **write mode** (`'w'`). To enable both reading and writing in this mode, use **read and write mode** (`'w+'`).

```python
with open("sample.txt", "w+") as text:
    text.write("This text will replace the entire content of the file")
    text.seek(0)  # Move the cursor to the beginning to read
    content = text.read()
    print(content)
```

- The `write()` method replaces the entire content of the file with the specified text.
- Use `seek(0)` to move the cursor to the beginning of the file if you want to read the updated content immediately after writing.

### Creating New Files

If you try to open a file in write or append mode and the file doesn’t exist, Python will automatically create a new file for you.

```python
with open("name.txt", "w+") as text:
    text.write("1, 2, 3, 4, 5")
    text.seek(0)
    content = text.read()
    print(content)
```

- If the file `name.txt` doesn’t exist, it will be created.
- If the file already exists, its content will be replaced with the new text.

### X Mode: Exclusive Creation of Files

The **exclusive creation mode** (`'x'`) is used to create a new file only if it doesn’t already exist. If the file exists, it raises an error.

```python
try:
    with open("name.txt", "x") as text:
        text.write("Hello, World!")
except FileExistsError:
    print("The file already exists.")
```

- Use `'x'` mode if you want to ensure that you don’t accidentally overwrite an existing file.
- If the file exists, a `FileExistsError` is raised.

### Seek(): Navigating Through the File

The `seek()` method allows you to move the cursor to a specific position in the file. This is particularly useful when you want to read the content after writing or appending.

```python
with open("sample.txt", "a+") as text:
    text.write("Appended text\n")
    text.seek(0)  # Move the cursor to the beginning
    content = text.read()
    print(content)
```

- `seek(0)` moves the cursor to the beginning of the file.
- You can specify any position to move the cursor to a specific location in the file.

### Tips and Tricks

1. **Use the `with` Statement**: Always use the `with` statement when working with files. It ensures that the file is properly closed after its suite finishes, even if an error is raised within it.

2. **Understand File Modes**:
   - `'a'`: Append mode (write only).
   - `'a+'`: Read and append mode.
   - `'w'`: Write mode (truncate the file).
   - `'w+'`: Read and write mode (truncate the file).
   - `'x'`: Create mode (raise an error if the file exists).

3. **Use `seek()` Wisely**: After writing or appending, use `seek(0)` if you want to read the content immediately.

4. **Handle Exceptions**: Always handle potential exceptions, especially when working with file operations. Use try-except blocks to manage errors like `FileExistsError`.

5. **Create Backup Files**: Before performing critical operations on important files, consider creating a backup.

By mastering these file operations, you can efficiently manage text files in your Python applications. Whether you need to append, write, or create new files, Python’s flexible file handling modes and methods make it easy to accomplish your goals.

---


#  004 Deleting Files



## How to Delete Files and Folders Using Python's OS Module

### Introduction to File Management with Python's OS Module

Managing files and folders is a common task in programming, and Python's `os` module provides powerful tools to handle these operations. In this blog post, we'll explore how to delete files and folders programmatically using Python. This can be especially useful for automating tasks and maintaining your file system efficiently.

### Deleting a Single File

To delete a single file, you can use the `os.remove()` function. This function takes the file path as an argument and deletes the file. Here's a simple example:

```python
import os

# Delete a file named "bob.txt"
os.remove("bob.txt")
```

**Note:** Be cautious when using `os.remove()`, as it permanently deletes the file without moving it to the trash. Ensure you have the necessary permissions and that the file exists before attempting to delete it.

### Checking if a File Exists Before Deleting

Before deleting a file, it's a good practice to check if it exists to avoid a `FileNotFoundError`. You can use `os.path.exists()` to verify the file's existence:

```python
import os

file_name: str = "hello.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print(f"Deleted {file_name}")
else:
    print(f"{file_name} does not exist.")
```

This code checks if `hello.txt` exists and deletes it if it does, providing a clear message either way.

### Deleting Multiple Files in a Folder

If you need to delete multiple files within a specific folder, you can combine the `os` module with a loop. Let's create a folder called `sample_folder` and delete all `.txt` files inside it:

```python
import os

# Define the folder path
folder_name: str = "sample_folder"

# Loop through all items in the folder
for file in os.listdir(folder_name):
    file_path: str = os.path.join(folder_name, file)
    
    # Check if the item is a file and has the .txt extension
    if os.path.isfile(file_path) and file.endswith(".txt"):
        try:
            os.remove(file_path)
            print(f"Deleted {file}")
        except FileNotFoundError:
            print(f"{file} not found in {folder_name}")
```

This script iterates over each item in `sample_folder`, checks if it's a `.txt` file, and deletes it if it is.

### Deleting a Folder

After deleting all files in a folder, you might want to delete the folder itself. Use `os.rmdir()` to remove an empty folder:

```python
import os

folder_name: str = "sample_folder"

try:
    os.rmdir(folder_name)
    print(f"Deleted folder: {folder_name}")
except FileNotFoundError:
    print(f"The folder {folder_name} does not exist.")
except OSError:
    print(f"The folder {folder_name} is not empty.")
```

**Note:** `os.rmdir()` will throw an error if the folder is not empty. To delete a folder with contents, you'll need to recursively delete all files and subfolders first.

### Tips and Tricks

1. **Use `os.path` Functions:** Always use `os.path` functions like `os.path.exists()`, `os.path.isfile()`, and `os.path.join()` to handle file paths correctly, especially across different operating systems.

2. **Handle Exceptions:** Use try-except blocks to handle potential errors when working with file operations. This makes your code more robust and user-friendly.

3. **Be Cautious with Absolute Paths:** When using absolute paths, double-check them to avoid accidentally deleting unintended files or folders.

4. **Test Your Code:** Before running scripts that delete files, test them in a safe environment to ensure they work as expected.

5. **Use Recursive Functions for Nested Folders:** For deleting folders with multiple subfolders and files, consider using `shutil.rmtree()` from the `shutil` module, which can handle recursive deletions.

### Conclusion

The `os` module in Python is a powerful tool for managing files and folders. By using functions like `os.remove()`, `os.rmdir()`, and `os.path.exists()`, you can automate file management tasks efficiently. Always remember to handle exceptions and test your code thoroughly to avoid unintended data loss.

---

This guide should help you get started with deleting files and folders in Python. Remember to use these functions responsibly and consider adding safety checks to prevent accidental deletions.

---


# 005 JSON



## Working with JSON in Python: A Comprehensive Guide

JSON (JavaScript Object Notation) is a lightweight, easy-to-read data interchange format that is widely used for exchanging data between servers and web applications. It is a text format that is language-independent but uses conventions familiar to programmers of the C-family of languages, such as C, C++, JavaScript, and Python. In this guide, we will explore how to work with JSON in Python, including reading and writing JSON data, and understanding its key differences from Python dictionaries.

---

### What is JSON?

JSON is a standardized format for representing structured data. It is modeled after JavaScript object notation but is language-independent. Data in JSON is structured as key-value pairs, making it easy to read and write for both humans and machines.

Here’s an example of JSON data:

```json
{
    "name": "John Doe",
    "age": 30,
    "is_student": false,
    "hobbies": ["reading", "coding", "traveling"]
}
```

As you can see, JSON data resembles a Python dictionary. However, there are a few key differences:

1. **Double Quotation Marks**: JSON requires double quotation marks for strings and keys, unlike Python, which allows single quotation marks.
2. **Boolean Values**: JSON uses lowercase `true` and `false` for boolean values, while Python uses `True` and `False`.
3. **Null Values**: JSON uses `null` to represent null values, while Python uses `None`.

---

### Reading JSON Data in Python

To work with JSON in Python, you need to use the `json` module. Let’s see how to read JSON data from a file:

#### Example: Reading JSON from a File

Suppose we have a JSON file named `sample.json` with the following content:

```json
{
    "name": "John Doe",
    "age": 30,
    "is_student": false,
    "hobbies": ["reading", "coding", "traveling"]
}
```

Here’s how you can read this JSON file in Python:

```python
import json

with open("sample.json") as file:
    content: dict = json.load(file)

print(content)
```

When you run this code, the JSON data will be parsed into a Python dictionary. The output will look like this:

```python
{'name': 'John Doe', 'age': 30, 'is_student': False, 'hobbies': ['reading', 'coding', 'traveling']}
```

Notice how the JSON `false` is converted to Python’s `False`.

---

### Writing JSON Data in Python

If you want to write Python data structures to a JSON file, you can use the `json.dump()` method. Here’s an example:

#### Example: Writing Python Data to a JSON File

```python
import json

data: dict = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "hobbies": ["reading", "coding", "traveling"]
}

with open("output.json", "w") as file:
    json.dump(data, file)
```

This will create a new file named `output.json` with the following content:

```json
{"name": "John Doe", "age": 30, "is_student": false, "hobbies": ["reading", "coding", "traveling"]}
```

---

### Tips and Tricks

1. **Use Double Quotation Marks**: Always use double quotation marks for keys and string values in JSON. Python dictionaries allow single quotation marks, but JSON does not.
2. **Validate Your JSON**: Before working with JSON data, ensure it is valid. You can use online tools like [JSONLint](https://jsonlint.com/) to validate your JSON.
3. **Handle Large JSON Files**: When working with large JSON files, consider using streaming JSON parsers to avoid memory issues.
4. **Use Dictionaries for JSON Data**: When working with JSON data in Python, treat it as a dictionary. This makes it easier to access and manipulate the data.
5. **Pretty Print JSON**: Use the `json.dumps()` method with the `indent` parameter to pretty print JSON data. For example:
   ```python
   import json

   data: dict = {"name": "John Doe", "age": 30}
   print(json.dumps(data, indent=4))
   ```
   This will output:
   ```json
   {
       "name": "John Doe",
       "age": 30
   }
   ```
6. **Include Error Handling**: Always include error handling when working with files and JSON data. For example:
   ```python
   import json

   try:
       with open("sample.json") as file:
           content: dict = json.load(file)
   except FileNotFoundError:
       print("The file does not exist.")
   except json.JSONDecodeError:
       print("Invalid JSON format.")
   ```

By following these tips, you can work more efficiently with JSON data in Python and avoid common pitfalls.

---

### Conclusion

JSON is a powerful and widely-used format for data exchange. While it resembles Python dictionaries, there are key differences, such as the use of double quotation marks and lowercase boolean values. By using the `json` module, you can easily read and write JSON data in Python. Remember to always validate your JSON and use error handling to ensure robust code.

---


# 006 Handling JSON



## Working with JSON Data in Python: A Comprehensive Guide

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. In Python, JSON data can be converted into a dictionary for easier manipulation. This guide will walk you through the process of importing JSON data, converting it into a dictionary, and vice versa.

### Importing JSON Data into Python

To work with JSON data in Python, you need to import the `json` module. This module provides methods for manipulating JSON data.

```python
import json
```

### Converting JSON Data to a Dictionary

When you open a JSON file, the data is read as a string. To convert this string into a dictionary, you can use the `json.loads()` method.

```python
with open("data.json", "r") as file:
    data: str = file.read()
    actual: dict = json.loads(data)
    print(actual) # dict type
    print(data) # String type
```

### Creating a Reusable Function

To make the process of reading JSON files reusable, you can create a function that returns the JSON data as a dictionary.

```python
def get_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: str = file.read()
        return json.loads(data)

sample_data = get_json("data.json")
print(sample_data)
```

### Converting a Dictionary to JSON

To convert a dictionary back into a JSON string, you can use the `json.dumps()` method.

```python
sample_dict: dict = {
    "name": "Elon",
    "age": 10,
    "has_mars": False
}

sample_json: str = json.dumps(sample_dict)
print(sample_json)
```

### Creating a JSON File

To create a JSON file from a dictionary, use the `json.dump()` method.

```python
sample_dict: dict = {
    "name": "Elon",
    "age": 10,
    "has_mars": False
}

with open("sample.json", "w") as file:
    json.dump(sample_dict, file)
```

### Tips and Tricks

1. **Use the Correct Methods**: 
   - Use `json.load()` when reading directly from a file.
   - Use `json.loads()` when converting a string to a dictionary.
   - Use `json.dump()` to write a dictionary to a file.
   - Use `json.dumps()` to convert a dictionary to a JSON string.

2. **Handle Different Data Types**: 
   - Python's `None` converts to JSON's `null`.
   - Python's `False` converts to JSON's `false`.

3. **Format JSON for Readability**: 
   - Use `json.dumps()` with the `indent` parameter for pretty printing.

4. **Use Helper Functions**: 
   - Create helper functions to streamline JSON operations.

By following this guide, you can efficiently work with JSON data in Python, converting between JSON and dictionaries as needed.

---


# 007 Caching JSON



```markdown
## Caching API Responses in Python Using JSON

In this blog post, we'll explore how to create a JSON cache to store API responses locally. This approach helps avoid making repeated API requests, which can be inefficient and costly. We'll walk through a sample program that demonstrates this concept in action.

### Why Cache API Responses?

Before diving into the code, let's understand why caching is important:

- **Efficiency**: Avoid unnecessary API calls, especially when the data doesn't change frequently.
- **Cost**: Many APIs are rate-limited or require payment for excessive usage.
- **Performance**: Fetching data from a local cache is much faster than making an HTTP request.

### Prerequisites

To follow along, you'll need:

- Python installed on your system
- The `requests` library (install it using `pip install requests`)
- A basic understanding of working with JSON and files in Python

### The Code

Here's the complete code that demonstrates caching API responses:

```python
import json
import requests

def fetch_data(*, update: bool = False, json_cache: str, url: str) -> dict:
    json_data = None
    
    if update:
        json_data = None  # Force update by setting json_data to None
    
    if json_data is None:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)
            print("Fetched data from local cache.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"No local cache found. Error: {e}")
            json_data = None
    
    if json_data is None:
        print("Fetching new JSON data and creating local cache.")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            json_data = response.json()
            
            with open(json_cache, 'w') as file:
                json.dump(json_data, file)
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}
    
    return json_data

if __name__ == "__main__":
    API_URL = "https://dummyjson.com/comments"
    CACHE_FILE = "comments.json"
    data: dict = fetch_data(update=False, json_cache=CACHE_FILE, url=API_URL)
    print("Data:", data)
```

### How It Works

Let's break down the code step by step:

#### 1. **Function Definition**

The `fetch_data` function is defined with keyword-only arguments for clarity and type hints for better code readability.

```python
def fetch_data(*, update: bool = False, json_cache: str, url: str) -> dict:
```

#### 2. **Initial Check**

We start by checking if we need to update the data. If `update` is `True`, we set `json_data` to `None` to force a fresh fetch.

```python
if update:
    json_data = None  # Force update by setting json_data to None
```

#### 3. **Loading from Cache**

If `json_data` is `None`, we attempt to load data from the local cache file.

```python
if json_data is None:
    try:
        with open(json_cache, 'r') as file:
            json_data = json.load(file)
        print("Fetched data from local cache.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"No local cache found. Error: {e}")
        json_data = None
```

#### 4. **Fetching New Data**

If no valid cache is found, we fetch new data from the API.

```python
if json_data is None:
    print("Fetching new JSON data and creating local cache.")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        json_data = response.json()
        
        with open(json_cache, 'w') as file:
            json.dump(json_data, file)
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
```

#### 5. **Return Data**

Finally, the function returns the fetched or cached data.

```python
return json_data
```

### Example Usage

In the `if __name__ == "__main__":` block, we demonstrate how to use the `fetch_data` function:

```python
API_URL = "https://dummyjson.com/comments"
CACHE_FILE = "comments.json"
data: dict = fetch_data(update=False, json_cache=CACHE_FILE, url=API_URL)
print("Data:", data)
```

### Output

When you run this script for the first time:

1. It will not find a local cache and will fetch data from the API.
2. It will create a `comments.json` file in your project directory.
3. It will print the fetched data.

On subsequent runs (with `update=False`):

1. It will load data from the local cache.
2. It will print the data from the cache.

If you set `update=True`, it will force a fresh fetch from the API and update the cache.

### Tips and Tricks

- **Add a Time-to-Live (TTL)**: Implement a TTL for your cache to automatically refresh it after a certain period.
- **Use Absolute File Paths**: Ensure your cache file is stored in a specific directory using absolute paths.
- **Handle Rate Limits**: Add retry logic with delays to handle rate-limited APIs.
- **Add Logging**: Include logging statements to monitor cache hits and misses.
- **Implement Rate Limiting**: Add delays between API requests to avoid overwhelming the server.

By following this approach, you can efficiently manage API requests and improve the performance of your applications.

---


# 008 Glob



## Mastering File Pattern Matching with Python's Glob Module

The `glob` module in Python is a powerful tool for file pattern matching, allowing you to search for files and directories using Unix shell-style wildcards. This guide will walk you through how to use the `glob` module effectively, covering its basic functionality, advanced features, and best practices.

### Introduction to the Glob Module

The `glob` module is part of Python's standard library, making it easy to include in your projects. To start using it, simply import the module:

```python
import glob
```

The primary function you'll use is `glob.glob()`, which returns a list of file paths that match the specified pattern.

### Basic Usage of Glob

Let's start with a simple example. Suppose you want to find a specific file named `index.js` in the current directory:

```python
import glob

print(glob.glob("index.js"))
```

This will return `['index.js']` if the file exists in your current directory, or an empty list `[]` if it doesn't.

#### Wildcard Matching with `?` and `*`

The `glob` module supports wildcard characters to match file patterns:

- `?` matches any single character.
- `*` matches any sequence of characters (including none).

For example, to find all JavaScript files that start with any two letters followed by `dex.js`:

```python
import glob

print(glob.glob("??.dex.js"))
```

This will match files like `index.dex.js` and `idex.dex.js`.

To find all JavaScript files in the current directory:

```python
import glob

print(glob.glob("*.js"))
```

This will return a list of all files ending with `.js`.

### Advanced Pattern Matching with `[]`

The `glob` module also supports character range matching using square brackets `[]`:

- `[IL]` matches any file starting with 'I' or 'L'.
- `[!IL]` matches any file that does *not* start with 'I' or 'L'.

For example:

```python
import glob

# Match files starting with I or L
print(glob.glob("[IL]*.js"))

# Match files that do NOT start with I or L
print(glob.glob("[!IL]*.js"))
```

### Recursive Search with `**`

To search through multiple directories recursively, use the `**` pattern combined with `recursive=True`:

```python
import glob

# Search for all .js files in all directories and subdirectories
js_files = glob.glob("**/*.js", recursive=True)
print(js_files)
```

This will return a list of all `.js` files in your project hierarchy.

### Using Generators for Memory Efficiency

When working with large datasets, using a generator can be more memory efficient. The `iglob()` function returns an iterator instead of a list:

```python
import glob

# Create a generator for .js files
js_generator = glob.iglob("*.js")

# Iterate through the generator
for file in js_generator:
    print(file)
```

### Tips and Tricks

1. **Test Your Patterns**: Always test your glob patterns with `glob.glob()` before using them in production code to ensure they match the expected files.

2. **Use Absolute Paths**: When searching through specific directories, use absolute paths for clarity and to avoid unexpected results.

3. **Be Cautious with Recursive Search**: Recursive searches can be slow if you have many nested directories. Consider limiting the depth or using more specific patterns.

4. **Exclude Certain Directories**: When using `**`, exclude certain directories (like `node_modules/`) to speed up your searches.

5. **Combine with Other Modules**: Combine `glob` with modules like `os` or `pathlib` for more complex file operations.

6. **Leverage Generators for Large Datasets**: Using `iglob()` can help reduce memory usage when working with large file lists.

By mastering the `glob` module, you'll be able to efficiently search for files and directories in your Python projects, making your code more flexible and powerful.

---


# 009 Pickling



## Understanding Pickling in Python: A Comprehensive Guide

### Introduction to Pickling

Pickling is a powerful feature in Python that allows you to serialize and de-serialize objects. It converts Python objects into byte streams, enabling you to save them to a file or send them over a network. This process is particularly useful when dealing with complex data structures that are not easily saved using traditional methods like JSON or text files.

### Saving Data: Beyond Text and JSON Files

Saving data in text or JSON files is straightforward for simple data types like strings or integers. For example:

```python
text = "Hello, World!"
number = 10

with open("save.txt", "w") as file:
    file.write(text + "\n")
    file.write(str(number))
```

When you read the file back:

```python
with open("save.txt", "r") as file:
    print(file.read())
```

This works well for simple data. However, when dealing with more complex objects like class instances, this approach falls short.

### Pickling Complex Objects

Consider a `Fruit` class with attributes and methods:

```python
class Fruit:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories
        
    def describe(self) -> None:
        print(f"{self.name} has {self.calories} calories.")
```

If you try to save an instance of `Fruit` using a text file, you'll only save a string representation, not the actual object. This is where pickling comes into play.

### Serializing Objects with Pickle

To pickle an object, import the `pickle` module and use `pickle.dump()`:

```python
import pickle

fruit = Fruit("Banana", 100)
fruit.calories = 150

with open("save.pickle", "wb") as file:
    pickle.dump(fruit, file)
```

This serializes the `fruit` object into a byte stream and saves it to `save.pickle`.

### Unpickling Objects

To retrieve the object, use `pickle.load()`:

```python
with open("save.pickle", "rb") as file:
    loaded_fruit = pickle.load(file)

loaded_fruit.describe()  # Output: Banana has 150 calories.
```

The object is restored with its original state, including any modifications made before pickling.

### Modifying and Saving Objects

After unpickling, you can modify the object and save it again:

```python
loaded_fruit.calories = 200
loaded_fruit.describe()  # Output: Banana has 200 calories.
```

### Security Considerations

**Disclaimer:** The `pickle` module is not secure for untrusted data. Only unpickle data from trusted sources. Unpickling untrusted data can execute arbitrary code, posing security risks.

### Tips and Tricks

1. **Use the `.pickle` Extension:** Name your pickled files with the `.pickle` extension for easy identification.
2. **Trust Only Trusted Data:** Never unpickle data from untrusted sources to avoid security risks.
3. **Leverage Pickle Protocols:** Use the `protocol` parameter in `pickle.dump()` for better compatibility and efficiency.
4. **Consider Alternatives:** For simple data, consider JSON or other formats. Use pickle for complex objects that require serialization.

By following these guidelines, you can effectively use pickling to serialize and de-serialize complex Python objects, enhancing your data persistence capabilities.

---
