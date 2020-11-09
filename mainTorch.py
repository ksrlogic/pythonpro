import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UIs import LoginUI

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

#실행시
if __name__ == "__main__":
    loginpage = LoginUI.Ui_LOGIN
    ui = loginpage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





