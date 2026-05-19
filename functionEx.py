"""
function :- function is a seperate block of code 

         :-   12-17 mst day
         :-   12:30 -> requirment
                       khaman -> 
                       idli ->  
                       
             user info:
                    add profile
                    update profile
                    show profile show
                    delete profile delete 
                    

def -: which is used to define function
function have meaning full name
    
def function():
    //code
    
function()
if we want to use function we call function using 
function name


code reduce

function pre-define userdefine

built-in function
print()
input() 
eval()



user define 
    which is created by programmer or developer


create multiple part of a single one program

BasicFunction




"""

# def  abc():
#     print("hello")
    

# for x in range(5):
#     abc()   
    
    
    
"""
function type->

no return no args   add profile
no return with args    for database data save 
return witn no args  use-  ins/car/rto
return with  args


"""

# no return
# def message():
#     print("hello")
    
    
# val= message()
# print(val)



# def message(fname):
#     print(f"hello {fname}")
    
    
# message("raj")
# message("mohan")
# message("anuj")

# # no return with args
# def add(val1,val2):
#     res=val1+val2
#     # print(res)

# add(3,6)
# add(4,9)



# no args with return
# def msg():
#     return "hy i am user"

# val=msg()
# print(val)



# def sum(a,b):
#     res=a+b
#     return res

# ans= sum(3,6)
# print(ans)











# def calculateprofit(amount,month):
#      emi = amount/month
#      for x in range(1,month+1):    
#         finalemi = emi+ emi*0.02
#         print(finalemi)
    
# calculateprofit(20000,12)

# calculateprofit(30000,6)





# default value


# def info(fname=None,age=None,address="Indore"):
#     print(f"firstName : {fname}\nage : {age}\naddress : {address}")
    
# position base
# info("shubham",23)
# info(23,"amit","ujjain")
# info(age=23,address="ujjian" ,fname="mohan")#key and value pair

# advance function type pending 





# def f1(val):
#     print(val)
    

# f1(1)

# f1(21,31)



# def f1(*args):
#     print(args)
    
    
# f1(21)
# f1(21,34,34)


# def f1(**kwargs):
#     print(kwargs)
    
# f1(fname="raj",lname="sharma",age=23,email="raj@gmail.com",address="indore")




# def addTwoValue(s):
      



"""
Lambda function is a function that have no name which is 
used to perform single line operations
lambda is a predefine keyword that is used to create 
function 

"""

# res = lambda x:x*x
# res = lambda x:x+x

# print(res(38))


"""
recursion function

a function that call it self is know recursion function

def fun():
    print()
    fun()

fun()


"""

# def fun1(val):
#     print(f"call {val}")
#     if val!=0:
#         val-=1
#         fun1(val)
# fun1(5)
# fct=1
# def fact(val):
#     global fct 
#     print(fct) 
#     if val>0:
#         fct=fct*val
#         val-=1
#         fact(val)

# fact(5)


# 4 basic
# 2
# 1
# 1

# call back funcion



"""
call back function is a cuntion that is call by another function

"""



def f1(val):
    print(val)

def callfun(functionName):
     functionName("mycalling")
    
callfun(f1)
