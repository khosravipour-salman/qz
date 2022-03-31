from get_data import get_login_data, get_register_data
from account import register, login
from users import (
    get_users, show_user_info,
    get_user_by_username,
    show_users_list,
)
from colored_text import colored_print

# c case
# colorize commands
#
try:
    while True:
        try:
            colored_print('Enter 0 for Login; Enter 1 for Register; (0/1): ', 'message', br=False)
            user_command = input()

            if user_command == '0':
                while True:
                    user_info = get_login_data()
                    if login(*user_info):
                        break

                while True:
                    colored_print('Enter "info" for your full account information; "list" for user list; ( info/list ): ', 'message', br=False)
                    whats_next = input()

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
            colored_print(e, 'warning')

except KeyboardInterrupt:
    colored_print('\nBye :) ', 'success')
    exit()
