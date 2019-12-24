## decorators. change the behaviour of underlying function, without
# changing implementaion details

## nested function

## variable :
# L : local variable
# E : Enclosing variable
# G : Global variable
# B : builtin variable
z=1000
def testA():
    x=10
    y=100
    def testB():
        nonlocal  x
        x=1
        global z
        z=100
        print('local x ',x)
        print('enclosing y',y)
        print('global',z)
        print('builtin',__name__)

    print('x is ',x)
    return testB


def test_main():
    x=10
    y=100
    def test_nested():
        nonlocal x
        x=20
        print('x in nested func',x)
    print('x in main func ',x)
    test_nested()
    print('x after nested func ',x)

def raise_to(number):
    def test():
        print(number+5)
    return test

##

def test11():
    x=10


if __name__ == '__main__':
    # test11()
    # y1 = testA()
    # print('global z is  ',z)
    # y1()
    # print('global z is no ',z)
    # test_main()
    my_func = raise_to(10)
    print(my_func.__closure__)
    print(test_main.__closure__)

