# -*-coding:utf-8 -*-

__author__ = 'shikun'
import re
from math import floor
import subprocess
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 获取APK信息
class ApkInfo():

    def __init__(self, apkPath):
        self.apkPath = apkPath

# 得到app的文件大小
    def getApkSize(self):
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"


    def getApkPackagename(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print(self.apkPath)
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)

#        print('packagename:' + packagename)
#        print('versionCode:' + versionCode)
#        print('versionName:' + versionName)
        return packagename

    # 得到应用名字
    def getApkName(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        t = output.decode().split()
        for item in t:
            # print(item)
            match = re.compile("application-label:(\S+)").search(item)
            if match is not None:
#                print match.group(1)
                return match.group(1)


    # 得到启动类
    def getApkActivity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        if match is not None:

            return match.group(1)

if __name__ == '__main__':
 #   ApkInfo("F:\\apk\\taobao.apk").getApkActivity()
 #   ApkInfo("F:\\apk\\taobao.apk").getApkBaseInfo()
    pass