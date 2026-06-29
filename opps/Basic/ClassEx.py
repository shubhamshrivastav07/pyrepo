"""
class 


"""

#this is class
# class User():
#     #state as a variable 
#     fname="raj"
#     lname="sharma"
#     age=23
#     email="raj@gmail.com"

#     # function ot method  are behivours 
#     def getdata(self):
#         return {"fname":self.fname,"lname":self.lname,"email":self.email,"age":self.age}
    



# this is user
# u = User()
# print(u.fname)
# print(u.lname)
# print(u.email)
# print(u.age)
# dictdata =u.getdata()
# print(dictdata)

# u.fname="mohan"

# print(u.getdata())






class  BasicFunctionality():


    """
    documents of info
    basic common function of the class info
    """
    # current instance of a class
    def save(self):
        self.fname="manish"
        print("save Data",self.fname)
    def update(self):
        print("update Data")
    def search(self):
        print("search Data")
    def delete(self):
        print("delete")


b= BasicFunctionality()
# b -> instance of class
# print(b.save())
print(b.__doc__)





