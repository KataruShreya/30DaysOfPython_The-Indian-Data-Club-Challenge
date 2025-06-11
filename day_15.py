import time

def time_to():
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Execution time: {end - start:.4f} seconds")
            return result
        return wrapper
    return decorator

@time_to()
def exec_time():
    for i in range(1, 1000):
        print(i)

exec_time()


# CODE LOGIC

'''

1. We import the "time" module to measure how long a function takes to execute.

2. We define a function "time_to()" which acts as a decorator factory:
   - This is useful if we want to extend the decorator later to take arguments.
   - For now, it simply returns the actual decorator function.

3. Inside "time_to()", we define the actual decorator function "decorator(func)":
   - It accepts the original function to be decorated as an argument.
   - This decorator wraps the original function to modify its behavior.

4. Inside "decorator(func)", we define a "wrapper(*args, **kwargs)" function:
   - This allows the decorated function to accept any number of positional or keyword arguments.
   - Before calling the original function, we record the start time using "time.time()".
   - We then call the original function and store its result.
   - After the function completes, we record the end time.
   - The difference between end and start gives us the execution time.
   - We print the execution time to 4 decimal places.
   - Finally, we return the result of the original function to preserve its behavior.

5. The "wrapper" is returned from the "decorator" to replace the original function with the enhanced version.

6. The "decorator" is returned from the "time_to()" function so it can be used with the @ syntax.

7. We define a function "exec_time()" that prints numbers from 1 to 999 using a for loop.
   - This simulates a time-consuming task.

8. We apply the "@time_to()" decorator to "exec_time", so when it's called, it also prints how long it took to run.

9. Finally, we call "exec_time()" to see both the output and the execution time.

This setup allows you to measure how long any function takes to execute without modifying the function's original logic.'

'''