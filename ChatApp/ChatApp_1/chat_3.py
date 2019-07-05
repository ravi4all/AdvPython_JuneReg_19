from PyQt5 import QtCore, QtGui, QtWidgets
import readChat

class Ui_MainWindow(QtWidgets.QMainWindow):

    def readUsers(self):
        self.users = readChat.readAllUsers()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1277, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 401, 741))
        self.listWidget.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")

        for i in range(len(self.users)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(450, 10, 801, 521))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setObjectName("frame")

        self.listWidget_2 = QtWidgets.QListWidget(self.frame)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 5, 800, 520))
        self.listWidget_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.listWidget_2.setObjectName("listWidget_2")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(450, 560, 801, 107))
        self.textEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 690, 351, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.textEdit_2.setReadOnly(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        for i in range(len(self.users)):
            item = self.listWidget.item(i)
            item.setText(_translate("MainWindow", self.users[i]))

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton.clicked.connect(self.sendMessage)

        self.listWidget.itemClicked.connect(self.changeUser)

    def changeUser(self, item):
        self.textEdit_2.setReadOnly(False)
        self.userName = item.text()
        self.conversation()

    def sendMessage(self):
        try:
            msg = {'msg':''}
            rply = {'rply':self.textEdit_2.toPlainText()}
            self.textEdit_2.setText("")
            chatData = readChat.insertMessage(self.userName,msg,rply)
            readChat.updateJson(chatData)
            # print(self.chatData)
            self.conversation()
        except BaseException as ex:
            print(ex)

    def conversation(self):
        self.listWidget_2.clear()
        try:
            self.chatData = readChat.readChatData(self.userName)
            for data in self.chatData:
                for i in range(len(data)):
                    item = QtWidgets.QListWidgetItem()
                    self.listWidget_2.addItem(item)
                    item = self.listWidget_2.item(i)
                    for key in data[i].keys():
                        if key == 'msg':
                            item.setText(data[i][key])
                            item.setTextAlignment(QtCore.Qt.AlignLeft)
                        else:
                            item.setText(data[i][key])
                            item.setTextAlignment(QtCore.Qt.AlignRight)
        except BaseException as ex:
            print(ex)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.readUsers()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())