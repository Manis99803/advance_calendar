"""
    Advance Calendar Application
"""
import sys
from month_calendar import MonthCalendar
from today_date import TodayDate
from calendar_interface import CalendarInterface

class Help:
    """
        Diplays the instruction about the application
    """
    def __init__(self):
        """
            initializes the help text
        """
        with open("help.txt") as file_reader:
            help_text = file_reader.readlines()

        self.help_text = [text.strip() for text in help_text]

    def print_help(self):
        """
            prints the instruction of running the application
        """
        for line in self.help_text:
            print(line)
        print()



if __name__ == "__main__":
    today_date = TodayDate()
    full_calendar = MonthCalendar(today_date)
    try:
        parameter = sys.argv[1]
        if parameter == "-help":
            Help().print_help()
        else:
            try:
                parameter = int(parameter)
                if parameter == 0:
                    calendar_date_info = full_calendar.get_month_calendar(today_date.curr_month)
                    cal_interface = CalendarInterface(calendar_date_info)
                    cal_interface.display_calendar()
                else:
                    updated_month = today_date.curr_month + parameter
                    if  1 <= updated_month <= 12:
                        today_date.curr_month = updated_month
                        calendar_date_info = full_calendar.get_month_calendar(updated_month)
                        cal_interface = CalendarInterface(calendar_date_info)
                        cal_interface.display_calendar()
                    else:
                        ERROR_MESSAGE = "Invalid input, updated month value expected " + \
                                        "to between [1, 12] \n" + \
                                        "Updated Month : %s" % updated_month
                        CalendarInterface.display_error_message(ERROR_MESSAGE)
            except ValueError:
                ERROR_MESSAGE = "Invalid input, input parameter expected be of type int" + "\n"
                CalendarInterface.display_error_message(ERROR_MESSAGE)

    except IndexError:
        calendar_date_info = full_calendar.get_month_calendar(today_date.curr_month)
        cal_interface = CalendarInterface(calendar_date_info)
        cal_interface.display_calendar()
