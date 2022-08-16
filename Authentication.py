import csv
import User_class as Uc


def add_user(details: list):
    """Function creates a new account and adds in to the database."""
    # it adds it to the file for now!

    with open('users.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(details)
    file.close()


def create_user_object(user_name):
    """If user logs in sucsessfully, this function creates a user object."""

    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            if line[0] == user_name:
                user_object = Uc.User(line[2], line[3], line[0], line[1])
                return user_object

