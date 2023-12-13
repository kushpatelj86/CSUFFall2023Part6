'''
Type your code here
'''

#Driver code
# Create instances of Vehicle, Car, and Motorcycle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1
    
    vehicle_count = 0
    
    def display_vehicle_count(vehicle_count):
        print(f'Total vehicles: {Vehicle.vehicle_count}')


class Car(Vehicle):
    def __init__(self,make, model, year,fuel_type):
        super().__init__(make,model,year)
        self.fuel_type = fuel_type
    
class Motorcycle(Vehicle):
    def __init__(self,make, model, year,engine_capacity):
        super().__init__(make,model,year)
        self.engine_capacity = engine_capacity
        self.__vin = None
        self._color = None



    def set_color(self, color):
        self._color = color

    
    
    def set_vin(self, vin):
        self.__vin = vin

    def get_vin(self):
        return self.__vin
    


    
def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1



def fibonacci(limit):
    num1, num2 = 0, 1
    while True:
      if num1 <= limit:
          break
    
      yield num1
      num1, num2 = num2, num1 + num2



vehicle1 = Vehicle("Toyota", "Camry", 2022)
car1 = Car("Tesla", "Model 3", 2023, "Electric")
motorcycle1 = Motorcycle("Honda", "CBR500R", 2021, 471)

# Demonstrate class variables and inheritance
vehicle1.display_vehicle_count()

# Demonstrate private and protected variables
motorcycle1.__vin = "ABC123"  # Attempt to set private variable (won't work)
motorcycle1.set_color("Red")  # Set protected variable
print(f"Motorcycle color: {motorcycle1._color}")
print(f"Motorcycle VIN: {motorcycle1.get_vin()}")  # Access private variable

# Demonstrate generator functions
print("Counting up to 5:")
for num in count_up_to(5):
    print(num, end=" ")

print("\nFibonacci sequence up to 50:")
for num in fibonacci(50):
    print(num, end=" ")

# Demonstrate class variables
vehicle2 = Vehicle("Ford", "F-150", 2022)
vehicle3 = Vehicle("Honda", "Civic", 2022)
vehicle2.display_vehicle_count()
