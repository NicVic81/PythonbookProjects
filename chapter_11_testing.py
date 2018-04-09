# # Exercise 11-1 City Country and 11-2 Population
#
#
# def format_city_country(city, country, population=''):
#     if population:
#         formatted_address = city.title() + ', ' + country.title() + " - population " + str(population.title()) + "."
#     else:
#         formatted_address = city.title() + ', ' + country.title()
#     return formatted_address
#
#
# my_city = format_city_country('arnoldsburg', 'west virginia', '7')
# print(my_city)


# Exercise 11-3 Employee
class Employee:
    """Simple class to create an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initializing the variables"""
        self.first_name = f_name
        self.last_name = l_name
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        if raise_amount > 0:
            self.salary = int(self.salary) + int(raise_amount)
            print("Your new salary is " + str(self.salary) + ".")
        elif raise_amount == 0:
            print("There is no raise to give.")
        else:
            print("You can not reduce the salary")
