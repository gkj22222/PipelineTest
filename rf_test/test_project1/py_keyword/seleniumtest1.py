from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
import requests
import selenium
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#driver = webdriver.Chrome()
#element = WebDriverWait(driver, 5, 0.5).until(expected_conditions.presence_of_element_located((By.ID, "kw")))
#element.send_keys('selenium')
#driver.quit()


class commonfunction():
    def __init__(self,url,un,pw):
        self.url = url
        self.un = un
        self.pw = pw

    def loginEnv(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()

if __name__ == "__main__":
  a = commonfunction('https://baidu.com','1','2')
  a.loginEnv()