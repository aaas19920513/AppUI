# -*-coding:utf-8 -*-
import xlrd

def readtable(filepath, sheetno):
    '''

    :param filepath:
    :param sheetno:
    :return:
    '''
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[sheetno]
    return table


# 读取xls表格，使用生成器yield进行按行存储
def readxls(filepath, sheetno):
    '''
    :param filepath:
    :param sheetno:
    :return:
    '''
    table = readtable(filepath, sheetno)
    for args in range(1, table.nrows):
        yield table.row_values(args)


# 读取元素标签和元素唯一标识
def locate(index, filepath, sheetno=0):
    """
     :param index:
     :param filepath:
     :param sheetno:
     :return:
     """
    table = readtable(filepath, sheetno)
    for i in range(1, table.nrows):
        if index in table.row_values(i):
            return table.row_values(i)[1:3]