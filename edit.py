"""
edit.py
-------
Edits module for editing and deleting tasks.
"""

import entry


class Edit:
    "Edit class modifies tasks and moves through them."

    def __init__(self, tasks):
        """Set tasks and index"""
        self.tasks = tasks
        self.index = 0

    def __len__(self):
        """Return length of taksk"""
        return len(self.tasks)

    def print_task(self):
        """Prints current task in list"""
        if self.index < 0 or self.index >= len(self):
            raise IndexError("No more found.")
        print(self.tasks[self.index])

    def edit_task(self):
        """Edits current task in list"""
        old_task = self.tasks[self.index]
        self.tasks[self.index] = entry.Entry().enter_all()
        new_task = self.tasks[self.index]
        self.index = 0
        return old_task, new_task

    def delete_task(self):
        """Deletes current task in list"""
        old_task = self.tasks[self.index]
        del self.tasks[self.index]
        self.index = 0
        return old_task

    def next(self):
        """Moves to next task in list"""
        self.index += 1
        if self.index >= len(self):
            raise IndexError("No more found.")

    def previous(self):
        """Moves to previous task in list"""
        self.index -= 1
        if self.index < 0:
            raise IndexError("No more found.")
