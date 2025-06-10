def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

try:
    n = int(input("Enter a non-negative integer to calculate its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")

except ValueError:
    print("Please enter a valid integer.")

finally:
    print("Program execution completed!")


# CODE LOGIC


'''

1. We define a function called "factorial(num)" to compute the factorial of a given number recursively.
   - If the input is 0 or 1, the factorial is 1 (base case).
   - Otherwise, the function recursively multiplies the number by the factorial of (number - 1).

2. We use a try-except-finally block to handle user input and error situations gracefully.

3. In the "try" block:
   - We prompt the user to enter a non-negative integer.
   - The input is converted to an integer using "int()".
   - If the number is negative, we display a message saying factorial is not defined for negative numbers.
   - If the number is valid, we call the "factorial" function and display the result.

4. In the "except" block:
   - If the user enters something that cannot be converted to an integer (like a string), a "ValueError" occurs.
   - We catch this error and display a friendly message asking the user to enter a valid integer.

5. In the "finally" block:
   - This block is executed no matter what — whether an exception occurs or not.
   - We use it to print a closing message ("Program execution completed!") to indicate the end of the program.

This setup ensures the program handles both valid and invalid inputs safely, and always prints a final message regardless of the outcome.

'''

