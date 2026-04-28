
"""
STring is a collection of character

    this is my content
    t
    h
    i 
    s
    
    
collection -> length ,index

immutable-> not changed after object creation

t -0
h-1
i-2
s-3
 -4
operation
    *
    +

"""
# text="this is my content"
# print(len(text))
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])

# for x in range(0 ,len(text)):
#     print(text[x])


# txt="hello "
# print(txt *9)

# fname="raj "
# lname="Sharma"
# print(fname+lname)


"""
scape sequence
\n - new line
\t - tab space
\' - single quote use in singel quote
\"

\\
"""

# text="this is \n my content"
# print(text)

# text="this is\tmy content"
# print(text)



# text="hello \"friend\""
# text='hello \'friend\''
# text='hello \\friend'
# print(text)


# String formating

# price=1000
# text=f"this is book price {price}"
# print(text)


text="this is my content"


# print(text[4:])
# print(text[4:9])
# print(text[:9])

# # [start index: end index:step]
# print(text[0:10:2])

# print(text[::-1])
# print(text[2])
# text[2]="mm"-> safe 



# funcntion or method

# text="RaJ"
# print(text.casefold())
# print(text.lower())
# text="raj"
# print(text.capitalize())
# print(text.upper())
# text="this is\tmy content"
# print(text)
# print(text.center(20))
# print(text.count("t"))
# print(text.index(" is "))
# print(text.find(" is"))
# print(text.expandtabs(50))

# text="this is my content"
# print(text.title())
# print(text.istitle())

# text="https://www.mywebsite.com"
# txt="hello.com"
# print(text.startswith("https://www."))
# print(txt.startswith("https://www."))

email="raj@gmail.com"

print(email.endswith("gmail.com"))

# text="  raj   "

# print(text)
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())


# text="text123"
# print(text.isalnum())
# print(text.isalpha())
# text="12.3"
# print(text.isdecimal())
# print(text.isdigit())
# text="©"
# print(text.isascii())
# text=" "
# print(text.isspace())

# text="my name {} and age {}"

# print(text.format("raj",23))
# print(text.format(24,"raj"))

# text="my name {name} and age {age}"
# print(text.format(age=23,name="raj"))