
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


# text="this is my content"


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

# email="raj@gmail.com"

# print(email.endswith("gmail.com"))

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



"""

3:20

count
for loop

a-4
g-4
c-4
"""
text="Abgkddilhgnishgvljshinaghlkbgilablb" #1 assin
num=len(text) # length of String 
newstr="" # new string for unique character
# for x in range(num):  # run text length 34
#     if text[x] not in newstr : # conditioncheck character not in new string
#         newstr+=text[x]
    
# print(newstr)    
# for y in newstr:
#     res=text.count(y)
#     print(f"{y} - {res}")




# text="raj mohan"

# print(text.replace("mohan","sharma"))

# text="Mr. Sahu Ji"
# print(text.removeprefix("Mr."))
# print(text.removesuffix("Ji"))


# print(" - ".join(["Raj is a ","software Engineer his salary","39999"]) )



text="In today’s fast-paced digital world, technology plays a crucial role in shaping how businesses operate and grow. From small startups to large enterprises, adopting modern tools and strategies has become essential for staying competitive. One of the key drivers of success is the ability to adapt to changing trends and continuously improve processes.Digital transformation is no longer an option but a necessity. Businesses are leveraging technologies like cloud computing, artificial intelligence, and data analytics to enhance productivity and deliver better customer experiences. These innovations help organizations make smarter decisions, reduce costs, and streamline operations.Another important aspect is online presence. A well-designed website, active social media engagement, and effective digital marketing strategies can significantly impact brand visibility. Search engine optimization (SEO) ensures that businesses reach the right audience at the right time, increasing traffic and potential conversions.Learning new skills is equally important in this evolving landscape. Professionals are constantly upgrading their knowledge in areas like programming, data science, and machine learning to stay relevant. Platforms offering industry-focused courses have made it easier than ever to gain practical knowledge and hands-on experience.Moreover, collaboration and communication tools have transformed the workplace. Remote work has become more efficient, allowing teams to connect and collaborate from anywhere in the world. This flexibility not only improves work-life balance but also boosts overall productivity.In conclusion, embracing technology and continuous learning are key factors for growth in the modern era. Whether you are a business owner or a professional, staying updated with the latest trends and tools will help you achieve long-term success and remain ahead in the competitive market.I prefer this response ChatGPT"
# print(text)
# print(text.split("."))
# for x in text.split("."):
#     print(x)


# for x in text.splitlines():
#     print(x)

# text="SwMg"
# print(text.swapcase())


"""
-> 
list
tuple
dict
set
frozenset



"""



