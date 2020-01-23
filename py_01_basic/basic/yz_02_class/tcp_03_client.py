import socket
import sys

localIP = "127.0.0.1"
localPort = 65000
bufferSize = 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (localIP, localPort)
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:

  # Send data
  message = "This is the message.  It will be repeated."
  print('sending "%s"' % message, file=sys.stderr)
  sock.sendall(str.encode(message))

  # Look for the response
  amount_received = 0
  amount_expected = len(message)

  while amount_received < amount_expected:
    data = sock.recv(bufferSize)
    amount_received += len(data)
    print('received "%s"' % data, file=sys.stderr)

finally:
  print('closing socket', file=sys.stderr)
  sock.close()
