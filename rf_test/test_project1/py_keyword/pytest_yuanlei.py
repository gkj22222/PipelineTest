class metaclasstest1(type):
    def __new__(cls,name, bases, attr):
        def testfunc(self,testdata):
            return testdata
        attr["attri1"] = "test1"
        attr["testfunc"] = testfunc
        return super().__new__(cls,name, bases, attr)

class testapplymeta(metaclass=metaclasstest1):
    pass

if __name__ == "__main__":
    a = testapplymeta()
    print(a.attri1)
    b = a.testfunc("xxx")
    print(b)