import typing
import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QScrollArea, QLabel, QWidgetItem, QSpacerItem
from PyQt5.QtCore import Qt, QSize, QThread
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.Qt import QColor
import worker
import db_director


from datetime import datetime as dt, timedelta as td, time as tm

import widgets_init


db_path = sys.argv[1]


class HomeWidgetBuilder:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.widget_init()

    def widget_init(self):
        self.window.home_widget_obj = widgets_init.HomeWidget(self.window.add_widget)


class StatisticWidgetBuilder:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.widget_init()

    def widget_init(self):
        self.window.statistic_widget_obj = widgets_init.StatisticWidget(self.window.statistic_widget)


class GraphDiagramBuilder:
    def __init__(self, window):
        self.window = window
        window.scene = QGraphicsScene(window.statistic_widget_obj.graphStatisticWidget)
        window.update_graph = self.update
        window.statistic_widget_obj.comboBox.currentIndexChanged.connect(self.update)

    def db_query(self, count=6):
        state = self.window.statistic_widget_obj.comboBox.currentText()
        state_dict = {'День': td(days=1), 'Неделя': td(weeks=1), 'Полмесяца': td(days=15), 'Месяц': td(days=30),
                      'Квартал': td(days=90), 'Полугодие': td(days=180), 'Год': td(days=365)}
        db_respond = self.window.db.find_by_pytime(dt.now() - state_dict[state], dt.now())
        times = []
        keys = []
        for i in db_respond:
            if i['name'].lower() not in keys:
                keys.append(i['name'].lower())
                times.append(i['end'] - i['start'])
            else:
                times[keys.index(i['name'].lower())] += i['end'] - i['start']
        lst = sorted(zip(keys, map(lambda x: x.seconds, times)), key=lambda x: x[1], reverse=True)
        other_time = sum(times[count:])
        res_names = [x[0] for x in lst[:count - 1]]
        res_names.append('Другое')
        res_times = [x[1] for x in lst[:count - 1]]
        res_times.append(other_time)
        return res_names, res_times

    def update(self):
        window = self.window
        self.clear_layout(window.statistic_widget_obj.textStatisticLayout)
        names, times = self.db_query()
        if not times or not sum(times):
            window.statistic_widget_obj.graphStatisticWidget.hide()
            return
        window.statistic_widget_obj.graphStatisticWidget.show()
        colors_ = ((200, 0, 0), (250, 150, 0), (0, 200, 0), (0, 200, 200), (0, 0, 200), (200, 0, 200), (0, 0, 0))
        colors = [QColor(*i) for i in colors_]

        self.draw(times, colors, window)
        self.set_texts(names, times, colors, window)

    @classmethod
    def set_texts(cls, names, times, colors, window):
        for name, time, color in zip(names, times, colors):
            time = time // 60
            hours = time // 60
            minutes = time % 60
            text = f'{name.capitalize()} -'
            if hours:
                text += f' {hours} час' if hours % 10 == 1 else f' {hours} часов'
            if minutes:
                text += f' {minutes} минута' if minutes % 10 == 1 else f' {minutes} минут'
            if not hours and not minutes:
                text += ' Меньше минуты'
            lbl = QLabel(text)
            lbl.setStyleSheet('QLabel { color: %s }' % (color.name()))
            window.statistic_widget_obj.textStatisticLayout.addWidget(lbl)

    @classmethod
    def clear_layout(cls, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if isinstance(item, QWidgetItem):
                item.widget().close()
            elif not isinstance(item, QSpacerItem):
                cls.clear_layout(item.layout())
            layout.removeItem(item)

    @staticmethod
    def draw(times, colors, window):
        start_angle = 0
        total = sum(times)
        for num, time in enumerate(times):
            # Max span is 5760, so we have to calculate corresponding span angle
            angle = round(time * 5760 / total)
            ellipse = QGraphicsEllipseItem(0, 0, 300, 300)
            ellipse.setPos(0, 0)
            ellipse.setStartAngle(start_angle)
            ellipse.setSpanAngle(angle)
            ellipse.setBrush(colors[num])
            start_angle += angle
            window.scene.addItem(ellipse)

        window.view = QGraphicsView(window.scene, window.statistic_widget_obj.graphStatisticWidget)
        window.view.setHorizontalScrollBarPolicy(False)
        window.view.setVerticalScrollBarPolicy(False)
        window.view.show()


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
        self.window.buttons_action_dct[self.window.sender().text()]()

    def menu_buttons_connect(self):
        self.window.menu_buttons = (self.window.homeButton, self.window.historyButton, self.window.statisticButton)
        for button in self.window.menu_buttons:
            button.clicked.connect(self.menu_button_click)
        self.window.buttons_action_dct = {'Домой': self.show_home, 'Статистика': self.show_statistic,
                                          'История': self.show_history, 'Настройки': self.close_all}

    def close_all(self):
        self.window.statistic_widget.hide()
        self.window.add_widget.hide()
        self.window.history_widget.hide()

    def show_home(self):
        self.close_all()
        HomeAddTaskBuilder.time_set(self)
        self.window.add_widget.show()

    def show_statistic(self):
        self.close_all()
        self.window.update_graph()
        self.window.statistic_widget.show()

    def show_history(self):
        self.close_all()
        self.window.history_widget_obj.endDateTimeEdit.setDateTime(dt.now())
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
        self.window.db = db_director.DataBase(db_path)

        self.connect()
        self.history_find_connect()

    def history_find_connect(self):
        def btn_clicked():
            start = self.window.history_widget_obj.startDateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
            end = self.window.history_widget_obj.endDateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
            self.connect_(self.window.history_widget_obj.pastScrollArea, self.window.db.find(start, end))
        self.window.history_widget_obj.find_btn.clicked.connect(btn_clicked)

    def connect(self):
        def update():
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
                scroll.tasks[item['id_']].task.update_info(item)
            else:
                print(f'task {item["id_"]=} was not found while set_difference')

    def add_news(self, scroll: QScrollArea, data: typing.Iterable):
        keys = tuple(scroll.tasks.keys())
        for item in data:
            if item['id_'] not in keys:
                scroll.add_task(self.window, **item)

    @staticmethod
    def remove_olds(scroll: QScrollArea, data: typing.Iterable):
        data = list(data)
        for id_ in list(scroll.tasks.keys()):
            if id_ not in [x['id_'] for x in data]:
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
        self.window.home_widget_obj.taskNameEdit.setText('')
        self.time_set(self)

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

    @staticmethod
    def time_set(self):
        time = dt.now()
        minutes = (time.minute + 30) % 60
        hours = (time.hour + (time.minute + 30) % 60) % 24
        self.window.home_widget_obj.dateTimeStart.setDateTime(time.replace(hour=hours, minute=minutes))
        self.window.home_widget_obj.timeDoing.setTime(tm(0, 30))

