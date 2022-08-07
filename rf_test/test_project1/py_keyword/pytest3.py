from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
ROBOT_AUTO_KEYWORDS = False

class test1():
    def __init__(self,data1):
        self.df = pd.DataFrame(data1)

class test2(test1):
    def __init__(self,data1):
        super().__init__(data1) #这步如果注释了会报错没有df  出错的原因：在子类中重写了构造函数，但新的构造函数没有初始化父类，当没有初始化父类的构造函数时，就会报错   #在子类中初始化父类的构造函数，因为在子类中重写了构造函数。如果子类中没有重写构造函数则不需要再一次初始化父类的构造函数
        self.df = self.df.astype("object", copy=False)

class test3(test1):
    def testfunc(self):
        print(self.df)

class test4(test1):
    def test2func(self):#没有重写构造函数 即可以直接使用父类的属性和方法
        self.df = self.df.astype("object", copy=False)

b = test2(['c','d',11])
print(b.df)
a = test3(['a','b',12])
print(a.testfunc())
c = test4(['e','f',13])
print(c.df)


class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B,C):
    def test(self):
        print('from D')

obj = D()
obj.test()