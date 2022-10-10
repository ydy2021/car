# encoding:utf-8

import requests
import base64
from aip import AipBodyAnalysis

""" 你的 APPID AK SK """
APP_ID = '27739746'
API_KEY = 'N5MaqhCVwttlHTQGPINRx8wx'
SECRET_KEY = 'E2ta4XTU0ZkefrsntrbXkAks2VIuhTcM'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
print("hello")
'''
人体关键点识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
# 二进制方式打开图片文件
f = open('/home/yahboom/codes/aip-python-sdk-4.16.7/1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = "24.207e490e7827632e0fd045c0dd9396bc.2592000.1667390809.282335-27739746"
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())