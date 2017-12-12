# -*- coding:utf-8 -*-


import xlrd
from config import globalparameter as gl

class ReadExcel():


    def __init__(self, excelPath, sheetNo):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_index(sheetNo)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols


    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

if __name__ == "__main__":
    filepath = gl.project_path + '\\data\\test.xls'
    sheetNo = 0
    data = ReadExcel(filepath, sheetNo)
    dict = data.dict_data()
    for i in range(2):
          print dict[i]