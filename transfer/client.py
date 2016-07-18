#!/usr/bin/python3
import os
from base64 import b64encode
import socket
import sys

def initClient(host, port,filename):

    print("ENTER CLIENT.PY")

    if not host or not port or not filename:
        sys.exit(0)

    TEMPORARY_FILE = '../data/TEMPORARY_FILE'
    TEMP_FRAG_DIR = '../data/send/'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    k = ' '
    size = 512

    while 1:
        k = input("Select file type\n1.Text File\n2.Image File\nChoice:\t")
        k = int(k)
        file_name = input("enter absolut path for the file *upload not available*")
        if (k == 1):
            with open(file_name, 'rb+') as file:
                with open(TEMPORARY_FILE, 'wb+') as temp:
                    temp.write(file)
                while os.listdir(TEMP_FRAG_DIR) != []:
                    file_list = os.listdir(TEMP_FRAG_DIR)
                    for file in file_list:
                        file_path = TEMP_FRAG_DIR + str(file)
                        client_socket.send(file_path)
                    end_transmit = "EOT"
                    client_socket.send(end_transmit)
