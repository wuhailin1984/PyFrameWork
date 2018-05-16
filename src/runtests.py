# -*- coding:utf-8 -*-
'''
Created on 2018年5月7日
@author: Hailin
'''
import pytest
import sys

origin = sys.stdout
hlog = open('C:\\Users\\hwu\\PycharmProjects\\MyFrameWork\\src\\test_log\\log.txt', 'w')
sys.stdout = hlog
if __name__ == '__main__':
    args = ['-q', '-s']
    pytest.main(args)
    sys.stdout = origin
    hlog.close()
    print("Test result！")
