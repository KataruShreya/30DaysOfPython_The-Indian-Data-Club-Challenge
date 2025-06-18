import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--value", type=float, help="Temperature value")
parser.add_argument("--unit", choices=["c2f", "f2c"], help="Conversion type")

args = parser.parse_args()

if args.unit == "c2f":
    result = (args.value * 9/5) + 32
    print(f"{args.value}°C = {result:.2f}°F")
else:
    result = (args.value - 32) * 5/9
    print(f"{args.value}°F = {result:.2f}°C")



# CODE LOGIC


'''

1. We import the argparse library:
   - argparse allows us to create command-line interfaces in Python.
   - It helps in reading user input when the script is run from the terminal.

2. We create an ArgumentParser object:
   - This sets up the structure for our command-line interface.
   - We'll use it to define what inputs the script expects.

3. We add two optional arguments using add_argument():
   a. --value: Takes a float input representing the temperature value.
   b. --unit: Accepts either 'c2f' (Celsius to Fahrenheit) or 'f2c' (Fahrenheit to Celsius).

4. We parse the command-line arguments using parser.parse_args():
   - This reads the values entered by the user when they run the script.

5. We check which conversion the user wants using an if-else condition:
   - If unit is 'c2f', we use the formula: (value * 9/5) + 32 to convert to Fahrenheit.
   - Else, we assume 'f2c', and apply the formula: (value - 32) * 5/9 to convert to Celsius.

6. We print the result in a readable format using f-strings:
   - It shows the original value along with the converted temperature.

7. Result:
   - The user gets a quick and clean temperature conversion right from their terminal.
   - Example usage: python temp_converter.py --value 100 --unit c2f

'''
