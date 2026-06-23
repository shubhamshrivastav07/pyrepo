text="ljsdfpkijpqwueppoqwoersccnncvnmvjasdfional"
uniqueText=""
for x in text:
    if x not in uniqueText:
        uniqueText+=x

for x in uniqueText:
    print(x," ",text.count(x))