"""
    file which deals with date object
"""
from datetime import date

class TodayDate:
    """
        return date object
    """
    def __init__(self):
        """
            initialized the necessary element for the date class
        """
        self.date = str(date.today())
        today_date = str(date.today())
        today_date = today_date.split("-")
        self.curr_year = int(today_date[0])
        self.curr_month = int(today_date[1])
        self.curr_date = int(today_date[2])

    def get_curr_year_month_date(self):
        """
            returns current year, month and date
        """
        return self.curr_year, self.curr_month, self.curr_date
