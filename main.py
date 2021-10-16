import ui_to_py

ui_to_py.convert()

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui

import table_and_data
from my_widgets.gui import Ui_MainWindow
import builders

from datetime import datetime as dt
import sys


class Director:
    def __init__(self):
        self.data = table_and_data.DataManager()
        self.window = None

    def build_window(self):
        window = SetupMainWindow()
        builders.MenuConnectBuilder(window)
        builders.HomeWidgetBuilder(window)
        builders.TaskListBuilder(window.home_widget_obj.nowScrollArea, window)
        builders.TaskListBuilder(window.home_widget_obj.futureScrollArea, window)
        builders.HistoryWidgetBuilder(window)
        builders.TaskListBuilder(window.history_widget_obj.historyScrollArea, window)
        builders.WidgetUpdateBuilder(window)
        builders.DaemonUpdateBuilder(window)
        window.home_widget_obj.futureScrollArea.add_task(window, id_=1, name='tk', description='des', start=dt(1, 1, 1, 1, 1),
                                                         end=dt(1, 1, 1, 1, 1))
        self.window = window
        return window


class SetupMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        width, height = a0.size().width(), a0.size().height()
        hp = height / 100
        self.centralwidget.setGeometry(0, 0, width, height)
        self.settingsButton.setMaximumHeight(round(10 * hp))
        self.horizontalWidget.setGeometry(0, 0, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Director().build_window()
    sys.exit(app.exec_())
