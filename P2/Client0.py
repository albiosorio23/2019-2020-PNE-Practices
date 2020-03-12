import socket
import termcolor



class Client:
    def ping(self):
        print("OK!")

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


