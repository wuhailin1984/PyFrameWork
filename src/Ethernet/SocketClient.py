import socket


class ClassSocketClient(object):
    """Common base class for socket client"""
    clientName=""

    def __init__(self, name, server_ip,server_port):
        ClassSocketClient.clientName = name
        self.serverIP = server_ip
        self.serverPort=server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.serverIP, self.serverPort))

    def send(self,data):

        self.sock.send(data)

    def recv(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()