

# def fun1(name="raj"):
#     print(name)


# fun1(name="manish")
# fun1()



# def num(num):
#     print(num)


# num(2)
# num(2,2)




# def fun2(*args):

#     print(args)


# fun2(2)
# fun2(2,2,3,5)
# fun2(2,2,3,4,4,4,3)


# fun(2)

# def info(**kwargs):
#     print(kwargs)


# info(name="raj")
# info(name="manoj",age=23)
# info(name="manoj",age=23,add="indore")

# def fun1(name):
#     print(name)


# fun1(name="manish",age=23)



# num= lambda x:(x+x-1)
# print(num(3))



# def fun1():
#     print("hello")
#     fun1()


# fun1()



# def fun1(funname,value):
#         funname(value)

# def fun2(number):
#         print("value",number)
        
# fun1(fun2,7)



# number=[1,2,3,4,5,6,7,8,9]
# data= filter(lambda x:x%2!=0 ,number)
# print(data)
# for x in data:
#     print(x)

number=[1,2,3,4,5,6,7,8,9]
data= map(lambda x:x+2 ,number)

for x in data:
    print(x)