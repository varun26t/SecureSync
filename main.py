#Global Imports
import os
import sys
import argparse
import threading

#Local Imports
# from crypto import encrypt
# from crypto import decrypt
# from transfer import server
from transfer import client
# from frag.fragmentation import Fragment

class SecureSync:

    def __int__(self):
        pass

    def parseAgs(self,args):
        print(args)
        if args.client and args.host and args.port and args.file:
            client.initClient(args.host,args.port,args.file)

if __name__ ==  '__main__':

    #init argparse
    parser = argparse.ArgumentParser()

    #add arguments
    parser.add_argument("--client")
    parser.add_argument("--server")
    parser.add_argument("--file")
    parser.add_argument("--host", default="127.0.0.1", help="Set host Address")
    parser.add_argument("--port", default=8426, help="Set port for application")

    args = parser.parse_args()

    classObject = SecureSync()
    classObject.parseAgs(args)
