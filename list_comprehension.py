## elegant way of generating a list

def calc_square(nos):
    square_list = []
    for x in nos:
        square_list.append(x**2)

    print(square_list)
    return square_list

## list comprehension consist of
# - output expression
## input sequence
## a variable which represents a input value
# optional condition
# [ expression for item in <input_iterable>]
#[ expression for item in <input> if condition]

if __name__ == '__main__':
    square_list = [ x**2 for x in range(1,6)]

    employee={}
    employee['name'] ='abcd'
    employee['age'] = 30
    op = [{x:1} for x in employee]
    print(op)
    print(square_list)

    nos = [1,2,3,4,5,6,7,8,9,10]
    even_nos = [x for x in nos if x%2==0]
    print(f"even nos are:{even_nos}")

    name= ['A','B','C','D']
    lower_name = [ x.lower() for x in name]
    print(lower_name)

    lower_names_map = list(map(lambda x : x.lower(),name))
    print(lower_names_map)

    ## dictionary comprehensio

    chars_ascii = { ord(x):x for x in ['a','b','c']}
    print(chars_ascii)
    new_list=[]
    for x in range(1,10):
        for y in range(1,x):
            new_list.append([x,y])

    new_list_comp = [ [x,y] for x in range(1,5) for y in range(1,x)]
    print(new_list_comp)

