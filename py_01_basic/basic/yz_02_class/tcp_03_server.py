import socket
import sys

localIP = "127.0.0.1"
localPort = 65000
bufferSize = 1024

# Create a TCP/IP Socket
TCP_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (localIP, localPort)

print("starting up on %s port %s" % server_address, file=sys.stderr)
TCP_Socket.bind(server_address)

TCP_Socket.listen(1)

while True:
  # waiting for connection
  print("waiting for a connection", file=sys.stderr)
  connection, client_address = TCP_Socket.accept()
  try:
    print("connection from", client_address, file=sys.stderr)

    while True:
      data = connection.recv(bufferSize)
      print('received "%s"' % data, file=sys.stderr)
      if data:
        print('sending data back to the client', file=sys.stderr)
      else:
        print('no more data from', client_address)
        break
  finally:
    connection.close()
