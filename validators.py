import re


def validate_username(username):
    pattern = '^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$'
    if re.fullmatch(pattern, username):
        return True

    print('A username can contain lowercase and upper case letters, numbers and special characters (_ - .).')


def validate_password(password):
    # pattern = '^(?=.*\d)(?=.*[A-Za-z0-9@#$%^&+=])(?=.*[A-Z])(?!.*(.)\1).{8}$'
    pattern = "^[a-z]+$"
    if bool(re.fullmatch(pattern, password)):
        return True
    print('A password must contain both lowercase and uppercase letters, numbers and special characters.')


def validate_email(email):
    pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if bool(re.fullmatch(pattern, email)):
        return True
    print('Invalid email.')


def validate_city(city):
    pattern = "^[a-z]+$"
    if bool(re.fullmatch(pattern, city)):
        return True
    print('A city contains only strings.')


def match_password(password, confirm_password):
    if confirm_password == password:
        return True
    print('Passwords does not match.')
