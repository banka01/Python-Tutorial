## for loop in python

## loop through all list elements and find sum of all

numbers = [1,2,3,4,5,6,7]

sum_nos = 0
for x in numbers:
    sum_nos = sum_nos + x
    print(x)
print(sum_nos)
print('aaaa')

for x in ('a','e'):
    print(x)

employee = {'name':'abcd','age':30}
print(employee.keys())

for x in employee.keys():
    print(x)

for x in employee.values():
    print(x)

for x in employee.keys():
    print(x)
print(employee.items())
for k,v in employee.items():
    print(k,v)

for k in employee:
    print(k)

# x = (1,2)
# y,z = x  ## tuple unpacking
# print(y,z)

## range(stop)
## range(start,stop)
## rangd(start,stop,step)

##
print("-"*10)
print("range(x)")
for x in range(5):
    print(x)
print("-"*10)


print("-"*10)
print("range(x,y)")
for x in range(5,10):
    print(x)
print("-"*10)

print("-"*10)
print("range(x,y,step)")
for x in range(5,10,2):
    print(x)
print("-"*10)



for x in range(0,len(numbers)):
    print(x,numbers[x])
#print(type(range(5)))


## enumerate()
print(type(enumerate(numbers)))
for x in enumerate(numbers):
    print(x)
for index,value  in enumerate(numbers):
    print(index,value)

for x,y in enumerate("ABCD"):
    print(x,y)

## enumerate with tuple
for x,y in enumerate(('Z','B')):
    print(x,y)

for x,y in enumerate(employee):
    print(x,y)
print('*'*30)
for x,y in enumerate(('Z','B'),start=1):
    print(x,y)

## zip(iterables) :
students = ['A','B','C']
marks = [10,11]
for x in zip(students,marks):
    print(x)
for x in zip(numbers):
    print(x)

for x in employee.keys():
    print(f"{x}:{employee[x]}")