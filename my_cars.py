from car import Car, ElectricCar


vw = Car("Volkswagon", "F7", "2005")
print(vw.describe_car())


tesla = ElectricCar("Tesla", "G7", "2019")
print(tesla.fill_gas_tank())