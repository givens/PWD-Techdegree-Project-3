from utils import print_error, clear_screen
import time

main = [
'What would you like to do?',
'Add new entry',
'Search existing entries',
'Quit program',
]

search = [
'How would you like to search?',
'Exact Date',
'Range of Dates',
'Time',
'Exact Search',
'Pattern Search',
'Return to main menu',
]

edit = [
'How do you want to proceed?',
'Next',
'Previous',
'Edit',
'Delete',
'Return to search menu',
'Return to main menu',
]

def make(menu):

    for index, menu_item in enumerate(menu):
        if index==0:
            print(menu_item)
        else:
            print('{} - {}'.format(index, menu_item))
    choice = input('What would you like to do?  ')
    try:
        choice = int(choice)
        if choice not in range(1, len(menu)):
            raise ValueError("Menu choice not listed.")
    except ValueError as err:
        print_error(err)
        time.sleep(0.5)
        return make(menu)
    else:
        return choice




