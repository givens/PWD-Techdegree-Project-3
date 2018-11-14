"""
tasks.py
--------
This module contains the Task and TaskList classes.
These classes are the basis of the worklog.
"""

import json
import datetime
import re

import utils


class Item:
    """Basic item class"""

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Task(Item):
    """The Task class contains title, minutes, date, and notes --
    all part of a task on a timesheet.
    The methods provide ways to search the Task."""

    def __init__(self, title, minutes, date, notes=""):
        super().__init__(title=title,
                         minutes=minutes,
                         date=date,
                         notes=notes)

    def __str__(self):
        """Print Task"""
        return """TITLE: {},
MINUTES: {},
DATE: {},
NOTES: {}
""".format(self.title,
           self.minutes,
           self.date.strftime(
               utils.fmt),
           self.notes)

    @property
    def to_dict(self):
        """Convert task to dictionary"""
        return {'title': self.title,
                'notes': self.notes,
                'minutes': self.minutes,
                #                'date': self.date}
                'date': self.date.strftime(utils.fmt)}

    @classmethod
    def create_task(cls, title, minutes, date, notes=""):
        """Creates a Task using classmethod"""
        return cls(title, minutes, datetime.datetime.strptime(
            date, utils.fmt), notes)

    def match_date(self, date):
        """Determine if Task matches date"""
        if self.date == date:
            return True
        return False

    def match_date_range(self, date1, date2):
        """Determine if Task within date range"""
        return (self.date >= date1 and self.date <= date2) or (
            self.date >= date2 and self.date <= date1)

    def match_time(self, minutes):
        """Determine if Task has the same minutes"""
        if self.minutes == minutes:
            return True
        return False

    def match_contains(self, string):
        """Determine if Task contains a string in title or notes"""
        return (string in self.title) or (string in self.notes)

    def match_pattern(self, pattern):
        """Determine if Task matches regex search pattern in title or notes"""
        prog = re.compile(r'{}'.format(pattern))
        title_match = prog.search(self.title)
        notes_match = prog.search(self.notes)
        if title_match or notes_match:
            return True
        return False

    def __eq__(self, task):
        """Determine if Task is exactly equal to another Task"""
        same_title = self.title == task.title
        same_notes = self.notes == task.notes
        same_time = self.minutes == task.minutes
        same_date = self.date == task.date
        return same_title and same_notes and same_time and same_date


class TaskList:
    "The TaskList class is a list of Tasks."

    def __init__(self, tasks=None):
        """Create a task list.  If tasks are none, create an empty list."""
        if tasks:
            self.tasks = tasks
        else:
            self.tasks = []

    @classmethod
    def create_tasklist(cls, task_list):
        """Create a TaskList from a list of tuples"""
        tasks = []
        for title, minutes, date, notes in task_list:
            tasks.append(Task(title, minutes, date, notes))
        return cls(tasks)

    @classmethod
    def import_tasklist(cls):
        """Import json file into TaskList object"""
        with open(utils.file_name, 'r') as tasks_file:
            text = json.load(tasks_file)
        tasks = []
        for task in text:
            tasks.append(
                Task.create_task(
                    task['title'],
                    task['minutes'],
                    task['date'],
                    task['notes']))
        return cls(tasks)

    def add(self, new_task):
        """Add an item in the task list"""
        self.tasks.append(new_task)

    def edit(self, old_task, new_task):
        """Edit an item in the task list"""
        self.tasks.remove(old_task)
        self.tasks.append(new_task)

    def delete(self, old_task):
        """Delete an item in the task list"""
        self.tasks.remove(old_task)

    def __len__(self):
        """Provides length of list of Tasks"""
        return len(self.tasks)

    def findall_date(self, date):
        """Finds all occurences matching a given date"""
        return [task for task in self.tasks if task.match_date(date)]

    def findall_time(self, time):
        """Finds all occurences matching a given time"""
        return [task for task in self.tasks if task.match_time(time)]

    def findall_contains(self, string):
        """Find all occurrences containing a given string"""
        return [task for task in self.tasks if task.match_contains(string)]

    def findall_pattern(self, pattern):
        """Find all occurences matching a given regex pattern"""
        return [task for task in self.tasks if task.match_pattern(pattern)]

    def findall_date_range(self, date1, date2):
        """Find all occurences that are within the two dates"""
        return [
            task for task in self.tasks if task.match_date_range(date1, date2)]

    def findall_exact(self, tsk):
        """Find all occurences that exactly match the given task"""
        return [task for task in self.tasks if task.match_exact(tsk)]

    def find_index_exact(self, tsk):
        """Find all indices where the task exactly matches"""
        return [index for index, task in enumerate(
            self.tasks) if self.task[index] == tsk]
