import socket
sock = socket.socket()
port = 80
sock.bind(('localhost',port))
sock.listen(5)
print("Socket listening")
conn, address = sock.accept()
print("Got connection from",address)
message = "Welcome User"
conn.send(message.encode('UTF-8'))
while True:
    data = conn.recv(1024).decode()
    print("Client :",data)
    message = input("Enter your message : ")
    conn.send(message.encode('UTF-8'))
    if data == 'bye':
        break

conn.close()