import functools
import os
import sys

file_name = 'tasks.json'

fmt = '%Y%m%d'

def clear():
    "Clear screen"
    os.system("cls" if os.name=="nt" else "clear")


def clear_screen(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        clear()
        return func(*args, **kwargs)
    return wrapper

def print_error(err):
    print("Invalid:  {}".format(err))

def quit_program():
    # save task list
    print("Goodbye!")
    sys.exit(0)




