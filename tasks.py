import csv
import json
import tablib
from datetime import datetime
import pdb
import re
from utils import fmt, file_name

# Item
# Task
# Inventory
# TaskIventory
# Timesheet

class Item:

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Task(Item):
    "Title, time spent (in minutes), valid date, and notes are contained in the Task object"

    def __init__(self, title, minutes, date, notes=""):
#        self.title = title
#        self.minutes = int(minutes)
#        self.date = date.strptime(date, '%Y%m%d')
#        self.notes = notes
#        pdb.set_trace()
        super().__init__(title=title,
            minutes=minutes,
            date=date,
            notes=notes)

    def __str__(self):
        return """
TITLE: {},
MINUTES: {},
DATE: {},
NOTES: {}
""".format(self.title, self.minutes, self.date.strftime(fmt), self.notes)

    @property
    def to_dict(self):
        return {'title': self.title,
                'notes': self.notes,
                'minutes': self.minutes,
#                'date': self.date}
                'date': self.date.strftime(fmt)}

    @classmethod
    def create_task_from_dict(cls, title, minutes, date, notes=""):
        return cls(title, minutes, datetime.strptime(date, fmt), notes)

    def match_date(self, date):
        if self.date==date:
            return True
        return False

    def match_date_range(self, date1, date2):
        return (self.date>=date1 and self.date<=date2) or (self.date>=date2 and self.date<=date1)

    def match_time(self, minutes):
        if self.minutes==minutes:
            return True
        return False

    def match_contains(self,string):
        return (string in self.title) or (string in self.notes)

    def match_pattern(self,pattern):
#        pdb.set_trace()
#       rstring = "r'{}'".format(pattern)
        prog = re.compile(r'{}'.format(pattern))
        title_match = prog.search(self.title)
        notes_match = prog.search(self.notes)
        if title_match or notes_match:
            return True
        return False

    def __eq__(self, task):
        same_title = self.title==task.title
        same_notes = self.notes==task.notes
        same_time = self.minutes==task.minutes
        same_date = self.date==task.date
        return same_title and same_notes and same_time and same_date



#class Inventory(list):

#    def __init__(self, item_class=None, *args, **kwargs):
#        if not item_class:
#            raise ValueError("You must provide an item class.")
#        super().__init__(*args, **kwargs)


#class TaskInventory(list):
#    def __init__(self, *args, **kwargs):
#        super().__init__(item_class=Task, *args, **kwargs)

#    @classmethod
#    def create_tasklist(cls, task_list):
#        tasks = []
#        for title, minutes, date, notes in task_list:
#            tasks.append(Task(title, minutes, date, notes))
#        return cls(tasks)

#    def match_date(self, date):
#        tasks  = []
#        for task in self.tasks:

class TaskList:

    def __init__(self, tasks=None):
        if tasks:
            self.tasks = tasks
        else:
            self.tasks = []

    @classmethod
    def create_tasklist(cls, task_list):
        tasks = []
        for title, minutes, date, notes in task_list:
            tasks.append(Task(title, minutes, date, notes))
        return cls(tasks)

    @classmethod
    def import_tasklist(cls):
        #pdb.set_trace()
        with open(file_name, 'r') as tasks_file:
            tks = json.load(tasks_file)
        tasks = []
        for task in tks:
            tasks.append(Task.create_task_from_dict(
                task['title'],
                task['minutes'],
                task['date'],
                task['notes']))
        return cls(tasks)

    def edit(self, new_task, old_task):
        self.tasks.remove(old_task)
        self.tasks.append(new_task)

    def delete(self, old_task):
        self.tasks.remove(old_task)

    def add(self, task):
        self.tasks.append(task)

    def add_tuple(self, title, minutes, date, notes):
        self.add(Task(title, minutes, date, notes))

    def __str__(self):
        for task in self.tasks:
            print(task)

    def __len__(self):
        return len(self.tasks)

    def findall_date(self, date):
        "Find all tasks that match the date"
        return [task for task in self.tasks if task.match_date(date)]

    def findall_time(self, time):
        "Find all tasks that match the time"
        return [task for task in self.tasks if task.match_time(time)]

    def findall_contains(self, string):
        "Find all tasks that contain the string"
        return [task for task in self.tasks if task.match_contains(string)]

    def findall_pattern(self, pattern):
        "Find all tasks that match the regex pattern"
        return [task for task in self.tasks if task.match_pattern(pattern)]

    def findall_date_range(self, date1, date2):
        "Find all tasks that are within the two dates"
        return [task for task in self.tasks if task.match_date_range(date1, date2)]

    def findall_exact(self, tsk):
        "Find all tasks that exactly match the given task"
        return [task for task in self.tasks if task.match_exact(tsk)]

    def find_index_exact(self, tsk):
        "Find all task indices where the task exactly matches"
        return [index for index, task in enumerate(self.tasks) if task.match_exact(tsk)]

# Testing
if __name__ == '__main__':

    ts = [
    {'title': 'clean room', 'notes': 'pick up under bed', 'minutes': 15, 'date': '20181105'},
    {'title': 'clean office', 'notes': 'remove DMD', 'minutes': 20, 'date': '20181105'},
    {'title': 'treehouse practice', 'notes': 'python', 'minutes': 60, 'date': '20181205'},
    {'title': 'treehouse project 3', 'notes': 'work log', 'minutes': 120, 'date': '20181205'},
    {'title': 'check cryptocurrency', 'notes': 'is bitcoin up?', 'minutes': 15, 'date': '20181205'}
    ]

    new_ts = {'title': 'clean kitchen', 'notes': 'do dishes', 'minutes': 60, 'date': '20181106'}



    old_task = Task.create_task_from_dict(**ts[0])
    print(old_task)

    new_task = Task.create_task_from_dict(**new_ts)
    print(new_task)

    print('----')

    tl = TaskList.import_tasklist()
    for task in tl.tasks:
        print(task)

    print('----')

    tl.edit(new_task, old_task)

    for task in tl.tasks:
        print(task)

    print('----')

    tl.delete(new_task)

    for task in tl.tasks:
        print(task)





