from socket import *
serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort)) 
serverSocket.listen(1)
print "ready"
while True:
	connectionSocket,Address = serverSocket.accept()
	message = connectionSocket.recv(1024)
	modifiedMessage = message.upper()
	connectionSocket.send(modifiedMessage)
	print "has send to:"+str(Address)