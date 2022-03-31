import bcrypt
from users import add_user_to_file
from logger import log_user_register
from datetime import datetime
from users import get_user_by_username, get_users
from colored_text import colored_print


def register(username, password, fname, lname, city, email):
    add_user_to_file(username, password, fname, lname, city, email)
    log_user_register(username, datetime.now().replace(microsecond=0))


def login(username, password):
    users = get_users()
    if not users.get(username):
        colored_print(f'"{username}" does not exist!', 'warning')
        return None

    user_password = bytes(users.get(username).get('password'), 'utf-8')

    if username in users:
        if bcrypt.checkpw(bytes(password, 'utf-8'), user_password):
            colored_print(f'\n{username} Logged in successfully. ', 'success')
            return True

        colored_print('\nInvalid credentials. ', 'warning')
