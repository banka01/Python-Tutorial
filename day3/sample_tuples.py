## tuples are datastuctutes.
## This are immutable

name = ()
print(type(name))
## length
print(len(name))

name = ('abcd',True,1,2.56,'abcd')
print(len(name))

## access indivual el
print(f"value : {name[0]}, type : {type(name[0])}")
print(f"value : {name[1]}, type : {type(name[1])}")
print(f"value : {name[2]}, type : {type(name[2])}")
print(f"value : {name[3]}, type : {type(name[3])}")

#name[4] = 'abcd'
print(name)
## functions for tuple:
print(name.count('abcd'))

## 1 value tuple
nos = (90,)
print(type(nos))