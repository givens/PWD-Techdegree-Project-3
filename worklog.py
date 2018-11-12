"""
worklog.py
----------
Module contains Worklog class.
Worklog provides menus and program flow
for the PWD-Techdegree-Project-3 cli tool.
"""

from datetime import datetime
import menu
import sys
import os
import pdb

import tasks
import entry
import search
import edit
import utils


class Worklog:
    """Worklog menus and program flow"""

    def __init__(self):
        """
        Load json file
        If no file exists, create an empty TaskList
        """
        if os.path.exists(utils.file_name):
            self.tl = tasks.TaskList.import_tasklist()
        else:
            self.tl = tasks.TaskList()

    def quit_program(self):
        """
        Quit program by writing to json file
        Print goodbye message
        """
        utils.write_tasks(self.tl)
        print("Goodbye!")
        sys.exit(0)

    @utils.pause_screen
    @utils.clear_screen
    def main_menu(self):
        """
        Main menu provides three options
        1 - Add new entry
        2 - Search existing entries
        3 - Quit program
        """
        while True:
            choice = menu.make(menu.main)
            if choice == 1:  # add new entry
                task = entry.Entry().enter_all()
                self.tl.add(task)
                self.main_menu()
            elif choice == 2:  # search existing entries
                if not self.tl:
                    print("Cannot search, no entries exist.")
                    utils.wait()
                    self.main_menu()
                else:
                    self.search_menu()
            elif choice == 3:  # quit program
                self.quit_program()

    @utils.pause_screen
    @utils.clear_screen
    def search_menu(self):
        """
        Search menu provides 6 options
        1 - Search by date
        2 - Search by date range
        3 - Search by time
        4 - Search by contains (this is the "exact search")
        5 - Search by pattern
        6 - Return to main menu
        """
        while True:
            choice = menu.make(menu.search)
            if choice == 1:  # search by exact date
                tasks = search.Search().search_by_date(self.tl)
            elif choice == 2:  # search by range of dates
                tasks = search.Search().search_by_date_range(self.tl)
            elif choice == 3:  # search by time
                tasks = search.Search().search_by_time(self.tl)
            elif choice == 4:  # exact string search
                tasks = search.Search().search_by_contains(self.tl)
            elif choice == 5:  # pattern search
                tasks = search.Search().search_by_pattern(self.tl)
            elif choice == 6:
                self.main_menu()

            if tasks:
                self.edit_menu(tasks)
            else:
                print("No tasks found.")
                self.search_menu()

    @utils.pause_screen
    def edit_menu(self, tasks):
        """
        edit.Edit menu provides 6 options
        1 - Next item
        2 - Previous item
        3 - Edit item
        4 - Delete item
        5 - Return to search menu
        6 - Return to main menu
        """
        # pdb.set_trace()
        ed = edit.Edit(tasks)
        while True:
            utils.clear()
            try:
                ed.print_task()
            except IndexError as err:
                print(err)
                self.search_menu()
            choice = menu.make(menu.edit)
            try:
                if choice == 1:  # next
                    ed.next()
                elif choice == 2:  # previous
                    ed.previous()
                elif choice == 3:  # edit
                    old_task, new_task = ed.edit_task()
                    self.tl.edit(old_task, new_task)
                elif choice == 4:  # delete
                    old_task = ed.delete_task()
                    self.tl.delete(old_task)
                elif choice == 5:  # search menu
                    self.search_menu()
                elif choice == 6:  # main menu
                    self.main_menu()
            except IndexError as err:
                print(err)
                self.search_menu()


if __name__ == '__main__':
    """
    Testing and validation
    """
    d1 = datetime.strptime("20181105", utils.fmt)
    d2 = datetime.strptime("20181106", utils.fmt)
    d3 = datetime.strptime("20181107", utils.fmt)
    ts = [('Organize filecase', 15, d1, 'pick up under bed'),
          ('clean office', 20, d1, 'remove DMD'),
          ('treehouse practice', 60, d2, 'python'),
          ('treehouse project 1', 180, d1, 'guessing game'),
          ('treehouse project 2', 480, d1, 'soccer league'),
          ('treehouse project 3', 1200, d2, 'work log'),
          ('check cryptocurrency', 15, d2, 'is bitcoin up?'),
          ('segmentation', 1000, d3, 'segment rods and screws from CT image')]
    tl = tasks.TaskList.create_tasklist(ts)
    utils.write_tasks(tl)
    tl = tasks.TaskList.import_tasklist()
    for task in tl.tasks:
        print(task)
