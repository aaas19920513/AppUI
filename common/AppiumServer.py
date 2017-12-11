# -*-coding:utf-8-*-
__author__ = 'tuihou'

import os
import requests
from multiprocessing import Process
import readConfig
import threading
import time
cf = readConfig.ReadConfig()


class AppiumServer:

    def __init__(self):
        global openAppium, baseUrl, stopAppium
        openAppium = cf.getcmdValue("openAppium")
        stopAppium = cf.getcmdValue("stopAppium")
        baseUrl = cf.getConfigValue("baseUrl")

    def start_server(self):
        """start the appium server
        :return:
        """
        t1 = RunServer(openAppium)
        p = Process(target=t1.start())
        p.start()

    def stop_server(self):
        """stop the appium server
        :return:
        """
        # kill myServer
        # 参考https://www.cnblogs.com/CoreXin/p/5566607.html
        os.popen(stopAppium)

    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        req = None
        url = baseUrl+"/status"
        try:
            req = requests.get(url)
            code = req.status_code
            if str(code).startswith('2'):
                return True
            else:
                return False
        except :
            return False
        finally:
            if req:
                req.close()


class RunServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)


if __name__ == "__main__":

    server = AppiumServer()
#    server.start_server()
    time.sleep(5)
    print("strart server")
    print("running server")
    if server.is_runnnig():
        print 1111
    else:
        print 22
        server.re_start_server()

 #   time.sleep(30)
#    server.stop_server()
 #  print("stop server")