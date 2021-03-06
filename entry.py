"""
entry.py
--------
Add task entry
"""


import datetime

import tasks
import utils


class Entry:
    """This class allows the user to enter all the information
    associated with a Task"""
    @utils.clear_screen
    def enter_date(self, task=None):
        """Obtain user-suppled task date"""
        print("Enter task date")
        if task:
            print('Current: {}'.format(task.date.strftime(utils.fmt)))
        date_str = input(
            "Please use YYYYMMDD or just enter for current date:  ")
        try:
            if not date_str:
                date = datetime.datetime.today()
                delta = datetime.timedelta(hours=date.hour,
                                           minutes=date.minute,
                                           seconds=date.second,
                                           microseconds=date.microsecond)
                date = date - delta
            else:
                date = datetime.datetime.strptime(date_str, utils.fmt)
        except ValueError as err:
            utils.print_error(err)
            utils.wait()
            return self.enter_date()
        else:
            return date

    @utils.clear_screen
    def enter_minutes(self, task=None):
        """Obtain user-supplied task time in minutes"""
        print("Enter task time")
        if task:
            print('Current: {}'.format(task.minutes))
        minutes_str = input("Please enter minutes:  ")
        try:
            if not minutes_str:
                raise ValueError("Minutes cannot be empty.")
            minutes = int(minutes_str)
        except ValueError as err:
            utils.print_error(err)
            utils.wait()
            return self.enter_minutes()
        else:
            return round(minutes)

    @utils.clear_screen
    def enter_title(self, task=None):
        """Obtain name of task"""
        print("Enter task title")
        if task:
            print('Current: {}'.format(task.title))
        title = input("What is the name?  ")
        try:
            if not title:
                raise ValueError("Title cannot be empty.")
        except ValueError as err:
            utils.print_error(err)
            utils.wait()
            return self.enter_title()
        else:
            return title

    @utils.clear_screen
    def enter_notes(self, task=None):
        """Obtain task notes"""
        print("Enter task notes")
        if task:
            print('Current: {}'.format(task.notes))
        notes = input("Do you have additional comments (can be empty)?  ")
        return notes

    def enter_all(self, task=None):
        """Obtain user-supplied info for task"""
        title = self.enter_title(task)
        date = self.enter_date(task)
        minutes = self.enter_minutes(task)
        notes = self.enter_notes(task)
        return tasks.Task(title, minutes, date, notes)
