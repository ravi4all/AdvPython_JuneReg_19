from PyQt5 import QtCore, QtGui, QtWidgets
import readChat
import socket
import sys
import traceback
from threading import Thread

class Ui_MainWindow(QtWidgets.QMainWindow):

    connections = []

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

        Thread(target=self.start_server).start()

    def readUsers(self):
        self.users = readChat.readAllUsers()

    def showUsers(self):
        self.listWidget.clear()
        for i in range(len(self.users)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            item = self.listWidget.item(i)
            item.setText(self.users[i])

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

    def recvMessage(self, clientMsg):
        try:
            msg = {'msg':clientMsg}
            rply = {'rply':''}
            chatData = readChat.insertMessage(self.userName,msg,rply)
            readChat.updateJson(chatData)
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

    def start_server(self):
        host = "127.0.0.1"
        port = 80

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
        print("Socket created")

        try:
            soc.bind((host, port))
        except:
            print("Bind failed. Error : " + str(sys.exc_info()))
            sys.exit()

        soc.listen(5)
        print("Socket now listening")

        while True:
            connection, address = soc.accept()
            ip, port = str(address[0]), str(address[1])
            print("Connected with " + ip + ":" + port)

            try:
                Thread(target=self.client_thread, args=(connection, ip, port)).start()
            except:
                print("Thread did not start.")
                traceback.print_exc()

        soc.close()

    def client_thread(self,connection, ip, port, max_buffer_size = 5120):
        is_active = True

        while is_active:
            client_input = self.receive_input(connection, max_buffer_size)
            # print(client_input)
            if 'name' in client_input:
                name = client_input.split()[-1]
                self.connections.append(name)
                readChat.insertUser(name)
                self.readUsers()
                self.showUsers()

            elif "--QUIT--" in client_input:
                print("Client is requesting to quit")
                connection.close()
                print("Connection " + ip + ":" + port + " closed")
                is_active = False
            else:
                self.recvMessage(client_input)
                # print("Processed result: {}".format(client_input))
                # msg = input("-> ")
                # connection.sendall(msg.encode("utf8"))

    def receive_input(self,connection, max_buffer_size):
        client_input = connection.recv(max_buffer_size)
        client_input_size = sys.getsizeof(client_input)

        if client_input_size > max_buffer_size:
            print("The input size is greater than expected {}".format(client_input_size))

        decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
        result = self.process_input(decoded_input)

        return result

    def process_input(self,input_str):
        print("Processing the input received from client")
        return input_str


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.readUsers()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
