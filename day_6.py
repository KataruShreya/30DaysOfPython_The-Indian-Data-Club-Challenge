import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

mandatory_chars = [
    random.choice(letters),
    random.choice(digits),
    random.choice(symbols)
]

all_chars = letters + digits + symbols
remaining_chars = random.choices(all_chars, k=5)

password_list = mandatory_chars + remaining_chars
random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your password is: {password}")



#CODE LOGIC

'''

1. We import the random and string modules.
   - The "random" module helps us generate random values.
   - The "string" module provides access to character sets like letters, digits, and punctuation.

2. We use "string.ascii_letters" to get a string containing all uppercase and lowercase English letters and store it in a variable named "letters".

3. We use "string.digits" to get a string containing digits from 0 to 9 and store it in a variable named "digits".

4. We use "string.punctuation" to get a string containing all punctuation symbols like @, #, $, etc., and store it in a variable named "symbols".

5. We ensure the password has at least one letter, one digit, and one symbol by selecting one character from each set using "random.choice"
   We store these characters in a list called "mandatory_chars".

6. We combine all characters into a single pool using string addition and store it in "all_chars".

7. We use "random.choices(all_chars, k=5)" to select 5 more characters randomly from the full character set to make the total password length 8. 
   These are stored in "remaining_chars".

8. We combine "mandatory_chars" and "remaining_chars" into a single list named "password_list".

9. We shuffle "password_list" using "random.shuffle()" to avoid placing the required characters in fixed positions.

10. We use ''.join(...) to convert the character list into a string and store it in the variable "password".

11. Finally, we print the generated password using an f-string.

'''

# ***Note!***

'''

You can also reuse this logic as a custom module.
For example, put the password generation code in a separate file, say password.py, and access it in another file, say code.py like this:

# password.py

import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

mandatory_chars = [
    random.choice(letters),
    random.choice(digits),
    random.choice(symbols)
]

all_chars = letters + digits + symbols
remaining_chars = random.choices(all_chars, k=5)
password_list = mandatory_chars + remaining_chars
random.shuffle(password_list)

password = ''.join(password_list)

# code.py

import password as ps
print(f"Your password is: {ps.password}")

'''
