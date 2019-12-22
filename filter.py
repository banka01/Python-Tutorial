## filter

## filter(func,iterable)

def check_even_odd(x):
    if x%2==0:
        return True
    else:
        return False

nos = [2,10,15,25,39,88,77,90]

print(list(filter(check_even_odd,nos)))

## check whether strings are palindrome or not

text =['ABBA','ABCCA','IAI','CBD']
print(list(filter(lambda x:x==x[::-1],text)))

##
## find the sum of all even nos in the list
nos=[1,2,3,4,5,6,7,8,9,10]
text=['ABCD','EFG','IJKL','MNOPQ']
from functools import reduce
print(reduce(lambda x,y: x+y,filter(lambda x: x%2 == 0,nos)))

print(reduce(lambda x,y: x+y,filter(lambda x: len(x) >=4,text)))

## map and reduce

print(reduce(lambda x,y:x+y,map(lambda x:x**2,[1,2,3])))


## map -> works on iterables and returns iterable with some computed va;ue
# map(func,iterable)
# no of inputs to func should be same as no of iterable

# reduce :
#reduce(function,iterbale), returns a single value
# to use reduce,
## from functools import reduce

## filter. -> filters the value of a iterable based on func return value
# return value of the func should be True or False
# filter(func,iterable). output would be list of values. use list()
# lambda expresssion can be used in place of functions, provided func has only 1 state
# statement

