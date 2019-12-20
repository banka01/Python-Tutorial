## functions

## function with no params and no return value
## function with no params and return value
## function with params and no return value
## function with params and return value

## user defined and system defined

## function defination,
## function call
## callables

## function with no params and no return value
## be default function returns the value of the last executed statement
def test_addition():
    print('in test_addtion')



print(type(test_addition))
test_addition()

## function with no param and return statement

def calc_sum(n):

    sum_nos = 0
    for x in range(n+1):
        sum_nos = sum_nos +x
    return sum_nos

def check_even():
    x=10
    if x%2 == 0:
        return True
    else:
        return False

def greet(name):
    print(type(name))
    print('Good Evening ',name)


def check_largest(x,y,z):

    if x>y:
        if x>z:
            return x
        else:
            return z
    elif y>z:
        return y
    else:
        return z

def get_even_nos(nos):

    even_nos = []
    for x in range(1,nos+1):
        if x%2==0:
            even_nos.append(x)
    return even_nos

def check_return_tuple():


    return ('ec','em')

def doubles_list_values(nos):
    ## in the given func, if the passed list is modified, change would be refeclect in main list
    # print(nos)
    nos[0] = 4


value = calc_sum(10)
print(value)
print(check_even())
greet('rakesh')
print(check_largest(1,2,3))
print(calc_sum(5))
print(get_even_nos(10))
print(check_return_tuple())
error_code,error_msg = check_return_tuple()

print(error_code,error_msg)
nos = [1,2,3]
print(f"before calling func nos are {nos}")
doubles_list_values(nos)
print(f"after calling func nos are {nos}")

