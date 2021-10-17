import ui_to_py

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui

from my_widgets.gui import Ui_MainWindow
import builders

import sys


ui_to_py.nothing()


class Director:
    def __init__(self):
        self.window = None

    def build_window(self):
        window = MainWindow()
        builders.MenuConnectBuilder(window)
        builders.HomeWidgetBuilder(window)
        builders.TaskListBuilder(window.home_widget_obj.nowScrollArea, window)
        builders.TaskListBuilder(window.home_widget_obj.futureScrollArea, window)
        builders.HistoryWidgetBuilder(window)
        builders.TaskListBuilder(window.history_widget_obj.pastScrollArea, window)
        builders.WidgetUpdateBuilder(window)
        builders.DaemonUpdateBuilder(window)
        builders.HomeAddTaskBuilder(window)
        self.window = window
        return window


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        width, height = a0.size().width(), a0.size().height()
        # print(width, height)
        self.centralwidget.setGeometry(0, 0, width, height)
        self.horizontalWidget.setGeometry(0, 0, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Director().build_window()
    sys.exit(app.exec_())
