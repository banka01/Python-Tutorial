"""
program for file operations
"""
def test_read():
    fd = open('sample_file.txt')
    print(type(fd))
    contents = fd.read()
    print(contents)
    print(type(contents))
    fd.close()

def test_readn(bytes=20):
    fd = open('sample_file.txt')
    print(type(fd))
    contents = fd.read(bytes)
    print(f"after reading {bytes} bytes {contents}")
    print('*'*50)
    print(fd.read())
    fd.close()

def test_readlines():
    fd = open('sample_file.txt')

    contents = fd.readline() ## readline output is string, readlines output is list of strings
    print(type(contents),contents)
    print(list(contents))
    # for line in contents:
    #     print(line.strip())
    # print(contents)


    fd.close()
if __name__ == '__main__':
    ## open a file
    # test_readn(bytes=5)
    #test_readlines()

    ## contextmanager, __enter__ and __exit__ method
    with open('sample_file.txt') as fd:
        ## anything written is code for the with block
        contents = fd.readlines()

        # for line in fd:
        #     print(line)

        # fd.seek(1,2)
        # print(fd.read())
    print('file read done successfully')
    # print(fd.readlines())

