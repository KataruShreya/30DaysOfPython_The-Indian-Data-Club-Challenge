def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci numbers to generate: "))
for num in fibonacci(n):
    print(num)



# CODE LOGIC

'''

1. We define a generator function called "fibonacci(n)" to generate the first n Fibonacci numbers:
   - The generator uses the "yield" keyword to produce values one at a time instead of returning a full list.
   - This makes it memory-efficient, especially for large n.

2. Inside the function:
   - We initialize two variables: a = 0 and b = 1, which represent the first two Fibonacci numbers.
   - We then run a for loop for "n" iterations using "for i in range(n):".

3. In each iteration:
   - We use "yield a" to output the current value of 'a' to the caller.
   - Then we update the values: a takes the value of b, and b takes the value of a + b.
   - This step ensures the Fibonacci sequence is correctly generated in the next iteration.

4. Outside the function:
   - We ask the user to input how many Fibonacci numbers they want using "int(input(...))".
   - This input is stored in variable "n".

5. We call the generator function with "fibonacci(n)" inside a for loop:
   - Each time through the loop, the next Fibonacci number is generated and printed.
   - This continues until "n" numbers have been printed.

This setup efficiently generates and prints the first n Fibonacci numbers one by one without storing the entire sequence in memory.

'''
