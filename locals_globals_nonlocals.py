

z=1000
def testA():
    x = 10
    y = 100
    def testB():
        nonlocal x
        x = 1
        # global z
        z = 100
        print('local x ', x)
        print('enclosing y', y)
        print('global', z)
        print('builtin', __name__)

    testB()
    print('x is ', x)

print('z before func call',z)
testA()
print('z after func call ',z)