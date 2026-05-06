# var=range(1,10)
# print(list(var))

# var=range(1,10,2) # 5-6 
# print(list(var))

"""
list
dict
tuple
frozenset
set
range

byte[] -> byte
"""





# # content-> media /text/html/json
# name=[2,3,4,5,7,8,203,23,29]

# # byteval= bytes(name)
# # print(byteval)


# bytearrval= bytearray(name)
# print(bytearrval)


# Data Type End

# advance in list
# Comprehension  
# List Comprehension
# Square=[x:x*x for x in range(1,6)]


# num=[x  for x in range(1,21,2)]
# print(num)

# names=["raj","mohan","rani","amit"]

# name= [x.startswith("r") for x in names ]
# print(name)


# Square={x:x*x for x in range(1,6)}
# print(Square)


# Square=[x*x for x in range(1,6)]
# print(Square)








# names=["raj","mohan","rani","amit","raj","amit"]

# namecount={x:names.count(x) for x in names}
# print(namecount)






# text="Abgkddilhgnishgvljshinaghlkbgilablb"
# charcount={x:text.count(x) for x in text}
# for x in charcount:
#     print(x,charcount[x])





# 2,6,12,20,30,42

# numlist=[ for x in range(1,43)]

# n=0
# for x in range(1,17):
#     if x%2==0:
#         n+=x 
#         print(n,end=" ")
        

# 1,5,9,11,15,19,21,25,29

for x in range(1,30):
    if x%2!=0 and x%10!=3 and x%10!=7 :
        print(x, end=" ")