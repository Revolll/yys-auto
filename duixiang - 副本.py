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
        self.frame.setGeometry(QRect(70, 30, 311, 51))
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
        # self.groupBox = QGroupBox(self.centralwidget)
        # self.groupBox.setObjectName(u"groupBox")
        # self.groupBox.setGeometry(QRect(10, 110, 581, 411))
        # self.groupBox_2 = QGroupBox(self.groupBox)
        # self.groupBox_2.setObjectName(u"groupBox_2")
        # self.groupBox_2.setGeometry(QRect(30, 20, 521, 51))
        # self.radioButton = QRadioButton(self.groupBox_2)
        # self.radioButton.setObjectName(u"radioButton")
        # self.radioButton.setGeometry(QRect(30, 20, 91, 16))
        # self.radioButton_3 = QRadioButton(self.groupBox_2)
        # self.radioButton_3.setObjectName(u"radioButton_3")
        # self.radioButton_3.setGeometry(QRect(130, 20, 61, 16))
        # self.radioButton_4 = QRadioButton(self.groupBox_2)
        # self.radioButton_4.setObjectName(u"radioButton_4")
        # self.radioButton_4.setGeometry(QRect(210, 20, 51, 16))
        # self.groupBox_3 = QGroupBox(self.groupBox)
        # self.groupBox_3.setObjectName(u"groupBox_3")
        # self.groupBox_3.setGeometry(QRect(30, 90, 521, 51))
        # self.radioButton_2 = QRadioButton(self.groupBox_3)
        # self.radioButton_2.setObjectName(u"radioButton_2")
        # self.radioButton_2.setGeometry(QRect(30, 20, 61, 16))
        # self.radioButton_5 = QRadioButton(self.groupBox_3)
        # self.radioButton_5.setObjectName(u"radioButton_5")
        # self.radioButton_5.setGeometry(QRect(110, 20, 61, 16))
        # self.radioButton_6 = QRadioButton(self.groupBox_3)
        # self.radioButton_6.setObjectName(u"radioButton_6")
        # self.radioButton_6.setGeometry(QRect(190, 20, 61, 16))
        # self.textBrowser = QTextBrowser(self.groupBox)
        # self.textBrowser.setObjectName(u"textBrowser")
        # self.textBrowser.setGeometry(QRect(30, 150, 521, 241))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 30, 91, 51))
        self.pushButton_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u68c0\u6d4b\u5230\u8bbe\u5907", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bbe\u5907\uff1a", None))
        # self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u672a\u68c0\u6d4b\u5230\u8bbe\u5907", None))
        # self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u526f\u672c", None))
        # self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5fa1\u9b42/\u65e5\u8f6e", None))
        # self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e1a\u539f\u706b", None))
        # self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5fa1\u7075", None))
        # self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f", None))
        # self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5237", None))
        # self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6253\u624b", None))
        # self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u53f8\u673a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
    # retranslateUi

