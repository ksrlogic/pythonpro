# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQt5 import QtCore, QtGui, QtWidgets
from evaluate import competeOk, isTMclassEmpty, isEmpty, isMorning, TMClassContinue
from UIs.result import UI_Result
from driver import driver
from getData_Selenium import getData, getCredit, clear
from UIs.loading import UI_Loading
from mainTorch import MainWindow

from evaluate import score

class Main_UI(object):
    def setupUi(self, MainWindow):  
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1137, 808)
        MainWindow.setStyleSheet("background-color: rgb(166, 170, 123);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 211, 21))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 421, 16))
        self.label_2.setObjectName("label_2")

        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(50, 110, 81, 16))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_1.clicked.connect(lambda : self.CheckOverlapped(self.checkBox_1)) # https://stackoverflow.com/questions/6784084/how-to-pass-arguments-to-functions-by-the-click-of-button-in-pyqt

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 110, 81, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.isBooked)
        self.checkBox_2.clicked.connect(lambda : self.CheckOverlapped(self.checkBox_2))

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 110, 81, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.clicked.connect(lambda : self.CheckOverlapped(self.checkBox_3))
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 300, 81, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.clicked.connect(lambda : self.CheckOverlapped2(self.checkBox_4))

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(170, 300, 91, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.clicked.connect(lambda : self.CheckOverlapped2(self.checkBox_5))
        
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(280, 300, 81, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.clicked.connect(lambda : self.CheckOverlapped2(self.checkBox_6))

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

        self.Alert = QtWidgets.QLabel(self.centralwidget)
        self.Alert.setGeometry(QtCore.QRect(530, 400, 541, 16))
        self.Alert.setObjectName("Alert")

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
        self.credit = getCredit(driver)
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
        self.label_6.setText(_translate("MainWindow", "3. 당신의 학점은 %s점!" % self.credit ))
        self.showTableBtn_2.setText(_translate("MainWindow", "더보기"))
        if int(self.credit) >= 16 :
            self.score_label.setText("학점 기준표를 보고 본인이 몇 학점까지 들을 수 있는지 확인해주세요.")
            self.showTableBtn_2.show()
        else:
            self.score_label.setText("16학점까지는 들어야 남은 학점을 이월할 수 있어요. 수정이 필요합니다.")
        self.showTableBtn_2.hide()
        self.label_7.setText(_translate("MainWindow", "4. GLS- 학업영역- 책가방으로 가서 여러분과 같은 수업을 담은 학생의 수를 확인해주세요!"))
        self.label_8.setText(_translate("MainWindow", "가장 치열한 다섯개 과목의 경쟁률을 소숫점 첫째자리까지 적어주세요."))
        self.label_9.setText(_translate("MainWindow", "( !단, 계열제 학생의 경우, 전공진입에 필요한 과목을 우선으로 배치해주세요. )"))
        self.Alert.setText(_translate("MainWindow", ""))        
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "1픽"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "2픽"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "3픽"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "4픽"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "5픽"))
        self.pushButton.setText(_translate("MainWindow", "완료!"))
        self.pushButton.clicked.connect(self.Complete)
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
    def CheckOverlapped(self, wanted):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        wanted.setChecked(True)
    def CheckOverlapped2(self, wanted):
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        wanted.setChecked(True)

    def Complete(self):
        print("Clicked!")
        weight = 0
        check1 = self.checkBox_1.isChecked()
        check2 = self.checkBox_2.isChecked()
        check3 = self.checkBox_3.isChecked()
        check4 = self.checkBox_4.isChecked()
        check5 = self.checkBox_5.isChecked()
        check6 = self.checkBox_6.isChecked()
        if not check1 and not check2 and not check3:
            self.Alert.setText("체크 되지 않은 부분이 있어요!")
            return
        else:
            self.Alert.setText("")
        if not check4 and not check5 and not check6:
            self.Alert.setText("체크 되지 않은 부분이 있어요!")
            return
        else:
            self.Alert.setText("")
        
        if int(self.credit) < 16:
            self.Alert.setText("학점이 너무 낮아요! 확인 후 다시 실행해주세요.")

        print("왔다")
        if check4:
            weight = 1
        if check5:
            weight = 2
        if check6:
            weight = 3

        print("weight: " , weight)

        pick1 = float(self.lineEdit.text())
        pick2 = float(self.lineEdit_2.text())
        pick3 = float(self.lineEdit_3.text())
        pick4 = float(self.lineEdit_4.text())
        pick5 = float(self.lineEdit_5.text())

        clist = [pick1, pick2, pick3, pick4, pick5]
        intCList = []
        for c in clist:
            if not isinstance(c, float) or c == "":

                self.Alert.setText("경쟁률을 제대로 입력해주세요! ex) 1.0, 4.5")
                return
            else:
                intCList.append(c)


        MainWindow.close()
        competeResult = competeOk(clist)
        timetable = getData(driver)
        realtimetable = clear(timetable)
        print(realtimetable, "시간표")
        #결과창 Text만들기
        self.Texts = []
        self.CheckEmptyText = isEmpty(realtimetable)
        self.Texts.append(self.CheckEmptyText)
        print(self.Texts, "텍스트들1")
        self.Texts = self.Texts + isTMclassEmpty(realtimetable)
        print(self.Texts, "텍스트들2")
        self.Texts.append(competeResult)

        self.Texts += isMorning(realtimetable, weight)

        self.Texts += TMClassContinue(realtimetable)

        print(self.Texts, "텍스트들3")

        self.Texts.append()
        self.window = QtWidgets.QMainWindow()
        self.resultUI = UI_Result(score, self.Texts)
        self.resultUI.setupUi(self.window)
        self.resultUI.setupUi(self.window)
        self.window.show()

        return weight
        


            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main_UI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
