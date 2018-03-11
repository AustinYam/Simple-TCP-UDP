#Austin Yam
#UDP Client

import socket
import sys

#create UDP client socket
UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 60000)
print('connecting to {} port {}'.format(*server_address))

try:
	#user input number
	msg = input('Enter number: ')
	try:
		val = int(msg)
	except ValueError:
		print('Not an int!')
	print('sending {!r}'.format(msg))
	send = UDPsock.sendto(msg.encode(), server_address)
	
	#server response
	response, server = UDPsock.recvfrom(4096)
	print('received: ', response.decode())
	
		
finally:
#close socket and program
	print('closing socket')
	UDPsock.close()
	sys.exit()
