# worker.py
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time


class Worker(QObject):
    update = pyqtSignal()

    @pyqtSlot()
    def procCounter(self):
        while True:
            time.sleep(1)
            self.update.emit()
