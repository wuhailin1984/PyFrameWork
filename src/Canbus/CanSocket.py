import socket, sys


class ClassCanSocketClient(object):
    """Common base class for can socket client"""
    clientName=""

    def __init__(self, CanClientName,CanInterfaceName):
        ClassCanSocketClient.clientName = CanClientName
        sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        interface = CanInterfaceName
        try:
            sock.bind((interface,))
        except OSError:
            sys.stderr.write("Could not bind to interface '%s'\n" % interface)
            # do something about the error...

    def send(self,data):

        self.sock.send(data)

    def recv(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()