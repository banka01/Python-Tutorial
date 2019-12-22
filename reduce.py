#reduce

# 1 --
# 2 --   x
# 3 -------
#        --- y
# 4 ---- ,z

## nos , find the product of all the numbers of list

from functools import reduce

nos = [1,2,3,4,5]
#print(list(map(lambda x,y:x*y,nos)))
#print(reduce(lambda x,y:x+y,nos,nos))

###

def test_reduce(x,y):
    print(f"x is {x},y is {y}")
    return x+y
print(reduce(test_reduce,[1,2,4],10))

print(reduce(lambda x,y:x+y,"ABCD","$%"))
