
def test1():
    pass

def test1(x):
    print(x)

def add_nos(x,y,z=0):  ## default values to argument
    result = x + y + z
    return result

## default arguments should be the last in the parameter list
def multiply_nos(z,x,y):
    pass

def login(user,password):
    print(user,password)
    pass

## variable number of arguments

def add_multiple_nos(*args):
    print(args)
    # print(type(args))
    sum_nos  = 0
    for  x in args:
        sum_nos = sum_nos + x
    return sum_nos

def multiply_multiple_nos(x,*args,y):  #after *args, y becomes the keyword arg and is must, we cannot define pos arg after *args
    print(x,args,y)
    # print(type(args))

## variable keyword args,, *args : variable positional args
## **kwargs : variable keyword args
def print_employee(**kwargs):
    print(kwargs,type(kwargs))
    pass
def test_http_conn(*args,url='google.com',ssh=22,**kwargs): #
    """

    :param args:
    :param url:
    :param ssh:
    :param kwargs:
    :return:
    """
    print(args,kwargs)
    for x in kwargs:
        print(x,kwargs[x])
    #print(type(url))

## * makes all the follwing params as keyword args
def check_balance(*,account_no,holders_name,type_):
    pass

if __name__ == '__main__':
    print(__name__)
    print(add_nos(5,6))
    print(add_nos(1,2,3))
    print(add_nos(1,2))
    #multiply_nos(1,2)
    print(add_nos(1,2,z=7))
    # login('abc','def')
    login(user='abcd',password='a')
    print(add_multiple_nos(1))
    print(add_multiple_nos(1,2))
    print(add_multiple_nos(1,2,3))
    print(add_multiple_nos(1,2,3,4))
    multiply_multiple_nos(1,'ABCD',y=2)
    print_employee(x=1,name='abcd',email='yyy@y.com')
    print_employee(name='XYZ',age=10)
    test_http_conn(1,2,3,ssh=22,http=80,url='aaa',telnet=24)
    check_balance(account_no=11111,holders_name='abcd',type_='current')
    #check_balance(account_no=1223,holders_name='abcd')

    #double underscore  dunder
