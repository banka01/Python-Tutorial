
## syntax error
## runtime

print('line 1')
# x=1/0

try:
    x=1/0
except ZeroDivisionError as e :
    print('got zero division error')
    print(e)
print('line 2')

employee={'name':'abcd'}
try:
    print(employee['age'])
except KeyError as ke:
    print(f"{ke} not found in dict")
    print(type(ke))

names=[]
try:
    print(names[0])
except IndexError as ie:
    print(ie)

try:
    print(employee['name'])
    print(names[0])
except KeyError as  ke:
    print(ke)
except IndexError as  ie:
    print(ie,' caught in multiple except')

try:
    print(employee['agename'])
    print(names[0])
except Exception as  ke:
    print(ke)
# except IndexError as  ie:
#     print(ie,' caught in multiple except')


try:
    print(employee['name'])
    print(names[0])
except (KeyError,IndexError) as  ke:
    print(ke)
# except IndexError as  ie:
#     print(ie,' caught in multiple except')

## finally
print('test finally code with exception gen')
try:
    print(employee['name'])
    print(names[0])
except (KeyError,IndexError) as  ke:
    print('exception generated ',ke)
finally:
    print('in finally code ')

print('test finally code with no exception gen')
try:
    print(employee['name'])
    # print(names[0])
except (KeyError,IndexError) as  ke:
    print('exception generated ',ke)
finally:
    print('in finally code ')


try:
    fd=open('a.txt')
    print(fd.readlines())
except FileNotFoundError as fe:
    print(fe)

## raise
def calc_sum(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x+y
    return x+y
    # raise TypeError('Please provider integer input')

# try:
print(calc_sum(1,'2'))
# except TypeError as te:
#     print(te)
