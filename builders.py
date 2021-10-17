from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QSize, QThread
import worker
import db_director


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

        self.add_remove()
        # for i in range(10):
        #     self.scroll.add_task(self.window, id_=i, name='tk', description='des', start=dt(1, 1, 1, 1, 1),
        #                          end=dt(1, 1, 1, 1, 1))

    def add_remove(self):
        def add_task(parent, **param_for_task):
            widget = QWidget(parent)
            task = widgets_init.TaskWidget(widget, **param_for_task)
            widget.task = task
            self.scroll.tasks.update({param_for_task['id_']: widget})
            self.scroll.vbox.addWidget(widget)
            print('add')

        def remove_task(id_):
            if id_ in self.scroll.tasks.keys():
                self.scroll.vbox.removeWidget(self.scroll.tasks[id_])
                self.scroll.tasks[id_].deleteLater()
                del self.scroll.tasks[id_]
                print('remove')
            else:
                print('id_ was not found')

        self.scroll.add_task = add_task
        self.scroll.remove_task = remove_task


class WidgetUpdateBuilder:
    def __init__(self, window):
        self.window = window
        self.window.db = db_director.DataBase('./db.sqlite')
        self.connect()

    def connect(self):
        def update():
            print('Updating...')
            for data in self.window.db.now():
                self.set_difference(self.window.home_widget_obj.nowScrollArea, data)
            # self.window.home_widget_obj.nowScrollArea.add_task(self.window, id_=1, name='Hello',
            #                                                    description='None', start=dt(1, 1, 1, 1, 1),
            #                                                    end=dt(1, 1, 1, 1, 1))
            # self.window.home_widget_obj.futureScrollArea.remove_task(id_)

        self.window.db_update = update

    def set_difference(self, scroll, data):
        scroll.tasks[data['id_']].set_text(data['name'])
        scroll.tasks[data['id_']].set_times(data['start'], data['end'])

    def add_news(self, scroll, datas):
        for data in datas:
            scroll.add_task(**data)

    def remove_olds(self, scroll, datas):
        for data in datas:
            scroll.remove_task(data['id_'])


class DaemonUpdateBuilder:
    def __init__(self, window):
        window.obj = worker.Worker()
        window.thread = QThread()

        window.obj.db_update.connect(window.db_update)
        window.obj.moveToThread(window.thread)
        window.obj.destroyed.connect(window.thread.quit)
        window.thread.started.connect(window.obj.procCounter)
        window.thread.start()
