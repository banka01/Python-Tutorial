## operator overloading
## 5 + 6

# x =10
# print(type(x))
# print(dir(x))
#
# ## top level func '+' __add__
# print(5+'aa')

class Box:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def __add__(self, other):
        new_length = 0
        new_breadth = self.breadth
        if isinstance(other,Box):
            print('I am of type Box')
            new_length = self.length + other.length
        elif isinstance(other,int):
            print('I am of type int')
            new_length = self.length + other
        else:
            raise TypeError('Invalid input')

        # print(f"type of other is {type(other)}")
        # print(f"type of self.length is {type(self.length)}")
        return Box(new_length,new_breadth)
        # print('in custom add')

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __len__(self):
        abc = []
        len(abc)
        pass
    def __repr__(self):
        return f'Box(l={self.length},b={self.breadth})'

class School:
    def __init__(self,students):
        self._students = students

    def __len__(self):
        print('In length of scholl')
        return len(self._students)

if __name__ == '__main__':
    b1= Box(1,2)
    b2 = Box(2,3)
    b3 = b1 + 5
    b4 = b1 + b2
    # b4= b1+b3
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(type(7.6))
    # print(b1+7.67)
    # print(b2)
    sch = School(['a','b','c','d','e'])
    print(len(sch))