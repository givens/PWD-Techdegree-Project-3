from tasks import TaskList
from datetime import datetime
from utils import fmt
from entry import Entry
import pdb

class Edit:

    def __init__(self, tasks):
        self.tasks = tasks
        self.index = 0

    def __len__(self):
        return len(self.tasks)

    def print_tasks(self):
        if not self.tasks:
            raise IndexError("Finished.")
        for index, task in enumerate(tasks):
            print('{} - {}'.format(index, task))

    def print_task(self):
        print(self.tasks[self.index])

    def edit_task(self):
        self.tasks[self.index] = Entry().enter_all()

    def delete_task(self):
        del self.tasks[self.index]
        self.index = 0

    def next(self):
        self.index += 1
        if self.index>=len(self):
            raise IndexError("No more found.")

    def previous(self):
        #pdb.set_trace()
        self.index -= 1
        if self.index<0:
            raise IndexError("No more found.")
