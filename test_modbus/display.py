# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyMainWindow(object):
    def setupUi(self, MyMainWindow):
        MyMainWindow.setObjectName("MyMainWindow")
        MyMainWindow.resize(839, 461)
        self.centralwidget = QtWidgets.QWidget(MyMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 821, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 2, 3, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MyMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 23))
        self.menubar.setObjectName("menubar")
        MyMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyMainWindow)
        self.statusbar.setObjectName("statusbar")
        MyMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyMainWindow)
        self.pushButton.clicked.connect(MyMainWindow.DisplayStop_click)
        QtCore.QMetaObject.connectSlotsByName(MyMainWindow)

    def retranslateUi(self, MyMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MyMainWindow.setWindowTitle(_translate("MyMainWindow", "Display"))
        self.label_2.setText(_translate("MyMainWindow", "Expression"))
        self.label_3.setText(_translate("MyMainWindow", "Action"))
        self.label.setText(_translate("MyMainWindow", "LED"))
        self.label_4.setText(_translate("MyMainWindow", "端口选择"))
        self.pushButton.setText(_translate("MyMainWindow", "停止"))

