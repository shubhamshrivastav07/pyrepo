"""
while condition
    increment op a+=1
    
    
range function


sequence number generate
range(5)  n= 5 n-1 4
0,1,2,3,4

range(2,5)
2,3,4

range(1,10,2)
1,3,5,7,9


range(end)
range(start ,end)
range(start ,end ,steps)


"""

# print(range(5))
# print(range(2,5))
# print(range(2,5,2))


"""

for is use for collection element
range - collection sequence number
list
tuple
set
frozenset
dict
string

"""

# for x in range(5):
#     print(x)    


# for x in range(5,10):
#     print(x)    


# for x in range(1,10):
#     if x%2==0:
#         print(x)    





# for x in range(5,0,-1):
#     print(x)
    
    
# for x in range(5): #row
#     for y in range(5): #col
#         print("* ", end="")
#     print()



"""

* 
* *  
* * *  
* * * *  
* * * * * 

"""

# n= int(input("input the num"))
# for x in range(n):
#     for y in range(x):
#         print("* ",end="")
#     print()





# n= int(input("input the num"))
# for x in range(n):
#     for y in range(n-x):
#         print(" ",end="")
    
#     for z in range(x):
#         print("*",end="")
        
#     print()


# for x in range(1,6):
#     print("* "*x)
    
# for x in range(1,6):
#     print(" "*(6-x) ,  "* "*x)
    
    
# for x in range(1,6):
#     print(" "*x ,  "* "*(6-x))


"""
a
a b
a b c
a b c d 
"""

# print(chr(65))

# for x in range(1,6):
#     for y in range(1,x):
#         print(chr(96+y),end=" ")
#     print()
    
    
"""

a
b c 
d e f 
g h i j 
"""

# n=1
# for x in range(1,6):
#     for y in range(1,x):
#         print(chr(96+n),end=" ")
#         n+=1
#     print()
    
    
"""
String se start


"""
    
invval=5000
day=90

for x in range(day):
    pf= invval * 2/100
    invval+=pf
    invval-=40
    print("inv -",int(invval)," pf ",int(pf)," day ",x)