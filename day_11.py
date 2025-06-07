from datetime import datetime

def get_date_input(dt):
    while True:
        user_input = input(dt)
        try:
            return datetime.strptime(user_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid format. Please enter the date in YYYY-MM-DD format.")


start_date = get_date_input("Enter the first date (YYYY-MM-DD): ")
end_date = get_date_input("Enter the second date (YYYY-MM-DD): ")

days_diff = abs((end_date - start_date).days)

print(f"\n Difference between {start_date} and {end_date} is: {days_diff} day(s).")


# CODE LOGIC

'''

1. We import the "datetime" class from the built-in "datetime" module.

2. We define a function called "get_date_input(dt)" that takes a prompt message and asks the user for input inside a "while True" loop.
   - It tries to convert the input string into a date using "datetime.strptime()" with the format "YYYY-MM-DD".
   - If successful, it returns a "date" object using ".date()" method.
   - If the input is invalid (e.g., wrong format or invalid date), a "ValueError" is raised.
   - In that case, it prints an error message and re-prompts the user.

3. We call "get_date_input()" twice to get two valid dates from the user.

4. We calculate the absolute difference between the two dates using subtraction:
   - Subtracting two date objects gives a "timedelta" object.
   - We use ".days" to extract the number of days from this timedelta.
   - "abs()" is used to ensure the difference is always positive, regardless of the order of dates.

5. We display the result using an f-string which clearly shows both the dates and the number of days between them.

'''

