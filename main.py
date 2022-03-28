from get_data import get_login_data, get_register_data
from account import register, login
from users import (
    get_users, show_user_info,
    get_user_by_username,
    show_users_list,
)

# c case
# colorize commands

try:
    while True:
        try:
            user_command = input('Enter 0 for Login; Enter 1 for Register; (0/1): ')

            if user_command == '0':
                user_info = get_login_data()
                while True:
                    if login(*user_info):
                        break

                while True:
                    whats_next = input(
                        'Enter "info" for your full account information; "list" for user list; ( info/list ): ')

                    if whats_next == 'info':
                        show_user_info(user_info[0])

                    elif whats_next == 'list':
                        show_users_list()

                    else:
                        raise ValueError(f'\n"{user_command}" is not recognized as an internal command.\n')

            elif user_command == '1':
                user_info = get_register_data()
                register(*user_info)

            else:
                raise ValueError(f'\n"{user_command}" is not recognized as an internal command.\n')

        except ValueError as e:
            print(e)

except KeyboardInterrupt:
    print('\nBye :) ')
    exit()
