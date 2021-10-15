from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from my_widgets.gui import Ui_MainWindow
import widgets_init


import sys


class Director:
    def __init__(self):
        self.window = None

    def build_window(self):
        window = SetupMainWindow()
        MenuConnectBuilder(window)
        ButtonConnectBuilder(window)
        self.window = window
        return window


class SetupMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.my_setupUi()

    def my_setupUi(self):
        self.home_widget_obj = widgets_init.HomeWidget(self.add_widget)
        self.statistic_widget_obj = widgets_init.StatisticWidget(self.statictic_widget)
        self.show()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        width, height = a0.size().width(), a0.size().height()
        hp = height / 100
        self.centralwidget.setGeometry(0, 0, width, height)
        self.settingsButton.setMaximumHeight(round(10*hp))
        self.horizontalWidget.setGeometry(0, 0, width, height)


class MenuConnectBuilder:
    def __init__(self, window):
        self.window = window
        self.menu_buttons_connect()
        self.close_all()

    def menu_buttons_connect(self):
        self.window.menu_buttons = (self.window.homeButton, self.window.historyButton, self.window.statisticButton,
                             self.window.settingsButton)
        for button in self.window.menu_buttons:
            button.clicked.connect(self.menu_button_click)
        self.window.buttons_action_dct = {'Домой': self.show_home, 'Статистика': self.show_statistic,
                                          'История': self.close_all, 'Настройки': self.close_all}

    def close_all(self):
        self.close_statistic()
        self.close_home()

    def show_home(self):
        self.close_all()
        self.window.add_widget.show()

    def close_home(self):
        self.window.add_widget.hide()

    def show_statistic(self):
        self.close_all()
        self.window.statictic_widget.show()

    def close_statistic(self):
        self.window.statictic_widget.hide()

    def menu_button_click(self):
        for button in self.window.menu_buttons:
            button.setStyleSheet('')
        self.window.sender().setStyleSheet('background: "#AAA";')
        print(f'Открыта вкладка {self.window.sender().text()}')
        self.window.buttons_action_dct[self.window.sender().text()]()


class ButtonConnectBuilder:
    def __init__(self, window):
        self.window = window
        self.connect_button()

    def connect_button(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Director().build_window()
    sys.exit(app.exec_())
