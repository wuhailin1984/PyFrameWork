import pytest
import allure
from src.Ethernet.SocketClient import ClassSocketClient
import time

class Test_Sensor1(object):

    #@pytest.fixture()
    def BeforeTest(self):
        i=0

    @allure.feature('Feature:Communication with sensor1')
    @allure.story('User story: Valid data')
    def test_Sensor1_Valid(self):
        soc = ClassSocketClient("Sensor1", "10.46.40.149", 3001)
        dataBytes = bytearray()
        dataBytes.append(0x88)
        dataBytes.append(0x5C)
        dataBytes.append(0x01)
        dataBytes.append(0)
        dataBytes.append(0)
        soc.send(dataBytes)
        time.sleep(2)
        soc.send(dataBytes)

        recv = soc.recv()
        result = recv.decode(encoding='utf-8')
        print(recv)
        print(result)
        assert ("dealed a message from sensor" in result)
        soc.close()

    @allure.feature('Feature:Communication with sensor1')
    @allure.story('User story: Invalid data')
    def test_Sensor1_Invalid(self):
        #soc = ClassSocketClient("Sensor1", "127.0.0.1", 3001)
        soc = ClassSocketClient("Sensor1", "10.46.40.149", 3001)
        dataBytes = bytearray()
        dataBytes.append(0x81)
        dataBytes.append(0x5C)
        dataBytes.append(0x01)
        dataBytes.append(0)
        dataBytes.append(0)

        key = bytes([0x81, 0x5C, 0x01, 0x00, 0x08])

        soc.send(dataBytes)
        time.sleep(2)
        soc.send(dataBytes)

        recv = soc.recv()
        result = recv.decode(encoding='utf-8')
        print(recv)
        print(result)
        soc.close()
        assert ("Wrong message" in result)

    @allure.feature('Feature:Communication with sensor1')
    @allure.story('User story: Invalid data length')
    def test_Sensor1_Invalid_length(self):
        soc = ClassSocketClient("Sensor1", "10.46.40.149", 3001)
        dataBytes = bytearray()
        dataBytes.append(0x81)
        dataBytes.append(0x5C)
        dataBytes.append(0x01)
        dataBytes.append(0)

        soc.send(dataBytes)
        time.sleep(2)
        soc.send(dataBytes)

        recv = soc.recv()
        result = recv.decode(encoding='utf-8')
        print(recv)
        print(result)
        soc.close()
        assert ("Wrong message" in result)