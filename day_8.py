class Car:
    def __init__(self, model, color, gear_type, passenger_capacity):
        self.model = model
        self.color = color
        self.gear_type = gear_type
        self.passenger_capacity = passenger_capacity

    def display(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Gear Type: {self.gear_type}")
        print(f"Passenger Capacity: {self.passenger_capacity}")
        print("\n")


ghost = Car("Rolls-Royce Ghost", "Black", "Automatic", 5)

harrier = Car("Tata Harrier", "Red", "Manual", 5)

ghost.display()
harrier.display()


# CODE LOGIC

'''

1. We define a class named "Car" to represent different car models and their characteristics.

2. Inside the class, we define the __init__() method, which acts as the constructor.
   - This method is automatically called when a new object of the class is created.
   - It takes four parameters: model, color, gear_type, and passenger_capacity.
   - These values are assigned to instance variables using self (e.g., self.model = model).

3. We then define a method called "display" inside the class.
   - This method prints out all the car attributes in a formatted way using f-strings.
   - "\n" is added to give spacing between multiple car outputs.

4. Outside the class, we create two objects:
   - "ghost" is an object of the Car class representing a Rolls-Royce Ghost with color Black, Automatic gear type, and 5 passenger seats.
   - "harrier" is another object representing a Tata Harrier with color Red, Manual gear type, and 5 passenger seats.

5. Finally, we call the "display()" method on each object (ghost.display() and harrier.display()).
   - This prints out the specifications of each car in a readable format.

'''
