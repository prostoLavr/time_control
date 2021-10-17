import typing

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QScrollArea
from PyQt5.QtCore import Qt, QSize, QThread
from PyQt5 import QtGui
import worker
import db_director


from datetime import datetime as dt
from datetime import time as tm

import widgets_init


class HomeWidgetBuilder:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.widget_init()

    def widget_init(self):
        self.window.home_widget_obj = widgets_init.HomeWidget(self.window.add_widget)


class HistoryWidgetBuilder:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.widget_init()

    def widget_init(self):
        self.window.history_widget_obj = widgets_init.HistoryWidget(self.window.history_widget)


class MenuConnectBuilder:
    def __init__(self, window: QMainWindow):
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
    def __init__(self, scroll: QScrollArea, parent: QWidget):
        self.window = parent
        self.scroll = scroll
        self.widget = QWidget()
        self.scroll.vbox = QVBoxLayout()
        self.scroll.tasks = {}

        self.widget.setLayout(self.scroll.vbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        w = parent.width()
        h = parent.height()
        self.scroll.resize(QSize(w // 2, h))

        self.add_remove_setup()

    def add_remove_setup(self):
        def add_task(parent, **param_for_task):
            widget = QWidget(parent)
            task = widgets_init.TaskWidget(self.window, widget, **param_for_task)
            widget.task = task
            self.scroll.tasks.update({param_for_task['id_']: widget})
            self.scroll.vbox.addWidget(widget)

        def remove_task(id_: int):
            if id_ in self.scroll.tasks.keys():
                self.scroll.vbox.removeWidget(self.scroll.tasks[id_])
                self.scroll.tasks[id_].deleteLater()
                del self.scroll.tasks[id_]
            else:
                print('id_ was not found')

        self.scroll.add_task = add_task
        self.scroll.remove_task = remove_task


class WidgetUpdateBuilder:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.window.db = db_director.DataBase('./db.sqlite')

        self.connect()
        self.history_find_connect()

    def history_find_connect(self):
        def btn_clicked():
            start = self.window.history_widget_obj.startDateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
            end = self.window.history_widget_obj.endDateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
            print('find: ', start, '-', end)
            print('found: ', *self.window.db.find(start, end))
            self.connect_(self.window.history_widget_obj.pastScrollArea, self.window.db.find(start, end))
        self.window.history_widget_obj.find_btn.clicked.connect(btn_clicked)

    def connect(self):
        def update():
            print('Updating...')
            self.connect_(self.window.home_widget_obj.nowScrollArea, self.window.db.now())
            self.connect_(self.window.home_widget_obj.futureScrollArea, self.window.db.future())

        self.window.db_update = update

    def connect_(self, scroll: QScrollArea, data: typing.Iterable):
        data = list(data)
        self.add_news(scroll, data)
        self.set_differences(scroll, data)
        self.remove_olds(scroll, data)

    @staticmethod
    def set_differences(scroll: QScrollArea, data: typing.Iterable):
        keys = tuple(scroll.tasks.keys())
        for item in data:
            if item['id_'] in keys:
                # print('edit', data)
                scroll.tasks[item['id_']].task.update_info(item)
            else:
                print(f'task {item["id_"]=} was not found while sef_difference')

    def add_news(self, scroll: QScrollArea, data: typing.Iterable):
        keys = tuple(scroll.tasks.keys())
        for item in data:
            if item['id_'] not in keys:
                print('add', item)
                scroll.add_task(self.window, **item)

    @staticmethod
    def remove_olds(scroll: QScrollArea, data: typing.Iterable):
        data = list(data)
        for id_ in list(scroll.tasks.keys()):
            if id_ not in [x['id_'] for x in data]:
                print('remove', id_, 'from', scroll.objectName())
                scroll.remove_task(id_)


class DaemonUpdateBuilder:
    def __init__(self, window: QMainWindow):
        window.obj = worker.Worker()
        window.thread = QThread()

        window.obj.db_update.connect(window.db_update)
        window.obj.moveToThread(window.thread)
        window.obj.destroyed.connect(window.thread.quit)
        window.thread.started.connect(window.obj.procCounter)
        window.thread.start()


class HomeAddTaskBuilder:
    def __init__(self, window):
        self.window = window
        self.connect()

    def connect(self):
        time = dt.now()
        minutes = (time.minute + 30) % 60
        hours = (time.hour + (time.minute + 30) % 60) % 24
        self.window.home_widget_obj.dateTimeStart.setDateTime(time.replace(hour=hours, minute=minutes))
        self.window.home_widget_obj.timeDoing.setTime(tm(0, 30))

        self.window.home_widget_obj.taskNameEdit.setText('')

        def foo():
            name = self.window.home_widget_obj.taskNameEdit.text()
            if name:
                self.window.db.start_now(name)
                self.window.home_widget_obj.taskNameEdit.setText('')
            self.window.db_update()

        self.window.home_widget_obj.startTaskButton.clicked.connect(foo)

        def foo():
            name = self.window.home_widget_obj.taskNameEdit.text()
            if name:
                start = self.window.home_widget_obj.dateTimeStart.dateTime()
                duration = self.window.home_widget_obj.timeDoing.time()
                self.window.db.add_to_time(name, start, duration)
                self.window.home_widget_obj.taskNameEdit.setText('')
            self.window.db_update()

        self.window.home_widget_obj.addTaskButton.clicked.connect(foo)
