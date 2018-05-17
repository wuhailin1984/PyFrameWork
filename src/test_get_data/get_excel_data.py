# -*- coding:utf-8 -*-

'''
File name：get_excle_data.py
Created on 2018年5月7日
@author: hailin
'''
import xlrd
import os


#file path
file_home = "../test_data/"
path2 = os.path.dirname(__file__)
print (path2)
file_home=os.path.abspath(os.path.join(path2, ".."))
print (file_home)

#file name
Testdata_p = xlrd.open_workbook(file_home+'\\test_data\\data.xlsx') #read data
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

