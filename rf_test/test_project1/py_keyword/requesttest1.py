from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
import requests
import unittest

class APIMethod():
    def __init__(self,url,methodtype,data=None,header=None,encodingtype="utf-8"):
        self.url = url
        self.methodtype = methodtype
        self.data = data
        self.header = header
        self.encodingtype = encodingtype

    def ExecuteMethod(self):
        if self.methodtype == "get":
            req = requests.get(url=self.url,params=self.data,headers=self.header)
        elif self.methodtype == "post":
            req = requests.post(url=self.url,data=self.data,headers=self.header)
        print("Response status code is : " + f'{req.status_code}')
        print("Response content is : " + f'{req.content.decode(self.encodingtype)}')
        print("Response header is : " + f'{req.headers}')
        print("Response cookie is : " + f'{req.cookies}')
        print("Response apparent_encoding is : " + f'{req.apparent_encoding}')
        return req

class APITest(unittest.TestCase):
    url = "https://httpbin.org"
    def test_001(self):
        #self.url = self.url + "/get"+"?name=xx&age=yy"  方法1
        self.url = self.url + "/get"
        params = {"name":"张三","age":"yy"}
        req1 = requests.get(self.url,params=params)
        print("-get 请求-")
        print(req1.headers)
        print(req1.cookies)
        print(req1.encoding) #编码方式 根据header判断
        print(req1.apparent_encoding) #编码方式 根据response content判断
        print(req1.status_code)
        print(req1.text) #默认以encoding方式解码
        print(req1.content.decode("unicode-escape")) #指定解码方式
        #print(req1.content.decode("utf8"))
        print("-session和cookie-")
        s = requests.Session()
        s.headers={
            "Cookies": "213135151"
        }
        s.headers.update({"TEST":"1"})
        print(s.headers)
        req2 = s.get(self.url, params=params, headers={"Test2":"2"})
        print(req2.text)
        req3 = s.get(self.url, params=params)
        print(req3.text)
        #session可以为请求方法提供缺省数据，比如第一次请求中的{'Test': '1'}就是缺省数据，此时的缺省数据就是跨请求参数。
        #方法级别的参数不会被跨请求保持，比如第二次请求时，没有携带headers={'Test2': '2'}，返回的结果中也没有，说明该参数没有在第一次请求后被保持住。
        print("--------------case1 finished---------------")

    def test_002(self):
        # 请求URL
        url = "https://httpbin.org/post"
        # 请求数据
        data = {
        "username": "slaine",
        "password": 123456
        }
        # 发送请求,一般还需要提供header信息，此处为demo，暂不关注
        reponse1 = requests.post(url=url, data=data)
        res_json = reponse1.json()
        print(res_json)
        flag = reponse1.status_code == 200 or res_json["status"] == 200 or res_json["msg"] == "login sucess"
        # 假如http code为200，status为“200” msg为“login sucess”则测试通过
        if flag:
          print("pass")
        else:
          print("fail")
        print("--------------case2 finished---------------")

    def test_003(self):
        testapi = APIMethod("https://httpbin.org/post", "post", {'name':'Slaine','age':'18'}, header={"test":"slaine"})
        testapi.ExecuteMethod()

if __name__ =="__main__":
    suite = unittest.TestSuite()
    #suite.addTest(APITest("test_003"))