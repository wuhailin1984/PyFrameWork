from src.Ethernet.SocketClient import ClassSocketClient
import time

#soc = ClassSocketClient("Sensor1","35.204.196.49",3001)
soc = ClassSocketClient("Sensor1","127.0.0.1",3001)
dataBytes=bytearray()
dataBytes.append(0x88 )
dataBytes.append(0x5C )
dataBytes.append(0x01 )
dataBytes.append(0 )
dataBytes.append(0 )
soc.send(dataBytes)
time.sleep(2)
soc.send(dataBytes)

recv=soc.recv()
result=recv.decode(encoding='utf-8')
print(recv)
print(result)
assert ("dealed a message from sensor" in result)
soc.close()
