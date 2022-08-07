from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
import requests
import unittest
from time import sleep
from py_keyword.seleniumtest1 import commonfunction
from HTMLTestRunner import HTMLTestRunner

class unittestplan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        test = commonfunction("https://baidu.com","un","pw")
        test.loginEnv()
        sleep(10)
        result = self.driver.find_element_by_xpath("//*[@value='百度一下']").value
        self.assertEqual(result,'百度一下','Test Fail')
        self.assertEqual(result, '百度一下', 'Test Fail')
        self.assertIn(result, '百度一下吗', 'Test Fail')
        print("SetUp done")

    def test_case1(self):
        print("Case done")

    def tearDown(self):
        self.driver.quit()

if __name__ =="__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittestplan("test_case1"))
    #suite.addTest(unittest.makeSuite(unittestplan)) 将测试类中的所有方法进行添加
    report = "D:\\Test\\rf_test\\test_report\\UnittestReport.html"
    cf = open(report,"wb")
    runner = HTMLTestRunner(stream=cf,title="Slaine's report",description="Test detail:")
    runner.run(suite)
    cf.close()