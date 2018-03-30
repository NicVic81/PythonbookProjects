# class Dog:
#     """A Simple attempt to model a dog."""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """Simulate a dog rolling over in response to a command"""
#         print(self.name.title() + " rolled over!")
#
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
#
# print("My dog's name is " + my_dog.name.title() + ",")
# print("My dog is " + str(my_dog.age) + " years ols.")
# my_dog.roll_over()
#
# print("\nYour dog's name is " + your_dog.name.title() + ",")
# print("Your dog is " + str(your_dog.age) + " years ols.")
# your_dog.roll_over()
#

# # Exercise 9-1 Restaurant and 9-2 Three Restaurants

#
# class Restaurant:
#     """Build a restaurant with a name and type then show it opening and describe it"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#
#     def describe_restaurant(self):
#         """defining a method for describing the restaurant """
#         print("There is a new " + self.type + " restaurant in town called " + self.name.title() + ".")
#
#     def open_restaurant(self):
#         """Letting everyone know the restaurant is open"""
#         print("The " + self.type + " restaurant, " + self.name.title() + ", is now open!")
#
#
# my_restaurant = Restaurant('dicks', 'cock cobbling')
# your_restaurant = Restaurant("robbie's", "mustache ride")
# some_restaurant = Restaurant("stinky's", 'dirty vag')
#
# print("The name of my restaurant is " + my_restaurant.name.title() + ".")
# print("I just opened a " + my_restaurant.type + " restaurant!")
# my_restaurant.open_restaurant()
# my_restaurant.describe_restaurant()
# your_restaurant.describe_restaurant()
# some_restaurant.describe_restaurant()


# Exercise 9-3 Users
#
#
# class User:
#     """Class for building user instances"""
#
#     def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.u_name = user_name
#         self.d_size = dick_size
#         self.sex_partners = sexual_partners
#
#     def describe_user(self):
#         print("The user " + self.u_name + " entered the following information: ")
#         print("First name - " + self.f_name.title())
#         print("Last name - " + self.l_name.title())
#         print("Dick size - " + str(self.d_size))
#         print("Sexual partners - " + str(self.sex_partners))
#
#     def greet_user(self):
#         print("Hello " + self.u_name + " it is nice to see you, " + self.f_name.title()
#               + ". Have you fucked more than " + str(self.sex_partners) + " people yet?")
#
#
# some_user = User('nicholas', 'johnson', 'bigNdog', 9, 19)
#
# some_user.describe_user()
# some_user.greet_user()

# Exercise 9-4 Number Served
#
# class Restaurant:
#     """Build a restaurant with a name and type then show it opening and describe it"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         """defining a method for describing the restaurant """
#         print("There is a new " + self.type + " restaurant in town called " + self.name.title() + ".")
#
#     def open_restaurant(self):
#         """Letting everyone know the restaurant is open"""
#         print("The " + self.type + " restaurant, " + self.name.title() + ", is now open!")
#
#     def set_number_served(self, number_customers):
#         """Setting the number of customers served"""
#         if number_customers > 0:
#             self.number_served = number_customers
#         else:
#             print("There can not be a negative amount of customers served")
#
#     def increment_number_served(self, customers_to_add):
#         if customers_to_add > 0:
#             self.number_served += customers_to_add
#         else:
#             print("You can't take away from the number of customers served")
#
#
# my_restaurant = Restaurant('dicks', 'cock cobbling')
# print("This restaurant has served " + str(my_restaurant.number_served)
#       + ' people.')
# my_restaurant.set_number_served(2)
# print("This restaurant has served " + str(my_restaurant.number_served)
#       + ' people.')
# my_restaurant.increment_number_served(5)
# print("This restaurant has now served " + str(my_restaurant.number_served)
#       + ' people.')
# print("The name of my restaurant is " + my_restaurant.name.title() + ".")
# print("I just opened a " + my_restaurant.type + " restaurant!")
# my_restaurant.open_restaurant()
# my_restaurant.describe_restaurant()

# Exercise 9-5 Login Attempts
#
# class User:
#     """Class for building user instances"""
#
#     def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.u_name = user_name
#         self.d_size = dick_size
#         self.sex_partners = sexual_partners
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("The user " + self.u_name + " entered the following information: ")
#         print("First name - " + self.f_name.title())
#         print("Last name - " + self.l_name.title())
#         print("Dick size - " + str(self.d_size))
#         print("Sexual partners - " + str(self.sex_partners))
#
#     def greet_user(self):
#         print("Hello " + self.u_name + " it is nice to see you, " + self.f_name.title()
#               + ". Have you fucked more than " + str(self.sex_partners) + " people yet?")
#
#     def increment_login_attempts(self):
#         """Just increment the number of login attempts by 1"""
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# some_user = User('nicholas', 'johnson', 'bigNdog', 9, 19)
#
# some_user.describe_user()
# some_user.greet_user()
#
# some_user.increment_login_attempts()
# some_user.increment_login_attempts()
# some_user.increment_login_attempts()
#
# print(some_user.f_name.title() + " has tried to login " + str(some_user.login_attempts) + " times.")
# some_user.reset_login_attempts()
# print(some_user.f_name.title() + " has tried to login " + str(some_user.login_attempts) + " times.")

# Exercise 9-6 Ice Cream Stand
#
# class Restaurant:
#     """Build a restaurant with a name and type then show it opening and describe it"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         """defining a method for describing the restaurant """
#         print("There is a new " + self.type + " restaurant in town called " + self.name.title() + ".")
#
#     def open_restaurant(self):
#         """Letting everyone know the restaurant is open"""
#         print("The " + self.type + " restaurant, " + self.name.title() + ", is now open!")
#
#     def set_number_served(self, number_customers):
#         """Setting the number of customers served"""
#         if number_customers > 0:
#             self.number_served = number_customers
#         else:
#             print("There can not be a negative amount of customers served")
#
#     def increment_number_served(self, customers_to_add):
#         if customers_to_add > 0:
#             self.number_served += customers_to_add
#         else:
#             print("You can't take away from the number of customers served")
#
#
# class IceCreamStand(Restaurant):
#     """Making an ice cream stand based on the restaurant class."""
#
#     def __init__(self, restaurant_name, size):
#         """Initializing the parent class attributes"""
#         super().__init__(restaurant_name, cuisine_type='ice cream')
#         self.flavors = ['ass hole', 'puke', 'wet dog']
#         self.size = size
#
#     def list_flavors(self):
#         print("We offer the following flavors: ")
#         for flavor in self.flavors:
#             print(flavor.title())
#
#
# my_stand = IceCreamStand('flavor ice', 'large')
# my_stand.open_restaurant()
# my_stand.list_flavors()

# Exercise 9-7 Admin

# class User:
#     """Class for building user instances"""
#
#     def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.u_name = user_name
#         self.d_size = dick_size
#         self.sex_partners = sexual_partners
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("The user " + self.u_name + " entered the following information: ")
#         print("First name - " + self.f_name.title())
#         print("Last name - " + self.l_name.title())
#         print("Dick size - " + str(self.d_size))
#         print("Sexual partners - " + str(self.sex_partners))
#
#     def greet_user(self):
#         print("Hello " + self.u_name + " it is nice to see you, " + self.f_name.title()
#               + ". Have you fucked more than " + str(self.sex_partners) + " people yet?")
#
#     def increment_login_attempts(self):
#         """Just increment the number of login attempts by 1"""
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
#         """Now to initialize the parent class attributes and any additional from above or default ones"""
#         super().__init__(first_name, last_name, user_name, dick_size, sexual_partners)
#         self.privileges = ['can add post', 'can delete post', 'can ban user', 'can do the secretary']
#
#     def show_privilege(self):
#         print("Since you are an admin you can do the following additional things: ")
#         for privilege in self.privileges:
#             print(privilege)
#
#
# some_user = Admin('nicholas', 'johnson', 'bigNdog', 9, 19)
#
# some_user.describe_user()
# some_user.greet_user()
#
# some_user.increment_login_attempts()
# some_user.increment_login_attempts()
# some_user.increment_login_attempts()
#
# print(some_user.f_name.title() + " has tried to login " + str(some_user.login_attempts) + " times.")
# some_user.reset_login_attempts()
# print(some_user.f_name.title() + " has tried to login " + str(some_user.login_attempts) + " times.")
# some_user.show_privilege()

#  Exercise 9-8 Privileges
# This shows how to make an instance within a class
#
# class User:
#     """Class for building user instances"""
#
#     def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
#         self.f_name = first_name
#         self.l_name = last_name
#         self.u_name = user_name
#         self.d_size = dick_size
#         self.sex_partners = sexual_partners
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("The user " + self.u_name + " entered the following information: ")
#         print("First name - " + self.f_name.title())
#         print("Last name - " + self.l_name.title())
#         print("Dick size - " + str(self.d_size))
#         print("Sexual partners - " + str(self.sex_partners))
#
#     def greet_user(self):
#         print("Hello " + self.u_name + " it is nice to see you, " + self.f_name.title()
#               + ". Have you fucked more than " + str(self.sex_partners) + " people yet?")
#
#     def increment_login_attempts(self):
#         """Just increment the number of login attempts by 1"""
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# class Privileges:
#     def __init__(self):
#         self.privileges = ['can add post', 'can delete post', 'can ban user', 'can do the secretary']
#
#     def show_privilege(self):
#         print("Since you are an admin you can do the following additional things: ")
#         for privilege in self.privileges:
#             print(privilege)
#
# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
#         """Now to initialize the parent class attributes and any additional from above or default ones"""
#         super().__init__(first_name, last_name, user_name, dick_size, sexual_partners)
#         self.admin_privileges = Privileges()
#
#
#
#
# some_user = Admin('nicholas', 'johnson', 'bigNdog', 9, 19)
#
# some_user.describe_user()
# some_user.greet_user()
#
# some_user.increment_login_attempts()
# some_user.increment_login_attempts()
# some_user.increment_login_attempts()
#
# print(some_user.f_name.title() + " has tried to login " + str(some_user.login_attempts) + " times.")
# some_user.reset_login_attempts()
# print(some_user.f_name.title() + " has tried to login " + str(some_user.login_attempts) + " times.")
# some_user.admin_privileges.show_privilege()

# Exercise 9-9 Battery Upgrade
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car|"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.tank_level = "empty"

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def fill_gas_tank(self):
        """Simulate filling up the gas tank"""
        self.tank_level = "full"

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can not add on a negative amount of miles!")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        # This would only work for exact battery sizes of 75 and 85 so really would need to add some > or < sings
        #  to deal with others if needed
        if self.battery_size == 70:
            range = 240
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
        elif self.battery_size == 85:
            range = 270
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
        else:
            message = "Please enter an appropriate battery size"

        print(message)

    def upgrade_battery(self):
        """Check the battery and if it is less than 85 upgrade it to 85"""
        if self.battery_size < 85:
            self.battery_size = 85
            print("Your battery has been upgraded to the 85kWh size.")
        elif self.battery_size == 85:
            print("You already have the 85kWh battery.")
        else:
            print("Your battery is already bigger than 85kWh.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # Here we assign an attribute "battery" the value of an instance from the battery class and of course we
        # just set everything default and did not pass any variables
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
# Here we reference the car that was made from the car class and then the method describe battery in the battery class
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_other_car = Car('chevy', 'corvette', '2018')
print("My car has a/an " + my_other_car.tank_level + " gas tank")
my_other_car.fill_gas_tank()
print("My car has a/an " + my_other_car.tank_level + " gas tank")
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
