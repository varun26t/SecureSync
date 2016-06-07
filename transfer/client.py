#!/usr/bin/python3
import os
import socket

TEMPORARY_FILE = '../data/TEMPORARY_FILE'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("",8426))

k = ' '
size = 512

while 1:
	k= input("Select file type\n1.Text File\n2.Image File\n3.Video")
	k = int (k)
	if(k == 1 ):
		file_name = input("enter absolut path for the file *upload not available*")
		with open(file_name,'rb') as file:
                	with open(TEMPORARY_FILE, 'wb') as temp:
                		temp.write(file)
			#write to a file 
	if( k == 2 or k == 3 ):
		pass




'''
#!/usr/bin/python
# TCP client example
import socket,os
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("", 5005))
k = ' '
size = 1024

while(1):
    print "Do you want to transfer a \n1.Text File\n2.Image\n3.Video\n"
    k = raw_input()
    client_socket.send(k)
    k = int (k)
    if(k == 1):
        print "Enter file name\n"
        strng = raw_input()
        client_socket.send(strng)
        size = client_socket.recv(1024)
        size = int(size)
        print "The file size is - ",size," bytes"
        size = size*2
        strng = client_socket.recv(size)
        print "\nThe contents of that file - "
        print strng

    if (k==2 or k==3):
        print "Enter file name of the image with extentsion (example: filename.jpg,filename.png or if a video file then filename.mpg etc) - "
        fname = raw_input()
        client_socket.send(fname)
        fname = 'documents/'+fname
        fp = open(fname,'w')
        while True:
            strng = client_socket.recv(512)
            if not strng:
                break
            fp.write(strng)
        fp.close()
        print "Data Received successfully"
        exit()
        #data = 'viewnior '+fname
        #os.system(data)
'''
