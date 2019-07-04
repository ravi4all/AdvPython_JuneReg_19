import socket
sock = socket.socket()
port = 80
sock.bind(('localhost',port))
sock.listen(5)
print("Socket listening")
message = "Thankyou for connecting"
while True:
    conn, address = sock.accept()
    print("Got connection from",address)
    conn.send(message.encode())
    conn.close()
