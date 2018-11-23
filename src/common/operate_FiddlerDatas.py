#coding=utf-8
######################################
# filename:operate_FiddlerDatas.py
# function: 操作fiddler本地打点文件数据
# datetime:2018-11-21
# author:kitzhao
######################################

from urllib import parse
import configparser
import os,re,codecs


class FiddlerData(object):
    """
    处理fiddler本地文件数据
    """

    def __init__(self):
        """
        初始化 获取对应的fiddler日志目录
        """
        config_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath("__file__")))) + os.sep + "config.ini"
        config = configparser.ConfigParser()
        config.readfp(codecs.open(config_path, 'r', "utf-8"))
        logtype = config.get("DEFAULT", "fiddler_logs")
        self.log_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath("__file__")))) + os.sep + "fiddler_logs" + os.sep + logtype
        print(self.log_path)


    def get_logfiles(self):
        """
        获取对应目录下的 日志文件 
        """
        files = os.walk(self.log_path)
        for i in files:
            logfiles = i[2]
            return logfiles


    def url_decode(self,data):
        """
        对上报的数据进行url_decode 解码操作
        """
        return parse.unquote(data)


    def get_iphoneSystemType(self,data):
        """
        手机系统类型 ios or android 
        """
        try:
            d = re.findall("(?<=sysdata\"\:).*(?=\,\"bizdata)", data)
            return ((eval(d[0]))["clnt_tp"])
        except:
            return False

    def analyze_androidData(self,data):
        """
        安卓的数据解析
        """
        try:
            datalist = re.findall("(?<=info_customevent\":\[)(.*?)(?=\]\,\"info_)", data)
            AndroidData = eval(datalist[0])
            return AndroidData
        except:
            return False

    def analyze_iosData(self,data):
        """
        IOS的数据解析
        """
        try:
            datalist = re.findall("(?<=info_customevent\":\[)(.*?)(?=\])", data)
            IosData=eval(datalist[0])
            print(IosData)
        except:
            return False



    def parseFiddlerData(self):
        for i in self.get_logfiles():
            with open((self.log_path + os.sep + i), 'r', encoding="utf-8") as f:
                print(i)
                data = self.url_decode(f.read())
                system_type = self.get_iphoneSystemType(data)
                if system_type == "android":
                    try:
                        list = self.analyze_androidData(data)
                        for a in list:
                            print(i,type(a),a)
                    except:
                        False
                elif system_type == "iPhone":
                    try:
                        list = self.analyze_iosData(data)
                        for b in list:
                            print(b)
                    except:
                        False


if __name__ == "__main__":
    a = FiddlerData()
    a.parseFiddlerData()



