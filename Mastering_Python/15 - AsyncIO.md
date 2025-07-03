

# 001 Getting Started




## Getting Started with Async IO in Python

In this section, we'll explore the basics of asynchronous programming in Python using the `asyncio` package. Async IO allows your program to perform multiple tasks concurrently, improving efficiency and responsiveness. Let's dive into how to get started with async IO.

### Introduction to Async IO

Traditional Python code executes one line at a time, waiting for each line to complete before moving on. This can be a problem when dealing with long-running tasks like API requests, which can block the execution of other code. Async IO solves this by enabling your program to perform other tasks while waiting for operations like network requests or I/O operations.

### Creating Asynchronous Functions

To create an asynchronous function in Python, you use the `async` keyword. Here's a simple example:

```python
async def main():
    # Asynchronous code goes here
    pass

# Run the asynchronous main function
asyncio.run(main())
```

The `asyncio.run()` function is the entry point for running asynchronous code. It takes a coroutine (an asynchronous function) and runs it.

### Understanding Coroutines

A coroutine is a function that can be paused and resumed. When you define a function with `async def`, it becomes a coroutine. Coroutines are non-blocking by nature, meaning other tasks can run while they're waiting for operations to complete.

### Fetching Data Asynchronously

Let's create a function that simulates fetching data from an API:

```python
import asyncio

async def fetch_data(data_id: int) -> dict:
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate an API request
    return {"data": data_id}
```

In this example:
- The `fetch_data` function is an async function.
- It uses `await asyncio.sleep(2)` to simulate waiting for an API response.
- The `await` keyword tells the event loop to pause this coroutine and allow other tasks to run.

### Counting Asynchronously

Let's create another async function to count numbers:

```python
async def counter() -> None:
    for i in range(10):
        await asyncio.sleep(0.5)
        print(i)
```

This function:
- Counts from 0 to 9.
- Waits 0.5 seconds between each number using `await asyncio.sleep(0.5)`.

### Running Multiple Tasks Concurrently

To run both `fetch_data` and `counter` concurrently, we can create tasks:

```python
async def main() -> None:
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(counter())

    # Wait for both tasks to complete
    data: dict = await task1
    await task2

    print("Data received:", data)

# Run the main coroutine
asyncio.run(main())
```

In this code:
- `asyncio.create_task()` schedules the coroutines to run as separate tasks.
- `await task1` waits for `fetch_data` to complete.
- `await task2` waits for `counter` to complete.

### Understanding Futures

When you create a task, it returns a `Future` object. A `Future` represents a value that will be available at some point in the future. You can await this future to get the result of the coroutine.

### Key Takeaways

- Use `async def` to define coroutines.
- Use `await` to wait for coroutines to complete.
- Use `asyncio.create_task()` to run coroutines concurrently.
- Use `asyncio.run()` as the entry point for your async program.

### Tips and Tricks

1. **Use Type Hints**: Always use type hints to make your code more readable and maintainable.
2. **Avoid Blocking Calls**: Never use blocking calls (like `time.sleep()`) in async functions. Use `asyncio.sleep()` instead.
3. **Concurrency**: Use `asyncio.gather()` to run multiple coroutines concurrently and wait for all of them to complete.
4. **Debugging**: Use `asyncio.run(debug=True)` to enable debugging mode.

By following these guidelines and examples, you can write efficient asynchronous code using Python's `asyncio` package. In the next sections of this course, we'll dive deeper into more advanced topics in async IO and asynchronous programming.


---


# 002 Tasks



## Understanding AsyncIO Tasks in Python

### Introduction to Tasks

Tasks in AsyncIO are wrappers around coroutines that schedule them to run on the event loop as soon as possible. When you create a task, it is queued and starts execution as soon as the event loop is available, allowing non-blocking execution of multiple tasks.

### Example Walkthrough

Let's revisit the example from the previous lesson, where we created a simple async program. We'll enhance it to explore tasks in more detail.

#### Fetch Data Function

```python
async def fetch_data(data_id: int) -> dict:
    print("Fetching data...")
    await asyncio.sleep(10)  # Simulating a long API request
    return {"id": data_id, "data": "Some data"}
```

#### Main Async Function

```python
async def async_main() -> None:
    task = asyncio.create_task(fetch_data(100))
    # Continue with other tasks...
    print("Doing something else...")
    await asyncio.sleep(1)
    print("Doing something else again...")
    
    data = await task
    print("Data:", data)
```

#### Running the Async Program

```python
import asyncio

async def async_main() -> None:
    # ... [previous code] ...

asyncio.run(async_main())
```

### Creating and Awaiting Tasks

To create a task, use `asyncio.create_task()`, which schedules the coroutine to run. To get the result, `await` the task:

```python
task = asyncio.create_task(fetch_data(100))
data = await task
```

### Canceling Tasks

If a task takes too long, you can cancel it:

```python
try:
    task = asyncio.create_task(fetch_data(100))
    await asyncio.sleep(2)  # Let the task run for 2 seconds
    task.cancel()
    try:
        data = await task
    except asyncio.CancelledError:
        print("Task was canceled.")
except asyncio.CancelledError:
    print("Task was already canceled.")
```

### Checking Task Status

Use `task.done()` to check if a task has completed:

```python
if task.done():
    data = task.result()
else:
    print("Data not ready yet.")
```

### Handling Task Results

Access the result safely using `task.result()` after ensuring the task is done:

```python
if task.done():
    data = task.result()
    print("Data:", data)
else:
    print("Task is not done yet.")
```

### Using Timeouts

Set a maximum wait time with `asyncio.wait_for()`:

```python
try:
    data = await asyncio.wait_for(task, timeout=5)
except asyncio.TimeoutError:
    print("Task took too long.")
```

### Tips and Tricks

- **Use `await` for Results**: Prefer `await task` over `task.result()` for asynchronous execution.
- **Handle Exceptions**: Always handle potential exceptions when dealing with tasks, especially `asyncio.CancelledError` and `TimeoutError`.
- **Check Task Status**: Use `task.done()` before accessing `task.result()` to avoid exceptions.
- **Use Timeouts Wisely**: Implement timeouts to prevent indefinite waits for long-running tasks.
- **Avoid Arbitrary Sleeps**: Instead of adding sleeps to check task status, use async functions to wait for task completion.

By following these guidelines, you can effectively manage tasks in AsyncIO, ensuring your asynchronous programs are efficient and robust.

---


# 003 Important!



## Handling Long-Running Tasks in Asyncio: Best Practices

Asyncio is a powerful library for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, and implementing network clients and servers. However, when dealing with long-running tasks, you might encounter issues where the event loop doesn't get a chance to process other tasks, leading to unexpected behavior. In this post, we'll explore how to handle such scenarios effectively.

### The Problem: Cooperative Scheduling

One of the key concepts in Asyncio is cooperative scheduling. This means that coroutines must explicitly yield control back to the event loop at certain points. If a coroutine is performing intensive computations without yielding, it can block the event loop, preventing other tasks from running.

Consider the following example where a long-running task monopolizes the event loop:

```python
import asyncio

async def long_running_task():
    for i in range(1, 1_000_000):
        print(i)
    return "Task completed"

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled")

asyncio.run(main())
```

In this example, `long_running_task` runs a loop that prints numbers from 1 to 1,000,000. The main coroutine creates this task, waits for 2 seconds, and then attempts to cancel it. However, due to the intensive loop without any `await` statements, the event loop doesn't get a chance to process the cancellation, and the task continues running beyond the intended timeout.

### The Solution: Adding Checkpoints

To address this issue, you need to introduce checkpoints within the long-running task. These checkpoints are points where the coroutine yields control back to the event loop, allowing other tasks to run. A common way to do this is by using `asyncio.sleep()` with a short duration.

Here's how you can modify the long-running task to include checkpoints:

```python
import asyncio

async def long_running_task():
    for i in range(1, 1_000_000):
        print(i)
        if i % 10_000 == 0:  # Checkpoint every 10,000 iterations
            await asyncio.sleep(0.01)  # Yield control back to the event loop
    return "Task completed"

async def main():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(2)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled")

asyncio.run(main())
```

In this modified version, the loop checks every 10,000 iterations whether it's time to yield control. By awaiting `asyncio.sleep(0.01)`, the coroutine gives the event loop an opportunity to process other tasks, such as handling the cancellation request.

### Explanation

- **Checkpoint Placement**: The checkpoint is placed inside the loop to ensure that the coroutine yields control periodically. The frequency of these checkpoints depends on the nature of the task. In this example, we yield every 10,000 iterations, but you can adjust this based on your specific requirements.

- **Short Sleep Duration**: The `asyncio.sleep(0.01)` is a short delay that allows the event loop to process other tasks without significantly impacting the performance of the long-running task.

- **Cancellation Handling**: When the main coroutine cancels the task after 2 seconds, the cancellation request is processed during one of the checkpoint yields. This ensures that the task is cancelled gracefully.

### Tips and Tricks

1. **Balance Between Yielding and Performance**: Too frequent yielding can impact the performance of your long-running task. Find a balance by determining the optimal frequency of checkpoints based on your task's requirements.

2. **Use `asyncio.sleep(0)` for Cooperative Yielding**: If you want to yield control without introducing a delay, you can use `asyncio.sleep(0)`. This allows the event loop to process other tasks immediately.

3. **Handle Cancellation Gracefully**: Always wrap your tasks in a try-except block to catch `asyncio.CancelledError` and perform any necessary cleanup operations.

4. **Avoid Blocking Calls**: Never use blocking calls (e.g., `time.sleep()`) within coroutines. Always use `asyncio.sleep()` to yield control back to the event loop.

5. **Test Thoroughly**: Test your implementation with different checkpoint frequencies and task durations to ensure that the cancellation works as expected under various conditions.

By incorporating these best practices into your Asyncio code, you can ensure that long-running tasks cooperate with the event loop, allowing for proper task cancellation and maintaining the responsiveness of your application.

### Final Thoughts

Handling long-running tasks in Asyncio requires careful consideration of cooperative scheduling. By introducing checkpoints within your tasks, you can ensure that the event loop has opportunities to process other tasks, including cancellation requests. This approach not only makes your code more robust but also improves the overall responsiveness of your application. Remember to balance performance with yielding and always handle cancellations gracefully to write efficient and reliable Asyncio code.

---


# 004 Gather



## Running Multiple Async Tasks with `asyncio.gather()`

In the previous tutorial, we explored how to create and run a single asynchronous task using Python's `asyncio` library. Now, let's take it a step further by learning how to run multiple tasks concurrently. This approach not only improves efficiency but also allows us to fetch data from multiple sources simultaneously.

### Introduction to `asyncio.gather()`

The `asyncio.gather()` function is a powerful tool that enables us to run multiple coroutines at the same time. Instead of waiting for one task to complete before starting another, we can execute them all asynchronously, significantly speeding up our program.

### Creating Multiple Tasks

Let's consider an example where we have a function `fetch_data` that asynchronously fetches data and returns it as a dictionary. We want to fetch data for multiple values simultaneously.

```python
import asyncio

async def fetch_data(value: int) -> dict:
    # Simulating an asynchronous data fetch
    await asyncio.sleep(1)
    return {"data": value}

async def main() -> None:
    # Creating multiple tasks using asyncio.gather()
    tasks = [
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    ]
    
    # Waiting for all tasks to complete
    results = await asyncio.gather(*tasks)
    
    # Printing the results
    print("Results:", results)

# Running the main coroutine
asyncio.run(main())
```

### Handling Exceptions

One of the challenges when dealing with multiple asynchronous tasks is handling exceptions. If one of the tasks raises an error, it can cause the entire program to fail. Let's modify our example to include error handling.

```python
import asyncio

async def fetch_data(value: int, return_exception: bool = False) -> dict:
    if value == 0:
        error = Exception("No data found")
        if return_exception:
            return {"exception": error}
        else:
            raise error
    await asyncio.sleep(1)
    return {"data": value}

async def main() -> None:
    tasks = [
        fetch_data(1),
        fetch_data(2),
        fetch_data(0, return_exception=True)
    ]
    
    try:
        results = await asyncio.gather(*tasks)
        print("Results:", results)
    except Exception as e:
        print("An error occurred:", str(e))

asyncio.run(main())
```

### Best Practices and Tips

1. **Use `return_exceptions=True`**:
   - By setting `return_exceptions=True` in `asyncio.gather()`, exceptions are returned as part of the results list instead of raising them. This allows you to handle errors gracefully without stopping the execution of other tasks.

2. **Limit Concurrency**:
   - While running multiple tasks concurrently is beneficial, too many tasks can overwhelm the system. Consider limiting the number of concurrent tasks based on your system's capacity.

3. **Handle Errors Appropriately**:
   - Always include error handling in your coroutines. This ensures that if one task fails, it doesn't crash the entire program.

4. **Monitor Task Progress**:
   - For long-running tasks, consider adding progress monitoring to keep track of how much time each task takes.

### Tips and Tricks

- **Use `asyncio.gather()` with Caution**:
  - While `asyncio.gather()` is a powerful tool, it can be resource-intensive if not used judiciously. Always test your code with different loads to ensure it scales well.

- **Leverage `async for`**:
  - If you're dealing with a large number of tasks, consider using `async for` to iterate over them as they complete. This can provide better control over the flow of your program.

- **Avoid Mixing CPU-Bound Tasks**:
  - Asyncio is most effective for I/O-bound tasks. For CPU-bound tasks, consider using `concurrent.futures.ProcessPoolExecutor` alongside asyncio.

By following these guidelines and examples, you can effectively run multiple asynchronous tasks using `asyncio.gather()`, making your programs more efficient and responsive. Remember to always handle exceptions properly and monitor the performance of your tasks to ensure optimal results.

---


# 005 Sleep



## Mastering asyncio.sleep() in Python: Usage and Benefits

Asyncio is a powerful library in Python that allows developers to write single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, and implementing network clients and servers. One of the most versatile and frequently used functions in asyncio is `asyncio.sleep()`. In this blog post, we will explore two primary use cases of `asyncio.sleep()`: blocking your program for a specific duration and triggering the start of new tasks.

---

### Blocking Your Program with asyncio.sleep()

The most straightforward use of `asyncio.sleep()` is to pause the execution of your program for a specified number of seconds. This can be particularly useful when you want to simulate delays, such as waiting for an API response or adding a cooldown between repeated actions.

Here’s an example of how you can use `asyncio.sleep()` to block your program:

```python
import asyncio

async def main() -> None:
    print("Started")
    await asyncio.sleep(1)  # Sleep for 1 second
    print("Finished")

asyncio.run(main())
```

In this code:
- The `main()` coroutine starts by printing "Started".
- It then awaits `asyncio.sleep(1)`, which pauses execution for 1 second.
- After the sleep duration, it prints "Finished".

When you run this program, you’ll see "Started" immediately, followed by "Finished" after a 1-second delay.

---

### Returning a Result from asyncio.sleep()

One lesser-known feature of `asyncio.sleep()` is its ability to return a result when the sleep duration is over. This can be useful for mocking data or creating dummy results without writing additional code.

Here’s how you can use this feature:

```python
import asyncio

async def main() -> None:
    print("Started")
    result = await asyncio.sleep(1, result={"item": "one", "two": 2, "three": 3})
    print(f"Result: {result}")

asyncio.run(main())
```

In this code:
- The `asyncio.sleep()` function is called with two arguments: `1` (the delay in seconds) and `result` (the value to return after the delay).
- The result is then printed to the console.

When you run this program, it will output:
```
Started
Result: {'item': 'one', 'two': 2, 'three': 3}
```

This feature is particularly handy for testing or when you need to simulate asynchronous operations that return data.

---

### Triggering New Tasks with asyncio.sleep()

Another important use of `asyncio.sleep()` is to give the event loop an opportunity to start new tasks. In asyncio, if one coroutine is running an intensive task, it can block other coroutines from executing until it completes. By using `asyncio.sleep()`, you can create a small break in the execution, allowing the event loop to switch contexts and start other tasks.

Here’s an example that demonstrates this:

```python
import asyncio

async def counter() -> None:
    for i in range(1000000000):
        pass  # Simulating a long-running task

async def main() -> None:
    task = asyncio.create_task(counter())
    await asyncio.sleep(0)  # Give the event loop a chance to start the task
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")

asyncio.run(main())
```

In this code:
- The `counter()` coroutine simulates a long-running task.
- In `main()`, we create a task for `counter()` and then call `await asyncio.sleep(0)`.
- The `sleep(0)` allows the event loop to start the `counter()` task.
- We then cancel the task and handle the `asyncio.CancelledError`.

The key takeaway here is that `asyncio.sleep(0)` doesn’t actually pause the program but instead yields control back to the event loop, allowing other tasks to run.

---

### Tips and Tricks

1. **Use asyncio.sleep(0) for Cooperative Scheduling**:
   - When you have a long-running task, use `await asyncio.sleep(0)` to give the event loop a chance to run other tasks. This is essential for maintaining concurrency in your program.

2. **Avoid Busy-Waiting**:
   - Never use a busy loop (e.g., `while True: pass`) to wait for something. Instead, use `asyncio.sleep()` to yield control back to the event loop.

3. **Return Mock Data**:
   - Use the `result` parameter of `asyncio.sleep()` to return mock data for testing or prototyping purposes.

4. **Use async/await Consistently**:
   - Always use `await` when calling `asyncio.sleep()` to ensure your coroutines are properly suspended and resumed.

5. **Don’t Overuse asyncio.sleep()**:
   - While `asyncio.sleep()` is a useful tool, overusing it can lead to inefficiencies. Only use it when necessary and prefer other asyncio primitives (e.g., `asyncio.Event`, `asyncio.Condition`) for more complex synchronization tasks.

---

### Conclusion

`asyncio.sleep()` is a versatile and essential tool in your asyncio toolkit. It can be used to pause execution, return mock data, and create opportunities for the event loop to run other tasks. By mastering the use of `asyncio.sleep()`, you can write more efficient and cooperative asynchronous code.

If you have any questions or need further clarification on using `asyncio.sleep()`, feel free to ask in the comments! Happy coding!

---
