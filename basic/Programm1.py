userdata=[]
sno=1 
while True:
        option=int(input("Please Enter only Number\nEnter Your Choice\n1 save\n2 update\n3 list\n4 delete\n5 detail\n"))
        match(option):
            case 1: 
                    print("Option 1 Save Your choice")
                    fname= input("Enter First Name  :  ")
                    lname= input("Enter Last Name  :  ")
                    email= input("Enter Email  :  ")
                    age= int(input("Enter Age  :  "))
                    pw= input("Enter Password  :  ")
                    keylist=["firstname","lastname","email","age","password"]
                    userdict=dict.fromkeys(keylist,"")
                    error=0
                    if fname.isalpha():
                        userdict.update({"firstname":fname})
                    else:
                        error+=1
                        print("invalid FirstName") 
                    if lname.isalpha():
                        userdict.update({"lastname":lname})
                    else:
                        error+=1
                        print("invalid LastName") 
                    if email.find("@") != -1 and email.endswith(".com"):
                        data= email.split("@")[1].split(".")[0]
                        d=["gmail","yahoo","microsoft"]
                        if data.strip() in d:
                            userdict.update({"email":email})
                        else:
                            error+=1
                            print("Invalid Email Domain ")
                    else:
                        error+=1
                        print("invalid Email") 
                    if age>18: 
                        userdict.update({"age":age})
                    else:
                        error+=1
                        print("invalid Age") 
                    
                    if pw.find("@")!=-1 or pw.find("$")!=-1 or pw.find("#")!=-1:
                        userdict.update({"password":pw})
                    else:
                        error+=1
                        print("Password Invalide")
                    if error==0:
                        userdict.update({"id":sno})
                        userdata.append(userdict)
                        sno+=1
                        print("Data Save Success")
                    else:
                        print("Data not Save Error Data")
                    print("===================================================")            
            case 2:
                print("your Choice Update")
                id=int(input("Enter The Id : "))
                for x in userdata:
                    if x["id"]==id:
                        index=userdata.index(x)
                        key=input("Enter The field :  ")
                        value= input("Enter The Value :   ")
                        x.update({key:value})
                        userdata[index]=x
                print("===================================================")
            case 3:
                print("your Choice List")
                if len(userdata) >0:
                    print("===================User List======================")
                    for x in userdata:
                        print(x)
                    print("===================================================")
                else:print("userList Empty")                
            case 4:
                id=int(input("Enter The Id :  "))
                for x in userdata:
                    if x["id"]==id:
                        index=userdata.index(x)
                        userdata.pop(index)
                print("===================================================")
            case 5:
                id=int(input("Enter The Id"))
                for x in userdata:
                    if x["id"]==id:
                        print(x)
                print("===================================================")








"""
Program For Write User Information
uniqueid-
firstname
lastname
email
age
password


save/update/showuserlist/delete/showUserDetail(id)/every Detail match


choice base option 
user input choice
condition match->

        operation-> save/update
        
        save code userinfo detail save
            validation
            fname/last name me number nhi hona chahiye
            email validate .com @
            age >18
            pass min 8 max 16 validate S$@#0  
            
        update me user update
        list
        detail
        delete
        
collection ->List  

    dict -> Key and Value

.com
@ 
gmail,yahoo,microsoft



int()
float() datype list

"""

