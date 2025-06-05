class Car:
    def __init__(self, model, color, passenger_capacity):
        self.model = model
        self.color = color
        self.passenger_capacity = passenger_capacity

    def display(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Passenger Capacity: {self.passenger_capacity}")


class ElectricCar(Car):
    def __init__(self, model, color, passenger_capacity, battery_capacity):
        super().__init__(model, color, passenger_capacity)
        self.battery_capacity = battery_capacity

   
    def display(self):
        super().display()  
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print("\n")


ev = ElectricCar("Tata Nexon EV", "Blue", 5, 46.08)

ev.display()


# CODE LOGIC

'''

1. We define a class named "Car" to represent standard car models and their basic characteristics.

2. Inside the "Car" class, we define the __init__() method, which is the constructor.
   - It takes three parameters: model, color, and passenger_capacity.
   - These values are assigned to instance variables using "self".

3. We then define a method called "display" in the "Car" class.
   - This method prints the basic details of the car using f-strings.
   - It displays the model, color, and passenger capacity.

4. We create a subclass called "ElectricCar" that inherits from the "Car" class.
   - This class represents electric vehicles and adds one more attribute: battery_capacity.

5. The "ElectricCar" class overrides the constructor (__init__) method.
   - It uses "super().__init__()" to call the constructor of the "Car" class to initialize shared attributes.
   - It also initializes the battery_capacity specific to electric vehicles.

6. We override the "display" method inside the "ElectricCar" class.
   - This is an example of **polymorphism** — the same method name with different behavior in the subclass.
   - It first calls "super().display()" to print common details.
   - Then it prints the battery capacity specific to the electric car.

7. We create an object of "ElectricCar" and call the "display()" method for each object.
   - Python automatically calls the correct version of "display()" based on the object type.
   - This is called **runtime polymorphism**.

8. When ev.display() is called:
   - Python executes the overridden display() method from the ElectricCar class.
   - Inside this method, super().display() is called first, which runs the Car class display() method and prints model, color & passenger capacity.
   - After that, the battery capacity is printed, completing the details of electric car.
   - Thus, the full information specific to an electric car is displayed, demonstrating how inherited and extended behaviors work together.

'''

