n = int(input("Enter a number: "))

count = 0

for i in range(1,n+1):     
    if n%i==0:             
        count = count + 1

if count==2:
    print(f"Awesome! {n} is a prime number — only divisible by 1 and itself.")
else:
    print(f"Oops! {n} is not a prime number! It has more than two divisors.") 


# CODE LOGIC

''' 
1. Using int(input()), we ask the user to enter a number and convert the input to an integer and store it in the variable n.

2. We create a variable 'count' and set it to 0 to track how many numbers can divide n without leaving a remainder.

3. We use a for loop with range(1, n + 1) to check every number from 1 up to n. 
   We use n + 1 because the range() function does not include the stop value. So to include it, we use n+1.

4. Inside the loop, we check if n % i == 0. This means we are checking if n is divisible by i without a remainder. 
   If true, we increase count by 1.

5. After the loop, we check if count == 2.
   A prime number is only divisible by 1 and itself — that is exactly 2 divisors.
   If count is 2, it's a prime number. If not, it means that it has more than 2 divisors, so it is not prime.

'''
