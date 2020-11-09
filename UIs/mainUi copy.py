# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

score = 17

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 677)
        MainWindow.setStyleSheet("background-color: rgb(125, 238, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 311, 21))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 421, 16))
        self.label_2.setObjectName("label_2")

        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(50, 110, 81, 16))
        self.checkBox_1.setObjectName("checkBox_1")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 110, 81, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.isBooked)

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 110, 81, 16))
        self.checkBox_3.setObjectName("checkBox_3")

        
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 300, 81, 16))
        self.checkBox_4.setObjectName("checkBox_4")

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(170, 300, 91, 16))
        self.checkBox_5.setObjectName("checkBox_5")

        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(280, 300, 81, 16))
        self.checkBox_6.setObjectName("checkBox_6")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 421, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 201, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 260, 421, 16))
        self.label_5.setObjectName("label_5")

        self.showTableBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showTableBtn.setGeometry(QtCore.QRect(300, 160, 75, 23))
        self.showTableBtn.setObjectName("showTableBtn")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 210, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.checkedImage)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 360, 131, 16))
        self.label_6.setObjectName("label_6")
        self.score_label = QtWidgets.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(50, 390, 481, 16))
        self.score_label.setText("")
        self.score_label.setObjectName("score_label")
        self.showTableBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.showTableBtn_2.setGeometry(QtCore.QRect(450, 390, 75, 23))
        self.showTableBtn_2.setObjectName("showTableBtn_2")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 70, 541, 16))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 90, 541, 16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(530, 110, 541, 16))
        self.label_9.setObjectName("label_9")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(550, 170, 91, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(680, 170, 91, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(820, 170, 91, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(610, 230, 91, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(760, 230, 91, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 480, 231, 131))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"font: 28pt \"새굴림\";")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 21))
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
        self.label.setText(_translate("MainWindow", "몇 가지만 더 물어볼게요."))
        self.label_2.setText(_translate("MainWindow", "1. 여러분은 다음 중 어떤 소속인가요? 여러분의 소속을 선택해주세요!"))
        self.checkBox_1.setText(_translate("MainWindow", "계열제생"))
        self.checkBox_2.setText(_translate("MainWindow", "전공예약생"))
        self.checkBox_3.setText(_translate("MainWindow", "학과생"))
        self.label_3.setText(_translate("MainWindow", "1-2. 전공진입 요건을 확인하였나요?"))
        self.label_3.hide()
        self.label_4.setText(_translate("MainWindow", "표를 보고 다시 한 번 확인해주세요!"))
        self.label_4.hide()
        self.showTableBtn.setText(_translate("MainWindow", "더보기"))
        self.showTableBtn.hide()
        self.pushButton_2.setText(_translate("MainWindow", "네, 확인했어요."))
        self.pushButton_2.hide()
        self.pushButton_3.setText(_translate("MainWindow", "변경할래요."))
        self.pushButton_3.hide()
        self.label_5.setText(_translate("MainWindow", "2. 학교까지 오는데 얼마나 걸리세요? 여러분의 통학시간을 체크해주세요."))
        self.checkBox_4.setText(_translate("MainWindow", "30분 미만"))
        self.checkBox_5.setText(_translate("MainWindow", "30분~1시간"))
        self.checkBox_6.setText(_translate("MainWindow", "1시간 이상"))
        self.label_6.setText(_translate("MainWindow", "3. 당신의 학점은 %s점!" % score ))
        self.showTableBtn_2.setText(_translate("MainWindow", "더보기"))
        if int(score) >= 16 :
            self.score_label.setText("학점 기준표를 보고 본인이 몇 학점까지 들을 수 있는지 확인해주세요.")
        else:
            self.score_label.setText("16학점까지는 들어야 남은 학점을 이월할 수 있어요. 수정이 필요합니다.")
        self.showTableBtn_2.hide()
        self.label_7.setText(_translate("MainWindow", "4. GLS- 학업영역- 책가방으로 가서 여러분과 같은 수업을 담은 학생의 수를 확인해주세요!"))
        self.label_8.setText(_translate("MainWindow", "가장 치열한 다섯개 과목의 경쟁률을 소숫점 첫째자리까지 적어주세요."))
        self.label_9.setText(_translate("MainWindow", "( !단, 계열제 학생의 경우, 전공진입에 필요한 과목을 우선으로 배치해주세요. )"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "1픽"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "2픽"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "3픽"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "4픽"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "5픽"))
        self.pushButton.setText(_translate("MainWindow", "완료!"))
    def isBooked(self):
        if self.checkBox_2.isChecked():
            self.showTableBtn.setHidden(not self.showTableBtn.isHidden())
            self.pushButton_2.setHidden(not self.pushButton_2.isHidden())
            self.pushButton_3.setHidden(not self.pushButton_3.isHidden())
            self.label_3.setHidden(not self.label_3.isHidden())
            self.label_4.setHidden(not self.label_4.isHidden())
        else:
            self.showTableBtn.setHidden(not self.showTableBtn.isHidden())
            self.pushButton_2.setHidden(not self.pushButton_2.isHidden())
            self.pushButton_3.setHidden(not self.pushButton_3.isHidden())
            self.label_3.setHidden(not self.label_3.isHidden())
            self.label_4.setHidden(not self.label_4.isHidden())
    
    def checkedImage(self):
            self.showTableBtn.setHidden(not self.showTableBtn.isHidden())
            self.pushButton_2.setHidden(not self.pushButton_2.isHidden())
            self.pushButton_3.setHidden(not self.pushButton_3.isHidden())
            self.label_3.setHidden(not self.label_3.isHidden())
            self.label_4.setHidden(not self.label_4.isHidden())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
