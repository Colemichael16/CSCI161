# Cole McLean CSCI 161 THURSDAY LAB

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def set_info(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


car_list = [
    Car("Toyota", "Camry", 2020),
    Car("Honda", "Civic", 2019),
    Car("Ford", "Fusion", 2018)
]

print("Car Information:")
for car in car_list:
    car.print_info()

car_list[0].set_info("Tesla", "Model S", 2022)

print("\nCar Information after modification:")
for car in car_list:
    car.print_info()
