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
        self.text = name
        self.start, self.duration, self.end = start, None, end
        self.setupUi(parent)

    def set_text(self, text):
        self.label.setText(text)

    def update_info(self, data):
        self.set_text(data['name'])
