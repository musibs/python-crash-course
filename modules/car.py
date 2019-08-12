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
