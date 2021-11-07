# main.py
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
import sys
import worker


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("0")

        self.obj = worker.Worker()
        self.thread = QThread()
        self.obj.db_update.connect(self.onIntReady)
        self.obj.moveToThread(self.thread)
        self.thread.started.connect(self.obj.procCounter)
        self.thread.start()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.label, 0, 0)

        self.move(300, 150)
        self.setWindowTitle('thread test')
        self.show()

    def onIntReady(self):
        self.label.setText(str(int(self.label.text()) + 1))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = Form()

    sys.exit(app.exec_())
