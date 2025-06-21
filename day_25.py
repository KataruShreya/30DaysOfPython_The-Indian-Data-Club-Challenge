from pydantic import BaseModel, EmailStr, ValidationError, validator

class UserProfile(BaseModel):
    name: str
    email: EmailStr
    age: int

    @validator('name')
    def name_must_be_alpha(cls, value):
        if any(char.isdigit() for char in value):
            raise ValueError('Name must not contain numbers')
        return value

    @validator('age')
    def check_age_range(cls, value):
        if value < 18 or value > 100:
            raise ValueError('Age must be between 18 and 100')
        return value

# Get user input
name = input("Enter your name: ")
email = input("Enter your email: ")
age = input("Enter your age: ")

try:
    user = UserProfile(
        name=name,
        email=email,
        age=int(age)
    )
    print("\nUser profile created successfully!")
    print(user.json(indent=2))
    print("\n")

except ValidationError as e:
    print("\nValidation error:")
    print(e)




# CODE LOGIC

'''

1. We import necessary modules from pydantic:
   - BaseModel: The base class for defining data models.
   - EmailStr: A special type to validate that the input is a valid email address.
   - ValidationError: Used to handle validation errors gracefully.
   - validator: A decorator to define custom validation logic for specific fields.

2. We define a class called UserProfile that inherits from BaseModel:
   - It has three fields: name (string), email (validated email), and age (integer).
   - This class automatically performs data validation on creation.

3. We define a custom validator for the 'age' field using @validator:
   - The method 'check_age_range' checks if age is between 18 and 100.
   - If not, it raises a ValueError with a custom message.

4. We define an additional validator for the 'name' field:
    - The method 'name_must_be_alpha' checks if the name contains any digits.
    - If a number is found in the input string, a ValueError is raised.
    - This ensures that names like "Alice123" or "John9" are rejected.

5. We prompt the user to input their name, email, and age:
   - Input is taken using the input() function from the console.

6. We attempt to create an instance of UserProfile using the input values:
   - The age input is explicitly converted to an integer.
   - If all inputs are valid, the object is created successfully.

7. If valid:
   - A success message is printed.
   - The user profile is displayed in JSON format using user.json().

8. If validation fails:
   - The error is caught in the except block and printed to the user.

9. Result:
   - A clean, validated, and structured user profile is created and displayed, ensuring all fields meet their criteria.

'''
