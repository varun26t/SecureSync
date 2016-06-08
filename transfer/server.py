#!/usr/bin/python3
import os
import socket

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
		with open(data, 'rb') as binary_data:
			with open(RECV_DATA, 'wb') as write_data:
				write_data.write(binary_data)

	if(choice!=1):
		pass




# import socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(("", 5005))
# server_socket.listen(5)
# import os


# client_socket, address = server_socket.accept()
# print "Conencted to - ",address,"\n"
# while (1):
#     choice = client_socket.recv(1024)
#     choice = int(choice)
#     if(choice == 1):
#         data = client_socket.recv(1024)
#         print "The following data was received - ",data
#         print "Opening file - ",data
#         fp = open(data,'r')
#         strng = fp.read()
#         size = os.path.getsize(data)
#         size = str(size)
#         client_socket.send(size)
#         client_socket.send (strng)
#         #client_socket.close()

#     if (choice == 2 or choice == 3):
#         data = client_socket.recv(1024)
#         print "The following data was received - ",data
#         print "Opening file - ",data
#         img = open(data,'r')
#         while True:
#             strng = img.readline(512)
#             if not strng:
#                 break
#             client_socket.send(strng)
#         img.close()
#         print "Data sent successfully"
#         exit()
#         #data = 'viewnior '+data
#         #os.system(data)