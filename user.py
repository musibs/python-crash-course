class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old")


somnath = User("Somnath", "Musib", 28)
jack = User("Jack", "Doe", 19)

somnath.describe_user()
jack.describe_user()