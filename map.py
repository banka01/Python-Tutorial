## map in python
def calc_square(x):
    return x ** 2
if __name__ == '__main__':
    nos = [1,2,3,4,5]
    for x in nos:
        print(calc_square(x))

    ## map(function,iterable)

    square_nos = list(map(calc_square,nos))
    print(square_nos)

    print(list(map(lambda x,y:x ** 2 - y,nos,[1,2,3,4,5])))

    check_even_odd = [1,2,3,4,5,6,7,8,9,10]
    print(map(lambda x:x%2,check_even_odd))

    ## string, ascii of the string
    name = 'ABCDEFGH'
    #ord(x))->asc of the input
    asc_nos = list(map(lambda x:ord(x),name))
    print(asc_nos)

