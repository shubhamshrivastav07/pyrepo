# tuple are immutable collection element
# a=(2,4)
# print(a)
# print(type(a))

# a[0]=9


names=("raj","mohan","arjun","amit")
# names[1]="manit" not posible change in tuple because of Immutablity

# print(names[0])
# print(names[1])
# print(names[2])
# # print(names[:2])
# # print(names[1:3])
# #         4-1 :3
# # obje[start index:end index(n-1)]
# # range(1,5)
# print(names[::-1])

# method
"""

tuple have two method count and index
work same as list method

count -> count element repeate
index -> find value positions
"""


print(names.count("raj"))
print(names.index("amit"))

