from PyQt5.QtWidgets import QWidget, QFrame
# from PyQt5.QtCore import QObject

from my_widgets import home_widget, task_widget, history_widget

from datetime import datetime as dt


class HomeWidget(home_widget.Ui_Frame, QWidget):
    def __init__(self, parent: QWidget):
        super(HomeWidget, self).__init__()
        self.setupUi(parent)


class HistoryWidget(history_widget.Ui_HistoryWidget, QWidget):
    def __init__(self, parent: QWidget):
        super(HistoryWidget, self).__init__()
        self.setupUi(parent)


class TaskWidget(task_widget.Ui_Frame, QFrame):
    def __init__(self, parent: QWidget, id_: int, name: str, description: str, start: dt, end: dt or None):
        self.id_ = id_
        self.description = description
        super(TaskWidget, self).__init__()
        self.text = name
        self.start, self.duration, self.end = start, None, end
        self.setupUi(parent)

    def set_text(self, text: str):
        self.title.setText(text)

    def update_info(self, data: dict):
        self.set_text(data['name'])
        self.startTime.setText(data['start'].strftime('%d.%m %H:%M'))
        self.endTime.setText(data['end'].strftime('%d.%m %H:%M'))

