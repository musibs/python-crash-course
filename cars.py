cars=['bmw', 'audi', 'tata' ,'suzuki']
print(f"List of cars: {cars}")
#cars.sort()
print(f"Temp sorted list of cars: {sorted(cars)}")
print(f"List of cars: {cars}")

cars.sort(reverse=True)
print(f"Reverse sorted list of cars: {cars}")
cars.reverse()
print(f"List of cars: {cars}")

print(f"Number of cars : {len(cars)}")

for car in cars:
    print(car)

for car in cars:
    print(f"{car.title()} is an awesone car. Try it.")

