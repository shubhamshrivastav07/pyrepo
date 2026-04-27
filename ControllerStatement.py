
"""
if(False):
    print("If run")
else:
    print("default option")

#print("out side block")
"""

"""

userid= input("Enter Uid ")
passw= input("Enter Password")

if userid=="admin" and passw=="admin123":
    print("Admin Login")
else:
    print("Userid/Password invalid")


pAmt= int(input("Enter monthly Order Amt"))

if(pAmt>100000):
    print("10k Dis Offer")


print("500rs free refer ")


"""

# num = int(input("Enter Number"))

# if num%2==0:
#     print("Even")

# if num%2!=0:
#     print("Odd")



"""
ladder  if  ->
     one variable 
        multiple condition



role = input("Enter Your Role  ")

if    role=="admin":
    print("admin Login")
elif  role=="superadmin":
    print("superadmin Login")
elif  role=="user":
    print("user Login")
else:
    print("no role Found")
    
"""


"""
nested 

      if  condition
              if  condition
                    if    condition
      else 
            if conditon
            
            else
                              






a=21

if a>10 and a<20:
    if a%2==0:
        print("evan")
    else:
        print("odd")
else:
    print("Condition not match")
    
    


uid =input("Enter Your Uid")
passw=input("Enter Your Password")
role=input("Enter Your role")


if uid =="shubham12" and  passw =="sh123":
    
    if role=="admin":
        print("You are Login Admin Role")
    elif role=="user":
        print("You are Login User Role")
    else:
        print("You are Login in Default Role(User)")

else:
    print("invalid uid and password")




    
"""



"""
        match




# choice=int(input("Enter Your Choice 1. NewFile 2. Open 3. Edit 4. delete"))


# match(choice):
#     case 1:print("New file Create")
#     case 2:print("File Open")
#     case 3:print("File Edit")
#     case 4:print("FileDelete")
    

"""



"""
Loop is used to repeate taks by given condition

print("hello")
a>

While condition
  
    check condition when true
    
"""

# a=0
# while a<5:
#     print("hello")
#     a+=1


"""
1,3,5,7,9  n numner 


"""

# n= int(input("Enter N number"))
# a=0
# while a<=n:
#     if a%2 !=0:
#         print(a)
#     a+=1





# n= int(input("Enter N number"))
# a=0
# while a<=n:
#     if a%2 ==0 and a!=0:
#         print("Even",a)
#     else:
#         print("odd",a)
#     a+=1



"""

2  4 8 16 32 64 n 

3 9 27 81 n

"""

# n= int(input("Enter N number"))
# a=1
# m=2
# while a<=n: 
#     m=m*2
#     print(m)
#     a+=1
    
    
    
# 3 9 27 81 n
# a=1
# n= int(input("Enter N number"))
# m=3
# while a<=n: 
#     print(m)
#     m=m*3
#     a+=1
    
    
"""
2 4 16 

1
2
3
"""
# a=1
# n= int(input("Enter N number"))
# m=2
# while a<=n: 
#     m=m**a
#     print(m)
#     a+=1


"""
1-100
1,3,5,7,9,13 15 17 19 23

even

2,4 6,8 10 ,12 ,14,16,18,20

4,8

"""
# a=1
# n= int(input("Enter N number"))
# m=2
# while a<=n: 
#     if a%10!=1 or a==1:
#         if a%2!=0 :
#              print(a)
#     a+=1





# a=1
# n= int(input("Enter N number"))
# m=2
# while a<=n: 
#     if a%2==0 :
#         if a%4!=0:
#              print(a)
#     a+=1
    

"""

nested loop
"""
#  c c c
# [1 1 1] row1
# [1 1 1] row2
# [1 1 1] row3


# a=0
# while a<3: 
#     b=0
#     while b<3 :
#         print(1,end=" ")
#         b+=1
#     print()
#     a+=1 


# 1 2 3
# 4 5 6
# 7 8 9

# a=0
# n=1
# while a<3:
#     b=0
#     while b<3:
#         print(n ,end=" ")
#         n+=1
#         b+=1
#     print()
#     a+=1


"""
1
1 1
1 1 1
1 1 1 1


"""
# a=0
# while a<4:
#     b=0
#     while b<=a:
#         print(1,end=" ")
#         b+=1
#     print()
#     a+=1



"""
1
2 3
4 5 6
7 8 9 10 
"""
a=0
n=1
while a<4:
    b=0
    while b<=a:
        print(n,end=" ")
        n+=1
        b+=1
    print()
    a+=1

