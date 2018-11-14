"""
worklog.py
----------
Module contains Worklog class.
Worklog provides menus and program flow
for the PWD-Techdegree-Project-3 cli tool.
"""

import sys
import os

import menu
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
            self.task_list = tasks.TaskList.import_tasklist()
        else:
            self.task_list = tasks.TaskList()

    def quit_program(self):
        """
        Quit program by writing to json file
        Print goodbye message
        """
        utils.write_tasks(self.task_list)
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
                self.task_list.add(task)
                return self.main_menu()
            elif choice == 2:  # search existing entries
                if not self.task_list:
                    print("Cannot search, no entries exist.")
                    utils.wait()
                    return self.main_menu()
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
                found_tasks = search.Search().search_by_date(self.task_list)
            elif choice == 2:  # search by range of dates
                found_tasks = search.Search().search_by_date_range(
                    self.task_list)
            elif choice == 3:  # search by time
                found_tasks = search.Search().search_by_time(self.task_list)
            elif choice == 4:  # exact string search
                found_tasks = search.Search().search_by_contains(
                    self.task_list)
            elif choice == 5:  # pattern search
                found_tasks = search.Search().search_by_pattern(self.task_list)
            elif choice == 6:
                return self.main_menu()

            if found_tasks:
                self.edit_menu(found_tasks)
            else:
                print("No tasks found.")
                utils.wait()
                return self.search_menu()

    @utils.pause_screen
    def edit_menu(self, found_tasks):
        """
        edit.Edit menu provides 6 options
        1 - Next item
        2 - Previous item
        3 - Edit item
        4 - Delete item
        5 - Return to search menu
        6 - Return to main menu
        """
        ed_tasks = edit.Edit(found_tasks)
        while True:
            utils.clear()
            try:
                ed_tasks.print_task()
            except IndexError as err:
                print(err)
                utils.wait()
                return self.search_menu()
            choice = menu.make(menu.edit)
            try:
                if choice == 1:  # next
                    ed_tasks.next()
                elif choice == 2:  # previous
                    ed_tasks.previous()
                elif choice == 3:  # edit
                    old_task, new_task = ed_tasks.edit_task()
                    self.task_list.edit(old_task, new_task)
                elif choice == 4:  # delete
                    old_task = ed_tasks.delete_task()
                    self.task_list.delete(old_task)
                    print("Task deleted.")
                    utils.wait()
                elif choice == 5:  # search menu
                    self.search_menu()
                elif choice == 6:  # main menu
                    self.main_menu()
            except IndexError as err:
                print(err)
                utils.wait()
                return self.search_menu()
