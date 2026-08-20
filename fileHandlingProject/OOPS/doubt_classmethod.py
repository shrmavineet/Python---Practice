class F1:
    a =10
    def childMethod(self):
        print(F1.a)

    @classmethod
    def secondMethod(cls):
        print(cls.a)

obj = F1()

obj.childMethod()
obj.secondMethod()