from make_user import User

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
