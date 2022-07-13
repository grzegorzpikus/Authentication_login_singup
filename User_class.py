

class User:
    """This class stores users details. After log-in the information about
    an user are kept in the object of this class."""

    def __init__(self, __name, __email, __user_name, __password):
        self.__name = __name
        self.__email = __email
        self.__user_name = __user_name
        self.__password = __password

    def __str__(self):
        """It represents a object as a string if the string is printed."""
        return f"{self.__name}"

    def __repr__(self):
        """This is a graphical representation of an object"""
        return f"{self.__user_name}"
