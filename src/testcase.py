#coding=utf-8
######################################
# filename:testcase.py
# function: 对testcase.xlsx数据操作
# datetime:2018-08-09
# author:kitzhao
######################################

from src.common.operate_dataExcel import *
from src.config import *
import os

class TestCaseXls(object):
    """测试用例类"""
    TestcaseName = ConfigIni.get_TestCaseName()
    if not os.path.abspath(TestcaseName):
        raise Exception("Don't find testcase file:%s" %TestcaseName)

    xlseng = XlsEngine(TestcaseName)
    testcase_col = eval(ConfigIni.get_testcase_col())

    @classmethod
    def get_TestCaseSheets(cls):
        """
        获取用例文件所有的sheets
        """
        return cls.xlseng.getsheets()

    @classmethod
    def Testid2Rown(cls, sheet, testid):
        """
        根据不同的testid转换成相应的行,
        """
        try:
            testid_col = cls.testcase_col['TestId']
            return cls.xlseng.readcol(sheet, testid_col).index(testid)  # 对Testid列进行数据读取，放置列表中——列表索引取值
        except:
            return False

    @classmethod
    def get_TestCaseName(cls, sheet, testid):
        """
        获取TestCaseName
        """
        TestCaseName_col = cls.testcase_col["TestCaseName"]
        TestCaseName_row = cls.Testid2Rown(sheet, testid)
        if TestCaseName_row is False:
            return False
        return cls.xlseng.readcell(sheet, TestCaseName_row, TestCaseName_col)

    @classmethod
    def get_TestCaseId(cls, sheet, testid):
        """
        获取TestCaseId
        """
        TestCaseId_col = cls.testcase_col["TestCaseId"]
        TestCaseId_row = cls.Testid2Rown(sheet, testid)
        if TestCaseId_row is False:
            return False
        return cls.xlseng.readcell(sheet, TestCaseId_row, TestCaseId_col)

    @classmethod
    def get_TestItem(cls, sheet, testid):
        """
        获取TestItem
        """
        TestItem_col = cls.testcase_col["TestItem"]
        TestItem_row = cls.Testid2Rown(sheet, testid)
        if TestItem_row is False:
            return False
        return cls.xlseng.readcell(sheet, TestItem_row, TestItem_col)

    @classmethod
    def get_TestType(cls, sheet, testid):
        """
        获取TestType
        """
        TestType_col = cls.testcase_col["TestType"]
        TestType_row = cls.Testid2Rown(sheet, testid)
        if TestType_row is False:
            return False
        return cls.xlseng.readcell(sheet, TestType_row, TestType_col)

    @classmethod
    def get_TestEnvironment(cls, sheet, testid):
        """"
        获取TestEnvironment
        """
        TestEnvironment_col = cls.testcase_col["TestEnvironment"]
        TestEnvironment_row = cls.Testid2Rown(sheet, testid)
        if TestEnvironment_row is False:
            return False
        return cls.xlseng.readcell(sheet, TestEnvironment_row, TestEnvironment_col)

    @classmethod
    def get_TestData(cls, sheet, testid):
        """
        获取TestData
        """
        TestData_col = cls.testcase_col["TestData"]
        TestData_row = cls.Testid2Rown(sheet, testid)
        if TestData_row is False:
            return False
        return cls.xlseng.readcell(sheet, TestData_row, TestData_col)

    @classmethod
    def get_Expectation(cls, sheet, testid):
        """
        获取Expectation
        """
        Expectation_col = cls.testcase_col["Expectation"]
        Expectation_row = cls.Testid2Rown(sheet, testid)
        if Expectation_row is False:
            return False
        return cls.xlseng.readcell(sheet, Expectation_row, Expectation_col)

    @classmethod
    def get_Alltestid(cls, *sheet):
        """
        获取所有testid，或指定sheet页中的所有testid
        """
        testid_col = cls.testcase_col["TestId"]
        if sheet:
            if type(sheet[0]) is list:
                sheelist = sheet[0]
            else:
                sheelist = [sheet[0]]
        else:
            sheelist = cls.xlseng.getsheets()
        alltestid = {}
        for sheet in sheelist:
            testid_allvalue = cls.xlseng.readcol(sheet, testid_col)  # 读取excel表中TestId列值
            testid_allvalue = [x for x in testid_allvalue if type(x) is float]  # 过滤 排除testId值
            testid_allvalue = list(set(testid_allvalue))  # 去重，通过元祖与列表之间的转换
            testid_allvalue = map(int, testid_allvalue)  # map高阶函数的使用
            alltestid[sheet] = testid_allvalue  # 拼装成字典
        return alltestid


if __name__ == "__main__":
    print(TestCaseXls.get_TestCaseSheets())
    print(TestCaseXls.Testid2Rown("v4.8_lianban_33120",4))
    print(TestCaseXls.get_TestCaseName("v4.8_lianban_33120",3))
    print(TestCaseXls.get_Alltestid(["IsCommentPost","v4.8_lianban_33120"]))


