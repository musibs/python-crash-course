class Restaurant:

    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.restaurant_type} restaurant and it serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant is open")


restaurant = Restaurant("Indian", "Vegeterian Foods")

restaurant.describe_restaurant()
restaurant.open_restaurant()