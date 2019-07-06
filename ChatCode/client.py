import socket
import sys
import json

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 80

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    file = open('data_1.json', 'rb')
    clients = json.load(file)
    flag = True
    while flag:
        username = input("Enter username : ")
        exitLoop = False
        for data in clients:
            for key in data.keys():
                if key == username:
                    print("User already Exist")
                    exitLoop = True
                    break
            if exitLoop:
                break
        else:
            flag = False
    file.close()

    username = "name : {}".format(username)
    soc.send(username.encode('utf8'))

    message = input(" -> ")

    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        data = soc.recv(1024)
        print(data.decode())

        message = input(" -> ")

    soc.send(b'--quit--')

if __name__ == "__main__":
    main()
