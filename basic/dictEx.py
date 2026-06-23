"""
list/tuple = index and value
each value have index index are unique



Dict- Dict Is a Key and Value pair  collection of any type of element
key (work as index/Key are unique)
each key have some value



dict- mutable and order or any type collection of element


data={"fname":"Raj","lname":"sharma"}

    fname -> key
    lname -> key
    RAj->value
    sharma -> value 
    

"""

# data={"fname":"raj","lname":"sharma","age":23}
# print(data)
# print(type(data))

# print(data["fname"])
# print(data["lname"])
# data['fname']="Mohan"
# print(data)

"""
slicing ->
not perform because dict not have sequence value
print(data[::-1])not perform
"""



# method

# udata=dict()

# udata.update({"fname":"raj"})
# udata.update({"lname":"sharma"})
# udata.update({"age":30})
# udata.update({"address":"indore"})
# print(udata)
"""
key are same  update value of key
key are different both are  update
"""
# udata.update({"age":98})
# print(udata)

# udata.clear() # cleare dict data  all record clean
# print("old",udata)
# newdict=udata.copy()
# print( "new",newdict)

# print(udata.get("lname"))
# print(udata.items())
# print(udata.keys())
# print(udata.values())
# print(udata.popitem())
# print(udata)
# print(udata.pop("lname"))
# print(udata)


# list=["fname","lname","email"]
# newdict=dict.fromkeys(list,"")
# # print(newdict)

# newdict.setdefault("status","Active")
# print(newdict)



email="rajgmail@yo.com"
d=["gmail","yahoo","microsoft"]


if email.find("gmail")!=-1 or email.find("yahoo")!=-1  :
    print("valid")
else:
    print("invalid")


# data= email.split("@")[1].split(".")[0]
# if data in d:
#     print("Valid")
# else:
#     print("false")

