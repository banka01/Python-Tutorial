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
    def test(y=20):
        print(number+y)
        
    def test1():
        print(number+10)
    return (test,test1)


##
def test11():
    x=10

def add(x,y):
    return x+y

def test_closure():
    local1 = 20
    def testnested_clos():
        x=20
        print("x is ",x)
        print("encosing from",local1)
    return testnested_clos

if __name__ == '__main__':
    # test11()
    # y1 = testA()
    # print('global z is  ',z)
    # y1()
    # print('global z is no ',z)
    # test_main()
    # my_func = raise_to(10)
    # my_func(y=100)
    a,b = raise_to(10)
    a()
    b()
    ## closure will have some values, only
    ## nested func, nested function should be returned from func
    # nested func should use variable of the enclosing func
    # print(my_func.__closure__)
    # print(test_main.__closure__)
    # print(add)
    # my_add =  add
    # print(my_add(10,20))
    # print(add(10,30))
    # print(add.__code__.co_varnames)
    # n_clos = test_closure()
    # print(n_clos.__closure__[0])

