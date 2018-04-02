class Restaurant:
    """Build a restaurant with a name and type then show it opening and describe it"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """defining a method for describing the restaurant """
        print("There is a new " + self.type + " restaurant in town called " + self.name.title() + ".")

    def open_restaurant(self):
        """Letting everyone know the restaurant is open"""
        print("The " + self.type + " restaurant, " + self.name.title() + ", is now open!")

    def set_number_served(self, number_customers):
        """Setting the number of customers served"""
        if number_customers > 0:
            self.number_served = number_customers
        else:
            print("There can not be a negative amount of customers served")

    def increment_number_served(self, customers_to_add):
        if customers_to_add > 0:
            self.number_served += customers_to_add
        else:
            print("You can't take away from the number of customers served")

