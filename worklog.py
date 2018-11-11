from datetime import datetime
import menu
import sys

from tasks import Task, TaskList
from entry import Entry
from search import Search
from edit import Edit
from utils import clear, clear_screen, fmt, wait, pause_screen, write_tasks


class Worklog:

    def __init__(self):
        self.tl = TaskList.import_tasklist()

    def quit_program(self):
        write_tasks(self.tl)
        print("Goodbye!")
        sys.exit(0)

    @pause_screen
    @clear_screen
    def main_menu(self):
        while True:
            choice = menu.make(menu.main)
            if choice == 1: # add new entry
                task = Entry().enter_all()
                self.tl.add(task) # or write to file
                self.main_menu()
            elif choice == 2: # search existing entries
                if not self.tl:
                    print("Cannot search, no entries exist.")
                    wait()
                self.search_menu()
            elif choice == 3: # quit program
                self.quit_program()

    @pause_screen
    @clear_screen
    def search_menu(self):
        #pdb.set_trace()
        while True:
            choice = menu.make(menu.search)
            if choice == 1: # search by exact date
                tasks = Search().search_by_date(self.tl)
            elif choice == 2: # search by range of dates
                tasks = Search().search_by_date_range(self.tl)
            elif choice == 3: # search by time
                tasks = Search().search_by_time(self.tl)
            elif choice == 4: # exact string search
                tasks = Search().search_by_contains(self.tl)
            elif choice == 5: # pattern search
                tasks = Search().search_by_pattern(self.tl)
            elif choice == 6:
                self.main_menu()
            else:
                self.search_menu()
            for task in tasks:
                print(task)
            if tasks:
                self.edit_menu(tasks)
    #            replace_tasks(tasks, new_tasks)
            else:
                print("No tasks found")
                self.search_menu()

    @pause_screen
    def edit_menu(self,tasks):
        ed = Edit(tasks)
        while True:
            clear()
            ed.print_task()
            choice = menu.make(menu.edit)
            try:
                if choice==1: # next
                    ed.next()
                elif choice==2: # previous
                    ed.previous()
                elif choice==3: # edit
                    old_task, new_task = ed.edit_task()
                    self.tl.edit(old_task, new_task)
                elif choice==4: # delete
                    old_task = ed.delete_task()
                    self.tl.delete(old_task)
                elif choice==5: # search menu
                    print("search menu")
                    self.search_menu()
                elif choice==6: # main menu
                    print("main menu")
                    self.main_menu()
            except IndexError as err:
                print(err)
                self.search_menu()

if __name__ == '__main__':
    """
    Creates an instance of our working class, and
    calls the run method which will handle the main problem logic.
    """
    d1 = datetime.strptime("20181105", fmt)
    d2 = datetime.strptime("20181106", fmt)
    ts = [('clean room', 15, d1, 'pick up under bed'),
        ('clean office', 20, d1, 'remove DMD'),
        ('treehouse practice', 60, d2, 'python'),
        ('treehouse project 3', 120, d2, 'work log'),
        ('check cryptocurrency', 15, d2, 'is bitcoin up?')]

    ts2 = [
    {'title': 'clean room', 'notes': 'pick up under bed', 'minutes': 15, 'date': '20181105'},
    {'title': 'clean office', 'notes': 'remove DMD', 'minutes': 20, 'date': '20181105'},
    {'title': 'treehouse practice', 'notes': 'python', 'minutes': 60, 'date': '20181205'},
    {'title': 'treehouse project 3', 'notes': 'work log', 'minutes': 120, 'date': '20181205'},
    {'title': 'check cryptocurrency', 'notes': 'is bitcoin up?', 'minutes': 15, 'date': '20181205'}
    ]
    tl = TaskList.create_tasklist(ts)
    write_tasks(tl)
    tl = TaskList.import_tasklist()
    for task in tl.tasks:
        print(task)




    #Worklog(ts).run()

    # logwrite()
    # writer.writeheader()

