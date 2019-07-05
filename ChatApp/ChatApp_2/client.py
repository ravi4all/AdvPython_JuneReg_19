import socket
import sys

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8888

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    username = input("Enter your name : ")
    soc.sendall(username.encode("utf8"))

    message = input(" -> ")

    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        data = soc.recv(1024)
        print(data.decode())

        message = input(" -> ")

    soc.send(b'--quit--')

if __name__ == "__main__":
    main()