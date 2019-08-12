""" A class that models real world cars """

class Car:

    """ A simple attempt to represent a car"""
    
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        car = f"{self.name} {self.model} {self.year} {self.odometer_reading}"
        return car

    def update_odometer(self, new_odometer_reading):
        if self.odometer_reading > new_odometer_reading:
            print("Sorry, you can't roll back existig readings")
        else:
            self.odometer_reading = new_odometer_reading

    def increment_odometer_reading(self, increment_mileage):
        self.odometer_reading += increment_mileage

    def fill_gas_tank(self):
        print("Gas tank filled")

class Battery:
    """A Simple attempt to model a battery"""

    def __init__(self, battery_power=75):
        self.battery_power = battery_power

    def describe_battery(self):
        print(f"This car has a battery of {self.battery_power} KWh")

class ElectricCar(Car):

    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        #self.battery_power = 75
        self.battery = Battery()

    def describe_battery(self):
        print(f"{self.name} has battery of {self.battery.battery_power} KWh")

    def fill_gas_tank(self):
        print(f"{self.name} is an electric car and it does not have a gas tank")



audi = Car("Audi", "A4", "2015")
print(audi.describe_car())
audi.update_odometer(27_400)
print(audi.describe_car())
audi.increment_odometer_reading(100)
print(audi.describe_car())
audi.update_odometer(200)
print(audi.describe_car())
audi.fill_gas_tank()

print("\n")
tesla = ElectricCar("Tesla", "S4", "2007")
print(tesla.describe_car())
tesla.describe_battery()
tesla.fill_gas_tank()