#coding=utf-8
########################################
#filename:Global.py
#function:全局变量和通用功能函数
#datetime:2018-11-23
#author:kitzhao
########################################
import logging
import time,datetime
import queue
import platform
from io import StringIO
import inspect
import os
import re
import requests
from src.common.EncryptLib import *
import threading



#日志
#global loggerfile,loggercontrol
loggerfile = logging.getLogger("logfile")
loggercontrol = logging.getLogger("control")

#断言任务队列
#global taskassert_queue
taskassert_queue = queue.Queue()

#保存测试结果
#global testcase_result
testcase_result = {}

#内存数据
#global memdata
memdata = StringIO()  #不能跨进程

########################################################################################################################

def get_someday(xx):
    """
    获取当前及之前的日期 格式:"%Y-%d-%m"
    """
    someday = datetime.date.today() + datetime.timedelta(days=xx)
    return someday.strftime("%Y-%m-%d")

def getnowstamp():
    """
    获取当前时间戳
    """
    return time.time()

def getnowtime():
    '''
    获取当前%Y-%m-%d %H:%M:%S格式时间
    '''
    nows = time.strftime("%Y-%m-%d %H:%M:%S")
    return nows

def ch2unicode(data):
    '''
    转换为unicode
    '''
    if type(data) is unicode:
        return data
    if type(data) is not str:
        data = str(data)
    try:
        data = unicode(data, 'utf-8')
    except UnicodeDecodeError:
        data = unicode(data, 'gbk')
    return data

def ch2s(s):
    '''
    写字符串时针对不同系统的编码转换
    '''
    systype = platform.system()
    if systype == 'Windows':
        us = ch2unicode(s)
        return us.encode('gbk')
    if systype == 'Linux':
        us = ch2unicode(s)
        return us.encode('utf-8')
    else:
        return s

def PrintLog(loglevel, fixd, *data):
    '''
    打印日志
    '''
    iscontrol = int(memdata.getvalue().split('+++')[0])
    isstdebug = int(memdata.getvalue().split('+++')[1])
    if loglevel == 'exception':
        getattr(loggerfile, loglevel)(fixd)
        if iscontrol != 0:
            getattr(loggercontrol, loglevel)(fixd)
    else:
        systype = platform.system()
        if systype == 'Windows' and isstdebug == 0:
            enty = 'gbk'
        else:
            enty = 'utf-8'

        #获取调用函数的文件名和行号
        filepath = inspect.stack()[1][1]
        filename = os.path.basename(filepath)
        linen = inspect.stack()[1][2]
        fixdd = u'%s[%d] - '

        fixdf = (fixdd + ch2unicode(fixd)).encode('utf-8')
        fixdc = (fixdd + ch2unicode(fixd)).encode(enty)
        valuesf = [filename,linen]
        valuesc = [filename,linen]
        for d in data:
            df = ch2unicode(d).encode('utf-8')
            dc = ch2unicode(d).encode(enty)
            valuesf.append(df)
            valuesc.append(dc)
        getattr(loggerfile, loglevel)(fixdf % tuple(valuesf))
        if iscontrol != 0:
            getattr(loggercontrol, loglevel)(fixdc % tuple(valuesc))

#根据不同环境下的接口，选取不同的处理方法
#生产环境提取token及userid
def Get_TokenUserid(username,password):
    url = 'http://passport.ewt360.com/login/prelogin?callback=jQuery111205653414290805507_1465181153664&sid=2&username=%s&password=%s&fromurl=http://www.ewt360.com/&isremember=1&_=1465181153665' %(username,password)
    response = requests.get(url)
    res = response.content
    token = re.findall('tk=(.*?)&fromurl', res)
    token = token[0]
    userid = re.findall("(.*?)-", token)
    userid = userid[0]
    c = 30205014
    userid = int(userid) ^ c
    return token, userid

#测试环境提起token及userid
def Get_TestTokenUserid(username,password):
    url = 'http://my.233.mistong.com/login/prelogin?callback=jQuery111205653414290805507_1465181153664&sid=2&username=%s&password=%s&fromurl=http://www.233.mistong.com/&isremember=1&_=1465181153665' % (username, password)
    response = requests.get(url)
    res = response.content
    token = re.findall('tk=(.*?)&fromurl', res)
    token = token[0]
    userid = re.findall("(.*?)-", token)
    userid = userid[0]
    c = 30205014
    userid = int(userid) ^ c
    return token, userid


#可以从cookie中取出token
def Get_Tokenforcookie(username,password):
    url = 'http://my.233.mistong.com/login/prelogin?callback=jQuery111205653414290805507_1465181153664&sid=2&username=%s&password=%s&fromurl=http://www.233.mistong.com/&isremember=1&_=1465181153665' %(username,password)
    response = requests.get(url)
    res = response.cookies
    token = re.findall('user=tk=(.*?)&info', str(res))
    return token[0]

#提交讲的评论之前需要调用该方法
def SubmitLesRecord(lessonid,data):
    url = "http://kc.ewt360.com/KeChengApi/LessonRecords"
    sign = generate_sign(data)
    params = {"lessonid":lessonid,"sign":sign}
    requests.post(url,params)

# 提取userid并进行异或处理
# def GetUserId(username, password):
#     userid = re.findall("(.*?)-", Get_Token(username, password))
#     a = userid[0]
#     c = 30205014
#     return int(a)^c






