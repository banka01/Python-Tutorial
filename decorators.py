## decorators. functions which modify the functionality of the existing func
# whithout changing the underlying implementions

from functools import wraps
from time import time

def timer(func,x,y):
    before = time()
    rv = func(x,y)
    after = time()
    print('elapsed time:', after - before)
    return rv

def new_timer(func):

    @wraps(func)
    def test_func(*args,**kwargs):
        """ test_func doc"""
        before = time()
        rv = func(*args,**kwargs)
        after = time()

        print('elapsed time:', after - before)
        return rv
    return test_func

@new_timer
def add(x,y):
    rv =  x + y
    return rv


@new_timer
def sub(x,y):
    '''
    function to subtract two nos
    :param x:
    :param y:
    :return:
    '''
    rv = x - y
    return rv

def test_params(func):
    def check_params(x,y):
        if x<0 or y < 0:
            print('please enter positive nos')
            raise TypeError('invalid nos')
        return func(x,y)
    # check_params.__name__ = func.__name__
    # check_params.__doc__  = func.__name__
    return check_params

@test_params
def calc_sum(x,y):
    return x+y

def test_mvargs(*args,**kwargs):
    '''
    test function to check the docstring
    :param args:
    :param kwargs:
    :return:
    '''

    print(args)
    print(kwargs)
    print(*args)
    print(**kwargs)
if __name__ == '__main__':

    # add = new_timer(add)
    # sub = new_timer(sub)
    # print('add(1,2):',timer(add,1,2))
    # print('add(2,4):', timer(add,2, 4))
    # print('add(3,2):', timer(add,3, 2))
    # print('sub(2,4):', timer(sub,2, 4))
    # print('sub(3,2):', timer(sub,3, 2))
    print('add(1,2):', add(1, 2))
    print('add(2,4):', add(2, 4))
    print('add(3,2):', add(3, 2))
    print('sub(2,4):', sub(2, 4))
    print('sub(3,2):', sub(3, 2))
    # x=10
    # y=20
    # test_mvargs(x,y,{'z':1})
    print("function name of test_mvargs",test_mvargs.__name__)
    print("function name of add", add.__name__)
    print('doc of test_mvargs',test_mvargs.__doc__)
    print('doc of sub is',sub.__doc__)
    print('name of sub is', sub.__name__)
    print(calc_sum(1,3))
    print("name of 'calc_sum' is ",calc_sum.__name__)

