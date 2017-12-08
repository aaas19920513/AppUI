# -*-coding:utf-8 -*-

from App_keywords import Action
from config import globalparameter as gl
import AppiumServer
import time

# 构建测试步骤
def buildStep( keyword, tag=None, loc=None, param=None, judge=None):

    key = keyword.lower()
    params = [tag, loc, param, judge]
    # 构建调用关键字方法的参数
    param_text = ""
    for index in range(0, len(params)):
        if params[index] == None or params[index] == "":
            continue
  #      if type(params[index]) == float:
        param_text += "'" + params[index] + "',"
    param_text = param_text[0:-1]
    if len(param_text) != 0:
        step = 'A.action_sign'+"(" + "\'" + key+'\',' + param_text + ")"
    else:
        step = 'A.action'+"(" + "\'" + key+'\''+")"
    return step

# 运行buildStep，filepath为测试用例文件，sheetno测试用例表名
def runStep(filepath = gl.project_path + '\\data\\test.xls',sheetno = 0):

    table = Action.readtable(filepath, sheetno)
    rows = table.nrows
    A = Action()
    for i in range(1, rows):
        value = table.row_values(i)[2:7]
        desc = table.row_values(i)[1]
        # 关键字
        key_word, tag, loc, para, judge = value[0], value[1], value[2], value[3], value[4]
        step = buildStep(key_word, tag, loc, para, judge)
        print desc+':' + step
 #       eval(step)

if __name__ == "__main__":
    server = AppiumServer.AppiumServer()
    server.start_server()
    time.sleep(10)
    A = Action()
    A.action_sign('click', 'id', 'com.taobao.taobao:id/home_searchedit')
    A.action_sign('send_keys', 'id', 'com.taobao.taobao:id/searchEdit', 'sssssss')
#    runStep()