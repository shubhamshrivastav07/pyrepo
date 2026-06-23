
# use for all function 
# import MyProgram
# msg= MyProgram.message()
# print(msg)

# alise use for new name creation(is a virtual name) 
# import MyProgram as mp

# msg= mp.message()
# print(msg)




# from MyProgram import mul,add

# print(mul(3,4))
# print(add(3,4))






"""pre define"""


# import random


# #1 max 10  
# # print(int(random.random()*10))


# # otp generate
# # otp=""
# # for x in range(4):
# #     num= int(random.random()*9)
# #     otp=otp+str(num)
# # print(otp)




# import math as m



# # print(m.pi) # for pi value
# # print(m.sqrt(25)) # for square root value
# # print(m.cbrt(27)) # for cube root value
# # print(m.pow(5,3))
# # print(m.factorial(5))
# # print(m.floor(5.7))
# # print(m.floor(5.4))
# # print(m.ceil(5.7))
# # print(m.ceil(5.4))
# # print(m.gcd(27,45))
# # print(m.inf) # declare infinite number
# # print(m.nan) # declare Not A number
# # datanum=[9,3,4,5,m.nan,m.inf]
# # print(datanum)

# # print(m.log2(23))



# import csv as cv

# file =open("datafile.csv","r").read()
# print(file)
# data=cv.reader(file)
# print(data.line_num)
    
    
    
import json as j

# json read
# file= open("data.json","r")
# data =j.load(file)
# print(data)
# print(type(data))


# discdata= {"fname":"raj","lname":"Sharma"}
# file=open("webdata.json","w")
# myjson=j.dumps(discdata)
# print(type(myjson))
# file.write(myjson)
    
    
    
# useinfo={"fname":"raj","lname":"Sharma"}
# file=open("userinfo.json","w") 
# j.dump(useinfo,file)
    




import datetime as d

# print(d.datetime.now())
# print(d.datetime.utcnow())
# print(d.datetime.today())

# print(d.datetime.fromtimestamp(1780308920))

# dated= d.date(2025,2,12)
# timed=d.time(11,23,36)
# print(d.datetime.combine(dated,timed))

# dt = d.datetime.strptime("2025-22-08 14:30", "%Y-%d-%m %H:%M")
# print(dt)
	
# dt = d.datetime(2025, 8, 22, 14, 30)
# print(dt)
# print(dt.strftime("%a, %d %b %y %H:%M"))

# date =d.date.today()
# print(date)

# newdate= date +d.timedelta(days=5)
# print(newdate)

# newdate1= date +d.timedelta(weeks=18)
# print(newdate1)

# newdate3= date-d.timedelta(days=5)
# print(newdate3)

# print(date> newdate)

# date =d.date.today()
# print(date)
# # print(d.datetime.weekday(date))
# # print(d.datetime.isoweekday(date))
# print(date.isocalendar())


import os

# print("current location do folder ", os.getcwd())

# path="C:\\Users\\infoviian\\OneDrive\\Desktop\\doc"
# foldername=input("enter Folder name")
# # os.mkdir(path+"\\"+foldername)


# path="E:\\doc"
# foldername=input("enter Folder name")
# os.rmdir(path+"\\"+foldername)


# fullpath=path+"\\"+foldername
# print(os.chdir(fullpath))
# print("current location do folder ", os.getcwd())

# import sys

# # print(sys.version)
# # print(sys.flags)
# # print(sys.copyright)
# # print(sys.exit())
# print(sys.getprofile())
# print(sys.getwindowsversion())


