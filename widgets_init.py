from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QFrame

from my_widgets.add_widget import Ui_Frame
from my_widgets.task_widget import Ui_Frame as Ui_TaskWidget


class HomeWidget(Ui_Frame, QWidget):
    def __init__(self, parent):
        super(HomeWidget, self).__init__()
        self.setupUi(parent)


class StatisticWidget(QScrollArea):
    def __init__(self, parent):
        super(StatisticWidget, self).__init__(parent)
        self.my_layout = QVBoxLayout(self)
        self.setLayout(self.my_layout)


class TaskWidget(Ui_TaskWidget, QFrame):
    def __init__(self, text, time_start, long_time,  parent):
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
        time_end = time_start + duration
        return time_start, time_end, duration
