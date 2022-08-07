from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
ROBOT_AUTO_KEYWORDS = False

x=pd.DataFrame([[1,23,5],[5,7,8],[9,7,0]],index=['a','b','c'],columns=['x','y','z'])
print(x)