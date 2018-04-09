import json


def get_stored_username():
    """Get stored username if available"""
    filename = 'OnlineResources/chapter_10/username.json'
    try:
        with open(filename) as f_object:
            username = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return username


def store_username():
    """Prompt to store a username"""
    print("I am sorry you have not stored your name yet.")
    username = input("What is your name? ")
    filename = 'OnlineResources/chapter_10/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Function to greet a user by name or prompt to save their name."""

    username = get_stored_username()
    if username:
        print("Is your username " + username.title() + " ? ")

        while True:
            correct_user = input("Please enter 'yes' or 'no' : ")
            if not (correct_user.lower() == 'yes' or correct_user.lower() == 'no'):
                msg = "That is not a correct response."
                print(msg)
            else:
                break
        if correct_user.lower() == 'yes':
            print("Welcome back " + username.title() + "!")
        else:
            username = store_username()
            print("We will remember you when you come back, " + username.title() + "!")


greet_user()
