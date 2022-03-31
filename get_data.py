from validators import (
    validate_username,
    validate_password,
    match_password,
    validate_city,
    validate_email,
)
from stdiomask import getpass


def get_login_data():
    while True:
        username = input('Enter your username: ')
        if not username:
            print('Empty username is not allowed')
            continue

        password = getpass('Enter your password: ')
        if not password:
            print('Empty password is not allowed')
            continue

        break

    return username, password


def get_register_data():
    while True:
        username = input('Enter your username: ')
        if not validate_username(username): continue

        password = getpass('Enter your password: ')
        if not validate_password(password): continue

        confirm_password = getpass('Confirm your password: ')
        if not match_password(password, confirm_password): continue

        fname = input('Enter your first name: ')
        if not validate_city(fname): continue

        lname = input('Enter your last name: ')
        if not validate_city(lname): continue

        city = input('Enter your city: ')
        if not validate_city(city): continue

        email = input('Enter your email: ')
        if not validate_email(email): continue

        break

    return username, password, fname, lname, city, email
