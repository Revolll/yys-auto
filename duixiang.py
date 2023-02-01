# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'duixiang.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 542)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 60, 311, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 15, 101, 22))
        self.comboBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 15, 75, 23))
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 54, 12))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 50, 91, 51))
        self.pushButton_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, 10, 311, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comboBox_3 = QComboBox(self.frame_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(90, 15, 101, 22))
        self.comboBox_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 54, 12))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u68c0\u6d4b\u5230\u8bbe\u5907", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bbe\u5907\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u526f\u672c\u81ea\u52a8\u6a21\u5f0f", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u624b\u52a8\u6a21\u5f0f", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\uff1a", None))
    # retranslateUi

