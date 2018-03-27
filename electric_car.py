# class Car:
#     """A simple attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car|"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#         self.tank_level = "empty"
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def fill_gas_tank(self):
#         """Simulate filling up the gas tank"""
#         self.tank_level = "full"
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def increment_odometer(self, miles):
#         if miles >= 0:
#             self.odometer_reading += miles
#         else:
#             print("You can not add on a negative amount of miles!")
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles"""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def fill_gas_tank(self):
#         """Electric cars do not have gas tanks."""
#         print("This car doesn't need a gas tank!")
#
#
# my_tesla = ElectricCar('tesla', 'model s', '2016')
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
# my_other_car = Car('chevy', 'corvette', '2018')
# print("My car has a/an " + my_other_car.tank_level + " gas tank")
# my_other_car.fill_gas_tank()
# print("My car has a/an " + my_other_car.tank_level + " gas tank")

# Now we are breaking the battery into a class by itself

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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # Here we assign an attribute "battery" the value of an instance from the battery class and of course we just set
        # everything default and did not pass any variables
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
