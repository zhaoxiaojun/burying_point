#coding=utf-8
######################################
# filename:config.py
# function: 对配置文件的操作
# datetime:2018-08-09
# author:kitzhao
######################################
import configparser
import os
import codecs

class ConfigIni():
    """
    配置类
    """
    config_path = os.path.dirname(os.path.dirname(os.path.abspath("__file__"))) + os.sep + 'config.ini'
    # print(config_path)
    if not os.path.isfile(config_path):
        raise Exception("This is not config file.")

    config = configparser.ConfigParser()
    config.readfp(codecs.open(config_path, 'r', "utf-8"))
    # config.read(config_path)

    @classmethod
    def get_TestCaseName(cls):
        """
        获取测试用例名称
        """
        return cls.config.get("DEFAULT","TestCaseName")


    @classmethod
    def get_RunMode(cls):
        """
        获取运行模式
        """
        return cls.config.get("DEFAULT","runmode")

    @classmethod
    def get_index(cls):
        """
        获取待执行的测试用例
        """
        return cls.config.get("DEFAULT","index")

    @classmethod
    def get_unindex(cls):
        """
        获取不被执行的测试用例
        """
        return cls.config.get("DEFAULT","unindex")

    @classmethod
    def get_testcase_col(cls):
        """
        获取测试用例列定义
        """
        return cls.config.get("DEFAULT","testcase_col")

    @classmethod
    def get_iscontrol(cls):
        """
        获取日志开关
        """
        return cls.config.get("DEFAULT","iscontrol")

    @classmethod
    def get_isstdebug(cls):
        """
        获取debug开关
        """
        return cls.config.get("DEFAULT","isstdebug")

    @classmethod
    def get_isSendMail(cls):
        """
        获取邮件开关
        """
        return cls.config.get("DEFAULT","isSendMail")

    @classmethod
    def get_send_emladdr(cls):
        """
        获取邮件地址
        """
        return cls.config.get("DEFAULT","send_emladdr")

    @classmethod
    def get_TestEnvironment_Info(cls,section,field):
        """
        获取接口测试环境信息
        """
        return cls.config.get(section,field)


if __name__ == "__main__":
    print(ConfigIni().get_testcase_col())
    print(eval(ConfigIni().get_testcase_col()))
    print(eval(ConfigIni().get_TestEnvironment_Info("DEFAULT","send_emladdr")))


