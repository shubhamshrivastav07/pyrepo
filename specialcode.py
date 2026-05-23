
# def call(func):
#     def wrapper(*args ,**kwargs):
#         print(f" data {args}  kw {kwargs}")
#         func()
#         print("gn")
#     return wrapper

# @call
# def abc():
#     print("work")
   
# # abc()
# # abc(23) 
# abc(num=90)



# def session(func):
#     def wrapper(*args, **kwargs):
#         if kwargs["session"] ==None:
#             kwargs.update({"session":True})
#             func(kwargs["session"])

#     return wrapper




# @session
# def login(session=None):
#     print("login",session)

# login(session=None)


# dictdata={}
# i=1
# def log(func):
#     def wrapper(*args, **kwargs):
#         global i
#         key=f"call {i}"
#         # print(key)
#         dictdata.update({key:func})
#         func()
#         i+=1
#     return wrapper


# @log
# def funcA():
#     print()
    
# @log
# def funcB():
#     print()
    
# @log
# def funcC():
#     print()
    

# funcA()
# funcB()
# funcB()
# funcC()
# funcB()

# print(dictdata)
# 





dictdata={}
i=1
def log(func):
    def wrapper(*args, **kwargs):
        global i
        key=f"call {i}"
        value=f" {func} {kwargs} "
        dictdata.update({key:value})
        func()
        i+=1
    return wrapper


@log
def UserData(Fname=None,Lname=None,Age=0):
        print()
@log
def Order(ProductName=None,Qty=0):
        print()


UserData(Fname="Raj",Lname="Sharma",Age=34)
Order(ProductName="Pizza",Qty=3)
Order(ProductName="Sendwich",Qty=2)
UserData(Fname="Mohan",Lname="Sahu",Age=24)
Order(ProductName="Momos",Qty=1)
UserData(Fname="Amit",Lname="Thakur",Age=14)
Order(ProductName="meggi",Qty=1)


print(dictdata)
