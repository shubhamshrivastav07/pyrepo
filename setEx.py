

"""
Set is a unorder of any type of collection fo elements
no duplicate 
set is mutable (change)


"""

# names={"raj","mohan","amit","aman"}
# # print(names)

# # method
# # add is used to add data in set
# names.add("manmohan")
# names.add("arpita")
# print(names)
# names.clear()
# print(names)
# newset= names.copy()
# print("new set",newset)

# list/tuple
# newname=["amit","mitali","priya"]
# names.update(newname)
# names.add(newname)
# print(names)
# names.remove("raj")
# names.remove("aman")
# print(names)
# #pop is remove from last element
# # remval=names.pop()
# # print(names)
# # print(remval)
# #discarr is work same remove
# # names.discard("aman")
# # print(names)



aname={"raj","mohan","amit","aman","govind"}
bname={"priya","rajesh","mohan","vinay","aman",}

# newdata= aname.union(bname)
# print(newdata)

# datadiff=aname.difference(bname)
# print(datadiff)
# data2diff=aname.symmetric_difference(bname)
# print(data2diff)

# print(aname)
# # aname.difference_update(bname)
# aname.symmetric_difference_update(bname)
# print(aname)
# print(aname)
# print(bname)
# print(aname.intersection(bname))
# print(aname.intersection_update(bname))


# a={"A","C","D","F","N","B","E"}
# b={"B","D","F"}

c={"M","O","P"}

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# print(a.issubset(b))
# print(b.issubset(a))

# print(a.issuperset(b))
# print(b.issuperset(a))




"""
frozenset-> immutable not ,change 


"""

# data=frozenset({"aman","raj","mohan"})
# print(type(data))




name=["raj","mohan","amit" ,"raj"]
print(type(name))
nametup=tuple(name)
print(nametup)
print(type(nametup))


data=[("fname","raj")]

# datadict=dict(data)
# print(datadict)

dataset=set(name)
print(dataset)