###

if __name__ == '__main__':
    my_func = lambda x:x+1
    print(my_func)
    print(my_func(5))

    new_expr  = lambda x,y:x+y+2
    print(new_expr(10,12))
    for x in range(1,10):
        print(my_func(x))