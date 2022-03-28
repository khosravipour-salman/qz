# from users import users_list, add_user_to_file, get_user_by_username
from users import add_user_to_file
from logger import log_user_register
from datetime import datetime
from users import get_user_by_username, get_users


def register(username, password, fname, lname, city, email):
    add_user_to_file(username, password, fname, lname, city, email)
    log_user_register(username, datetime.now().replace(microsecond=0))


def login(username, password):
    users = get_users()

    if username in users:
        if password == users[username]['password']:
            print(f'Logged in successfully. ')
            return True

        print('Invalid credentials. ')


# fix while loop bug
