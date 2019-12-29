##
def append_file():
    with open('sample1.txt','a') as fd:
        print(fd.tell())
        fd.write('\nnew content')

def read_write_file():
    with open('sample.txt','r+') as fd:
        content = fd.readlines()
        print(f'read line from file is :{content}')
        fd.writelines(['\nline4','\nline5'])

def write_x_mode():
    with open('sample_new.txt','x') as fd:
        fd.writelines(['\nline4','\nline5'])
if __name__ == '__main__':
    # cities = ['abc\n','def\n']
    # with open('sample.txt','w') as fd:
    #     fd.write('This is first line')
    #     fd.write("\nthis is second line")
    #     fd.writelines(cities)
    # print('file write done successfully')

    # append_file()
    # read_write_file()
    write_x_mode()
    print('file append done successfully')
