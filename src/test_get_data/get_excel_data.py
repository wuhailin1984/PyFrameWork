# -*- coding:utf-8 -*-

'''
File name：get_excle_data.py
Created on 2018年5月7日
@author: hailin
'''
import xlrd
#file path
file_home = "C:/Users/hwu/PycharmProjects/MyFrameWork/src/test_data/"
#file name
Testdata_p = xlrd.open_workbook(file_home+'data.xlsx') #read data
table = Testdata_p.sheets()[0] #choose sheet

def read_requestdata(test_case_name):
    nrows = table.nrows  # total lines
    for rownum in range(1, nrows):
        domain = table.cell(rownum,1).value  #read domain
        nm=table.cell(rownum,0).value #read test case name associated with current row
        print(domain)
        if nm==test_case_name:
            url = domain+table.cell(rownum,2).value
            print(url)
            return  url    #read path
    return ""

read_requestdata("test_get_node")