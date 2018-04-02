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
