# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Result(object):
    def __init__(self, score, competeResult):
        self.score = score
        self.competeResult = competeResult

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 745)
        font = QtGui.QFont()
        font.setFamily("서울한강 장체M")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 12pt \"메이플스토리\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 851, 131))
        self.label_2.setStyleSheet("font: 75 28pt \"타이포_쌍문동 B\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, -30, 241, 281))
        self.label_3.setStyleSheet("\n"
"color: rgb(239, 239, 239);\n"
"font: 81 72pt \"나눔스퀘어OTF ExtraBold\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 501, 41))
        font = QtGui.QFont()
        font.setFamily("08서울남산체 B")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 14pt \"08서울남산체 B\";")
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(670, 560, 231, 51))
        self.label_9.setStyleSheet("border-color: rgb(170, 255, 127);\n"
"font: 75 11pt \"타이포_쌍문동 B\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(600, 610, 131, 31))
        self.label_10.setStyleSheet("font: 75 12pt \"나눔스퀘어OTF Bold\";\n"
"background-color: rgb(0, 115, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(750, 610, 151, 31))
        self.label_11.setStyleSheet("font: 75 12pt \"나눔스퀘어OTF Bold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 115, 0);\n"
"")
        self.label_11.setObjectName("label_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 210, 761, 341))
        self.textBrowser.setStyleSheet("background-color: rgb(246, 255, 151);\n"
"font: 75 12pt \"맑은 고딕\";")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 21))
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
        self.label.setText(_translate("MainWindow", "내 시간표는 몇 점?!"))
        self.label_2.setText(_translate("MainWindow", "당신의 점수는!! "))
        self.label_3.setText(_translate("MainWindow", "00점"))
        self.label_4.setText(_translate("MainWindow", "어디서 깎였냐구요? 찬찬히 설명해줄게요! "))
        self.label_9.setText(_translate("MainWindow", "시간표 수정할건가요?"))
        self.label_10.setText(_translate("MainWindow", " 네, 수정할래요."))
        self.label_11.setText(_translate("MainWindow", " 아니요, 확정이요."))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'맑은 고딕\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Agency FB\';\"><br /></p></body></html>"))
        for text in self.competeResult:
                self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + text)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_Result(0, ["A","B","C","D"])
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
