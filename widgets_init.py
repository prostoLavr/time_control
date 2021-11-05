from PyQt5.QtWidgets import QWidget, QFrame
# from PyQt5.QtCore import QObject

from status import Status

from my_widgets import home_widget, task_widget, history_widget, statistic_widget

from datetime import datetime as dt


class HomeWidget(home_widget.Ui_Frame, QWidget):
    def __init__(self, parent: QWidget):
        super(HomeWidget, self).__init__()
        self.setupUi(parent)


class HistoryWidget(history_widget.Ui_HistoryWidget, QWidget):
    def __init__(self, parent: QWidget):
        super(HistoryWidget, self).__init__()
        self.setupUi(parent)


class StatisticWidget(statistic_widget.Ui_StatisticWidget, QWidget):
    def __init__(self, parent: QWidget):
        super(StatisticWidget, self).__init__()
        self.setupUi(parent)


class TaskWidget(task_widget.Ui_Frame, QFrame):
    def __init__(self, window, parent: QWidget, id_: int, name: str, description: str,
                 start: dt, end: dt or None, status: Status):
        self.my_parent = window
        self.id_ = id_
        self.description = description
        super(TaskWidget, self).__init__()
        self.text = name
        self.start, self.duration, self.end = start, None, end
        self.setupUi(parent)
        self.checkBox.setChecked(status == Status.done)
        self.refactor(status)
        self.checkBox.clicked.connect(self.set_like_checkbox)

    def set_text(self, text: str):
        self.title.setText(text)

    def update_info(self, data: dict):
        self.set_text(data['name'])
        self.startTime.setText('C ' + data['start'].strftime('%d.%m %H:%M'))
        self.endTime.setText('По сейчас' if data['end'] is None else 'По ' + data['end'].strftime('%d.%m %H:%M'))

    def set_run_by_btn(self):
        self.my_parent.db.set_task_status(self.id_, Status.run.value)
        self.set_run()
        self.my_parent.db_update()

    def set_like_checkbox(self):
        value = Status.from_checkbox(self.checkBox.checkState())
        self.refactor(value)
        self.my_parent.db_update()

    def refactor(self, value):
        self.my_parent.db.set_task_status(self.id_, value.value)
        if value == Status.run:
            self.set_run()
        if value == Status.notdone:
            self.set_not_done()
        if value == Status.done:
            self.set_done()
        self.display_difference()

    def display_difference(self):
        self.update_info({'name': self.text, 'start': self.start, 'end': self.end})

    def set_run(self):
        self.adaptateButton.setText('Завершить сейчас')
        self.start = dt.now()
        self.adaptateButton.clicked.connect(self.set_done_by_btn)
        if self.end is None:
            self.adaptateButton.hide()
        else:
            self.adaptateButton.show()

    def set_done_by_btn(self):
        self.my_parent.db.set_task_status(self.id_, Status.done.value)
        self.set_done()
        self.end = dt.now()
        self.checkBox.setChecked(True)
        self.my_parent.db_update()

    def set_not_done(self):
        self.adaptateButton.setText('Начать')
        self.adaptateButton.clicked.connect(self.set_run_by_btn)
        self.adaptateButton.show()

    def set_done(self):
        if not self.end:
            self.end = dt.now()
            self.my_parent.db.set_end_time(self.id_, self.end)
        self.adaptateButton.setText('Завершено')
        self.adaptateButton.hide()
