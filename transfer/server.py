#!/usr/bin/python3
import os
import socket
from hashlib import md5

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 8426))
server_socket.listen(1)

RECV_BLOCK = 512
RECV_DATA = os.path.join(os.path.join('/data/recv/tempdata'))

client_socket, addr = server_socket.accept()
print("Connected to client {} \n".format(addr))

while (1):
	choice = client_socket.recv(RECV_BLOCK)
	choice = int(choice)

	if(choice==1):
		data = client_socket.recv(RECV_BLOCK)
		if data == "EOT":
			break
		else:
			md5sum = md5(data)
			client_socket.send(md5sum)
			with open(data, 'rb') as binary_data:
				with open(RECV_DATA, 'wb') as write_data:
					write_data.write(binary_data)

	if(choice!=1):
		pass

