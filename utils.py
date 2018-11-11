import functools
import os
import time
import json

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


def wait():
    time.sleep(0.5)


def pause_screen(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        wait()
        return output
    return wrapper


def print_error(err):
    print("Invalid:  {}".format(err))



def write_tasks(tl):
    tasks = []
    for task in tl.tasks:
        tasks.append(task.to_dict)
    with open(file_name, 'w') as tasks_file:
        json.dump(tasks, tasks_file)




