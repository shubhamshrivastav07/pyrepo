


# class User():

#     fname="raj"
#     lname="sharma"

#     def setInfo(self):
#         self.age=90
#         print(f"Save Info  {self.fname}")

#     def readInfo(self):
#         print(f"read Info  {self.age} ")



# u= User() object it will automatic call
# print(u.fname)
# print(u.lname)

# u.setInfo() call by object
# u.readInfo()




class User():


    def __init__(self):
        print("call init")


    def read(self):
        print("read")
    

    def write(self):
        print("write")


u=User()