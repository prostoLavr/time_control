# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './my_widgets/task_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(389, 100)
        Frame.setMinimumSize(QtCore.QSize(260, 90))
        Frame.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.startTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.startTime.setAlignment(QtCore.Qt.AlignCenter)
        self.startTime.setObjectName("startTime")
        self.gridLayout.addWidget(self.startTime, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        self.EditButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.EditButton.setObjectName("EditButton")
        self.gridLayout.addWidget(self.EditButton, 3, 0, 1, 1)
        self.adaptateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.adaptateButton.setObjectName("adaptateButton")
        self.gridLayout.addWidget(self.adaptateButton, 3, 1, 1, 1)
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setIndent(-1)
        self.title.setOpenExternalLinks(False)
        self.title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 1)
        self.endTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.endTime.setAlignment(QtCore.Qt.AlignCenter)
        self.endTime.setObjectName("endTime")
        self.gridLayout.addWidget(self.endTime, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.startTime.setText(_translate("Frame", "11.12 13:00"))
        self.checkBox.setText(_translate("Frame", "Выполнено"))
        self.EditButton.setText(_translate("Frame", "Удалить"))
        self.adaptateButton.setText(_translate("Frame", "Начать"))
        self.title.setText(_translate("Frame", "Задача №1"))
        self.endTime.setText(_translate("Frame", "11.12 14:00"))
