from colorama import init
from termcolor import cprint


def colored_print(text, mode, br=True):
    init()
    WARNING = 'red'
    SUCCESS = 'green'
    MESSAGE = 'blue'
    CYAN = 'cyan'

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

    elif mode == 'cyan':
        if br:
            cprint(text, CYAN)
        else:
            cprint(text, CYAN, end='')
            
    else:
        cprint('Invalid color mode!', WARNING)
