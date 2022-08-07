from decimal import Decimal
from robot.api.deco import keyword
from selenium import webdriver
import string
import pandas as pd
ROBOT_AUTO_KEYWORDS = False

class Human(object):
    #print("基类：人")
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def callthename(self):
        print('%s is a human' %self.name)

    def bianxing(self,resex):
        self.sex = resex
        print("Current sex is %s" %self.sex)
        return self.sex

class GMhuman(Human):
    #print("光明中学人员类")
    # 类私有参数1 教师编号前缀
    __pro_1 = "T"
    # 类私有参数2 学生编号前缀
    __pro_2 = "S"
    # 默认人员名称
    name = "default"

    def __init__(self,name,age,tel,sex,resex):
        #print("实例初始化")
        super().__init__(name,age,sex) #继承Human类的参数
        self.tel = tel #此类中的属性
        self.resex = Human(name,age,sex).bianxing(resex) #类的组合

    @classmethod
    def NumberIDdef(cls,role,numberid):
      if role == 'Teacher':
        PersonID = cls.__pro_1 + numberid
      elif role == 'Student':
        PersonID = cls.__pro_2 + numberid
      else:
          raise Exception("Invalid role!")
      print(cls.name + "的id是：" + PersonID) #这里使用的是类属性cls.name
      return PersonID

    def test(self):
        super().callthename()
        Human.callthename(self)
        #对于非实例方法的调用（继承）

class Test(object):
    name = "xxx"
    def __init__(self,sex):
        #print("测试类")
        self.sex = sex

    def test2(self):
        Human.bianxing(self,self.sex)
        Human.callthename(self)
        # 对于实例方法的调用（非继承）调用



a = GMhuman("小马",17,10086,"man","y")
#GMhuman.name="小马"      输出小马（因为修改了类属性)
#a.name = "小马"       输出default(只是改了实例属性)
print(a.NumberIDdef("Student","010325"))
print("*"*20)
print(a.test())
print(a.name)
print(a.resex)
print("*"*20)
b = Test("x")
print(b.test2())
print("*"*20)


#带参装饰器和参数的练习
def log_test(typetext):
    def log_core(func):
        def wrapper(*args,**kwargs): #接收func的不定量参数
          if typetext=="Error":
              print("warning：%s" % func.__name__)
          else:
              print("Normal log:%s" % func.__name__)
          revalue = func(*args,**kwargs)
          return revalue  # 执行的是wrapper()，在wrapper的函数体内再执行最原始的test_fun
        return wrapper #返回的是wrapper函数对象
    return  log_core #返回的是log_core函数对象

@log_test(typetext="Error")
def test_func(name):
    print("my name is %s" %name)


test_func("Tom")
#print(test_func("Tom")) 返回none 因为log_test没有返回值
print("*"*20)
print(test_func.__name__) #输出wrapper   实际等于运行的是wrapper
#解释：先调用log_test(typetext="Error")，得到@log_core，log_core是一个闭包函数，包含了对外部作用域名字typetext的引用，@log_core的语法意义与无参装饰器一样。func变量(test_func函数对象的一个引用)将会封存在闭包的执行环境中，不会随着log_test的返回而被回收。
#等价于 test_func = log_core(test_func) 指向的是wrapper的返回(当func=test_func时) 并不执行内部语句 只是返回当时函数冻结的信息
#同样 等价于 得到test_func = wrapper，wrapper携带对外作用域的引用：func=原始的test_func

#最后讲Tom传入 即为wrapper传入Tom参数 此时等于执行了内部func函数 返回的是test_func实际的结果