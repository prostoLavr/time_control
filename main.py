from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QScrollArea, QVBoxLayout, QFrame
from PyQt5 import QtGui
from my_widgets.gui import Ui_MainWindow
from my_widgets.add_widget import Ui_Frame
from my_widgets.task_widget import Ui_Frame as Ui_TaskWidget

import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.my_setupUi()
        self.add_task()

    def my_setupUi(self):
        self.home_widget_obj = HomeWidget(self.add_widget)
        self.statictic_widget_obj = StatisticWidget(self.statictic_widget)
        self.buttons_connect()
        self.close_all()
        self.show()

    def buttons_connect(self):
        self.menu_buttons = (self.homeButton, self.historyButton, self.statisticButton, self.settingsButton)
        for button in self.menu_buttons:
            button.clicked.connect(self.menu_button_click)
        self.buttons_action_dct = {'Домой': self.show_home, 'Статистика': self.show_statistic,
                                   'История': self.close_all, 'Настройки': self.close_all}

    def close_all(self):
        self.close_statistic()
        self.close_home()

    def show_home(self):
        self.close_all()
        self.add_widget.show()

    def close_home(self):
        self.add_widget.hide()

    def show_statistic(self):
        self.close_all()
        self.statictic_widget.show()

    def close_statistic(self):
        self.statictic_widget.hide()

    def menu_button_click(self):
        for button in self.menu_buttons:
            button.setStyleSheet('')
        self.sender().setStyleSheet('background: "#AAA";')
        print(f'open {self.sender().text()}')
        self.buttons_action_dct[self.sender().text()]()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        width, height = a0.size().width(), a0.size().height()
        hp = height / 100
        wp = width / 100
        self.centralwidget.setGeometry(0, 0, width, height)
        # self.homeButton.setFixedHeight(round(90 * hp))
        self.settingsButton.setMaximumHeight(round(10*hp))
        self.horizontalWidget.setGeometry(0, 0, width, height)
        # self.leftWidget.setGeometry(0, 0, 50*wp, height)

    def add_task(self):
        new_task = TaskWidget('hello', 15, 5, self.statictic_widget_obj)
        self.statictic_widget_obj.my_layout.addStretch(1)
        self.statictic_widget_obj.my_layout.addWidget(new_task)


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
        self.set_text(text)
        self.set_times(time_start, long_time)
        self.setupUi(parent)

    def text_for_label(self):
        return '|'.join(map(str, (self.text, self.time_start, self.long_time)))

    def set_text(self, text):
        self.text = text

    def set_times(self, time_start, long_time):
        self.time_start = time_start
        self.long_time = long_time
        self.end_time = time_start + long_time


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
