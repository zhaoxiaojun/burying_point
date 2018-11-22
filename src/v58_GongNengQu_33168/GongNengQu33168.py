#coding=utf-8
########################################
#filename:GongNengQu33168.py
#function:功能区的数据解析
#datetime:2018-11-21
#author:kitzhao
########################################

import json
from src.common.operate_FiddlerDatas import *


class GongNengQu33168(object):
    """
    获取接口环境信息，并进行相应解析处理
    """
    def __ini__(self):
        pass

    def parseFiddlerData(self,data):
        pass


    def parseExpectationForAssert(self,Expectation):
        """
        解析预期数据
        """
        try:
            if Expectation == '':
                raise ValueError
            else:
                ExpectationDict = json.loads(Expectation)
            return ExpectationDict
        except:
            return False

    def parseResponseForAssert(self,Response):
        """
        解析响应数据
        """
        try:
            if Response == "":
                raise ValueError
            else:
                ResponseDict = json.loads(Response)
            return ResponseDict
        except:
            return False


class GongNengQu33168_Assert(object):
    """
    GongNengQu33168_Assert断言
    """
    def __init__(self):
        pass

    def parseResponseCode(self,response):
        """
        HTTP状态码校验
        """
        httpCode = response.status_code
        assert httpCode == 200,u"HTTP响应码错误:ErrorResponseCode:%s" % str(httpCode)


    def checkMsgField(self,ExpectationDict,ResponseDict):
        """
        因该接口返回字段中没有msg字段，所以通过code值校验
        """
        if ExpectationDict['code'] == 200:
            assert ResponseDict['code'] == ExpectationDict['code'],u'msg——获取收藏课程列表失败！'
        if ExpectationDict['code'] == 705:
            assert ResponseDict['code'] == ExpectationDict['code'],u'msg——输入参数错误！'
        if ExpectationDict['code'] == 703:
            assert ResponseDict['code'] == ExpectationDict['code'],u'msg——sign签名校验失败！'
        if ExpectationDict['code'] == 555:
            assert ResponseDict['code'] == ExpectationDict['code'],u'异常！'

    def checkKeysField(self,ExpectationDict,ResponseDict):
        """
        keys检验
        """
        AddAudioRecordInstance = AddAudioRecord()
        ExpectationDict_keys = AddAudioRecordInstance.getKeys(ExpectationDict)
        ResponseDict_keys = AddAudioRecordInstance.getKeys(ResponseDict)
        assert ExpectationDict_keys == ResponseDict_keys,u'响应与预期结果数据不匹配'

    def AddAudioRecordAssert(self,Response,ExpectationDict):
        """
        AddAudioRecord断言入口
        """
        try:
            #解析响应数据
            a = AddAudioRecord()
            ResponseDict = a.parseResponseForAssert(Response)

            #检查响应
            self.parseResponseCode(Response)

            #检查明文中的code对应的msg
            self.checkMsgField(ExpectationDict,ResponseDict)

            #检查明文中的key值
            self.checkKeysField(ExpectationDict,ResponseDict)
            return "PASS",
        except AssertionError as e:
            return "FAIL", unicode(e)
        except Exception as e:
            return "ERROR", unicode(e)





