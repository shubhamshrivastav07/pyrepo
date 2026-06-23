

"""
generator  function
mainy use for generate next value 

yield retur one value

function
"""


# uname=["raj","mohan","rohan","amit"]

# def functionGen(val):
#     yield val
    
# val=None
# for x in uname:
#    val= functionGen(x)
#    print(next(val))

    

# def option():
#     yield "file"
#     yield "Open"
#     yield "Save"
#     yield "Exit"
    
# val= option()
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))



    


# value=90

# def functuin1():
#     print("inside function",value)

# print("outside function",value)

# functuin1()




# def function2():
#     #local
#     requirment="Water"
#     print(requirment)
    
# print(requirment)





# #global
# num=0
# def fun1():
#     global num
#     num=num+9
#     print(num)

# fun1()
# print(num)
        
        




#global

def fun1():
    num=0
    num=num+9
    def fun2():
        nonlocal num
        print(num)
    fun2()
fun1()


