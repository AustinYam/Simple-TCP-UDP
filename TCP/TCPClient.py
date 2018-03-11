#Austin Yam
#TCP Client

import socket
import sys

#create TCP client socket
TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 60000)
print('connecting to {} port {}'.format(*server_address))
TCPsock.connect(server_address)

while True:
	try:
	#user input number
		msg = input('Enter number: ')
		try:
			val = int(msg)
		except ValueError:
			print('Not an int!')
		print('sending {!r}'.format(msg))
		TCPsock.sendall(msg.encode())
		
		#server response
		response = TCPsock.recv(16)
		print('received: ', response.decode())
	
		
	finally:
	#close socket and program
		print('closing socket')
		TCPsock.close()
		sys.exit()
