from car import Car

my_new_car = Car("Audi", "A5", "2019")
print(my_new_car.describe_car())
my_new_car.update_odometer(100)
print(my_new_car.describe_car())
my_new_car.fill_gas_tank()