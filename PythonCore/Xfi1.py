class calc:
    num = 100

    def __init__(self,a,b):
        # self is object && self key is mandatory to call var into methods && constructor starts with __init__()
        self.a1 = a
        self.b1 = b
        print("i will be called automatically - constructor")

    def greeting(self):
        print("Hello Raghuu")

    def add(self):
        return self.a1 + self.b1 + calc.num

    def sub(self):
        return self.a1 - self.b1 - calc.num


xdf = calc(11,20)
xdf.greeting()
print(xdf.num)
print(xdf.add())
print(xdf.sub())


print("*******************")

xdf1 = calc(21,20)
xdf1.greeting()
print(xdf1.num)
print(xdf1.add())
print(xdf1.sub())

