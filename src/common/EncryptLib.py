#coding=utf-8
######################################
# filename:EncryptLib.py
# function:常见的数据的加减密机编码处理
# datetime:2018-11-21
# author:kitzhao
######################################

import hashlib
import base64
from urllib import parse


def generate_sign(data):
    """
    进行MD5处理
    """
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

def get_sha1(data):
    """
    sha1加密
    """
    s = hashlib.sha1()
    s.update(data)
    return s.hexdigest()

def get_base64(data):
    """
    base64加密
    """
    b64 = base64.b64encode(data)
    return b64

def getde_base64(encrypted):
    """
    base64解密
    """
    data = base64.b64decode(encrypted)
    return data

def url_decode(data):
    """
    url_decode解码
    """
    return parse.unquote(data)

