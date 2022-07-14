import csv
import hashlib as hl

def hashing(password):
    password_hash = hl.sha256(str.encode(password)).hexdigest()
    return password_hash

def user_exists(user_name):
    """This function checks if user name exists. It returns true if it does,
    otherwise it return false."""

    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            if line[0] == user_name:
                return True
            else:
                return False


def password_correct(user_name, password):
    """This function checks if user name exists. It returns true if it does,
    otherwise it return false."""

    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            if line[0] == user_name:
                if line[1] == hashing(password):
                    return True
                else:
                    return False


def char_num_user(string):
    """This function checks if user_name is long enough."""

    number = 6
    if len(string) >= number:
        return True
    else:
        return False


def char_num_password(string):
    """This function checks if user_name is long enough."""

    number = 10
    if len(string) >= number:
        return True
    else:
        return False
