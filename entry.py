from tasks import Task
from datetime import datetime
from utils import fmt, clear_screen, print_error
import pdb

class Entry:

    @clear_screen
    def enter_date(self):
        "Obtain user-suppled task date"
        print("Enter task date")
        date_str = input("Please use YYYYMMDD:  ")
        try:
            if not date_str:
                raise ValueError("Date cannot be empty.")
            date = datetime.strptime(date_str, fmt)
        except ValueError as err:
            print_error(err)
            return enter_date(self)
        else:
            return date

    @clear_screen
    def enter_minutes(self):
        "Obtain user-supplied task time in minutes"
        print("Enter task time")
        minutes_str = input("Please enter minutes:  ")
        try:
            if not minutes_str:
                raise ValueError("Minutes cannot be empty.")
            minutes = int(minutes_str)
        except ValueError as err:
            print_error(err)
            return enter_minutes(self)
        else:
            return round(minutes)

    @clear_screen
    def enter_title(self):
        "Obtain name of task"
        print("Enter task title")
        title = input("What is the name?  ")
        try:
            if not title:
                raise ValueError("Title cannot be empty.")
        except ValueError as err:
            print_error(err)
            return enter_title(self)
        else:
            return title

    @clear_screen
    def enter_notes(self):
        "Obtain task notes"
        print("Enter task notes")
        notes = input("Do you have additional comments (can be empty)?  ")
        return notes

    def enter_all(self):
        "Obtain user-supplied info for task"
        title = self.enter_title()
        date = self.enter_date()
        minutes = self.enter_minutes()
        notes = self.enter_notes()
        return Task(title, minutes, date, notes)
