"""
List is a collection of element   mutable(change after object creation)

Order
list have duplicate element
any type of elementor value

index  position of element /value
length -> total element/or value
"""
datalist=["raj","sharma",23,True,9989.98]
                                    
# print(datalist[0])
# print(datalist[1])
# print(datalist[2])
# print(datalist[3])
# print(datalist[13])


# for x in datalist:
#     print(x)

# for x in range(len(datalist)):
#     print(datalist[x])


"""
datalist[1]="yadav" # change means mutable
print(datalist)

slicing - > substring

"""

# namelist=["raj","arjun","mohan","manish","rajpal","haniraj","viraj"," mahipal","arpan"]

# print(namelist)
# print(namelist[1:4])
# print(namelist[:4])
# print(namelist[4:])
# print(namelist[::-1])#0-10
# print(namelist[::-2])#0-10


"""
method

"""

names=[]
# names=list()


"""
append-> use for add element  after object creation

"""

names.append("raj")
names.append("mohan")
names.append("arjun")
names.append("prince")
names.append("virendra")
names.append("karna")
names.append("sunil")
names.append("ravi")
names.append("kunal")
# print(names)
# names.clear()
# print(names)
# name=names.copy()
# print(name)
# # name[1]="maru"
# # print("original ",names)
# # print("duplicate",name)

# print(names.count("rapan"))
names.extend(["raj","arpan","prince"])
# print(names)

# print(names.index("karna"))
# print(names)
# print(names.index("raj",3))

# names.insert(6,"rampal")
# print(names)
# print(names.remove("raj"))
# print(names)
# rmname=  names.pop()
# print(names)
# print(rmname)
# print(names.pop(3))
# print(names)


# names.reverse()
# print(names)
names.sort(reverse=False) #only same type data
print(names)