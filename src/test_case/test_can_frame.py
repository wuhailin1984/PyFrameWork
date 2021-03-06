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


    @allure.feature('Feature:Communication with virtual can0')
    @allure.story('User story: Valid data')
    def test_Can0_Valid(self):
        soc = ClassCanSocketClient("vcan0","vcan0")
        fmt = "<IB3x8s"
        #can_id = 0x1af0 | socket.CAN_EFF_FLAG
        can_id = 0x1af0 | 0x80000000
        can_pkt = struct.pack(fmt, can_id, len(b"hello"), b"hello")
        soc.send(can_pkt)
        print(can_pkt)

        rec_data=soc.recv()

        print(rec_data)

        rec_data_tuple=struct.unpack(fmt,rec_data)
        data1 = rec_data_tuple[0]
        data2 = rec_data_tuple[1]
        data3 = rec_data_tuple[2]
        print(data1)
        print(data2)
        print(data3)


