
"""
Polymorphism
            is  a functionality  which use to  run logic with same  method
            but different form


def add(a,b):

def add(a,b,c)

def add(a,b,c,d)

"""
# Compile Time Polymorphism
# class Calc():

#     def add(self,a=None,b=None,c=None,d=None):
#         if a!=None and b!=None and c ==None and d==None:
#             return a+b
#         elif  a!=None and b!=None and c !=None and d==None:
#              return a+b+c
#         elif  a!=None and b!=None and c !=None and d!=None:
#              return a+b+c+d

    
# c= Calc()
# print(c.add(2,4)) 
# print(c.add(2,4,5)) 
# print(c.add(10,14,5,5)) 









# class Cal1():
#     def add(self,a,b):
#         print(a+b)
    

# class Bank():
#     def add(self,amout,bankNo):
#         print(f"amount  {amout}  {bankNo}")


# class Group():
#     def add(self,friendId,GroupId):
#         print(f"add Friend {friendId} In Group {GroupId}")




# class ObjectCalling():
#     def  call(self,obj,param1,param2):
#             obj.add(param1,param2)

# b= Bank() 
# g=Group()

# objcall=ObjectCalling()
# objcall.call(b,12000,9876)
# objcall.call(g,101,121)







class Base():

    def call(self):
        print("call Parent")


class Derived(Base):

    def call(self):
        print("call Child")


d= Derived()
d.call() #-> overriding


# Banking  ke alawa 

# means  same method in defferent program
# 
"""
    Bank
        UPI pay()
        ATM pay()
        NetBankin pay()

        

Mobile 
    call()
whatsapp
    call()
insta   
    call()
    

"""
