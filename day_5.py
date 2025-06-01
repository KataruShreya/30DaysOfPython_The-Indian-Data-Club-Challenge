def sum_avg(numbers):
    return sum(numbers)

while True:
    length = int(input("Enter the number of elements you want in the list: "))
    if length <= 0:
        print("List must contain at least one number. Please try again.")
    else:
        break

numbers = []

for i in range(length):
    element = int(input(f"Enter element {i+1}: "))
    numbers.append(element)

print(f"This is your list of numbers: {numbers}")

total = sum_avg(numbers)
average = total / len(numbers)

print(f"The sum of the list of numbers is: {total}")
print(f"The average of the list of numbers is: {average}") 



# CODE LOGIC

'''
1. We define a function sum_avg(numbers) that takes a list of numbers as input and returns the sum using built-in sum() function of Python.

2. We use a "while True:" loop to keep asking the user for a valid (positive) number of elements. 
   If the user enters a number less than or equal to 0, an error message is shown. Otherwise, we store it in length variable and break the loop.

3. We create an empty list called numbers to store the user's inputs and use a for loop with range(length) to run the loop exactly length times.
   Inside the loop, we use int(input()) again to get each number from the user, one by one.
   Each number entered by the user is added to the list using the .append() method.

4. After collecting all the numbers, we print the list using an f-string to show the user what they entered.

5. We call the sum_avg(numbers) function and store the result (sum of the list) in a variable named total
   We calculate the average by dividing total by len(numbers) and store it in the variable average.

6. Finally, we print both the sum and average using f-strings to show the results clearly.

**Note**
I chose to write the function this way (returning only the sum) to demonstrate how functions can be reused — the returned value is used both to print the total and to calculate the average outside the function.

'''
