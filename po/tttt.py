# -*- coding:utf-8 -*-

import requests
baseUrl='http://127.0.0.1:4723/wd/hub'
def is_runnnig():
    """Determine whether server is running
    :return:True or False
    """
    response = None
    url = baseUrl + "/status"

    req = requests.get(url)
    code = req.status_code
#   print req.status_code
    if str(code).startswith('2'):
        print req.status_code


is_runnnig()