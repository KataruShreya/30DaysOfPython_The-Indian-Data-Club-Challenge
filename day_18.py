class SimpleMeta(type):
    def __new__(cls, name, bases, dct):
        bad_methods = []

        for key, value in dct.items():
            if key.startswith('__'):
                continue
            if not callable(value):
                continue                

            if key != key.lower():
                print(f"{key} : not in lowercase form!")
                bad_methods.append(key)
            else:
                print(f"{key} : all good!")

        if bad_methods:                 
            raise TypeError(f"Bad method names: {bad_methods}\nUse only lowercase for naming the methods!")

        return super().__new__(cls, name, bases, dct)



class greet(metaclass=SimpleMeta):
    intro = "Hey! I am learning Metaclasses today!"

    def Hello(self):
        print("Hi")

    def show(self):
        print("Bye!")



# CODE LOGIC

'''

1. We define a metaclass named "SimpleMeta" that inherits from Python's built-in "type".
   - This metaclass is used to enforce a naming convention for methods in any class that uses it.

2. Inside the "__new__" method of the metaclass:
   - We loop through the dictionary "dct" which contains all attributes and methods of the class being created.
   - For each key-value pair:
       a. We skip any special Python-defined attributes (like __init__, __module__) using "key.startswith('__')".
       b. We skip constants/variables using "not callable(value)" because the rule applies only to methods.
       c. If the method name is not lowercase (i.e., key != key.lower()), we add it to a list called "bad_methods".
       d. If it is lowercase, we print a message saying the method is good.

3. After checking all attributes:
   - If the "bad_methods" list is not empty, we raise a TypeError with a message showing which methods failed the naming rule.
   - This prevents the class from being created until the naming issue is fixed.

4. Finally, if all method names are valid (i.e., lowercase), we proceed to create the class using the parent "__new__" method.

5. We then create a sample class "greet" using this metaclass:
   - It has a variable "intro" (which is ignored in the check).
   - It has a method "Hello" which violates the lowercase rule.
   - It has a method "show" which follows the lowercase rule.
   - Because "Hello" is invalid, the class creation fails and a TypeError is raised.

'''