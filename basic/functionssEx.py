
# print("")
# print("")
# print("")
# print("")
# for x in range(6):
#     print("")
# for x in range(6):
#     print("")
# for x in range(6):
#     print("")

# print("")
# print("")


# def message():
#     print("hello")

# message()


# 1 type of funciton()
# no return no args
def function1():
    print(" ")

# 2 return with no args
def function2():
    return "hello"

# 3 no return with args
def function3(a,b):
    print(a,b)

# function3(2,3)

# 4 return with args

def function4(a,b):
    return a+b

res= function4(3,4)
# print(res)

# 5 default  args

def function5(num1=1,num2=1):
    print(num1*num2)

# function5(2,2)

# variable length  
def function6(*args):
    print(args)


# function6(2)
# function6(2,3,4)
# function6(2,4,5,6,7,0)


def function7(**kwargs):
    print(kwargs)

function7(fname="raj",lname="sharma")
function7(fname="amit",lname="sharma",age=34)