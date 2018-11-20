#coding=utf-8

from src.common.operate_excel import *
from src.config import *
import os

TestcaseName = ConfigIni.get_TestCaseName()
if not os.path.abspath(TestcaseName):
    raise Exception("Don't find testcase file:%s" %TestcaseName)

xls = XlsEngine(TestcaseName)
testcase_col = eval(ConfigIni.get_testcase_col())

print(xls.getsheets())
testid_col = testcase_col["TestId"]
print(testid_col)
a = xls.readcol("v4.8联版33120",testid_col)
print(a)


def Testid2Rown(cls, sheet, testid):
    """
    根据不同的testid转换成相应的行,
    """
    try:
        testid_col = cls.testcase_col['TestId']
        return cls.xlseng.readcol(sheet, testid_col).index(testid)  # 对Testid列进行数据读取，放置列表中——列表索引取值
    except:
        return False


def get_TestCaseName(sheet, testid):
    """
    获取TestCaseName
    """
    TestCaseName_col = testcase_col["TestCaseName"]
    TestCaseName_row = Testid2Rown(sheet, testid)
    if TestCaseName_row is False:
        return False
    return xls.readcell(sheet, TestCaseName_row, TestCaseName_col)

if __name__ == "__main__":
    # get_TestCaseName("v4.8_lianban_33120",'2')
    pass
