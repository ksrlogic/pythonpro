# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Loading(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 600)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 180, 501, 101))
        font = QtGui.QFont()
        font.setFamily("타이포_쌍문동 B")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 260, 621, 81))
        font = QtGui.QFont()
        font.setFamily("타이포_쌍문동 B")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 631, 191))
        self.label_3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 370, 291, 61))
        self.label_4.setStyleSheet("font: 25pt \"Tw Cen MT Condensed Extra Bold\";")
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "◑◐평가 중이에요◑◐"))
        self.label_2.setText(_translate("MainWindow", "조금만 기다려주세요"))
        self.label_4.setText(_translate("MainWindow", "..... LOADING....."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_Loading()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
