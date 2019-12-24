for x in [1,2,3]:
    print(x)

print("using iteration")
my_list = [1,2,3,4,5]
obj = iter(my_list)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print('done')

## __iter__
## __next__