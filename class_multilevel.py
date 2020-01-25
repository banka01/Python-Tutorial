# A-> B
# B->C

class A:

    def testA(self):
        print('IN A')

class B(A):
    def __init__(self,name):
        self.name = name

    def testB(self):
        print(self)
        print('IN testB of B,',self.name)

class C(B):
    def __init__(self,name):
        super().__init__(name)

    def testC(self):
        print('IN C,',self.name)

    def testB(self):
        print('self before super is',self)
        super().testB()
        # B.testB(self)
        # super().testB()
        print('testB method of C,',self.name)
if __name__ == '__main__':
    # c= C('XYZ')
    # c.testA()
    # c.testB()
    b= B('ABC')
    b.testB()
    # print(C.mro())