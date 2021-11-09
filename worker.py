from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import time
import platform
import os
import db_director
from configuration import *


class Worker(QObject):
    db_update = pyqtSignal()

    @pyqtSlot()
    def procCounter(self):
        timers = start_counts
        functions = (self.db_update_foo, sleep, wakeup)
        while True:
            time.sleep(time_wait)
            timers = [(timer + 1) % count for timer, count in zip(timers, counts)]
            for timer, function in zip(timers, functions):
                if not timer:
                    function()

    def db_update_foo(self):
        self.db_update.emit()


def wakeup():
    push('Пора за работу', 'Не забудьте возобновить дела')


def sleep():
    push('Отдохните', 'Не забудьте поставить дела на паузу')


def push(title, message):
    plt = platform.system()
    if plt == "Darwin":
        command = '''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''
        os.system(command)
    elif plt == "Linux":
        command = f'''
        notify-send "{title}" "{message}"
        '''
        os.system(command)
    elif plt == "Windows":
        import win10toast
        win10toast.ToastNotifier().show_toast(title, message)
    else:
        print('Invalid OS')
