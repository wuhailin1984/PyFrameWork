import pytest
import allure
from src.Canbus.CanSocket import ClassCanSocketClient
import time
import struct
import socket

class Test_Sensor1(object):

    #@pytest.fixture()
    def BeforeTest(self):
        i=0

        

    @allure.feature('Feature:Communication with sensor1')
    @allure.story('User story: Valid data')
    def test_Sensor1_Valid(self):
        soc = ClassCanSocketClient("Vcan0","Vcan0")
        fmt = "<IB3x8s"
        can_id = 0x1af0 | socket.CAN_EFF_FLAG
        can_pkt = struct.pack(fmt, can_id, len(b"hello"), b"hello")
        soc.send(can_pkt)