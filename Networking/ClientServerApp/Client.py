import socket
sock = socket.socket()
port = 80
sock.connect(('localhost',port))
data = sock.recv(1024)
print(data)
print(data.decode())
sock.close()