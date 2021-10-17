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
    def __init__(self, window, parent: QWidget, id_: int, name: str, description: str,
                 start: dt, end: dt or None, status: int):
        self.my_parent = window
        self.id_ = id_
        self.description = description
        super(TaskWidget, self).__init__()
        self.text = name
        self.start, self.duration, self.end = start, None, end
        self.setupUi(parent)
        self.checkBox.setChecked(status == 2)
        self.refactor(status)
        self.checkBox.clicked.connect(self.set_like_checkbox)

    def set_text(self, text: str):
        self.title.setText(text)

    def update_info(self, data: dict):
        self.set_text(data['name'])
        self.startTime.setText(data['start'].strftime('%d.%m %H:%M'))
        self.endTime.setText('Идёт...' if data['end'] is None else data['end'].strftime('%d.%m %H:%M'))

    def set_like_checkbox(self):
        value = self.checkBox.checkState()
        self.refactor(value)

    def refactor(self, value):
        self.my_parent.db.set_task_status(self.id_, value)
        if value == 0:
            self.set_run()
        if value == 1:
            self.set_not_done()
        if value == 2:
            self.set_done()

    def run(self):
        self.adaptateButton.setText('Завершить')

    def set_not_done(self):
        self.adaptateButton.setText('Начать')
        self.adaptateButton.show()

    def set_done(self):
        self.adaptateButton.setText('Завершенно')
        self.adaptateButton.hide()
