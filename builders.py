from PyQt5.QtWidgets import QWidget


from datetime import datetime as dt
import widgets_init


class HomeWidgetBuilder:
    def __init__(self, window):
        self.window = window
        self.home_widget_init()

    def home_widget_init(self):
        self.window.home_widget_obj = widgets_init.HomeWidget(self.window.add_widget)


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


class TaskListBuilder:
    def __init__(self, v_layout, parent):
        self.v_layout = v_layout
        self.parent = parent
        for _ in range(3):
            self.add_test_task()

    def add_test_task(self):
        widget = QWidget(self.parent)
        task = widgets_init.TaskWidget('test', dt(1, 1, 1, 1, 1), None, widget)
        widget.task = task
        self.v_layout.addWidget(widget)


class ButtonConnectBuilder:
    def __init__(self, window):
        self.window = window
        self.connect_button()

    def connect_button(self):
        pass
