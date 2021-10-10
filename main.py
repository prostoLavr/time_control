from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from my_widgets.gui import Ui_MainWindow
import widgets_init


import sys


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
        # wp = width / 100
        self.centralwidget.setGeometry(0, 0, width, height)
        self.settingsButton.setMaximumHeight(round(10*hp))
        self.horizontalWidget.setGeometry(0, 0, width, height)


class MenuConnectMainWindow(SetupMainWindow):
    def __init__(self, *args, **kwargs):
        super(MenuConnectMainWindow, self).__init__(*args, **kwargs)
        self.menu_buttons_connect()
        self.close_all()

    def menu_buttons_connect(self):
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
        print(f'Открыта вкладка {self.sender().text()}')
        self.buttons_action_dct[self.sender().text()]()


class ButtonConnectMainWindow(MenuConnectMainWindow):
    def __init__(self, *args, **kwargs):
        super(ButtonConnectMainWindow, self).__init__(*args, **kwargs)
        self.connect_button()

    def connect_button(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonConnectMainWindow()
    sys.exit(app.exec_())
