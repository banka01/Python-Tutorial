print('This is introduction to Python List')

## create a list
cities = [] ## empty list
print(cities)

## length of list
print(len(cities))

## create a list wth values
pincodes = [123456,560067]
print(pincodes)
print(type(pincodes))

pincodes.append(560089)
print("list after additions is ",pincodes)

## remove

pcode = pincodes.pop()
print(pcode)
print("list after pop",pincodes)

cities.append('bng')
cities.append('mumbai')
cities.append('mysore')
print("list after new cities",cities)

## pop with index value
print(cities.pop(2))
print("list after new cities",cities)

#print(cities.pop(12))
print("list after new cities",cities)

## get the index pos
print(cities.index('mumbai'))

cities.clear()  ## clear the list
print(len(cities))

cities.append('delhi')
cities.append('bng')
cities.append('kolkata')
print(cities.remove('bng'))
print(cities)

print(cities.count('delhi'))

## insert at specified pos
cities.insert(1,'lucknow')
print(cities)

## extend
cities.extend(['a','b','c'])
print(cities)


cities.insert(0,['d','e','f'])
print(cities)

del cities[0]
print(cities)

## nested list

matrix_2_2 = [[1,2],[2,3]]

new_list = [1,2,3] + [4,5,6]  ## extend
print(new_list)

## access the elements
print(cities[0])
print(cities[1])
print(matrix_2_2[0][1])

## slice of array elements returns new list
print(cities[0:])
print(cities[1:4])
print(cities[1:4:2])
print(cities[::-1])
## list reverse

cities.reverse()
print(cities)

## we are creating a ref while assigning list to another list

new_cities = cities
print(" cities after assignment",cities)
new_cities[0] = 'D'
print("new cities" ,new_cities)
print(" cities after modifying new list",cities)

import copy
x = copy.deepcopy(cities)
x[0]='abc'
print(x)
print(cities)