

# import packageA.a as A

from packageA.a  import *
from packageA.a import calc_sum

# from packageA.a import calc_sub,OS_NAME

print(dir())
# print(dir(A))
print(calc_sum(5,6))
print(OS_NAME)
# print(calc_sub(5,3))
# print(A.OS_NAME)
# print(A.__name__)
# print(A.__file__)
# print(A.__doc__)
import sys
# print(dir(sys))
print(type(sys.path))
print(sys.path)
sys.path.append('D:\\test')
