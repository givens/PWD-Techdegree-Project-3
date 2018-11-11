from tasks import TaskList
from datetime import datetime
from utils import fmt, print_error
import pdb

class Search:

    def search_by_date(self, tl):
        "Search by user-entered date string"
        print("Search by exact date")
        date_str = input("Please use YYYYMMDD:  ")
        try:
            date = datetime.strptime(date_str, fmt)
        except ValueError as err:
            print_error(err)
            return self.search_by_date(tl)
        else:
            return tl.findall_date(date)

    def search_by_date_range(self, tl):
        "Search by user-entered date range"
        pdb.set_trace()
        print("Search by date range")
        dates = input("Please use YYYYMMDD-YYYYMMDD for date range:  ")
        date1_str, date2_str = dates.split('-')
        try:
            date1 = datetime.strptime(date1_str, fmt)
            date2 = datetime.strptime(date2_str, fmt)
        except ValueError as err:
            print_error(err)
            return self.search_by_date_range(tl)
        else:
            return tl.findall_date_range(date1, date2)

    def search_by_time(self, tl):
        "Search by unser-entered time in minutes"
        print("Search by minutes")
        minutes = input("Please enter the number of minutes for the task:  ")
        try:
            minutes = int(minutes)
        except ValueError as err:
            print_error(err)
            return self.search_by_time(tl)
        else:
            return tl.findall_time(minutes)

    def search_by_contains(self, tl):
        "Search task title and notes by user-entered string"
        print("Search by string")
        string = input("Please enter search string:  ")
        return tl.findall_contains(string)

    def search_by_pattern(self, tl):
        "Search task title and notes by user-entered regex pattern"
        print("Search by regex pattern")
        pattern = input("Please enter search pattern:  ")
        return tl.findall_pattern(pattern)









