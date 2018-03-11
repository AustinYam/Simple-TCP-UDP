#Austin Yam
#UDP Server 

import socket
import sys
import math

#create UDP socket
UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 60000)
print('starting up on {} port {}'.format(*server_address))
UDPsock.bind(server_address)

while 1:
	#Waiting for client message
	print('waiting for message...')
	data, addr = UDPsock.recvfrom(4096)
	data = data.decode()
	data = int(data)
	print('received:', data)
	if data:
		#square root function on received data
		data = math.sqrt(data)
		data = str(data)
		#sending square root of data back to client
		print('sending data back to client')
		UDPsock.sendto(data.encode(),addr)
		print('sent:', data)
	else:
		print('no data from client')
		break 