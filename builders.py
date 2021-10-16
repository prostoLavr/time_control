from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QSize, QThread, QObject
import worker


from datetime import datetime as dt
import widgets_init


class HomeWidgetBuilder:
    def __init__(self, window):
        self.window = window
        self.widget_init()

    def widget_init(self):
        self.window.home_widget_obj = widgets_init.HomeWidget(self.window.add_widget)


class HistoryWidgetBuilder:
    def __init__(self, window):
        self.window = window
        self.widget_init()

    def widget_init(self):
        self.window.history_widget_obj = widgets_init.HistoryWidget(self.window.history_widget)


class MenuConnectBuilder:
    def __init__(self, window):
        self.window = window
        self.menu_buttons_connect()
        self.close_all()

    def menu_button_click(self):
        for button in self.window.menu_buttons:
            button.setStyleSheet('')
        self.window.sender().setStyleSheet('background: "#AAA";')
        print(f'Открыта вкладка {self.window.sender().text()}')
        self.window.buttons_action_dct[self.window.sender().text()]()

    def menu_buttons_connect(self):
        self.window.menu_buttons = (self.window.homeButton, self.window.historyButton, self.window.statisticButton,
                                    self.window.settingsButton)
        for button in self.window.menu_buttons:
            button.clicked.connect(self.menu_button_click)
        self.window.buttons_action_dct = {'Домой': self.show_home, 'Статистика': self.show_statistic,
                                          'История': self.show_history, 'Настройки': self.close_all}

    def close_all(self):
        self.window.statictic_widget.hide()
        self.window.add_widget.hide()
        self.window.history_widget.hide()
        self.window.settings_widget.hide()

    def show_home(self):
        self.close_all()
        self.window.add_widget.show()

    def show_statistic(self):
        self.close_all()
        self.window.statictic_widget.show()

    def show_history(self):
        self.close_all()
        self.window.history_widget.show()


class TaskListBuilder:
    def __init__(self, scroll, parent):
        self.window = parent
        self.scroll = scroll
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        self.widget.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        w = parent.width()
        h = parent.height()
        self.scroll.resize(QSize(w // 2, h))

        for _ in range(10):
            self.add_test_task()

    def add_test_task(self):
        widget = QWidget(self.window)
        task = widgets_init.TaskWidget('test', dt(1, 1, 1, 1, 1), None, widget)
        widget.task = task
        self.vbox.addWidget(widget)

    def add_test_tasks(self):
        for _ in range(10):
            self.add_test_task()


class UpdateBuilder:
    def __init__(self, window):
        window.obj = worker.Worker()
        window.thread = QThread()

        window.obj.update.connect(window.db_update)
        window.obj.moveToThread(window.thread)
        window.obj.destroyed.connect(window.thread.quit)
        window.thread.started.connect(window.obj.procCounter)
        window.thread.start()
