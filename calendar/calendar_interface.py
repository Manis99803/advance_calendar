"""
    Calendar Interface File
"""

from tkinter import Tk, Text, mainloop, END, DISABLED

class CalendarInterface:
    """
        Class for displaying the calendar in graphical way
    """
    def __init__(self, calendar_date_info):
        """
            initializing all the necessary elements required for building
            calendar UI
        """
        self.row_index = calendar_date_info["row_index"]
        self.column_index = calendar_date_info["column_index"]
        self.month_calendar = calendar_date_info["month_calendar"]
        self.date_len = calendar_date_info["date_len"]

    def display_calendar(self):
        """
            displays the calendar
        """
        root = Tk()
        root.title("Calendar")
        ui_text = Text(root, height=8, width=22)
        ui_text.pack(padx=20, pady=20)
        ui_text.insert(END, self.month_calendar,)
        if self.date_len == 1:
            ui_text.tag_add("date", str(self.row_index) + "." + str(self.column_index - 1),
                            str(self.row_index) + "." + str(self.column_index))
        else:
            ui_text.tag_add("date", str(self.row_index) + "." + str(self.column_index - 2),
                            str(self.row_index) + "." + str(self.column_index))
        ui_text.tag_config("date", background="black", foreground="white")
        ui_text.config(state=DISABLED)
        mainloop()

    @staticmethod
    def display_error_message(error_message):
        """
            displays the error message
        """
        root = Tk()
        root.title("Error message")
        ui_text = Text(root, height=10, width=50)
        ui_text.pack(padx=20, pady=20)
        ui_text.insert(END, error_message)
        ui_text.config(state=DISABLED)
        mainloop()
