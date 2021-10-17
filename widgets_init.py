from PyQt5.QtWidgets import QWidget, QFrame

from my_widgets import home_widget, task_widget, history_widget

from datetime import datetime as dt


class HomeWidget(home_widget.Ui_Frame, QWidget):
    def __init__(self, parent):
        super(HomeWidget, self).__init__()
        self.setupUi(parent)


class HistoryWidget(history_widget.Ui_HistoryWidget, QWidget):
    def __init__(self, parent):
        super(HistoryWidget, self).__init__()
        self.setupUi(parent)


class TaskWidget(task_widget.Ui_Frame, QFrame):
    def __init__(self, parent, id_, name: str, description: str, start: dt, end: dt or None):
        super(TaskWidget, self).__init__()
        self.text = self.set_text(name)
        self.start, self.duration, self.end = self.set_times(start, end)
        self.setupUi(parent)

    def text_for_label(self):
        return '|'.join(map(str, (self.text, self.start, self.duration)))

    @staticmethod
    def set_text(text):
        return text

    @staticmethod
    def set_times(start, end):
        # duration = None if end is None else start + end
        return start, None, end
