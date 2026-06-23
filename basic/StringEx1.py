

# name="shubham"
# print(name[0])
# print(name[3])
# name[0]="m" not change 

# String scape sequence

"""
\n- new line
\t for tab space
"""
# method

# text="abca"
# print(text.count("a"))

# text="ABCD"
# print(text.casefold())
# print(text.lower())
# text="this is my content"
# print(text.upper())
# print(text.title())
# print(text.capitalize())


# text="The End"
# print(text.center(10))
# print(text.center(80,"*"))

# text="this is my\tcontent"
# print(text.expandtabs(2))
    

# text="https://www.myweb.in"
# print(text.startswith("https://"))

# text="https://www.myweb.in"
# print(text.endswith(".com"))

# text="shubham"
# print(text.index("am"))
# print(text.find("an"))


# text="89"

# print(text.isalnum())
# print(text.isalpha())
# print(text.isnumeric())
# print(text.isdigit())

# text="©"
# print(text.isascii())

# print(chr(65))


# text="avc"
# print(text.isupper())
# print(text.islower())
# text="This Is "
# print(text.istitle())

# name=input("Enter The name")
# age=int(input("Enter the age"))
# status=bool(input("enter the status"))
# amt=float(input("enter the amt"))

# msg=f"my name is {name} ,age is {age} and status is {status} amt is {amt:.2f}"
# print(msg)

text="my name is {}, {}"
print(text.format("raj",23))
print(text.format(23,"mohan"))

text="my name is {name}, {age}"
print(text.format(name="raj",age=23))
print(text.format(age=23,name="mohan"))
