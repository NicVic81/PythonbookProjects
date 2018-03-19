class Dog:
    """A Simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ",")
print("My dog is " + str(my_dog.age) + " years ols.")
my_dog.roll_over()

print("\nYour dog's name is " + your_dog.name.title() + ",")
print("Your dog is " + str(your_dog.age) + " years ols.")
your_dog.roll_over()


# # Exercise 9-1 Restaurant and 9-2 Three Restaurants


class Restaurant:
    """Build a restaurant with a name and type then show it opening and describe it"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """defining a method for describing the restaurant """
        print("There is a new " + self.type + " restaurant in town called " + self.name.title() + ".")

    def open_restaurant(self):
        """Letting everyone know the restaurant is open"""
        print("The " + self.type + " restaurant, " + self.name.title() + ", is now open!")


my_restaurant = Restaurant('dicks', 'cock cobbling')
your_restaurant = Restaurant("robbie's", "mustache ride")
some_restaurant = Restaurant("stinky's", 'dirty vag')

print("The name of my restaurant is " + my_restaurant.name.title() + ".")
print("I just opened a " + my_restaurant.type + " restaurant!")
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
some_restaurant.describe_restaurant()


# Exercise 9-3 Users


class User:
    """Class for building user instances"""

    def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
        self.f_name = first_name
        self.l_name = last_name
        self.u_name = user_name
        self.d_size = dick_size
        self.sex_partners = sexual_partners

    def describe_user(self):
        print("The user " + self.u_name + " entered the following information: ")
        print("First name - " + self.f_name.title())
        print("Last name - " + self.l_name.title())
        print("Dick size - " + str(self.d_size))
        print("Sexual partners - " + str(self.sex_partners))

    def greet_user(self):
        print("Hello " + self.u_name + " it is nice to see you, " + self.f_name.title() + ". Have you fucked more than "
              + str(self.sex_partners) + " people yet?")


some_user = User('nicholas', 'johnson', 'bigNdog', 9, 19)

some_user.describe_user()
some_user.greet_user()
