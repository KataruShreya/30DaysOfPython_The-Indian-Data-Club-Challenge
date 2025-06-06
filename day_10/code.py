try:
    with open("data.txt") as f:
        for line in f:
            line = line.strip()

            try:
                num = int(line)
                print(f"Number: {num}")
            except ValueError:
                print(f"Invalid number: {line}")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("No permission to read the file.")

finally:
    print("End of the program")



# CODE LOGIC

'''

1. We use a try-except block to attempt opening a file named "data.txt".

2. Inside the try block, we use a with statement to open the file.
   - The with statement ensures the file is automatically closed after reading.
   - The file is opened in read mode.

3. We loop over each line in the file using a for loop.
   - Each line includes a trailing newline character "\n" by default.
   - To clean this up, we call "line.strip()" to remove any leading/trailing whitespace, including spaces, tabs, and newlines.

4. After stripping, we use a nested try-except block to convert the cleaned line which is by default a string, to an integer using "int(line)".
   - If the line contains valid numeric data (e.g., "45"), it's converted to an integer and printed.
   - If the line is not a valid number (e.g., contains letters, symbols, or is empty after stripping), a ValueError is raised.

5. If ValueError occurs, it means the line could not be converted to an integer.
   - In that case, we print a message saying the line is invalid.

6. If the file does not exist:
   - A FileNotFoundError is caught, and an appropriate message is printed.

7. If we do not have permission to read the file:
   - A PermissionError is caught, and a corresponding message is shown.

We include a finally block at the end.
   - The code inside this block will **always execute**, whether an exception was raised or not.
   - It's typically used for cleanup tasks or displaying a final message.
   - In this case, it simply prints: "End of the program".

8. This structure ensures:
   - Valid numbers are printed.
   - Invalid or corrupted data is gracefully handled.
   - File-related issues do not crash the program and are reported clearly.
   - A final message is printed to confirm the end of execution regardless of success or failure.

'''
