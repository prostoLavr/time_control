from PyQt5.QtWidgets import QWidget, QFrame

from my_widgets import add_widget, task_widget, history_widget

from datetime import datetime as dt


class HomeWidget(add_widget.Ui_Frame, QWidget):
    def __init__(self, parent):
        super(HomeWidget, self).__init__()
        self.setupUi(parent)


class TaskWidget(task_widget.Ui_Frame, QFrame):
    def __init__(self, text: str, time_start: dt, long_time: dt or None,  parent):
        super(TaskWidget, self).__init__()
        self.text = self.set_text(text)
        self.time_start, self.duration, self.time_end = self.set_times(time_start, long_time)
        self.setupUi(parent)

    def text_for_label(self):
        return '|'.join(map(str, (self.text, self.time_start, self.long_time)))

    @staticmethod
    def set_text(text):
        return text

    @staticmethod
    def set_times(time_start, duration):
        time_end = None if duration is None else time_start + duration
        return time_start, time_end, duration
