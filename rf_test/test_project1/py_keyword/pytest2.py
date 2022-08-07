from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
ROBOT_AUTO_KEYWORDS = False

def testreturn(func):
    def testreturn2(a):
        print("test2")
        a = "test"
        return a
    print("test1")
    return testreturn2

class Circle(object):
   pi = 3.14  # 类属性
   def __init__(self, r):
       self.r = r

circle1 = Circle(1)
circle2 = Circle(2)
print('----未修改前-----')
print('pi=\t', Circle.pi)
print('circle1.pi=\t', circle1.pi)  #  3.14
print('circle2.pi=\t', circle2.pi)  #  3.14
print('----通过类名修改后-----')
Circle.pi = 3.14159  # 通过类名修改类属性，所有实例的类属性被改变
print('pi=\t', Circle.pi)   #  3.14159
print('circle1.pi=\t', circle1.pi)   #  3.14159
print('circle2.pi=\t', circle2.pi)   #  3.14159
print('----通过circle1实例名修改后-----')
circle1.pi=3.14111   # 实际上这里是给circle1创建了一个与类属性同名的实例属性
print('pi=\t', Circle.pi)     #  3.14159
print('circle1.pi=\t', circle1.pi)  # 实例属性的访问优先级比类属性高，所以是3.14111
print('circle2.pi=\t', circle2.pi)  #  3.14159
print('----删除circle1实例属性pi-----')

class test1():
    clspro = "testclspro"
    def testfunc1(self):
        self.clspro = self.clspro + 's'
        #test1.clspro = self.clspro + 's'
        #clspro = self.clspro + 's' 局部内创建的局部变量会在函数结束后释放空间 如果想保留可以用global
        print("类属性为",test1.clspro)
        print("实例属性为", self.clspro)   #会找到当前类属性复制一个空间
    print("类属性为",clspro)

index = testreturn("index")
print("*"*20)
index("xx")
print("*"*20)
print(index("xx"))
print('----测试类属性和实例属性-----')
a = test1()
b = test1()
print(a.testfunc1()) #修改与类属性同名的实例属性
print(a.clspro) #实例属性与类属性同时存在时 优先显示实例属性
print(test1.clspro) #类属性
print("*"*20)
test1.clspro = "1"
print(a.clspro)
print(a.testfunc1())
print(a.clspro)

