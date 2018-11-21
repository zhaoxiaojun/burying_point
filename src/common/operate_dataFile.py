#coding=utf-8
######################################
# filename:operate_dataFile.py
# function: 操作fiddler本地打点文件数据
# datetime:2018-11-21
# author:kitzhao
######################################

from urllib import parse
import os,re


filepath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath("__file__")))) + os.sep + "logs"
print(filepath)
files = os.walk(filepath)
for i in files:
    a = (i[2][0])
    files = filepath + os.sep + a
    with open(files,'r',encoding="utf-8") as f:
        b = f.read()

def url_decode(txt):
    return parse.unquote(txt)

c = url_decode(b)
print(c)
#android

#iphone
def get_iphonetype(data):
    c = url_decode(data)
    d = re.findall("(?<=sysdata\"\:).*(?=\,\"bizdata)",c)
    return ((eval(d[0]))["clnt_tp"])

print(get_iphonetype(b))


# android
def analyze_androidData(txt):
    datatxt = url_decode(txt)
    datalist = re.findall("(?<=info_customevent\":).*(?=\,\"info_page)", datatxt)
    return eval(datalist[0])

# ios
def analyze_iosData(txt):
    list_a = (re.findall("(?<=info_customevent\":\[).*(?=\]\})", txt))
    return eval(list_a[0])


if __name__ == "__main__":
    # print(analyze_androidData(b))
    # print(analyze_iosData(b))
    # print(len(analyze_iosData(b)))
    # for i in analyze_iosData(b):
    #     if "appHomeexposure" in i.values():
    #         del i["event_detail"]["id"]
    #         print(i["event_detail"])
    #     elif "click" in i.values():
    #         del i["event_detail"]["id"]
    #         print(i["event_detail"])
    pass


