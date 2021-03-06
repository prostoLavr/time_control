import sys
from PyQt5.QtWidgets import QApplication


def main():
    from PyQt5.QtWidgets import QMainWindow
    from PyQt5 import QtGui

    from my_widgets.gui import Ui_MainWindow
    import builders

    class Director:
        @staticmethod
        def build_window():
            window = MainWindow()
            builders.MenuConnectBuilder(window)

            builders.HomeWidgetBuilder(window)
            builders.TaskListBuilder(window.home_widget_obj.nowScrollArea, window)
            builders.TaskListBuilder(window.home_widget_obj.futureScrollArea, window)

            builders.HistoryWidgetBuilder(window)
            builders.TaskListBuilder(window.history_widget_obj.pastScrollArea, window)

            builders.StatisticWidgetBuilder(window)

            builders.WidgetUpdateBuilder(window)
            builders.DaemonUpdateBuilder(window)

            builders.GraphDiagramBuilder(window)

            builders.HomeAddTaskBuilder(window)

            window.db_update()

            return window

    class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.setupUi(self)
            self.show()

        def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
            width, height = a0.size().width(), a0.size().height()
            self.centralwidget.setGeometry(0, 0, width, height)
            self.horizontalWidget.setGeometry(0, 0, width, height)

    app = None
    try:
        app = QApplication(sys.argv)
        ex = Director.build_window()
    finally:
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()

