# functions checker

def log_in():
    """This is a log-in checker function that examines inputs provided by the
    user before the log-in details are passed through."""

    def username_fn():
        """The function checks if username is provided correctly."""

        inp = input(' Provide your username: ')
        if len(inp.split()) != 1:
            print("No space are allowed, try again")
            inp = username_fn()
        return inp

    def password_fn():
        """The function checks if password of a user is provided correctly."""
        pass

    username = username_fn()
    password = input(" Provide your password: ")
    print(f"{username}, {password}")


def sing_up():
    """This is a sign-up checker function that examines inputs provided by the
        user before the sign-up details are passed through."""

    def name_fn():
        """The function checks if name of the user is provided correctly."""

        inp = input(" Provide your name: ")
        if len(inp.split()) != 2:
            print(" Provide your first name and surname separated by space! "
                  "Try again.")
            inp = name_fn()
        return inp

    def email_fn():
        """The function checks if e-mail of the user is provided correctly."""

        inp = input(' Provide your e-mail address: ')
        if "@cern.ch" not in inp:
            print(" Wrong format! Try again.")
            inp = email_fn()
        return inp

    def username_fn():
        """The function checks if username is provided correctly."""

        inp = input(' Provide your username: ')
        if len(inp.split()) != 1:
            print(" No space are allowed, try again")
            inp = username_fn()
        return inp

    def password_fn():
        """The function checks if password of a user is provided correctly."""
        pass

    name = name_fn()
    email = email_fn()
    username = username_fn()
    password = input(" Provide your password: ")
    print(f"{name}, {email}, {username}, {password}")






