# Austin Yam
#Server
import socket
import sys
import math

#create socket
TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 60000)
print('Starting up on {} port {}'.format(*server_address))
TCPsock.bind(server_address)

TCPsock.listen(1)

while 1:
	print('waiting for connection')
	connection, client_address = TCPsock.accept()
	try:
		print('connection from: ', client_address)
		
		data = connection.recv(16)
		data = data.decode()
		data = int(data)
		print('received:', data)
		if data:
			data = math.sqrt(data)
			data = str(data)
			print('sending data back to client')
			connection.sendall(data.encode())
		else:
			print('no data from ', client_address)
			break
	finally:
		connection.close()
		
				
			


