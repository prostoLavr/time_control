from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import time


time_wait = 5


class Worker(QObject):
    db_update = pyqtSignal()

    @pyqtSlot()
    def procCounter(self):
        while True:
            self.db_update.emit()
            time.sleep(time_wait)
