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

# def describe_city(city_name, city_country ='MERICA'):
#     """Now display a city and the country it is in"""
#     print(city_name.title() + " is a city in " + city_country.title() + ".")
#
# describe_city("parkersburg")
# describe_city(city_name='vienna')
# describe_city(city_name='london', city_country='Europe')
# End of Exercise 8-5
# def get_formatted_name(first_name, last_name):
#     """Return a full name neatly formatted."""
#     full_name = first_name + " " + last_name
#     # This takes the user entered names and puts it in title format then returns it to the
#     # full name variable, I think you could just do it by putting .title() on each variable in
#     # the line above
#     return full_name.title()
#
#
# musician = get_formatted_name('jim', 'hendrix')
# print(musician)

# Now setting an optional argument

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted"""
#     # The if middle name is a true false statement and if it is empty it is false
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jim', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# Now using a function to return dictionary values
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     return person
#
# musician = build_person('jimi', 'hendrix')
# print(musician)

# Now adding in an optional age entry into the dictionary

# def build_person(first_name, last_name, age=''):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# Using a function with a while loop

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# # This is an infinite loop because there is nothing to tell it to stop asking for a name.
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# Here we add some if statements to break out of the while loop

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# Exercise 8-6 City Names
# def city_country(city_name, country_name):
#     """Return the citry and country neatly formatted"""
#     formatted_location = city_name + ", " + country_name
#     return formatted_location.title()
#
#
# place = city_country('parkersburg', 'merica')
# print(place)

# Exercise 8-7 Album

# def make_album(artist_name, album_name):
#     """Build dictionary of albums"""
#     album_dictionary = {"artist" : artist_name.title(), "album" : album_name.title()}
#     return album_dictionary
#
# user_album = make_album('NIN','pretty hate machine')
# print(user_album)
# user_album = make_album(artist_name='tool', album_name='undertow')
# print(user_album)
# user_album = make_album('your mom', 'queefs')
# print(user_album)

# Exercise 8-8 User Albums

# def make_album(artist_name, album_name):
#     """Build dictionary of albums"""
#     album_dictionary = {"artist" : artist_name.title(), "album" : album_name.title()}
#     return album_dictionary
#
# print("Please enter an artist and then the album name and I will build a dictionary of the inputs")
# print("Enter 'quit' at any time to finish")
#
# while True:
#     user_artist = input("\nArtist Name: ")
#     if user_artist.lower() == 'quit':
#         break
#     user_album = input("Album Name: ")
#     if user_album.lower() == 'quit':
#         break
#
#     user_list = make_album(user_artist, user_album)
#
#     print("\nHere is your list:")
#     print(user_list)

#  We are going to be passing lists into functions now. This one is passing a list and then greeting each user.
# def greet_users(names):
#     """Print a simple greeting to each user in the list"""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)
#
# Without using functions we are goign to move items from one list to another
# #  We are going to start with some things that need 3D printed
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # Simulate printing until they are all done
# # Move each design to the completed listed after printing
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # Simulate creating a 3D print form each design
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#
# # Display all completed models
# print("\nThe following models have been printed:")
# for completed_model in sorted(completed_models):
#     print(completed_model.title())

# Now we are going to do this more efficiently by using functions
# First here we had to send in both lists because we are working with both
# def print_models(unprinted_designs[:], completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed model list after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#
#         # Simulate creating a 3D print from the design
#         print("Printing model: " + current_design.title())
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     """Show all the models that were printed"""
#     print("\nThe following models have been printed: ")
#     for completed_model in sorted(completed_models):
#         print(completed_model.title())
#
# # Now that that is all setup we now make the lists
# unprinted_designs = ['iphone case', 'robot pendant','dodecahedron']
# completed_models = []
# # And now we call the functions with the list from above as the variables
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Exercise 8-9 Magicians
# def show_magicians(magician_list):
#     """Print the magicians"""
#     print("Here is the list of magicians:")
#     for printed_magician in sorted(magician_list):
#         print(printed_magician.title())
#
# magician_list = ['victoria johnson', 'addison johnson', 'emry johnson', 'rob mason']
# show_magicians(magician_list)

# Exercise 8-10 Great Magicians page 150

# def make_great(magician_list):
#     """Add 'The Great' to the magicians name"""
#     for magician in range(len(magician_list)):
#         # having it count the number of magicians in the list and having it only run the  loop that many times
#         # so it does not get stuck in the loop
#         magician_list[magician] = magician_list[magician] + ' The Great'
#         # now telling it to add the "The Great" to whatever number in the list it is at
#
#
# def show_magicians(magician_list):
#     """Print the magicians"""
#     print("Here is the list of magicians:")
#     for printed_magician in sorted(magician_list):
#         print(printed_magician.title())
#
#
# magician_list = ['victoria johnson', 'addison johnson', 'emry johnson', 'rob mason']
# make_great(magician_list)
# show_magicians(magician_list)

# Exercise 8-11 Unchanged Magicians


# def make_great(magician_list, great_magicians_list):
#     """Add 'The Great' to the magicians name"""
#     while magician_list:
#         magician = magician_list.pop() + ' The Great'
#         great_magicians_list.append(magician)
#
#
# def show_magicians(magician_list):
#     """Print the magicians"""
#     print("Here is the list of magicians:")
#     for printed_magician in sorted(magician_list):
#         print(printed_magician.title())
#
# great_magicians_list = []
# magician_list = ['victoria johnson', 'addison johnson', 'emry johnson', 'rob mason']
# # Here we use the [:] to send a copy of the list so it does not change it
# make_great(magician_list[:], great_magicians_list)
# show_magicians(magician_list)
# show_magicians(great_magicians_list)

# Passing an arbitrary number of argumetns.
# the * and then the variable name means it will take as many variables as we send it
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Now with a loop to better print out the toppings
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Now we are going to add another variable and since it is a fixed on the arbitrary one needs to come last

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMaking  a " + str(size) + "-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The double asterisk in the next example tell python to build that variable as a dictionary


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstain',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

# Exercise 8-12 Sandwiches
#
# def make_sandwich(*sandwich_items):
#     """Summarize and print the sandwich we are making """
#     print("\nWe are making with the following itesm: ")
#     for item in sandwich_items:
#         print("- " + item.title())
#
#
# make_sandwich('Dis Dick', 'some vag', 'your mom')

# Exercise 8-13 User Profile
# def make_profile (first, last, **user_info):
#     """Going to make a profile dictionary"""
#     user_profile = {}
#     user_profile['first name'] = first
#     user_profile['last name'] = last
#     for key, value in user_info.items():
#         user_profile[key] = value
#     return user_profile
#
#
# my_profile = make_profile('nicholas', 'johnson',
#                           dick='huge',
#                           humor='dark',
#                           speech='smart ass')
# print(my_profile)

# Exercise 8-14 Cars
def make_car(make, model, **other_info):
    """Make a dictionary of info on a car"""
    car_info = {}
    car_info["Make"] = make
    car_info["Model"] = model
    for key, value in other_info.items():
        car_info[key] = value
    return car_info


car = make_car('chevy', 'corvette',
               color='black',
               Z06='Yes')
print(car)