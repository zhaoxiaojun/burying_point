#coding=utf-8
######################################
# filename:operate_dataExcel.py
# function: excel文件的操作
# datetime:2018-08-09
# author:kitzhao
######################################
import xlrd
import os


class XlsEngine():
    """
    The XlsEngine is a class for excel operation
    """
    def __init__(self,xlsname):
        """
        define class variable
        """
        self.xlsname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  + "\\" +  xlsname
        self.xlrd_object = xlrd.open_workbook(self.xlsname)

    def getsheets(self):
        """
        get xls file's sheets
        """
        return self.xlrd_object.sheet_names()

    def getrows(self,sheetname):
        """
        get xls file all rows
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.nrows

    def getcols(self,sheetname):
        """
        get xls file all cols
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.ncols

    def readrow(self,sheetname,rown):
        """
        read file's a row content to list
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.row_values(rown)

    def readcol(self,sheetname,coln):
        """
        read file's a col content to list
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.col_values(coln)

    def readcell(self,sheetname,rown,coln):
        """
        read file's cell
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.cell_value(rown,coln)


    def writecell(self,sheetname,rown,coln,value):
        """
        write a cell to file,other cell is not change
        """
        pass

if __name__ == "__main__":
    a = XlsEngine("burring_point_testcase.xlsx")
    print(a.readcol("v5.3功能区33168",2))
    print(a.readcol("v5.3功能区33168",0))
    print(a.readrow("v5.3功能区33168",1))

