"""
utils.py
--------
Utility functions for the worklog
"""

import functools
import os
import time
import json

file_name = 'tasks.json'
fmt = '%Y%m%d'


def clear():
    """Clear screen"""
    os.system("cls" if os.name == "nt" else "clear")


def clear_screen(func):
    """Clear screen decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        clear()
        return func(*args, **kwargs)
    return wrapper


def wait():
    """Wait for a fraction of a second"""
    time.sleep(0.5)


def pause_screen(func):
    """Pause screen decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Return wrapper file"""
        output = func(*args, **kwargs)
        wait()
        return output
    return wrapper


def print_error(err):
    """Print error when invalid"""
    print("Invalid:  {}".format(err))


def write_tasks(tl):
    """Write task list to a json file"""
    tasks = []
    for task in tl.tasks:
        tasks.append(task.to_dict)
    with open(file_name, 'w') as tasks_file:
        json.dump(tasks, tasks_file)
