"""
    file which deals with generating month calendar
"""
import calendar

class MonthCalendar:
    """
        displays the full calendar
    """
    def __init__(self, today_date):
        """
            constructor for initializng the necessary items for full calendar class
        """
        self.today_date = today_date

    def highlight_current_date(self, month_calendar):
        """
            highlights the current date
        """
        row_index = 3
        cal_len = len(month_calendar)

        date_str_length = int()
        date_row_index = int()
        date_col_index = int()
        for j in range(2, cal_len):
            dates = month_calendar[j]
            dates_len = len(dates)
            column_index = 1
            for i in range(dates_len):
                if dates[i] == str(self.today_date.curr_date):
                    return row_index, column_index, 1
                elif (i + 1) < dates_len and \
                    ((dates[i] + dates[i + 1]) == str(self.today_date.curr_date)):
                    return row_index, column_index + 1, 2
                column_index += 1
            row_index += 1

        return date_row_index, date_col_index, date_str_length

    def get_month_calendar(self, month):
        """
            returns full month calendar for the given month
        """
        calendar_date_info = dict()
        month_calendar = calendar.month(self.today_date.curr_year, month)
        month_calendar = month_calendar.split("\n")
        row_index, column_index, date_len = self.highlight_current_date(month_calendar)
        month_calendar_str = str()
        for row in month_calendar:
            month_calendar_str += (row + "\n")
        calendar_date_info["month_calendar"] = month_calendar_str
        calendar_date_info["row_index"] = row_index
        calendar_date_info["column_index"] = column_index
        calendar_date_info["date_len"] = date_len
        return calendar_date_info
