from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 30, 341, 71))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 441, 81))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 170, 471, 71))
        self.lineEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 441, 81))
        self.label_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 290, 471, 71))
        self.lineEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 400, 441, 81))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 410, 471, 71))
        self.lineEdit_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 530, 131, 91))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 253, 194);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 530, 131, 91))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 253, 194);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 530, 131, 91))
        self.pushButton_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 253, 194);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 530, 131, 91))
        self.pushButton_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 253, 194);")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1152, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "Basic Calculator"))
        self.label_2.setText(_translate("MainWindow", "Enter first number"))
        self.label_3.setText(_translate("MainWindow", "Enter second number"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "/"))
        self.pushButton_4.setText(_translate("MainWindow", "*"))

        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        f_num = int(self.lineEdit.text())
        s_num = int(self.lineEdit_2.text())
        result = f_num + s_num
        self.lineEdit_3.setText(str(result))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
