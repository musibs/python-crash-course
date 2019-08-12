from car import Car

""" A real world car battery """

class Battery:
    """A Simple attempt to model a battery"""

    def __init__(self, battery_power=75):
        self.battery_power = battery_power

    def describe_battery(self):
        print(f"This car has a battery of {self.battery_power} KWh")

""" A real world Electric Car"""
class ElectricCar(Car):

    """ A simple attempt to model an electric car """
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        #self.battery_power = 75
        self.battery = Battery()

    def describe_battery(self):
        print(f"{self.name} has battery of {self.battery.battery_power} KWh")

    def fill_gas_tank(self):
        print(f"{self.name} is an electric car and it does not have a gas tank")