import socket, sys
import select

class ClassCanSocketClient(object):
    """Common base class for can socket client"""
    clientName=""

    def __init__(self, CanClientName,CanInterfaceName):
        ClassCanSocketClient.clientName = CanClientName
        self.sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        interface = CanInterfaceName
        try:
            self.sock.bind((interface,))
        except OSError:
            sys.stderr.write("Could not bind to interface '%s'\n" % interface)
            # do something about the error...

    def send(self,data):

        self.sock.send(data)

    def recv(self):

        ready = select.select([self.sock], [], [], 5)
        if ready[0]:
            return (self.sock.recv(100))
        return b""

    def close(self):
        self.sock.close()