# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from getData_Selenium import login, getData, clear
from driver import driver
from UIs import MainUI
from mainTorch import app, MainWindow


realTimetable = []
path = os.getcwd()
ImageUrl = path.replace('\\', '/') + "/UIs/logo.png"

print(ImageUrl)
class Ui_LOGIN(object):
    def setupUi(self, LOGIN):
        LOGIN.setObjectName("LOGIN")
        LOGIN.resize(460, 372)
        LOGIN.setStyleSheet("\n"
"background-color: rgb(255, 170, 255);")

        self.ID = QtWidgets.QLineEdit(LOGIN)
        self.ID.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.ID.setAutoFillBackground(False)
        self.ID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ID.setMaxLength(30)
        self.ID.setObjectName("ID")

        self.password = QtWidgets.QLineEdit(LOGIN)
        self.password.setGeometry(QtCore.QRect(120, 190, 113, 20))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password.setText("")
        self.password.setMaxLength(30)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        self.label = QtWidgets.QLabel(LOGIN)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 71))
        self.label.setStyleSheet("image: url(%s);" % ImageUrl)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/%s" % ImageUrl))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(LOGIN)
        self.pushButton.setGeometry(QtCore.QRect(280, 190, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginEvent)

        self.textBrowser = QtWidgets.QTextBrowser(LOGIN)
        self.textBrowser.setGeometry(QtCore.QRect(110, 10, 341, 81))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(LOGIN)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)

    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "Dialog"))
        self.ID.setPlaceholderText(_translate("LOGIN", "아이디.."))
        self.password.setPlaceholderText(_translate("LOGIN", "비밀번호..."))
        self.pushButton.setText(_translate("LOGIN", "로그인"))
        self.textBrowser.setHtml(_translate("LOGIN", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">이 프로그램은 성균관대학교에 갓 입학한 신입생들을 위한 시간표 피드백 프로그램입니다</span><span style=\" font-family:\'함초롬바탕\'; font-size:8pt;\">.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">에브리타임 아이디와 비밀번호를 입력해주세요</span><span style=\" font-family:\'함초롬바탕\'; font-size:8pt;\">. </span><span style=\" font-size:8pt;\">살펴봐줄게요</span><span style=\" font-family:\'함초롬바탕\'; font-size:8pt;\">.</span></p></body></html>"))

    def loginEvent(self):
        ID = self.ID.text()
        password = self.password.text()
        login(ID, password, driver)
        time.sleep(0.5)
        try:
            alert = driver.switch_to_alert()
            self.ID.setText("")
            self.password.setText("")
            self.textBrowser.setText(alert.text)
            alert.accept()
        except:
            "There is no alert"
            self.window = QtWidgets.QMainWindow()
            self.ui = MainUI.Main_UI()
            self.ui.setupUi(self.window)
            MainWindow.close()
            self.window.show()
            print(realTimetable)

            

