## generators:
## no return, yield instead of return

def generate_nos():
    nos = []
    for x in range(1,20):
        print('x is :',x)
        nos.append(x)
        yield x

    # return nos

if __name__ == '__main__':
    my_func = generate_nos()
    print(type(my_func))
    for x in my_func:

        if x == 5:
            print(x)
            break
    print('done with my processing')

