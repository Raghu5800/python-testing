from Xfi1 import calc


class xd1(calc):
    num1 = 200

    def __init__(self):
        calc.__init__(self,2,10)
        # ! Create constructor in child class when u see constructor in parent class !

    def getdata(self):
        return self.num1 + self.num + self.add()


fc = xd1()
print(fc.getdata())
