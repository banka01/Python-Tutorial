##  sets are data structure . Unordered collection of items
## Sets are mutable
## THey are heterogenous. string,int,float,bool

## they cannot contain another list or dict
## they do not contain duplicates.


## create empty sets.

numbers = set()
print(type(numbers))

print(len(numbers))

numbers = {1,2,1}
print(type(numbers))
print(numbers)
print(len(numbers))

java_students = {'A','B','C','D'}
python_students = {'A','B','E'}

print(java_students-python_students)

## sets do not allow indexing
java_students.add('F')
print(java_students)
#java_students.add([1,2,3])

#print(java_students)
java_students.add(12)
java_students.add(True)
java_students.add(34.4)
print(java_students)

vowels = ['a','e','i','o','u']
vowels_set = set()
vowels_set.update(vowels)
print(f"vowels sets {vowels_set}")
print(len(vowels_set))
## vowels_set.add(vowels)

vowels_set.update(('A','E'))
print(vowels_set)
vowels_set.update("IOU")
print(vowels_set)
vowels_set.add("IOU")
print(vowels_set)

## remove from set
print(vowels_set.pop())  ## randonly removes element and returns the elem
print(vowels_set)
print(vowels_set.remove('IOU'))
print(vowels_set)

## union
football_students = {'ABC','DEF','GHI'}
cricket_students = {'ABC','JKL'}

print(football_students.union(cricket_students))
print(football_students.intersection(cricket_students))
print(football_students.difference(cricket_students)) ## A-B