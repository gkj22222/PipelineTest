from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
ROBOT_AUTO_KEYWORDS = False
@keyword
def test_py(txt):
    """
    test kw
    """
    return txt


t=pd.Series([1,3213,3131],index=list("xyz"))
t=t.astype(int)
value=t["x"]
valuesame=t[0]
valuefirst2=t[:2]#前两行
valueis=t[[0,2]]#隔开取
valueis2=t[["x","z"]]#隔开2
valuebuer=t[t>1]
print(t)
print(value)
print(valuesame)
print(valuefirst2)
print(valueis)
print(valueis2)
print(valuebuer)
print(t.index)
print(t.values)
