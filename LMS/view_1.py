from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 10, 561, 101))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 160, 551, 511))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.image = QtGui.QPixmap('img_1.jpg')
        self.label_2.setPixmap(self.image)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 160, 321, 91))
        self.comboBox.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 187, 153);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 251, 61))
        self.label_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 470, 321, 91))
        self.comboBox_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 187, 153);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 480, 251, 61))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 300, 281, 71))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 610, 281, 71))
        self.pushButton_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1231, 731))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(370, 30, 501, 61))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 200, 421, 81))
        self.label_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(100, 330, 421, 81))
        self.label_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(580, 200, 561, 71))
        self.lineEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 340, 561, 71))
        self.lineEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 540, 381, 81))
        self.pushButton_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(87, 196, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1241, 731))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 190, 1191, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(290, 600, 161, 101))
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 610, 451, 81))
        self.pushButton_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 4);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 120, 301, 51))
        self.label_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(410, 10, 401, 61))
        self.label_10.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 120, 113, 51))
        self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(500, 120, 351, 51))
        self.label_11.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(860, 120, 113, 51))
        self.lineEdit_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(1110, 120, 113, 51))
        self.lineEdit_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(1010, 120, 91, 51))
        self.label_12.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1241, 731))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(410, 10, 371, 71))
        self.label_13.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 120, 1191, 481))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 31))
        self.menubar.setObjectName("menubar")
        self.menuLogin_Options = QtWidgets.QMenu(self.menubar)
        self.menuLogin_Options.setObjectName("menuLogin_Options")
        self.menuRegistration_Options = QtWidgets.QMenu(self.menubar)
        self.menuRegistration_Options.setObjectName("menuRegistration_Options")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTeacher = QtWidgets.QAction(MainWindow)
        self.actionTeacher.setObjectName("actionTeacher")
        self.actionStudent = QtWidgets.QAction(MainWindow)
        self.actionStudent.setObjectName("actionStudent")
        self.actionAdmin = QtWidgets.QAction(MainWindow)
        self.actionAdmin.setObjectName("actionAdmin")
        self.actionTeacher_2 = QtWidgets.QAction(MainWindow)
        self.actionTeacher_2.setObjectName("actionTeacher_2")
        self.actionStudent_2 = QtWidgets.QAction(MainWindow)
        self.actionStudent_2.setObjectName("actionStudent_2")
        self.actionAdmin_2 = QtWidgets.QAction(MainWindow)
        self.actionAdmin_2.setObjectName("actionAdmin_2")
        self.menuLogin_Options.addAction(self.actionTeacher)
        self.menuLogin_Options.addAction(self.actionStudent)
        self.menuLogin_Options.addAction(self.actionAdmin)
        self.menuRegistration_Options.addAction(self.actionTeacher_2)
        self.menuRegistration_Options.addAction(self.actionStudent_2)
        self.menuRegistration_Options.addAction(self.actionAdmin_2)
        self.menubar.addAction(self.menuLogin_Options.menuAction())
        self.menubar.addAction(self.menuRegistration_Options.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Library Management System"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Teacher"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Student"))
        self.label_3.setText(_translate("MainWindow", "Login As"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Teacher"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Student"))
        self.label_4.setText(_translate("MainWindow", "Register As"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.label_5.setText(_translate("MainWindow", "Login As "))
        self.label_6.setText(_translate("MainWindow", "Enter login ID"))
        self.label_7.setText(_translate("MainWindow", "Enter login Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Book Author"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Issue Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Return Date"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Return Book"))
        self.label_8.setText(_translate("MainWindow", "OR"))
        self.pushButton_4.setText(_translate("MainWindow", "Issue Another Book"))
        self.label_9.setText(_translate("MainWindow", "Total Books Issued : "))
        self.label_10.setText(_translate("MainWindow", "Welcome "))
        self.label_11.setText(_translate("MainWindow", "Currently Books Issued : "))
        self.label_12.setText(_translate("MainWindow", "Fine :"))
        self.label_13.setText(_translate("MainWindow", "Books in the Library"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Book Author"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Book Availability"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Issue Book"))
        self.menuLogin_Options.setTitle(_translate("MainWindow", "Login As"))
        self.menuRegistration_Options.setTitle(_translate("MainWindow", "Registration As"))
        self.actionTeacher.setText(_translate("MainWindow", "Teacher"))
        self.actionStudent.setText(_translate("MainWindow", "Student"))
        self.actionAdmin.setText(_translate("MainWindow", "Admin"))
        self.actionTeacher_2.setText(_translate("MainWindow", "Teacher"))
        self.actionStudent_2.setText(_translate("MainWindow", "Student"))
        self.actionAdmin_2.setText(_translate("MainWindow", "Admin"))

        self.frame.hide()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())