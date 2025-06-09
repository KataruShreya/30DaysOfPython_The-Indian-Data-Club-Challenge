from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        print(f"Inserted '{val}' in the stack")
        
    def pop(self):
        if self.is_empty():
            print("Cannot delete. The stack is already empty.")
        else:
            print(f"Deleted '{self.container.pop()}' from the stack")
    
    def peek(self):
        if self.is_empty():
            print("Cannot peek. The stack is empty.")
        else:
            print(f"The topmost element of the stack is '{self.container[-1]}'")
    
    def is_empty(self):
        return len(self.container)==0
    
    
st = Stack()

print("Choose an operation:")
print("1: Insert")
print("2: Delete")
print("3: Peek")
print("4: Check if stack is empty")
print("5: Exit")

while True:
    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        val = input("Enter the value to insert: ")
        st.push(val)
    elif choice == '2':
        st.pop()
    elif choice == '3':
        st.peek()
    elif choice == '4':
        print("Is stack empty?", st.is_empty())
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

# CODE LOGIC

'''

1. We import "deque" from the built-in "collections" module.
   - A deque (double-ended queue) allows efficient and fast stack operations like push and pop.

2. We define a class named "Stack" to simulate the behavior of a stack using deque.
   - Inside the constructor (__init__), we initialize an empty deque called "container".

3. The "push(val)" method:
   - Takes a value as input and adds it to the top of the stack using the "append()" method.
   - Prints a message confirming the insertion.

4. The "pop()" method:
   - First checks if the stack is empty using the "is_empty()" method.
   - If not empty, removes the top element using "pop()" and prints a confirmation.
   - If already empty, prints a warning message saying deletion is not possible.

5. The "peek()" method:
   - Checks the top element of the stack without removing it.
   - If the stack is empty, prints a message stating that the stack is empty.

6. The "is_empty()" method:
   - Returns True if the stack has no elements, otherwise returns False.

7. After defining the class, we create a "Stack" object called "st".

8. We then display a menu to the user with options to:
   - Insert (push) an element
   - Delete (pop) the top element
   - Peek at the top element
   - Check if the stack is empty
   - Exit the program

9. A loop is used to continuously ask for the user’s choice:
   - Based on input, it calls the corresponding method (push, pop, peek, is_empty).
   - If the user enters 5, the loop breaks and the program exits.
   - Handles invalid input by prompting the user again.

This interactive setup allows users to experiment with stack operations in real time and understand the stack behavior more clearly.

'''


# ***Note***:

'''
We can also use lists to define stack data structure as written below but it is not efficient.
a list is cosidered as a dynamic array and When it grows beyond its current capacity, it needs to:
  - Allocate new memory,
  - Copy all existing elements to the new memory block,
  - And then append the new element.
This process might be costly and thus is not suggested.

st = []

def insert(val):
    st.append(val)
    print("Inserted:", val)

def delete():
    if is_empty():
        print("Stack is empty. Cannot delete.")
    else:
        print("Deleted:", st.pop())

def peek():
    if is_empty():
        print("Stack is empty. No top element.")
    else:
        print("Top element is:", st[-1])

def is_empty():
    return len(st) == 0

print("User choices:\n1. Insert\n2. Delete\n3. View top element\n4. Check if empty\n5. Exit")

while True: 
    try:
        choice = int(input("\nEnter your choice (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        val = input("Enter element to insert: ")
        insert(val)
    elif choice == 2:
        delete()
    elif choice == 3:
        peek()
    elif choice == 4:
        print("Is stack empty?", is_empty())
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Enter a valid choice (1-5).")

'''

