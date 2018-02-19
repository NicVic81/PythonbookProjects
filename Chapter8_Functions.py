#def is what you use to define a function
def greet_user():
    #This is called a docstring and is used in the documentation of a function
    """Display a simple greeting"""
    print("Hello!")

#This just calls the function
greet_user()

#We can now do the same thing but use the () to pass in a value
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

greet_user('jesse')