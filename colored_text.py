from colorama import init
from termcolor import cprint


def colored_print(text, mode, br=True):
    init()
    WARNING = 'red'
    SUCCESS = 'green'
    MESSAGE = 'blue'

    if mode == 'warning':
        if br:
            cprint(text, WARNING)
        else:
            cprint(text, WARNING, end='')

    elif mode == 'success':
        if br:
            cprint(text, SUCCESS)
        else:
            cprint(text, SUCCESS, end='')

    elif mode == 'message':
        if br:
            cprint(text, MESSAGE)
        else:
            cprint(text, MESSAGE, end='')

    else:
        cprint('Invalid color mode!', WARNING)
