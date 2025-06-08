import re

email = input("Enter your email:")
pattern = r"^[A-Za-z0-9.]+@gmail\.com$"


if re.fullmatch(pattern, email):
    print("Valid")
else:
    print("Invalid")



# CODE LOGIC 

r'''

1. Import the "re" module to work with regular expressions.

2. Take the email input from the user exactly as entered (no trimming).

3. Define the regex pattern as a raw string (r'...'):
   - The "r" before the string tells Python to treat backslashes "\" literally and not as escape characters.
   - This makes writing regex easier and less error-prone because backslashes are common in regex.
   - For example, "\." in regex means a literal dot; without "r", Python might misinterpret it.

4. The pattern uses:
   - "^" at the start, which means "match from the beginning of the string".
   - "$" at the end, which means "match until the end of the string".
   - Together, ^...$ ensure the entire string matches the pattern exactly, with no extra characters before or after.
   - This is important because without these anchors, the regex could match a substring anywhere inside the input, which might validate wrong emails.

5. Inside the pattern:
   - "[A-Za-z0-9.]+" means one or more letters (uppercase or lowercase), digits, or dots.
   - "@gmail\.com" matches the exact domain "@gmail.com", where "\." means a literal dot.

6. We use "re.fullmatch()" to check if the entire input matches the pattern. 
   This is an additional safety check, ensuring the whole input fits the pattern.

7. If it matches, print "Valid", else print "Invalid".


'''
