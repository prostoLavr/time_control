# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './my_widgets/gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(10, 10, 541, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setStyleSheet("")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftWidget = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setStyleSheet("QPushButton{\n"
"border-radius: 0;\n"
"background: \"#CCC\"\n"
"}\n"
"QPushButton:hover{\n"
"background: \"#BBB\"\n"
"}\n"
"QPushButton:focus{\n"
"background: \"#BBB\"\n"
"}")
        self.leftWidget.setObjectName("leftWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upLayout = QtWidgets.QGridLayout()
        self.upLayout.setHorizontalSpacing(2)
        self.upLayout.setVerticalSpacing(0)
        self.upLayout.setObjectName("upLayout")
        self.statisticButton = QtWidgets.QPushButton(self.leftWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statisticButton.sizePolicy().hasHeightForWidth())
        self.statisticButton.setSizePolicy(sizePolicy)
        self.statisticButton.setMinimumSize(QtCore.QSize(90, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statisticButton.setFont(font)
        self.statisticButton.setMouseTracking(True)
        self.statisticButton.setAutoDefault(False)
        self.statisticButton.setDefault(False)
        self.statisticButton.setFlat(False)
        self.statisticButton.setObjectName("statisticButton")
        self.upLayout.addWidget(self.statisticButton, 0, 2, 1, 1)
        self.homeButton = QtWidgets.QPushButton(self.leftWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
        self.homeButton.setMinimumSize(QtCore.QSize(75, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.homeButton.setFont(font)
        self.homeButton.setAutoDefault(False)
        self.homeButton.setDefault(False)
        self.homeButton.setFlat(False)
        self.homeButton.setObjectName("homeButton")
        self.upLayout.addWidget(self.homeButton, 0, 1, 1, 1)
        self.historyButton = QtWidgets.QPushButton(self.leftWidget)
        self.historyButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyButton.sizePolicy().hasHeightForWidth())
        self.historyButton.setSizePolicy(sizePolicy)
        self.historyButton.setMinimumSize(QtCore.QSize(75, 65))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.historyButton.setFont(font)
        self.historyButton.setAutoDefault(False)
        self.historyButton.setObjectName("historyButton")
        self.upLayout.addWidget(self.historyButton, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.upLayout)
        self.bottomLayout = QtWidgets.QVBoxLayout()
        self.bottomLayout.setSpacing(0)
        self.bottomLayout.setObjectName("bottomLayout")
        self.verticalLayout.addLayout(self.bottomLayout)
        self.verticalLayout.setStretch(0, 7)
        self.horizontalLayout.addWidget(self.leftWidget)
        self.add_widget = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_widget.sizePolicy().hasHeightForWidth())
        self.add_widget.setSizePolicy(sizePolicy)
        self.add_widget.setStyleSheet("")
        self.add_widget.setObjectName("add_widget")
        self.horizontalLayout.addWidget(self.add_widget)
        self.statistic_widget = QtWidgets.QWidget(self.horizontalWidget)
        self.statistic_widget.setObjectName("statistic_widget")
        self.horizontalLayout.addWidget(self.statistic_widget)
        self.history_widget = QtWidgets.QWidget(self.horizontalWidget)
        self.history_widget.setObjectName("history_widget")
        self.horizontalLayout.addWidget(self.history_widget)
        self.settings_widget = QtWidgets.QWidget(self.horizontalWidget)
        self.settings_widget.setObjectName("settings_widget")
        self.horizontalLayout.addWidget(self.settings_widget)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 6)
        self.horizontalLayout.setStretch(3, 6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.homeButton, self.statisticButton)
        MainWindow.setTabOrder(self.statisticButton, self.historyButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.statisticButton.setText(_translate("MainWindow", "????????????????????"))
        self.homeButton.setText(_translate("MainWindow", "??????????"))
        self.historyButton.setText(_translate("MainWindow", "??????????????"))
