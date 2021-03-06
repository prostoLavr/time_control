# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './my_widgets/home_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(500, 542)
        Frame.setMinimumSize(QtCore.QSize(490, 390))
        Frame.setStyleSheet("")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 489, 541))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upVerticalLayout = QtWidgets.QVBoxLayout()
        self.upVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.upVerticalLayout.setObjectName("upVerticalLayout")
        self.upHorizontalLayout = QtWidgets.QHBoxLayout()
        self.upHorizontalLayout.setObjectName("upHorizontalLayout")
        self.taskNameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.taskNameEdit.setObjectName("taskNameEdit")
        self.upHorizontalLayout.addWidget(self.taskNameEdit)
        self.upVerticalLayout.addLayout(self.upHorizontalLayout)
        self.startTaskButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.startTaskButton.setObjectName("startTaskButton")
        self.upVerticalLayout.addWidget(self.startTaskButton)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_doing = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_doing.setObjectName("label_doing")
        self.gridLayout.addWidget(self.label_doing, 0, 1, 1, 1)
        self.dateTimeStart = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget_2)
        self.dateTimeStart.setObjectName("dateTimeStart")
        self.gridLayout.addWidget(self.dateTimeStart, 1, 0, 1, 1)
        self.label_start = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_start.setObjectName("label_start")
        self.gridLayout.addWidget(self.label_start, 0, 0, 1, 1)
        self.timeDoing = QtWidgets.QTimeEdit(self.verticalLayoutWidget_2)
        self.timeDoing.setObjectName("timeDoing")
        self.gridLayout.addWidget(self.timeDoing, 1, 1, 1, 1)
        self.addTaskButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addTaskButton.setAutoDefault(False)
        self.addTaskButton.setDefault(False)
        self.addTaskButton.setFlat(False)
        self.addTaskButton.setObjectName("addTaskButton")
        self.gridLayout.addWidget(self.addTaskButton, 1, 2, 1, 1)
        self.upVerticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.upVerticalLayout)
        self.bottomVerticalLayout = QtWidgets.QVBoxLayout()
        self.bottomVerticalLayout.setSpacing(0)
        self.bottomVerticalLayout.setObjectName("bottomVerticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.bottomVerticalLayout.addWidget(self.label)
        self.nowScrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.nowScrollArea.setAutoFillBackground(False)
        self.nowScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.nowScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nowScrollArea.setWidgetResizable(True)
        self.nowScrollArea.setObjectName("nowScrollArea")
        self.scrollAreaWidgetContents1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents1.setGeometry(QtCore.QRect(0, 0, 459, 129))
        self.scrollAreaWidgetContents1.setObjectName("scrollAreaWidgetContents1")
        self.nowScrollArea.setWidget(self.scrollAreaWidgetContents1)
        self.bottomVerticalLayout.addWidget(self.nowScrollArea)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.bottomVerticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bottomVerticalLayout.addLayout(self.horizontalLayout)
        self.futureScrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.futureScrollArea.setStyleSheet("")
        self.futureScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.futureScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.futureScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.futureScrollArea.setWidgetResizable(True)
        self.futureScrollArea.setObjectName("futureScrollArea")
        self.scrollAreaWidgetContents2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(QtCore.QRect(0, 0, 459, 195))
        self.scrollAreaWidgetContents2.setStyleSheet("")
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")
        self.futureScrollArea.setWidget(self.scrollAreaWidgetContents2)
        self.bottomVerticalLayout.addWidget(self.futureScrollArea)
        self.bottomVerticalLayout.setStretch(1, 2)
        self.bottomVerticalLayout.setStretch(4, 3)
        self.verticalLayout.addLayout(self.bottomVerticalLayout)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        Frame.setTabOrder(self.taskNameEdit, self.startTaskButton)
        Frame.setTabOrder(self.startTaskButton, self.dateTimeStart)
        Frame.setTabOrder(self.dateTimeStart, self.timeDoing)
        Frame.setTabOrder(self.timeDoing, self.addTaskButton)
        Frame.setTabOrder(self.addTaskButton, self.futureScrollArea)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.startTaskButton.setText(_translate("Frame", "???????????? ????????????"))
        self.label_doing.setText(_translate("Frame", "?????????? ????????????????????"))
        self.label_start.setText(_translate("Frame", "?????????? ????????????"))
        self.addTaskButton.setText(_translate("Frame", "????????????????"))
        self.label.setText(_translate("Frame", "???? ????????????????????"))
        self.label_2.setText(_translate("Frame", "??????????????????????????"))
