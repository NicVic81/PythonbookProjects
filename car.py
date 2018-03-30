"""A class that can be used to represent a car"""


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
