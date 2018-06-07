import socket
import select


class ClassSocketClient(object):
    """Common base class for socket client"""
    clientName=""

    def __init__(self, name, server_ip,server_port):
        ClassSocketClient.clientName = name
        self.serverIP = server_ip
        self.serverPort=server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.serverIP, self.serverPort))
        self.sock.setblocking(0)
        #self.sock.settimeout(5)

    def send(self,data):

        self.sock.send(data)

    def recv(self):
        ready = select.select([self.sock], [], [], 5)
        if ready[0]:
            return self.sock.recv(100)
        return  b""


    def close(self):
        self.sock.close()