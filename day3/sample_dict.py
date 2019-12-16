## key / value
## mutable
## key should be unique
## values can be any other object.
    # basic data types
    # list
    # dict

## dictionary

employee = {}
print(type(employee))
print(len(employee))

## dictionary with key / values
## colon used to separate key and value
employee = {'name':'abc','age':30}
print(employee)

employee['city'] = 'bng'
print(employee)
## retrieval of keys and values dictionaty is random

## access the keys

print(employee.keys())
print(employee.values())

## access specific value for a key

print(employee['name'])
print(employee['age'])

#employee.clear()
#print(employee)
print(employee.pop('name'))  # return values is the value of the dict at given key
print(employee)
#print(employee.pop('name1'))

print(employee.popitem())
print(employee)


person = dict()
print(type(person))
employee['pancard'] = 'YYYYY'
print(employee.items())

employee['skills'] = ['python','c++','java']
print(employee['skills'])
employee['address'] ={'houseno':88,'area':'btm'}
print(employee['address'])
print(employee)

## length on dict is count of keys
print(len(employee))

print(employee.get('age',))
print(employee)

print(employee.get('age1',[]))
print(employee)

employee.setdefault('age1',100)
print(employee)

