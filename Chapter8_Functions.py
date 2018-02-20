# # def is what you use to define a function
# def greet_user():
#     # This is called a docstring and is used in the documentation of a function
#     """Display a simple greeting"""
#     print("Hello!")
#
#
# # This just calls the function
# greet_user()
#
#
# # We can now do the same thing but use the () to pass in a value
# def greet_user(username):
#     """Display a simple greeting"""
#     print("Hello, " + username.title() + "!")
#
#
# greet_user('jesse')
#
# # Now using positional arguments
#
#
# def describe_pet(animal_type, pet_name):
#     """Display Information about a pet"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet('lemur', 'steve')

# Now using keyword arguments


# def describe_pet(animal_type, pet_name):
#     """Display Information about a pet"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(animal_type='lemur', pet_name='steve')

# Setting default values for arguments. You can still override them but if you don't define
# them in the function call it will use the default

# def describe_pet(pet_name, animal_type='dog'):
#     """Display Information about a pet"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(pet_name='steve')

# Exercise 8-3 T-Shirt
# def make_shirt(shirt_size, shirt_message):
#     """Now display the size and messatge trhe use wants for thier shirt"""
#     print("You have ordered a " + shirt_size + " shirt with \"" + shirt_message + "\" printed"
#                                                                                   " on it")
#
#
# make_shirt('small', 'Eat a Dick')
# make_shirt(shirt_size='large', shirt_message='Suck a bag of Dicks')

# Exercise 8-4 Large Shirt

# def make_shirt(shirt_size='large', shirt_message='I Love Dong'):
#     """Now display the size and messatge trhe use wants for thier shirt"""
#     print("You have ordered a " + shirt_size + " shirt with \"" + shirt_message + "\" printed"
#                                                                                   " on it")
#
#
# make_shirt()
# make_shirt('medium')
# make_shirt('small', 'Give me that DICK')

# Exercise 8-5 Cities

def describe_city(city_name, city_country='MERICA'):
    """Now display a city and the country it is in"""
    print(city_name.title() + " is a city in " + city_country.title() + ".")

describe_city("parkersburg")
describe_city(city_name='vienna')
describe_city(city_name='london', city_country='Europe')