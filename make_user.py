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