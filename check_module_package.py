# from packageA.a import  calc_sum
y1=20
def testA():
    from packageA.a import calc_sum
    def testB():
        pass
    x1 = 10
    global y1
    y1='abcde'
    # print(locals())
    print(y1)
    calc_sum(5,10)
    # print(locals())
    pass

def calc_square(x):
    def check_variable():
        print("in check var")
    print(locals())
testA()
print(globals())
print(locals())
calc_square(5)
# print(calc_sum(4,5))
# import packageA.b as B
#
# from packageA.a import calc_sum as sum
#
# y=10
# print(globals())
#
# if __name__ == '__main__':
#
#     print("call sum ",sum(3,20))
#     print("call multiply from " ,B.calc_mul(4,10))
#     print(f"name is {__name__}")
#     x=10
#     print(locals())
