import socket

localHost=socket.gethostbyaddr() # get local machine addr
localPort = 60000  # reserve a port for your service

fileDownload=socket.socket() #create a socket object
fileDownload.bind((localHost, localPort))
fileDownload.listen(5)

print("Server listening......")

while True:
  connection, addr=fileDownload.accept()
