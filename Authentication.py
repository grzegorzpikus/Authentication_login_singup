import csv
import Checking_functions as Ch_f
import User_class as Uc


def sign_up():
    """Function that creates a new account."""

    def user_name_provider():
        username = input('provide your username: ')
        if Ch_f.user_exists(username) is True:
            print('User name already exists. Provide a different one: ')
            user_name_provider()
        if Ch_f.char_num_user(username) is False:
            print('The user name is too short. Provide a different one: ')
            user_name_provider()
        return username

    def password_provider():
        password = input('provide your password: ')
        if Ch_f.char_num_password(password) is False:
            print('The password is too short. Provide a different one: ')
            password_provider()
        password = Ch_f.hashing(password)
        return password

    name = input('provide your name: ')
    email = input('provide your e-mail address: ')
    user_name = user_name_provider()
    password = password_provider()
    row = (user_name, password, name, email)

    with open('users.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(row)
    file.close()

def log_in():
    """Function that starts the script."""

    user_name = input('username: ')
    password = input('password: ')

    user_name_verification = Ch_f.user_exists(user_name)
    password_verification = Ch_f.password_correct(user_name, password)

    if user_name_verification is True and password_verification is True:
        print('You successfully logged in.')
        # here we initiate another action to move forward
    elif user_name_verification is not True:
        print('the user name does not exist. Try again.')
        log_in()
    else:
        print('the password is incorrect. Try again.')
        log_in()

    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            if line[0] == user_name:
                user_object = Uc.User(line[2], line[3], line[0], line[1])
                return user_object


sign_up()
# x = log_in()
# print(x)
