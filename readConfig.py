# -*-coding:utf-8-*-
from config import globalparameter as gl
import configparser
global configfile_path

# 获取配置文件路径
configfile_path = gl.configfile_path


class ReadConfig:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configfile_path)

    def getConfigValue(self, name):
        value = self.cf.get("config", name)
        return value

    def getcmdValue(self, name):
        value = self.cf.get("cmd", name)
        return value