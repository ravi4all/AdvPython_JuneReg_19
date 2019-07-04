import socket
sock = socket.socket()
port = 80
sock.connect(('localhost',port))
while True:
    data = sock.recv(1024)
    print("Server :",data.decode())
    message = input("-> ")
    sock.send(message.encode('UTF-8'))
    if data.decode() == 'bye':
        break

sock.close()