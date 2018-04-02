class User:
    """Class for building user instances"""

    def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
        self.f_name = first_name
        self.l_name = last_name
        self.u_name = user_name
        self.d_size = dick_size
        self.sex_partners = sexual_partners
        self.login_attempts = 0

    def describe_user(self):
        print("The user " + self.u_name + " entered the following information: ")
        print("First name - " + self.f_name.title())
        print("Last name - " + self.l_name.title())
        print("Dick size - " + str(self.d_size))
        print("Sexual partners - " + str(self.sex_partners))

    def greet_user(self):
        print("Hello " + self.u_name + " it is nice to see you, " + self.f_name.title()
              + ". Have you fucked more than " + str(self.sex_partners) + " people yet?")

    def increment_login_attempts(self):
        """Just increment the number of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    """Show the privileges an admin has."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can do the secretary']

    def show_privilege(self):
        print("Since you are an admin you can do the following additional things: ")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """Make an admin user."""
    def __init__(self, first_name, last_name, user_name, dick_size, sexual_partners):
        """Now to initialize the parent class attributes and any additional from above or default ones"""
        super().__init__(first_name, last_name, user_name, dick_size, sexual_partners)
        self.admin_privileges = Privileges()

