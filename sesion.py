
"""
r-4
c-4

1  2  3  4    1 odd
8  7  6  5    2 even
9  10 11 12   3 odd
16 15 14 13   4 even

"""

a=1
n=1
while a<=4:
    
    if a%2!=0:
        b=1
        while b<=4:
            print(n, end=" ")
            n+=1  
            b+=1
    else:
        c=1
        rev= n+4-1
        while c<=4:
            print(rev, end=" ")
            rev-=1
            c+=1
        n+=4
    print()
    a+=1







# n=1
# while n<=4:
#     print("s",n,end=" ")
#     n+=1
    

# print(n)


"""
 1 2 3
 8 9 4 
 7 6 5


"""
