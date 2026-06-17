userdataList =[] # store data in dict form

#user data save for 
def save():

    fname= input("Enter The fname")
    lname= input("Enter The Lname")
    email= input("Enter The Email")
    if (fname !=None or len(fname)>0) and (lname != None or len(lname)>0) and (email !=None or len(email)>0):
        userdict={"fname":fname,"lname":lname,"email":email}
        userdataList.append(userdict)
        print("Data Save Success")
    else:
        print("Data Is Empty")


#user data updata for 
def update():
     email= input("Enter Your Email ")
     if(email !=None or len(email)>0):
         for data in userdataList:
             if email == data.get("email"):
                idx= userdataList.index(data)
                key = input("Enter The Key")
                val = input("Enter The Value")
                data[key]=val
                userdataList[idx]=data



#user data show for 
def show():
    if len(userdataList)>0:
        for data in userdataList:
            print(data)
    else:
        print("No Data")

#delete User
def delete():
    print()
#user data unique By Id for 
def searchUserById():
    print()
