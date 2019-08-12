class Dog:
    """A Simple attempt to model a Dog"""

    def __init__(self, name, age):
        """Initialize name and age of the Dog"""
        self.name = name
        self.age = age

    def sit(self):
        """"Simulate dog sitting"""
        print(f"{self.name} is currently sitting")

    def roll_over(self):
        """"Simulate dog rolling over"""
        print(f"{self.name} is rolling over")


my_dog = Dog("Jackie", 6)
your_dog = Dog("Lucie", 3)
print("My Dogs details:")
print(f"My Dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()


print("\nYour Dogs details:")
print(f"Your Dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()